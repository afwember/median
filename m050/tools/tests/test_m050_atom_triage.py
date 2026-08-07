import base64
import importlib.util
import json
from pathlib import Path
import sys
import threading
from urllib.error import HTTPError
from urllib.request import Request, urlopen

import pytest


ROOT = Path(__file__).parents[3]
TOOL = ROOT / "m050/tools/m050_atom_triage.py"


def _module():
    spec = importlib.util.spec_from_file_location("m050_atom_triage_for_tests", TOOL)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    try:
        spec.loader.exec_module(module)
    finally:
        sys.modules.pop(spec.name, None)
    return module


@pytest.fixture(scope="module")
def triage():
    return _module()


@pytest.fixture(scope="module")
def corpus(triage):
    return triage.load_corpus(ROOT)


def test_loads_every_completed_candidate_with_unique_bound_atoms(corpus):
    assert len(corpus.atoms) == 6550
    assert len(corpus.candidate_hashes) == 18
    assert len(corpus.source_labels) == 18
    assert len(corpus.by_key) == 6550
    assert {atom.source_id for atom in corpus.atoms} == set(corpus.candidate_hashes)


def test_modern_atom_joins_full_source_block_and_siblings(corpus):
    atom = next(
        atom
        for atom in corpus.atoms
        if atom.source_id == "M050-SRC-EMBODIMENT-001"
        and atom.block_id
        and len(corpus.block_members[atom.block_key]) > 1
    )
    assert atom.exact_source_text in atom.source_text
    assert atom.section
    assert atom.block_type != "unknown"
    rendered = _module().render_atom(corpus, atom.corpus_position - 1, {}, width=60)
    assert "CURRENT ATOM" in rendered
    assert "SOURCE TEXT" in rendered
    assert "OTHER ATOMS FROM THIS SOURCE BLOCK" in rendered
    assert "SOURCE PROGRESS:" in rendered
    assert "CORPUS PROGRESS:" in rendered


def test_display_hides_extraction_coordinates_and_labels_unheaded_preface(corpus):
    atom = next(
        atom
        for atom in corpus.atoms
        if atom.source_id == "M050-SRC-EMBODIMENT-001"
        and atom.section == "Unheaded source preface"
    )
    rendered = _module().render_atom(corpus, atom.corpus_position - 1, {}, width=60)
    assert "SECTION: Unheaded source preface" in rendered
    assert "<!--@" not in rendered


def test_display_strips_markdown_heading_furniture(corpus):
    atom = next(atom for atom in corpus.atoms if "nest rest" in atom.exact_source_text.lower())
    rendered = _module().render_atom(corpus, atom.corpus_position - 1, {}, width=60)
    assert "SECTION: 6. EMBODY Mode Families" in rendered
    assert "SECTION: **" not in rendered


def test_legacy_atom_has_stable_location_block(corpus):
    atom = next(atom for atom in corpus.atoms if atom.source_id == "M050-SRC-PA-001")
    assert atom.block_id is None
    assert atom.block_type == "legacy_record"
    assert "__LOCATION__" in atom.block_key
    assert atom.source_text == atom.exact_source_text


def test_decisions_save_reload_resume_and_undo_atomically(tmp_path, triage, corpus):
    path = tmp_path / "decisions.jsonl"
    store = triage.DecisionStore(path, corpus)
    first, second = corpus.atoms[:2]
    previous_first = store.apply((first,), "retain")
    previous_second = store.apply(
        (second,),
        "exclude",
        exclusion_reason="obsolete_or_superseded",
    )
    assert path.is_file()
    assert store.next_undecided() == 2
    reloaded = triage.DecisionStore(path, corpus)
    assert reloaded.counts() == {
        "exclude": 1,
        "retain": 1,
        "uncertain": 0,
        "decided": 2,
        "undecided": 6548,
        "total": 6550,
    }
    reloaded.restore(previous_second)
    assert second.key not in reloaded.decisions
    reloaded.restore(previous_first)
    assert path.read_text(encoding="utf-8") == ""


def test_latest_decision_can_be_undone_after_resume(tmp_path, triage, corpus):
    path = tmp_path / "resume-undo.jsonl"
    store = triage.DecisionStore(path, corpus)
    block = next(value for value in corpus.block_members.values() if len(value) >= 3)
    store.apply(block, "retain", scope="block")
    resumed = triage.DecisionStore(path, corpus)
    assert len(resumed.undo_latest()) == len(block)
    assert resumed.decisions == {}
    assert path.read_text(encoding="utf-8") == ""


def test_block_decision_is_bounded_and_reversible(tmp_path, triage, corpus):
    block = next(value for value in corpus.block_members.values() if len(value) >= 3)
    path = tmp_path / "block-decisions.jsonl"
    store = triage.DecisionStore(path, corpus)
    previous = store.apply(block, "uncertain", scope="block")
    assert set(store.decisions) == {atom.key for atom in block}
    assert {item["decision_scope"] for item in store.decisions.values()} == {"block"}
    store.restore(previous)
    assert store.decisions == {}


def test_candidate_hash_drift_invalidates_existing_decision(tmp_path, triage, corpus):
    atom = corpus.atoms[0]
    path = tmp_path / "bad.jsonl"
    store = triage.DecisionStore(path, corpus)
    store.apply((atom,), "retain")
    record = json.loads(path.read_text(encoding="utf-8"))
    record["candidate_sha256"] = "0" * 64
    path.write_text(json.dumps(record) + "\n", encoding="utf-8")
    with pytest.raises(triage.TriageError, match="binding drifted"):
        triage.DecisionStore(path, corpus)


def _request_json(url, *, pin=None, body=None, origin=None):
    headers = {}
    if pin:
        token = base64.b64encode(f"asa:{pin}".encode()).decode()
        headers["Authorization"] = f"Basic {token}"
    if body is not None:
        headers["Content-Type"] = "application/json"
        data = json.dumps(body).encode()
    else:
        data = None
    if origin:
        headers["Origin"] = origin
    request = Request(url, data=data, headers=headers, method="POST" if body is not None else "GET")
    with urlopen(request, timeout=3) as response:
        return response.status, response.headers, response.read()


def test_mobile_web_api_auth_decision_undo_and_page(tmp_path, triage, corpus):
    store = triage.DecisionStore(tmp_path / "web-decisions.jsonl", corpus)
    server = triage.create_web_server(corpus, store, host="127.0.0.1", port=0, pin="2468")
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    base = f"http://127.0.0.1:{server.server_address[1]}"
    try:
        with pytest.raises(HTTPError) as unauthorized:
            _request_json(f"{base}/api/state")
        assert unauthorized.value.code == 401

        status, headers, page = _request_json(f"{base}/", pin="2468")
        assert status == 200
        assert headers["X-Content-Type-Options"] == "nosniff"
        assert b'<meta name="viewport"' in page
        assert b"Authorial Atom Triage" in page
        assert b'id="excludeButton"' in page

        _status, _headers, raw_state = _request_json(f"{base}/api/state", pin="2468")
        state = json.loads(raw_state)
        first_key = state["atom"]["atom_key"]
        assert state["stats"]["total"] == 6550
        assert state["stats"]["decided"] == 0

        _status, _headers, raw_next = _request_json(
            f"{base}/api/decision",
            pin="2468",
            body={
                "atom_key": first_key,
                "decision": "retain",
                "exclusion_reason": None,
                "scope": "atom",
                "source_id": None,
            },
        )
        next_state = json.loads(raw_next)
        assert next_state["stats"]["decided"] == 1
        assert next_state["atom"]["atom_key"] != first_key

        second_key = next_state["atom"]["atom_key"]
        _status, _headers, raw_third = _request_json(
            f"{base}/api/decision",
            pin="2468",
            body={
                "atom_key": second_key,
                "decision": "retain",
                "exclusion_reason": None,
                "scope": "atom",
                "source_id": None,
            },
        )
        third_state = json.loads(raw_third)
        assert third_state["stats"]["decided"] == 2
        assert third_state["atom"]["atom_key"] not in {first_key, second_key}

        _status, _headers, raw_undo = _request_json(
            f"{base}/api/undo",
            pin="2468",
            body={"source_id": None},
        )
        undone = json.loads(raw_undo)
        assert undone["undone"] == 1
        assert undone["stats"]["decided"] == 1
        assert undone["atom"]["atom_key"] == second_key

        with pytest.raises(HTTPError) as cross_origin:
            _request_json(
                f"{base}/api/undo",
                pin="2468",
                body={"source_id": None},
                origin="https://example.com",
            )
        assert cross_origin.value.code == 403
    finally:
        server.shutdown()
        server.server_close()
        thread.join(timeout=3)


def test_non_loopback_web_access_requires_pin(tmp_path, triage, corpus):
    store = triage.DecisionStore(tmp_path / "web-decisions.jsonl", corpus)
    with pytest.raises(triage.TriageError, match="requires loopback or an exact Tailscale address"):
        triage.create_web_server(corpus, store, host="10.10.10.10", port=0)
    with pytest.raises(triage.TriageError, match="requires loopback or an exact Tailscale address"):
        triage.create_web_server(corpus, store, host="192.168.1.9", port=0, pin="2468")
    with pytest.raises(triage.TriageError, match="wildcard web binding is prohibited"):
        triage.create_web_server(corpus, store, host="0.0.0.0", port=0, pin="2468")


def test_web_host_allowlist_is_tailscale_bounded(triage):
    assert triage._web_host_allowed("127.0.0.1")
    assert triage._web_host_allowed("localhost")
    assert triage._web_host_allowed("100.122.50.97")
    assert not triage._web_host_allowed("10.10.10.10")
    assert not triage._web_host_allowed("192.168.1.9")
    assert not triage._web_host_allowed("example.com")


def test_canonical_write_requires_active_triage_authority(tmp_path, triage, corpus):
    state_path = tmp_path / triage.STATE
    state_path.parent.mkdir(parents=True)
    decision_path = tmp_path / triage.DEFAULT_DECISIONS
    state = {
        "status": "AUTHORIAL_TRIAGE_ACTIVE",
        "execution_state": "AUTHORIAL_TRIAGE_ACTIVE",
        "triage": {
            "status": "ACTIVE",
            "decision_record": triage.DEFAULT_DECISIONS.as_posix(),
            "decision_schema_version": triage.SCHEMA_VERSION,
            "input_atom_count": len(corpus.atoms),
        },
        "authority": {
            "repository_writes_authorized": True,
            "triage_authorized": True,
            "source_work_authorized": False,
        },
    }
    state_path.write_text(json.dumps(state), encoding="utf-8")
    triage._require_canonical_write_authority(tmp_path, decision_path, corpus)
    state["authority"]["triage_authorized"] = False
    state_path.write_text(json.dumps(state), encoding="utf-8")
    with pytest.raises(triage.TriageError, match="write authority"):
        triage._require_canonical_write_authority(tmp_path, decision_path, corpus)
