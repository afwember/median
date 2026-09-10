import copy
import hashlib
import json
from pathlib import Path
import sys

import pytest


ROOT = Path(__file__).parents[3]
TOOLS = ROOT / "m050/tools"
sys.path.insert(0, str(TOOLS))
try:
    import m050_reconciliation as reconciliation
finally:
    sys.path.remove(str(TOOLS))


@pytest.fixture(scope="module")
def corpus():
    return reconciliation.ReconciliationCorpus(ROOT)


@pytest.fixture(scope="module")
def empty_store(corpus, tmp_path_factory):
    return reconciliation.ReconciliationStore(
        tmp_path_factory.mktemp("reconciliation") / "units.jsonl", corpus
    )


@pytest.fixture(scope="module")
def packet(corpus, empty_store):
    return reconciliation.build_packet(
        corpus,
        empty_store,
        tranche_id="away-crossing-pilot",
        msid_prefix="Away.Crossing",
        selector="exact",
    )


def test_stage_5_corpus_is_exact_complete_stage_4_output(corpus):
    assert len(corpus.atoms) == 5382
    assert len(corpus.by_key) == 5382
    counts = {}
    for item in corpus.atoms:
        status = item.mapping["mapping_status"]
        counts[status] = counts.get(status, 0) + 1
    assert counts == {"unmapped": 418, "mapped": 3799, "human_required": 1165}
    assert not any("m051" in item.atom.source_id.lower() for item in corpus.atoms)


def test_pilot_packet_is_exact_hash_bound_and_deduplicates_source_blocks(packet):
    assert packet["semantic_boundary"] == {
        "msid_prefix": "Away.Crossing",
        "selector": "exact",
    }
    assert len(packet["required_atom_keys"]) == 105
    assert len(packet["required_atom_keys"]) == len(set(packet["required_atom_keys"]))
    target_keys = {item["atom_key"] for item in packet["atoms"]}
    context_keys = {item["atom_key"] for item in packet["context_atoms"]}
    assert target_keys == set(packet["required_atom_keys"])
    assert target_keys.isdisjoint(context_keys)
    block_keys = [item["block_key"] for item in packet["source_blocks"]]
    assert len(block_keys) == len(set(block_keys))
    unhashed = dict(packet)
    packet_hash = unhashed.pop("packet_sha256")
    assert packet_hash == hashlib.sha256(
        reconciliation._canonical_bytes(unhashed)
    ).hexdigest()


def _proposal(packet):
    return {
        "schema_version": reconciliation.PROPOSAL_SCHEMA_VERSION,
        "packet_id": packet["packet_id"],
        "packet_sha256": packet["packet_sha256"],
        "units": [
            {
                "unit_local_id": "U001",
                "unit_status": "reconciled",
                "primary_msid": "Away.Crossing",
                "canonical_claim": "A grounded test proposition.",
                "members": [
                    {"atom_key": key, "disposition": "supporting"}
                    for key in packet["required_atom_keys"]
                ],
                "authority_basis_atom_keys": [],
                "related_local_ids": [],
                "rationale": "The test groups the exact mechanically bound packet.",
                "human_question": None,
            }
        ],
    }


def test_proposal_requires_exact_atom_coverage(packet, corpus):
    proposal = _proposal(packet)
    reconciliation.validate_proposal(packet, proposal, corpus)
    proposal["units"][0]["members"].append(copy.deepcopy(proposal["units"][0]["members"][0]))
    with pytest.raises(reconciliation.TriageError, match="exactly once"):
        reconciliation.validate_proposal(packet, proposal, corpus)


def test_semantic_review_is_independently_hash_bound(packet, corpus):
    proposal = _proposal(packet)
    reconciliation.validate_proposal(packet, proposal, corpus)
    review = {
        "schema_version": reconciliation.REVIEW_SCHEMA_VERSION,
        "packet_id": packet["packet_id"],
        "packet_sha256": packet["packet_sha256"],
        "proposal_sha256": hashlib.sha256(
            reconciliation._canonical_bytes(proposal)
        ).hexdigest(),
        "verdict": "accept",
        "defects": [],
    }
    reconciliation.validate_review(packet, proposal, review)
    review["proposal_sha256"] = "0" * 64
    with pytest.raises(reconciliation.TriageError, match="binding drifted"):
        reconciliation.validate_review(packet, proposal, review)


def test_provider_request_is_disabled_until_model_and_output_cap_are_configured(packet):
    provider = {
        "enabled": False,
        "name": "Anthropic",
        "model": None,
        "reasoning_effort": "high",
        "cache_ttl": "1h",
        "maximum_output_tokens": None,
        "pricing": None,
        "proposal_review_required": True,
    }
    with pytest.raises(reconciliation.TriageError, match="model is not configured"):
        reconciliation.build_proposer_request(packet, provider)
    provider.update({
        "model": "test-model",
        "maximum_output_tokens": {"proposal": 40000, "review": 8000},
    })
    request = reconciliation.build_proposer_request(packet, provider)
    assert request["model"] == "test-model"
    assert request["max_tokens"] == 40000
    assert request["messages"][0]["content"][0]["cache_control"]["ttl"] == "1h"
    assert request["output_config"]["format"]["type"] == "json_schema"


def test_proposal_and_review_share_the_cached_packet_prefix(packet):
    provider = {
        "model": "claude-sonnet-5",
        "reasoning_effort": "high",
        "cache_ttl": "1h",
        "maximum_output_tokens": {"proposal": 40000, "review": 8000},
    }
    proposal = _proposal(packet)
    proposer = reconciliation.build_proposer_request(packet, provider)
    reviewer = reconciliation.build_reviewer_request(packet, proposal, provider)
    assert proposer["system"] == reviewer["system"]
    assert (
        proposer["messages"][0]["content"][0]
        == reviewer["messages"][0]["content"][0]
    )
    assert (
        proposer["messages"][0]["content"][1]
        == reviewer["messages"][0]["content"][1]
    )
    cached_packet = json.loads(proposer["messages"][0]["content"][0]["text"])
    atom_evidence = json.loads(proposer["messages"][0]["content"][1]["text"])
    assert {**cached_packet, **atom_evidence} == packet
    assert proposer["max_tokens"] == 40000
    assert reviewer["max_tokens"] == 8000
    prefix_count_body = reconciliation._token_count_body(
        reviewer, cache_prefix_only=True
    )
    assert len(prefix_count_body["messages"][0]["content"]) == 1
    assert "max_tokens" not in prefix_count_body


def test_counted_preflight_prices_cache_miss_with_margin():
    request = {
        "max_tokens": 40000,
        "messages": [{"content": [{
            "cache_control": {"type": "ephemeral", "ttl": "1h"}
        }]}],
    }
    pricing = {
        "input_usd_per_million_tokens": "5",
        "output_usd_per_million_tokens": "25",
        "cache_5m_write_multiplier": "1.25",
        "cache_1h_write_multiplier": "2",
    }
    token_count = {
        "full": {"response": {"input_tokens": 100000}},
        "cache_prefix": {"response": {"input_tokens": 90000}},
    }
    forecast = reconciliation.counted_call_ceiling(request, pricing, token_count)
    assert forecast["reserved_cache_prefix_tokens"] == 91800
    assert forecast["reserved_uncached_suffix_tokens"] == 10512
    assert forecast["total_ceiling_usd"] == "1.97056"


def test_token_count_preflight_uses_free_endpoint_twice(monkeypatch, tmp_path, packet):
    provider = {
        "model": "claude-sonnet-5",
        "reasoning_effort": "high",
        "cache_ttl": "1h",
        "maximum_output_tokens": {"proposal": 36000, "review": 8000},
    }
    request = reconciliation.build_proposer_request(packet, provider)
    observed = []
    counts = iter((100000, 90000))

    def fake_send(endpoint, body, _key_file, _timeout):
        observed.append((endpoint, body))
        return 200, json.dumps({"input_tokens": next(counts)}).encode("utf-8")

    monkeypatch.setattr(reconciliation, "_send_anthropic_to", fake_send)
    evidence = reconciliation._count_anthropic_request(
        request, tmp_path / "unused-key", 1.0
    )
    assert len(observed) == 2
    assert all(
        endpoint == reconciliation.ANTHROPIC_TOKEN_COUNT_ENDPOINT
        for endpoint, _body in observed
    )
    assert all("max_tokens" not in body for _endpoint, body in observed)
    assert evidence["full"]["response"]["input_tokens"] == 100000
    assert evidence["cache_prefix"]["response"]["input_tokens"] == 90000


def test_run_ledger_is_append_only_and_hash_chained(tmp_path):
    path = tmp_path / "run_ledger.jsonl"
    reconciliation._append_ledger(path, {"role": "proposal", "attempt": 1})
    reconciliation._append_ledger(path, {"role": "review", "attempt": 1})
    events = reconciliation._ledger_events(path)
    assert len(events) == 2
    assert events[0]["previous_event_sha256"] is None
    assert events[1]["previous_event_sha256"] == events[0]["event_sha256"]
    drifted = json.loads(path.read_text(encoding="utf-8").splitlines()[0])
    drifted["attempt"] = 2
    path.write_text(json.dumps(drifted) + "\n", encoding="utf-8")
    with pytest.raises(reconciliation.TriageError, match="hash chain drifted"):
        reconciliation._ledger_events(path)


def test_ready_lifecycle_grants_nothing_and_spark_up_assessment_is_read_only(
    corpus, empty_store
):
    state = json.loads((ROOT / reconciliation.STATE).read_text(encoding="utf-8"))
    original = copy.deepcopy(state)
    assessed, report = reconciliation.plan_lifecycle_transition(
        state, corpus, empty_store, "prepare-spark-up"
    )
    assert assessed == original
    assert report["tranche_id"] == "away-crossing-pilot"
    assert report["required_atoms"] == 105
    assert state["authority"]["repository_writes_authorized"] is False
    assert state["authority"]["reconciliation_authorized"] is False
    assert state["authority"]["provider_calls_authorized"] is False


def test_proceed_activates_reconciliation_and_preconfigured_provider(
    corpus, empty_store
):
    state = json.loads((ROOT / reconciliation.STATE).read_text(encoding="utf-8"))
    active, report = reconciliation.plan_lifecycle_transition(
        state,
        corpus,
        empty_store,
        "activate-on-proceed",
        expected_tranche_id="away-crossing-pilot",
    )
    assert report["activated"] is True
    assert active["status"] == "RECONCILIATION_ACTIVE"
    assert active["authority"]["repository_writes_authorized"] is True
    assert active["authority"]["reconciliation_authorized"] is True
    assert active["authority"]["semantic_acceptance_authorized"] is True
    assert active["authority"]["provider_calls_authorized"] is True
    assert active["spend"]["active"] is True
    assert active["spend"]["remaining_usd"] == "2.0000000"


def test_stopdown_rejects_incomplete_tranche(corpus, empty_store):
    state = json.loads((ROOT / reconciliation.STATE).read_text(encoding="utf-8"))
    active, _ = reconciliation.plan_lifecycle_transition(
        state,
        corpus,
        empty_store,
        "activate-on-proceed",
        expected_tranche_id="away-crossing-pilot",
    )
    with pytest.raises(reconciliation.TriageError, match="complete tranche coverage"):
        reconciliation.plan_lifecycle_transition(
            active, corpus, empty_store, "prepare-stopdown"
        )


def test_canonical_store_rejects_duplicate_primary_members(corpus, tmp_path):
    item = corpus.atoms[0]
    member = {
        "atom_key": item.key,
        "effective_claim_sha256": item.effective_claim_sha256,
        "disposition": "basis",
    }
    base = {
        "schema_version": reconciliation.SCHEMA_VERSION,
        "unit_id": "reconciliation_1",
        "unit_status": "reconciled",
        "primary_msid": "Away.Crossing",
        "canonical_claim": "One grounded claim.",
        "members": [member],
        "authority_basis_atom_keys": [],
        "related_unit_ids": [],
        "rationale": "Bound test record.",
        "decision_origin": "provider_reviewed",
        "evidence": {
            "packet_sha256": "1" * 64,
            "proposal_response_sha256": "2" * 64,
            "review_response_sha256": "3" * 64,
        },
        "recorded_by": "test",
        "recorded_at": "2026-09-10T00:00:00+00:00",
    }
    duplicate = copy.deepcopy(base)
    duplicate["unit_id"] = "reconciliation_2"
    path = tmp_path / "units.jsonl"
    path.write_text(
        json.dumps(base) + "\n" + json.dumps(duplicate) + "\n",
        encoding="utf-8",
    )
    with pytest.raises(reconciliation.TriageError, match="multiple canonical"):
        reconciliation.ReconciliationStore(path, corpus)
