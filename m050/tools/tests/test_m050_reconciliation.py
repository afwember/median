import copy
from decimal import Decimal
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


def test_provider_comparison_reuses_exact_preserved_pilot_packet(corpus):
    packet = reconciliation.load_preserved_comparison_packet(ROOT, corpus)
    assert packet["tranche_id"] == reconciliation.COMPARISON_TRANCHE_ID
    assert len(packet["required_atom_keys"]) == 105
    assert packet["packet_sha256"] == (
        "45a5f84becb658d0d77b3588d4bb3c0d76a7b39486a9a063c8530c236ec4fcdc"
    )


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


def _ready_state():
    """Derive a READY lifecycle fixture without assuming the live run is stopped."""
    state = json.loads((ROOT / reconciliation.STATE).read_text(encoding="utf-8"))
    state["status"] = state["execution_state"] = "RECONCILIATION_READY"
    state["reconciliation"]["status"] = "READY"
    for key in (
        "repository_writes_authorized",
        "semantic_acceptance_authorized",
        "reconciliation_authorized",
        "provider_calls_authorized",
    ):
        state["authority"][key] = False
    state["spend"]["active"] = False
    state["dashboard"]["status"] = "READY — Stage 5 reconciliation"
    return state


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


def test_review_schema_binds_all_evidence_hashes(packet):
    proposal = _proposal(packet)
    proposal_sha = hashlib.sha256(
        reconciliation._canonical_bytes(proposal)
    ).hexdigest()
    schema = reconciliation.review_response_schema(packet, proposal_sha)
    properties = schema["properties"]
    assert properties["packet_id"] == {"type": "string", "const": packet["packet_id"]}
    assert properties["packet_sha256"] == {
        "type": "string", "const": packet["packet_sha256"]
    }
    assert properties["proposal_sha256"] == {"type": "string", "const": proposal_sha}
    assert properties["defects"]["items"]["type"] == "string"


def test_anthropic_response_completion_states_remain_distinct(packet):
    proposal = _proposal(packet)
    raw = {
        "type": "message",
        "role": "assistant",
        "stop_reason": "end_turn",
        "content": [{"type": "text", "text": json.dumps(proposal)}],
    }
    assert reconciliation.extract_anthropic_structured_response(raw) == proposal
    raw["stop_reason"] = "max_tokens"
    with pytest.raises(reconciliation.ContractError, match="max_tokens"):
        reconciliation.extract_anthropic_structured_response(raw)


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


def test_proposal_schema_binds_packet_and_rejects_empty_placeholders(packet):
    schema = reconciliation.proposal_response_schema(packet)
    properties = schema["properties"]
    assert properties["packet_id"] == {"type": "string", "const": packet["packet_id"]}
    assert properties["packet_sha256"] == {
        "type": "string", "const": packet["packet_sha256"]
    }
    unit = properties["units"]["items"]["properties"]
    assert unit["unit_local_id"]["pattern"] == r"^U[0-9]+$"
    assert unit["rationale"]["type"] == "string"
    assert unit["canonical_claim"]["anyOf"][0]["type"] == "string"
    assert json.dumps(schema).count('"pattern"') == 2


def test_proposal_validator_rejects_every_failed_placeholder_shape(packet, corpus):
    cases = [
        ("unit_local_id", "", "local IDs"),
        ("primary_msid", "", "non-current MSID"),
        ("canonical_claim", "", "lacks a claim"),
        ("rationale", "", "rationale is absent"),
    ]
    for field, value, message in cases:
        proposal = _proposal(packet)
        proposal["units"][0][field] = value
        with pytest.raises(reconciliation.TriageError, match=message):
            reconciliation.validate_proposal(packet, proposal, corpus)


def test_proposal_validator_rejects_blank_human_question(packet, corpus):
    proposal = _proposal(packet)
    unit = proposal["units"][0]
    unit["unit_status"] = "human_required"
    unit["primary_msid"] = None
    unit["canonical_claim"] = None
    unit["human_question"] = "  "
    with pytest.raises(reconciliation.TriageError, match="human-required proposal shape"):
        reconciliation.validate_proposal(packet, proposal, corpus)


def test_review_validator_rejects_blank_defect(packet):
    proposal = _proposal(packet)
    review = {
        "schema_version": reconciliation.REVIEW_SCHEMA_VERSION,
        "packet_id": packet["packet_id"],
        "packet_sha256": packet["packet_sha256"],
        "proposal_sha256": hashlib.sha256(
            reconciliation._canonical_bytes(proposal)
        ).hexdigest(),
        "verdict": "revise",
        "defects": ["  "],
    }
    with pytest.raises(reconciliation.TriageError, match="defects are invalid"):
        reconciliation.validate_review(packet, proposal, review)


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
    cached_packet = json.loads(proposer["messages"][0]["content"][0]["text"])
    assert cached_packet == packet
    assert proposer["max_tokens"] == 40000
    assert reviewer["max_tokens"] == 8000
    prefix_count_body = reconciliation._token_count_body(
        reviewer, cache_prefix_only=True
    )
    assert len(prefix_count_body["messages"][0]["content"]) == 1
    assert "max_tokens" not in prefix_count_body


def test_bounded_revision_hash_binds_prior_proposal_and_review(packet):
    provider = {
        "model": "claude-sonnet-5",
        "reasoning_effort": "high",
        "cache_ttl": "1h",
        "maximum_output_tokens": {"proposal": 36000, "review": 8000},
    }
    proposal = _proposal(packet)
    review = {
        "schema_version": reconciliation.REVIEW_SCHEMA_VERSION,
        "packet_id": packet["packet_id"],
        "packet_sha256": packet["packet_sha256"],
        "proposal_sha256": hashlib.sha256(
            reconciliation._canonical_bytes(proposal)
        ).hexdigest(),
        "verdict": "revise",
        "defects": ["Preserve one omitted grounded distinction."],
    }
    request = reconciliation.build_revision_request(
        packet, proposal, review, provider
    )
    supplemental = json.loads(request["messages"][0]["content"][-1]["text"])
    assert supplemental["prior_proposal"] == proposal
    assert supplemental["independent_review"] == review
    assert supplemental["prior_proposal_sha256"] == review["proposal_sha256"]
    assert supplemental["independent_review_sha256"] == hashlib.sha256(
        reconciliation._canonical_bytes(review)
    ).hexdigest()


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


def test_token_count_preflight_uses_free_anthropic_endpoint_twice(
    monkeypatch, tmp_path, packet
):
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


def test_anthropic_usage_cost_debits_all_cache_classes():
    state = json.loads((ROOT / reconciliation.STATE).read_text(encoding="utf-8"))
    provider = state["reconciliation"]["provider"]
    raw = {
        "usage": {
            "input_tokens": 700,
            "cache_read_input_tokens": 200,
            "cache_creation_input_tokens": 100,
            "cache_creation": {
                "ephemeral_5m_input_tokens": 0,
                "ephemeral_1h_input_tokens": 100,
            },
            "output_tokens": 50,
        }
    }
    updated, cost = reconciliation._debit_response(state, raw, provider)
    assert cost["uncached_input_usd"] == "0.0021"
    assert cost["cache_read_usd"] == "0.00006"
    assert cost["cache_1h_write_usd"] == "0.0006"
    assert cost["output_usd"] == "0.00075"
    assert cost["total_usd"] == "0.00351"
    assert Decimal(updated["spend"]["remaining_usd"]) == (
        Decimal(state["spend"]["remaining_usd"]) - Decimal("0.00351")
    )


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


def test_unchanged_max_token_failure_cannot_be_repeated(tmp_path):
    request = {"model": "test", "max_tokens": 8000}
    request_path = tmp_path / "review_001_request.json"
    request_path.write_text(json.dumps(request), encoding="utf-8")
    ledger = tmp_path / "run_ledger.jsonl"
    reconciliation._append_ledger(ledger, {
        "role": "review",
        "result": "mechanical_failure",
        "error": "Anthropic response did not end cleanly: max_tokens",
        "request": request_path.name,
    })
    with pytest.raises(reconciliation.TriageError, match="unchanged request"):
        reconciliation._reject_redundant_provider_request(
            tmp_path, ledger, "review", request
        )
    changed = dict(request, max_tokens=12000)
    reconciliation._reject_redundant_provider_request(
        tmp_path, ledger, "review", changed
    )


def test_completed_provider_comparison_cannot_be_repeated(tmp_path):
    ledger = tmp_path / "run_ledger.jsonl"
    reconciliation._append_ledger(ledger, {
        "role": "comparison_proposal",
        "result": "mechanically_valid",
    })
    with pytest.raises(reconciliation.TriageError, match="already complete"):
        reconciliation._reject_redundant_provider_request(
            tmp_path, ledger, "comparison_proposal", {"model": "test"}
        )


def test_ready_lifecycle_grants_nothing_and_spark_up_assessment_is_read_only(
    corpus, empty_store
):
    state = _ready_state()
    original = copy.deepcopy(state)
    assessed, report = reconciliation.plan_lifecycle_transition(
        state, corpus, empty_store, "prepare-spark-up"
    )
    assert assessed == original
    assert report["tranche_id"] == "away-crossing-squirrel-001"
    assert report["required_atoms"] == 65
    assert state["authority"]["repository_writes_authorized"] is False
    assert state["authority"]["reconciliation_authorized"] is False
    assert state["authority"]["provider_calls_authorized"] is False


def test_proceed_activates_reconciliation_and_preconfigured_provider(
    corpus, empty_store
):
    state = _ready_state()
    active, report = reconciliation.plan_lifecycle_transition(
        state,
        corpus,
        empty_store,
        "activate-on-proceed",
        expected_tranche_id="away-crossing-squirrel-001",
    )
    assert report["activated"] is True
    assert active["status"] == "RECONCILIATION_ACTIVE"
    assert active["authority"]["repository_writes_authorized"] is True
    assert active["authority"]["reconciliation_authorized"] is True
    assert active["authority"]["semantic_acceptance_authorized"] is True
    assert active["authority"]["provider_calls_authorized"] is True
    assert active["spend"]["active"] is True
    assert active["spend"]["remaining_usd"] == state["spend"]["remaining_usd"]


def test_stopdown_rejects_incomplete_tranche(corpus, empty_store):
    state = _ready_state()
    active, _ = reconciliation.plan_lifecycle_transition(
        state,
        corpus,
        empty_store,
        "activate-on-proceed",
        expected_tranche_id="away-crossing-squirrel-001",
    )
    with pytest.raises(reconciliation.TriageError, match="complete tranche coverage"):
        reconciliation.plan_lifecycle_transition(
            active, corpus, empty_store, "prepare-stopdown"
        )


def test_stopdown_revokes_unused_one_time_spend():
    state = json.loads((ROOT / reconciliation.STATE).read_text(encoding="utf-8"))
    state["spend"].update({
        "active": True,
        "refresh_window_usd": "5.0000000",
        "authorized_usd": "55.0000000",
        "cumulative_spent_usd": "53.2500000",
        "remaining_usd": "1.7500000",
    })
    reconciliation._revoke_one_time_spend_on_stopdown(state)
    assert state["spend"]["active"] is False
    assert state["spend"]["refresh_window_usd"] == "2.0000000"
    assert state["spend"]["authorized_usd"] == "53.2500000"
    assert state["spend"]["remaining_usd"] == "0.0000000"


def test_completed_tranche_dashboard_cannot_offer_same_pilot(empty_store):
    state = json.loads((ROOT / reconciliation.STATE).read_text(encoding="utf-8"))
    state["reconciliation"]["target"] = {
        "tranche_id": "away-crossing-pilot",
        "msid_prefix": "Away.Crossing",
        "selector": "exact",
    }
    dashboard = reconciliation._dashboard(state, empty_store, active=False)
    assert dashboard["now"] == (
        "Away.Crossing pilot is complete; the Compile Worker is Stopped Down"
    )
    assert dashboard["next"] == (
        "Supervisor/author quality adjudication must select any next boundary"
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
