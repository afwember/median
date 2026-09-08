import importlib.util
import json
from pathlib import Path
import sys
import threading
from urllib.error import HTTPError
from urllib.request import Request, urlopen

import pytest


ROOT = Path(__file__).parents[3]
TOOL = ROOT / "m050/tools/m050_atom_rewrite.py"


def _module():
    spec = importlib.util.spec_from_file_location("m050_atom_rewrite_for_tests", TOOL)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    try:
        spec.loader.exec_module(module)
    finally:
        sys.modules.pop(spec.name, None)
    return module


@pytest.fixture(scope="module")
def rewrite():
    return _module()


@pytest.fixture(scope="module")
def corpus(rewrite):
    return rewrite.RewriteCorpus(ROOT)


def test_input_is_exact_completed_rewrite_list(corpus):
    assert len(corpus.atoms) == 98
    assert len(corpus.by_key) == 98
    assert all(atom in corpus.full_corpus.atoms for atom in corpus.atoms)
    assert not any("m051" in atom.source_id.lower() for atom in corpus.atoms)


def test_rewrite_is_trimmed_bound_and_authorially_accepted(tmp_path, rewrite, corpus):
    atom = corpus.atoms[0]
    path = tmp_path / "rewrites.jsonl"
    store = rewrite.RewriteStore(path, corpus)
    store.apply(atom.key, "  A clearer source-grounded replacement.  ")
    record = rewrite.RewriteStore(path, corpus).rewrites[atom.key]
    assert record["resolution"] == "rewrite"
    assert record["replacement_claim"] == "A clearer source-grounded replacement."
    assert record["authorially_accepted"] is True
    assert record["candidate_sha256"] == atom.candidate_sha256
    assert record["triage_decision_sha256"] == corpus.triage_sha256
    assert record["original_claim_sha256"] == rewrite._text_sha256(atom.normalized_claim)


def test_empty_claim_is_rejected_and_unchanged_claim_is_accepted(tmp_path, rewrite, corpus):
    atom = corpus.atoms[0]
    store = rewrite.RewriteStore(tmp_path / "rewrites.jsonl", corpus)
    with pytest.raises(rewrite.TriageError, match="nonempty"):
        store.apply(atom.key, "  ")
    store.apply(atom.key, atom.normalized_claim)
    record = rewrite.RewriteStore(store.path, corpus).rewrites[atom.key]
    assert record["resolution"] == "accept"
    assert record["replacement_claim"] == atom.normalized_claim


def test_exclusion_uses_existing_authorial_reason(tmp_path, rewrite, corpus):
    atom = corpus.atoms[0]
    path = tmp_path / "exclusions.jsonl"
    store = rewrite.RewriteStore(path, corpus)
    store.exclude(atom.key)
    record = rewrite.RewriteStore(path, corpus).rewrites[atom.key]
    assert record["resolution"] == "exclude"
    assert record["replacement_claim"] is None
    assert record["exclusion_reason"] == "other_authorial_exclusion"
    assert store.counts()["excluded"] == 1
    assert store.counts()["resolved"] == 1


def test_binding_drift_is_rejected(tmp_path, rewrite, corpus):
    atom = corpus.atoms[0]
    path = tmp_path / "rewrites.jsonl"
    store = rewrite.RewriteStore(path, corpus)
    store.apply(atom.key, "A valid replacement.")
    record = json.loads(path.read_text(encoding="utf-8"))
    record["original_claim_sha256"] = "0" * 64
    path.write_text(json.dumps(record) + "\n", encoding="utf-8")
    with pytest.raises(rewrite.TriageError, match="binding drifted"):
        rewrite.RewriteStore(path, corpus)


def test_working_store_advances_sources_and_checkpoints_complete_slate(tmp_path, rewrite, corpus):
    canonical_path = tmp_path / "canonical.jsonl"
    working_path = tmp_path / "working.jsonl"
    canonical_path.write_text("", encoding="utf-8")
    working = rewrite.prepare_working_store(canonical_path, working_path, corpus)
    first_source = rewrite._source_ids(corpus)[0]
    atoms = [atom for atom in corpus.atoms if atom.source_id == first_source]
    for index, atom in enumerate(atoms, start=1):
        working.apply(atom.key, f"Authorial replacement {index}.")
    lifecycle = rewrite._lifecycle(
        corpus, rewrite.RewriteStore(canonical_path, corpus), working
    )
    assert lifecycle["checkpoint_required"] is False
    assert lifecycle["active_source_id"] == rewrite._source_ids(corpus)[1]
    with pytest.raises(rewrite.TriageError, match="slate is not complete"):
        rewrite.checkpoint_working(canonical_path, working_path, corpus)

    for atom in corpus.atoms:
        if atom.key not in working.rewrites:
            working.apply(atom.key, atom.normalized_claim)
    lifecycle = rewrite._lifecycle(
        corpus, rewrite.RewriteStore(canonical_path, corpus), working
    )
    assert lifecycle["checkpoint_required"] is True
    assert lifecycle["active_source_id"] is None
    result = rewrite.checkpoint_working(canonical_path, working_path, corpus)
    assert result["checkpointed_scope"] == "complete_rewrite_slate"
    assert result["canonical_dispositions"] == len(corpus.atoms)
    assert result["next_source_id"] is None
    assert result["phase_complete"] is True


def test_undo_crosses_source_boundaries_but_preserves_canonical(tmp_path, rewrite, corpus):
    canonical_path = tmp_path / "canonical.jsonl"
    working_path = tmp_path / "working.jsonl"
    canonical = rewrite.RewriteStore(canonical_path, corpus)
    canonical.apply(corpus.atoms[0].key, corpus.atoms[0].normalized_claim)
    working = rewrite.prepare_working_store(canonical_path, working_path, corpus)
    later = next(atom for atom in corpus.atoms if atom.source_id != corpus.atoms[0].source_id)
    working.apply(later.key, later.normalized_claim)

    protected = frozenset(canonical.rewrites)
    assert working.undo_latest(protected_keys=protected) == later.key
    assert working.undo_latest(protected_keys=protected) is None
    assert corpus.atoms[0].key in working.rewrites


def _request(url, *, body=None, origin=None):
    headers = {}
    data = None
    if body is not None:
        headers["Content-Type"] = "application/json"
        data = json.dumps(body).encode()
    if origin:
        headers["Origin"] = origin
    request = Request(url, data=data, headers=headers, method="POST" if body is not None else "GET")
    with urlopen(request, timeout=3) as response:
        return response.status, response.headers, response.read()


def test_mobile_api_accepts_rewrite_skip_and_undo(tmp_path, rewrite, corpus):
    store = rewrite.RewriteStore(tmp_path / "working.jsonl", corpus)
    server = rewrite.create_web_server(corpus, store, host="127.0.0.1", port=0)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    base = f"http://127.0.0.1:{server.server_address[1]}"
    try:
        status, headers, page = _request(f"{base}/")
        assert status == 200
        assert headers["X-Content-Type-Options"] == "nosniff"
        assert b"Authorial Rewrite" in page
        assert b">Accept claim</button>" in page
        assert b'id="exclude"' in page
        assert b'$("replacement").value=a.normalized_claim' in page
        _, _, raw = _request(f"{base}/api/state")
        state = json.loads(raw)
        key = state["atom"]["atom_key"]
        _, _, raw = _request(
            f"{base}/api/rewrite",
            body={"source_id": state["atom"]["source_id"], "atom_key": key, "replacement_claim": "A replacement accepted by the author."},
        )
        advanced = json.loads(raw)
        assert advanced["stats"]["rewritten"] == 1
        assert advanced["stats"]["accepted"] == 1
        _, _, raw = _request(
            f"{base}/api/undo",
            body={"source_id": state["atom"]["source_id"], "atom_key": advanced["atom"]["atom_key"], "visible_atom_key": advanced["atom"]["atom_key"]},
        )
        undone = json.loads(raw)
        assert undone["undone"] == 1
        assert undone["stats"]["rewritten"] == 0
        _, _, raw = _request(
            f"{base}/api/exclude",
            body={"source_id": state["atom"]["source_id"], "atom_key": key},
        )
        excluded = json.loads(raw)
        assert excluded["stats"]["excluded"] == 1
        assert excluded["stats"]["resolved"] == 1
        with pytest.raises(HTTPError) as cross_origin:
            _request(
                f"{base}/api/rewrite", origin="https://example.com",
                body={"source_id": state["atom"]["source_id"], "atom_key": key, "replacement_claim": "Rejected cross-origin replacement."},
            )
        assert cross_origin.value.code == 403
    finally:
        server.shutdown(); server.server_close(); thread.join(timeout=3)


def test_mobile_api_advances_to_next_source_without_checkpoint(tmp_path, rewrite, corpus):
    store = rewrite.RewriteStore(tmp_path / "working.jsonl", corpus)
    first_source, second_source = rewrite._source_ids(corpus)[:2]
    first_atoms = [atom for atom in corpus.atoms if atom.source_id == first_source]
    for atom in first_atoms[:-1]:
        store.apply(atom.key, atom.normalized_claim)
    server = rewrite.create_web_server(corpus, store, host="127.0.0.1", port=0)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    base = f"http://127.0.0.1:{server.server_address[1]}"
    try:
        _, _, raw = _request(f"{base}/api/state")
        state = json.loads(raw)
        assert state["atom"]["atom_key"] == first_atoms[-1].key
        _, _, raw = _request(
            f"{base}/api/rewrite",
            body={
                "source_id": first_source,
                "atom_key": first_atoms[-1].key,
                "replacement_claim": first_atoms[-1].normalized_claim,
            },
        )
        advanced = json.loads(raw)
        assert advanced["checkpoint_required"] is False
        assert advanced["atom"]["source_id"] == second_source
    finally:
        server.shutdown(); server.server_close(); thread.join(timeout=3)


def test_network_boundary_requires_loopback_or_exact_tailscale(tmp_path, rewrite, corpus):
    store = rewrite.RewriteStore(tmp_path / "working.jsonl", corpus)
    with pytest.raises(rewrite.TriageError, match="wildcard"):
        rewrite.create_web_server(corpus, store, host="0.0.0.0", port=0)
    with pytest.raises(rewrite.TriageError, match="loopback or an exact Tailscale"):
        rewrite.create_web_server(corpus, store, host="192.168.1.8", port=0)
    assert rewrite._web_host_allowed("100.122.50.97")


def test_repository_state_retires_external_rewrite_authority(rewrite, corpus):
    with pytest.raises(rewrite.TriageError, match="authority is inactive"):
        rewrite._require_authority(ROOT, corpus)
