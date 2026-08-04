import copy
from decimal import Decimal
import hashlib
import importlib.util
import json
from pathlib import Path
from types import SimpleNamespace

import pytest

from median_gate5.errors import ContractError, IntegrityError
from median_gate5.extraction_machine import (
    anthropic_usage_cost,
    append_run_ledger_event,
    build_anthropic_request,
    build_chunk_payload,
    build_generic_response_schema,
    build_generic_source_prompt,
    conservative_call_ceiling,
    debit_compile_state_spend,
    draft_block_dispositions,
    extract_anthropic_structured_response,
    read_run_ledger,
    plan_source_chunks,
    provider_preflight,
    require_run_ready_for_next_call,
    validate_extraction_response,
)


ROOT = Path(__file__).parents[4]
AUTHGRAM = ROOT / "m050/extraction/calibration/authorial-grammar"
MACHINE_TOOL = ROOT / "m050/tools/m050_extraction_machine_v0_1.py"
AUTHGRAM_CONFIG = ROOT / "m050/extraction/control/M050_Authorial_Grammar_Extraction_Machine_Config_v0_6_MEDIANv0_5_0.json"
COMPILE_STATE = ROOT / "m050/extraction/control/M050_Compile_State_MEDIANv0_5_0.json"
CURRENT_PACKET = ROOT / "m050/extraction/runs/authorial-grammar-target-coverage-calibration/M050_Authorial_Grammar_Target_Coverage_C0003_Call_Packet_v0_15_MEDIANv0_5_0.json"
CURRENT_LEDGER = ROOT / "m050/extraction/runs/authorial-grammar-target-coverage-calibration/M050_Authorial_Grammar_Target_Coverage_Run_Ledger_v0_11_MEDIANv0_5_0.jsonl"
ACCEPTED_C0001_PACKET = ROOT / "m050/extraction/runs/authorial-grammar-structural-source/M050_Authorial_Grammar_Structural_C0001_Call_Packet_v0_4_MEDIANv0_5_0.json"
ACCEPTED_C0001_OUTCOME = ROOT / "m050/extraction/runs/authorial-grammar-structural-source/M050_Authorial_Grammar_Structural_C0001_Outcome_v0_4_MEDIANv0_5_0.json"
ACCEPTED_C0001_RAW = ROOT / "m050/extraction/runs/authorial-grammar-structural-source/M050_Authorial_Grammar_Structural_C0001_Raw_Response_v0_4_MEDIANv0_5_0.json"
SECOND_SOURCE_MANIFEST = ROOT / "m050/extraction/control/source-identities/blocks/M050_Human_Rulings_Block_Manifest_v0_1_MEDIANv0_5_0.json"


def _json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def _jsonl(path):
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines()]


def _pricing():
    return {
        "input_usd_per_million_tokens": "2",
        "output_usd_per_million_tokens": "10",
        "cache_read_multiplier": "0.1",
        "cache_5m_write_multiplier": "1.25",
        "cache_1h_write_multiplier": "2",
    }


def _simple_manifest():
    return {
        "source_id": "M050-SRC-TEST-001",
        "source_sha256": "a" * 64,
        "blocks": [
            {"block_id": "B1", "block_type": "heading", "text": "# Rules\n", "status_markers": []},
            {"block_id": "B2", "block_type": "paragraph", "text": "A thing must happen.\n", "status_markers": []},
            {"block_id": "B3", "block_type": "whitespace", "text": "\n", "status_markers": []},
        ],
    }


def test_payload_is_source_agnostic_and_accounts_for_exclusions():
    payload = build_chunk_payload(
        _simple_manifest(),
        [
            {"block_id": "B1", "disposition": "context_only"},
            {"block_id": "B2", "disposition": "eligible"},
            {"block_id": "B3", "disposition": "excluded"},
        ],
        {"chunk_id": "C0001", "block_ids": ["B1", "B2", "B3"]},
    )
    assert payload["source_id"] == "M050-SRC-TEST-001"
    assert [item["block_id"] for item in payload["context_blocks"]] == ["B1"]
    assert [item["block_id"] for item in payload["target_blocks"]] == ["B2"]
    assert payload["excluded_block_ids"] == ["B3"]
    assert len(payload["payload_sha256"]) == 64


def test_request_caches_only_stable_system_prefix_for_one_hour():
    request = build_anthropic_request(
        prompt="Stable source policy",
        response_schema={"type": "object", "properties": {"dispositions": {"type": "array"}}},
        payload={"source_id": "S", "required_target_disposition_count": 1, "target_blocks": [{"block_id": "B1"}]},
        model="claude-sonnet-5",
        reasoning_effort="low",
        maximum_output_tokens=6000,
        cache_ttl="1h",
    )
    assert request["system"][0] == {
        "type": "text",
        "text": "Stable source policy",
        "cache_control": {"type": "ephemeral", "ttl": "1h"},
    }
    assert request["system"][1]["text"].startswith("BOUND_RESPONSE_SCHEMA\n")
    assert "cache_control" not in request["system"][1]
    assert request["output_config"]["format"]["schema"]["properties"]["dispositions"]["minItems"] == 1
    assert "maxItems" not in request["output_config"]["format"]["schema"]["properties"]["dispositions"]
    assert "cache_control" not in request["messages"][0]


def test_generic_validator_replays_accepted_authorial_c0001():
    payload = _json(ACCEPTED_C0001_PACKET)["payload"]
    response = _json(ACCEPTED_C0001_OUTCOME)["structured_proposal"]
    schema = _json(AUTHGRAM / "M050_Authorial_Grammar_Pilot_001_R6_Response_Schema_v0_6_MEDIANv0_5_0.json")
    report = validate_extraction_response(
        payload=payload,
        response=response,
        response_schema=schema,
        allowed_streams=["evidence_authorial_rule"],
    )
    assert report["passed"] is True
    assert report["errors"] == []
    assert report["checks"]["review_required_blocks"] == 0


def test_extracts_accepted_c0001_from_raw_anthropic_envelope():
    raw = _json(ACCEPTED_C0001_RAW)
    structured = extract_anthropic_structured_response(raw)
    assert structured["source_id"] == "M050-SRC-AUTHORIAL-GRAMMAR-001"
    assert len(structured["dispositions"]) == 15

    raw["stop_reason"] = "max_tokens"
    with pytest.raises(ContractError, match="did not end cleanly"):
        extract_anthropic_structured_response(raw)


def test_generic_validator_fails_closed_for_source_stream_and_coverage_drift():
    payload = {
        "source_id": "S1",
        "target_blocks": [
            {"block_id": "B1", "text": "Do the thing.\n", "status_markers": []}
        ],
        "context_blocks": [],
        "excluded_block_ids": [],
    }
    schema = {"type": "object"}
    response = {
        "source_id": "S2",
        "dispositions": [
            {
                "block_id": "B1",
                "kind": "atoms",
                "atoms": [
                    {
                        "proposal_id": "P1",
                        "source_id": "S2",
                        "block_id": "B1",
                        "stream": "wrong",
                        "exact_source_text": "invented",
                        "normalized_claim": "Invented",
                    }
                ],
            }
        ],
    }
    report = validate_extraction_response(
        payload=payload,
        response=response,
        response_schema=schema,
        allowed_streams=["allowed"],
    )
    assert report["passed"] is False
    assert report["decision_required"] is True
    assert any("source_id" in error for error in report["errors"])
    assert any("stream" in error for error in report["errors"])
    assert any("ground" in error for error in report["errors"])


def test_validator_requires_table_headers_and_delimiters_to_be_non_substantive():
    payload = {
        "source_id": "S1",
        "target_blocks": [
            {"block_id": "B1", "block_type": "table_row", "text": "| Construction | Meaning | Example |\n", "status_markers": []},
            {"block_id": "B2", "block_type": "table_row", "text": "|---|:---:|---:|\n", "status_markers": []},
            {"block_id": "B3", "block_type": "table_row", "text": "| Bare singular | Archetypal body | Mouse builds. |\n", "status_markers": []},
        ],
        "context_blocks": [],
        "excluded_block_ids": [],
    }
    schema = build_generic_response_schema("S1", ["allowed"])
    response = {
        "schema_version": "M050-EVIDENCE-PROPOSAL-0.1",
        "proposal_set_id": "table-test",
        "request_id": "table-test",
        "source_id": "S1",
        "dispositions": [
            {
                "block_id": "B1",
                "kind": "atoms",
                "atoms": [{
                    "proposal_id": "P1", "source_id": "S1", "block_id": "B1",
                    "exact_source_text": "| Construction | Meaning | Example |",
                    "normalized_claim": "The table has three columns.",
                    "claim_kind": "layout", "stream": "allowed",
                }],
            },
            {"block_id": "B2", "kind": "no_substantive_claim", "atoms": []},
            {
                "block_id": "B3",
                "kind": "atoms",
                "atoms": [{
                    "proposal_id": "P2", "source_id": "S1", "block_id": "B3",
                    "exact_source_text": "| Bare singular | Archetypal body | Mouse builds. |",
                    "normalized_claim": "Bare singular denotes an archetypal body.",
                    "claim_kind": "rule", "stream": "allowed",
                }],
            },
        ],
    }
    rejected = validate_extraction_response(
        payload=payload, response=response, response_schema=schema,
        allowed_streams=["allowed"],
    )
    assert rejected["passed"] is False
    assert rejected["checks"]["table_structure_errors"] == 1
    assert any("structural table header" in error for error in rejected["errors"])

    response["dispositions"][0] = {
        "block_id": "B1", "kind": "no_substantive_claim", "atoms": []
    }
    accepted = validate_extraction_response(
        payload=payload, response=response, response_schema=schema,
        allowed_streams=["allowed"],
    )
    assert accepted["passed"] is True
    assert accepted["checks"]["table_structure_errors"] == 0


def test_payload_marks_pure_structural_labels_and_validator_enforces_nonclaim():
    manifest = {
        "source_id": "S1", "source_sha256": "c" * 64,
        "blocks": [
            {"block_id": "B1", "block_type": "paragraph", "text": "Prefer:\n", "status_markers": []},
            {"block_id": "B2", "block_type": "code_fence", "text": "```text\nGood example.\n```\n", "status_markers": []},
            {"block_id": "B3", "block_type": "paragraph", "text": "Plural nouns take plural agreement:\n", "status_markers": []},
        ],
    }
    payload = build_chunk_payload(
        manifest,
        [
            {"block_id": "B1", "disposition": "eligible"},
            {"block_id": "B2", "disposition": "context_only"},
            {"block_id": "B3", "disposition": "eligible"},
        ],
        {"chunk_id": "C0001", "block_ids": ["B1", "B2", "B3"]},
    )
    targets = {block["block_id"]: block for block in payload["target_blocks"]}
    assert targets["B1"]["structural_role"] == "pure_example_or_polarity_label"
    assert targets["B1"]["required_disposition"] == "no_substantive_claim"
    assert "required_disposition" not in targets["B3"]

    schema = build_generic_response_schema("S1", ["allowed"])
    response = {
        "schema_version": "M050-EVIDENCE-PROPOSAL-0.1",
        "proposal_set_id": "label-test", "request_id": "label-test", "source_id": "S1",
        "dispositions": [
            {
                "block_id": "B1", "kind": "atoms",
                "atoms": [{
                    "proposal_id": "P1", "source_id": "S1", "block_id": "B1",
                    "exact_source_text": "Prefer:",
                    "normalized_claim": "A preferred example follows.",
                    "claim_kind": "layout", "stream": "allowed",
                }],
            },
            {
                "block_id": "B3", "kind": "atoms",
                "atoms": [{
                    "proposal_id": "P2", "source_id": "S1", "block_id": "B3",
                    "exact_source_text": "Plural nouns take plural agreement:",
                    "normalized_claim": "Plural nouns take plural agreement.",
                    "claim_kind": "rule", "stream": "allowed",
                }],
            },
        ],
    }
    rejected = validate_extraction_response(
        payload=payload, response=response, response_schema=schema,
        allowed_streams=["allowed"],
    )
    assert rejected["passed"] is False
    assert rejected["checks"]["required_disposition_errors"] == 1
    response["dispositions"][0] = {
        "block_id": "B1", "kind": "no_substantive_claim", "atoms": []
    }
    accepted = validate_extraction_response(
        payload=payload, response=response, response_schema=schema,
        allowed_streams=["allowed"],
    )
    assert accepted["passed"] is True


def test_payload_marks_semantic_inventories_substantive_or_review_required():
    manifest = {
        "source_id": "S1", "source_sha256": "c" * 64,
        "blocks": [
            {"block_id": "B1", "block_type": "code_fence", "text": "```text\nDefined Example\n```\n", "status_markers": []},
        ],
    }
    payload = build_chunk_payload(
        manifest,
        [{
            "block_id": "B1", "disposition": "eligible",
            "reason_code": "semantic_code_or_reference_inventory",
        }],
        {"chunk_id": "C0001", "block_ids": ["B1"]},
    )
    target = payload["target_blocks"][0]
    assert target["structural_role"] == "semantic_code_or_reference_inventory"
    assert target["allowed_dispositions"] == ["atoms", "review_required"]

    schema = build_generic_response_schema("S1", ["allowed"])
    response = {
        "schema_version": "M050-EVIDENCE-PROPOSAL-0.1",
        "proposal_set_id": "inventory-test", "request_id": "inventory-test", "source_id": "S1",
        "dispositions": [{"block_id": "B1", "kind": "no_substantive_claim", "atoms": []}],
    }
    rejected = validate_extraction_response(
        payload=payload, response=response, response_schema=schema,
        allowed_streams=["allowed"],
    )
    assert rejected["passed"] is False
    assert rejected["checks"]["required_disposition_errors"] == 1
    response["dispositions"][0] = {
        "block_id": "B1", "kind": "review_required", "atoms": []
    }
    review = validate_extraction_response(
        payload=payload, response=response, response_schema=schema,
        allowed_streams=["allowed"],
    )
    assert review["passed"] is True
    assert review["decision_required"] is True


def test_cache_aware_cost_accounting_matches_uncached_r6_and_cached_examples():
    uncached = anthropic_usage_cost(
        {
            "input_tokens": 6595,
            "output_tokens": 5665,
            "cache_creation_input_tokens": 0,
            "cache_read_input_tokens": 0,
        },
        _pricing(),
        cache_ttl="1h",
    )
    assert uncached["total_usd"] == "0.06984"
    assert uncached["display_usd_rounded_up"] == "0.07"

    cached = anthropic_usage_cost(
        {
            "input_tokens": 1000,
            "output_tokens": 500,
            "cache_creation_input_tokens": 4000,
            "cache_read_input_tokens": 3000,
            "cache_creation": {
                "ephemeral_5m_input_tokens": 0,
                "ephemeral_1h_input_tokens": 4000,
            },
        },
        _pricing(),
        cache_ttl="1h",
    )
    assert cached["uncached_input_usd"] == "0.002"
    assert cached["cache_1h_write_usd"] == "0.016"
    assert cached["cache_read_usd"] == "0.0006"
    assert cached["output_usd"] == "0.005"
    assert cached["total_usd"] == "0.0236"
    assert cached["display_usd_rounded_up"] == "0.03"


def _compile_state(*, source_id="S1", spent="1.92", authorized=True):
    return {
        "schema_version": "M050-COMPILE-STATE-1.0",
        "source": {
            "id": source_id,
            "source_work_authorized": authorized,
            "whole_source_candidate_complete": False,
        },
        "authority": {
            "repository_writes_authorized": authorized,
            "source_work_authorized": authorized,
        },
        "calibration": {"offline_gate_passed": True},
        "spend": {
            "active": True,
            "authorized_usd": "2.00",
            "cumulative_spent_usd": spent,
            "remaining_usd": format(Decimal("2.00") - Decimal(spent), "f"),
            "display_usd_rounded_up": f"{Decimal(spent):.2f}",
        },
    }


def test_source_grant_plus_budget_derives_provider_permission():
    request = build_anthropic_request(
        prompt="policy",
        response_schema={"type": "object", "properties": {"dispositions": {"type": "array"}}},
        payload={"source_id": "S1", "required_target_disposition_count": 1, "target_blocks": [{"block_id": "B1"}]},
        model="claude-sonnet-5",
        reasoning_effort="low",
        maximum_output_tokens=100,
        cache_ttl="1h",
    )
    ceiling = conservative_call_ceiling(request, _pricing())
    uncached_request = copy.deepcopy(request)
    uncached_request["system"][0].pop("cache_control")
    assert ceiling > conservative_call_ceiling(uncached_request, _pricing())
    result = provider_preflight(
        compile_state=_compile_state(),
        source_id="S1",
        call_ceiling_usd=ceiling,
    )
    assert result["permission_basis"] == "active_source_work_plus_cumulative_budget"
    assert Decimal(result["remaining_after_reservation_usd"]) >= 0

    with pytest.raises(ContractError, match="source-work"):
        provider_preflight(
            compile_state=_compile_state(authorized=False),
            source_id="S1",
            call_ceiling_usd=ceiling,
        )


def test_budget_halts_before_next_call_and_debits_canonical_state():
    with pytest.raises(ContractError, match="cannot cover"):
        provider_preflight(
            compile_state=_compile_state(),
            source_id="S1",
            call_ceiling_usd=Decimal("0.081"),
        )
    original = _compile_state()
    updated = debit_compile_state_spend(original, "0.06984")
    assert updated["spend"]["cumulative_spent_usd"] == "1.98984"
    assert updated["spend"]["remaining_usd"] == "0.01016"
    assert updated["spend"]["display_usd_rounded_up"] == "1.99"
    assert original["spend"]["cumulative_spent_usd"] == "1.92"


def test_budget_never_selects_or_advances_a_source():
    with pytest.raises(ContractError, match="does not cover"):
        provider_preflight(
            compile_state=_compile_state(),
            source_id="S2",
            call_ceiling_usd=Decimal("0.01"),
        )
    complete = _compile_state()
    complete["source"]["whole_source_candidate_complete"] = True
    with pytest.raises(ContractError, match="already complete"):
        provider_preflight(
            compile_state=complete,
            source_id="S1",
            call_ceiling_usd=Decimal("0.01"),
        )


def test_compact_run_ledger_allows_validated_replacement_after_failure(tmp_path):
    ledger = tmp_path / "run.jsonl"
    assert require_run_ready_for_next_call(
        read_run_ledger(ledger), "S1", "C0001", "a" * 64
    ) == 0
    captured = append_run_ledger_event(
        ledger,
        {
            "state": "call_captured",
            "source_id": "S1",
            "chunk_id": "C0001",
            "packet_file_sha256": "a" * 64,
            "outcome_sha256": "o" * 64,
        },
    )
    assert captured["sequence"] == 1
    with pytest.raises(ContractError, match="prior outcome"):
        require_run_ready_for_next_call(
            read_run_ledger(ledger), "S1", "C0001", "a" * 64
        )
    failed = append_run_ledger_event(
        ledger,
        {
            "state": "review_failed",
            "source_id": "S1",
            "chunk_id": "C0001",
            "outcome_sha256": "o" * 64,
        },
    )
    assert failed["predecessor_event_sha256"]
    with pytest.raises(ContractError, match="must be corrected"):
        require_run_ready_for_next_call(
            read_run_ledger(ledger), "S1", "C0001", "a" * 64
        )
    assert require_run_ready_for_next_call(
        read_run_ledger(ledger), "S1", "C0001", "b" * 64
    ) == 1
    with pytest.raises(ContractError, match="before advancing"):
        require_run_ready_for_next_call(
            read_run_ledger(ledger), "S1", "C0002", "b" * 64
        )
    with pytest.raises(ContractError, match="another source"):
        require_run_ready_for_next_call(
            read_run_ledger(ledger), "S2", "C0001", "b" * 64
        )


def test_authorial_full_plan_prepares_source_agnostically_with_stable_cache_prefix(tmp_path):
    spec = importlib.util.spec_from_file_location("m050_extraction_machine", MACHINE_TOOL)
    assert spec is not None and spec.loader is not None
    tool = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(tool)

    target_ids = []
    context_ids = []
    excluded_ids = []
    stable_prompt_prefixes = []
    packets = []
    config = _json(AUTHGRAM_CONFIG)
    plan = _json(ROOT / config["artifacts"]["chunk_plan"])
    chunk_ids = [chunk["chunk_id"] for chunk in plan["chunks"]]
    for chunk_id in chunk_ids:
        packet = tool.build_packet(ROOT, AUTHGRAM_CONFIG, chunk_id)
        packets.append(packet)
        assert packet["source_id"] == "M050-SRC-AUTHORIAL-GRAMMAR-001"
        assert packet["binding"]["cache_ttl"] == "1h"
        assert packet["binding"]["cache_required"] is True
        assert Decimal(packet["cache_miss_call_ceiling_usd"]) > 0
        payload = packet["payload"]
        chunk_targets = [item["block_id"] for item in payload["target_blocks"]]
        chunk_context = [item["block_id"] for item in payload["context_blocks"]]
        chunk_excluded = payload["excluded_block_ids"]
        assert payload["required_target_disposition_count"] == len(chunk_targets)
        dispositions_schema = packet["provider_request"]["output_config"]["format"]["schema"]["properties"]["dispositions"]
        assert dispositions_schema["minItems"] == 1
        assert "maxItems" not in dispositions_schema
        target_ids.extend(chunk_targets)
        context_ids.extend(chunk_context)
        excluded_ids.extend(chunk_excluded)
        stable_prompt_prefixes.append(packet["provider_request"]["system"][0])

    manifest = _json(ROOT / config["artifacts"]["block_manifest"])
    primary_ids = [block_id for chunk in plan["chunks"] for block_id in chunk["block_ids"]]
    assert primary_ids == [block["block_id"] for block in manifest["blocks"]]
    assert len(target_ids) == len(set(target_ids)) == 228
    assert len(excluded_ids) == len(set(excluded_ids)) == 280
    assert all(len(packet["payload"]["target_blocks"]) <= 20 for packet in packets)
    assert plan["quantization"]["generated_chunk_count"] == len(chunk_ids) == 13
    assert plan["quantization"]["chunk_count_is_input"] is False
    assert context_ids
    assert all(prefix == stable_prompt_prefixes[0] for prefix in stable_prompt_prefixes)
    assert stable_prompt_prefixes[0]["cache_control"] == {
        "type": "ephemeral",
        "ttl": "1h",
    }

    state = _compile_state(
        source_id=packets[0]["source_id"], spent="0.00", authorized=True
    )
    state["calibration"].update({
        "configuration": packets[0]["configuration_path"],
        "pilot_chunk_id": packets[0]["chunk_id"],
        "cache_miss_call_ceiling_usd": packets[0]["cache_miss_call_ceiling_usd"],
    })
    packet_hash = hashlib.sha256(tool.canonical_json_bytes(packets[0])).hexdigest()
    preflight = tool._preflight(
        packets[0], packet_hash, state, tmp_path / "run.jsonl", ROOT
    )
    assert preflight["reserved_call_ceiling_usd"] == packets[0]["cache_miss_call_ceiling_usd"]
    tampered = copy.deepcopy(packets[0])
    tampered["payload"]["target_blocks"][0]["text"] += "tampered"
    tampered_body = dict(tampered)
    tampered_body.pop("packet_sha256")
    tampered["packet_sha256"] = hashlib.sha256(
        tool.canonical_json_bytes(tampered_body)
    ).hexdigest()
    with pytest.raises(IntegrityError, match="deterministic current configuration"):
        tool._preflight(
            tampered,
            hashlib.sha256(tool.canonical_json_bytes(tampered)).hexdigest(),
            state,
            tmp_path / "run.jsonl",
            ROOT,
        )
    with pytest.raises(ContractError, match="current canonical chunk"):
        tool._preflight(
            packets[1],
            hashlib.sha256(tool.canonical_json_bytes(packets[1])).hexdigest(),
            state,
            tmp_path / "run.jsonl",
            ROOT,
        )


def test_second_spec_doc_scaffolds_without_source_specific_worker_code():
    manifest = _json(SECOND_SOURCE_MANIFEST)
    dispositions = draft_block_dispositions(manifest)
    assert len(dispositions) == len(manifest["blocks"])
    assert all(item["draft_requires_identity_review"] for item in dispositions)
    plan = plan_source_chunks(
        manifest,
        dispositions,
        max_input_tokens=1800,
        target_blocks_per_chunk=60,
        quantization_basis="offline test calibration",
    )
    primary = [block_id for chunk in plan["chunks"] for block_id in chunk["block_ids"]]
    assert primary == [block["block_id"] for block in manifest["blocks"]]
    assert all(chunk["estimated_input_tokens"] <= 1800 for chunk in plan["chunks"])
    assert all(chunk["target_blocks"] <= 60 for chunk in plan["chunks"])
    assert plan["quantization"] == {
        "unit": "provider_eligible_target_blocks",
        "target_blocks_per_chunk": 60,
        "basis": "offline test calibration",
        "generated_chunk_count": len(plan["chunks"]),
        "chunk_count_is_input": False,
    }

    schema = build_generic_response_schema(
        manifest["source_id"], ["evidence_game_semantic"]
    )
    prompt = build_generic_source_prompt(
        manifest["source_id"],
        ["evidence_game_semantic"],
        "Extract this source's own claims without importing other sources.",
    )
    payload = build_chunk_payload(manifest, dispositions, plan["chunks"][0])
    request = build_anthropic_request(
        prompt=prompt,
        response_schema=schema,
        payload=payload,
        model="claude-sonnet-5",
        reasoning_effort="low",
        maximum_output_tokens=6000,
        cache_ttl="1h",
    )
    assert request["system"][0]["cache_control"]["ttl"] == "1h"
    fake = {
        "schema_version": "M050-EVIDENCE-PROPOSAL-0.1",
        "proposal_set_id": "offline-fake",
        "request_id": "offline-fake",
        "source_id": manifest["source_id"],
        "dispositions": [
            {"block_id": block["block_id"], "kind": "no_substantive_claim", "atoms": []}
            for block in payload["target_blocks"]
        ],
    }
    report = validate_extraction_response(
        payload=payload,
        response=fake,
        response_schema=schema,
        allowed_streams=["evidence_game_semantic"],
    )
    assert report["passed"] is True
    assert report["decision_required"] is True


def _structural_manifest():
    block_types_and_text = [
        ("heading", "# Structural examples\n"),
        ("paragraph", "The rules are:\n"),
        ("whitespace", "\n"),
        ("list_item", "- first;\n"),
        ("list_item", "- second.\n"),
        ("paragraph", "The matrix is:\n"),
        ("whitespace", "\n"),
        ("table_row", "| A | B |\n"),
        ("table_row", "|---|---|\n"),
        ("table_row", "| one | two |\n"),
        ("paragraph", "Example:\n"),
        ("whitespace", "\n"),
        ("code_fence", "```text\none\n```\n"),
        ("paragraph", "In-world rendering:\n"),
        ("whitespace", "\n"),
        ("paragraph", "> One voice.\n"),
        ("whitespace", "\n"),
        ("paragraph", "> The same voice.\n"),
        ("paragraph", "The plate is titled:\n"),
        ("whitespace", "\n"),
        ("heading", "## THE PLATE\n"),
        ("whitespace", "\n"),
        ("table_row", "| Label | Value |\n"),
        ("table_row", "|---|---|\n"),
        ("table_row", "| alpha | beta |\n"),
    ]
    return {
        "source_id": "M050-SRC-STRUCTURAL-TEST-001",
        "source_sha256": "b" * 64,
        "blocks": [
            {
                "block_id": f"B{index:04d}",
                "block_type": block_type,
                "text": block_text,
                "status_markers": [],
            }
            for index, (block_type, block_text) in enumerate(block_types_and_text, 1)
        ],
    }


def _structural_dispositions(manifest):
    return [
        {
            "block_id": block["block_id"],
            "disposition": (
                "excluded"
                if block["block_type"] == "whitespace"
                else "context_only"
                if block["block_type"] == "heading"
                else "eligible"
            ),
        }
        for block in manifest["blocks"]
    ]


def test_chunk_planning_keeps_semantic_lead_ins_and_dependent_bodies_indivisible():
    manifest = _structural_manifest()
    plan = plan_source_chunks(
        manifest,
        _structural_dispositions(manifest),
        max_input_tokens=1800,
        target_blocks_per_chunk=4,
        quantization_basis="structural grouping test",
    )
    chunk_for = {
        block_id: chunk["chunk_id"]
        for chunk in plan["chunks"]
        for block_id in chunk["block_ids"]
    }
    for group in (
        range(2, 6),
        range(6, 11),
        range(11, 14),
        range(14, 19),
        range(19, 26),
    ):
        assert len({chunk_for[f"B{index:04d}"] for index in group}) == 1
    assert [block_id for chunk in plan["chunks"] for block_id in chunk["block_ids"]] == [
        block["block_id"] for block in manifest["blocks"]
    ]


def test_chunk_planning_fails_when_complete_semantic_group_exceeds_quantization():
    manifest = _structural_manifest()
    with pytest.raises(ContractError, match="indivisible structural group exceeds chunk limits: B0006"):
        plan_source_chunks(
            manifest,
            _structural_dispositions(manifest),
            max_input_tokens=1800,
            target_blocks_per_chunk=3,
            quantization_basis="structural grouping test",
        )


def test_scaffold_command_writes_provider_disabled_source_package(tmp_path):
    spec = importlib.util.spec_from_file_location("m050_extraction_machine_scaffold", MACHINE_TOOL)
    assert spec is not None and spec.loader is not None
    tool = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(tool)

    repo = tmp_path / "repo"
    source = repo / "m050/docs/spec.md"
    card = repo / "m050/extraction/control/card.md"
    source.parent.mkdir(parents=True)
    card.parent.mkdir(parents=True)
    source.write_text("# Test source\n\nA rule applies.\n", encoding="utf-8")
    card.write_text(
        "# Approved boundary\n\nStatus: `APPROVED`\n"
        "Author/root of authority: Asa Wember\n\nOnly this source is in scope.\n",
        encoding="utf-8",
    )
    base = "m050/extraction/onboarding/test"
    args = SimpleNamespace(
        repo_root=str(repo),
        source_id="M050-SRC-TEST-SPEC-001",
        source_path="m050/docs/spec.md",
        identity_card="m050/extraction/control/card.md",
        allowed_stream=["evidence_game_semantic"],
        max_input_tokens=12000,
        target_blocks_per_chunk=50,
        model="claude-sonnet-5",
        reasoning_effort="low",
        maximum_output_tokens=6000,
        output_block_manifest=f"{base}/manifest.json",
        output_disposition_ledger=f"{base}/dispositions.jsonl",
        output_chunk_plan=f"{base}/plan.json",
        output_prompt=f"{base}/prompt.md",
        output_response_schema=f"{base}/schema.json",
        output_config=f"{base}/config.json",
    )
    assert tool.command_scaffold(args) == 0
    config = _json(repo / f"{base}/config.json")
    assert config["status"] == "DRAFT_REQUIRES_SOURCE_REVIEW_AND_PILOT_CALIBRATION"
    assert config["execution"] == {
        "cadence": "sequential_one_call_review",
        "next_chunk_requires_substantive_review_of_prior_chunk": True,
    }
    loaded, paths = tool.load_config(repo, repo / f"{base}/config.json")
    assert loaded["source_id"] == "M050-SRC-TEST-SPEC-001"
    assert set(paths) == {
        "identity_card", "block_manifest",
        "disposition_ledger", "chunk_plan", "prompt", "response_schema",
    }


def test_identity_card_approval_is_checked_without_parallel_receipt(tmp_path):
    spec = importlib.util.spec_from_file_location("m050_extraction_machine_identity", MACHINE_TOOL)
    assert spec is not None and spec.loader is not None
    tool = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(tool)
    card = tmp_path / "card.md"
    card.write_text(
        "# Draft boundary\n\nStatus: `DRAFT_AWAITING_AUTHOR_REVIEW`\n"
        "Author/root of authority: Asa Wember\n",
        encoding="utf-8",
    )
    with pytest.raises(ContractError, match="not marked APPROVED"):
        tool.require_approved_identity_card(card)


def test_replan_reapportions_complete_source_from_calibrated_quantization(tmp_path):
    spec = importlib.util.spec_from_file_location("m050_extraction_machine_replan", MACHINE_TOOL)
    assert spec is not None and spec.loader is not None
    tool = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(tool)
    output = tmp_path / "replanned.json"
    args = SimpleNamespace(
        repo_root=str(ROOT),
        block_manifest="m050/extraction/control/source-identities/blocks/M050_Authorial_Grammar_Block_Manifest_v0_1_MEDIANv0_5_0.json",
        disposition_ledger="m050/extraction/calibration/authorial-grammar/M050_Authorial_Grammar_Block_Disposition_Ledger_v0_1_MEDIANv0_5_0.jsonl",
        max_input_tokens=1800,
        target_blocks_per_chunk=20,
        calibration_basis="23 complete dispositions exhausted 6000 output tokens; quantized to 20",
        predecessor_chunk_plan="historical-plan.json",
        output_chunk_plan=str(output.relative_to(ROOT)) if output.is_relative_to(ROOT) else "m050/extraction/control/replanned.json",
    )
    if not output.is_relative_to(ROOT):
        repo = tmp_path / "repo"
        repo.mkdir()
        manifest_source = ROOT / args.block_manifest
        disposition_source = ROOT / args.disposition_ledger
        manifest_target = repo / args.block_manifest
        disposition_target = repo / args.disposition_ledger
        manifest_target.parent.mkdir(parents=True)
        disposition_target.parent.mkdir(parents=True)
        manifest_target.write_bytes(manifest_source.read_bytes())
        disposition_target.write_bytes(disposition_source.read_bytes())
        args.repo_root = str(repo)
        args.output_chunk_plan = "m050/extraction/control/replanned.json"
        output = repo / args.output_chunk_plan
    assert tool.command_replan(args) == 0
    plan = _json(output)
    assert plan["quantization"]["target_blocks_per_chunk"] == 20
    assert plan["quantization"]["chunk_count_is_input"] is False
    assert all(chunk["target_blocks"] <= 20 for chunk in plan["chunks"])
    assert [block_id for chunk in plan["chunks"] for block_id in chunk["block_ids"]] == [
        block["block_id"] for block in _json(Path(args.repo_root) / args.block_manifest)["blocks"]
    ]


def test_accepted_chunk_cannot_retry_after_source_completion():
    spec = importlib.util.spec_from_file_location("m050_extraction_machine_retry", MACHINE_TOOL)
    assert spec is not None and spec.loader is not None
    tool = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(tool)
    packet = _json(CURRENT_PACKET)
    state = _json(COMPILE_STATE)
    with pytest.raises(ContractError, match="accepted chunk cannot be called again"):
        require_run_ready_for_next_call(
            read_run_ledger(CURRENT_LEDGER),
            packet["source_id"],
            packet["chunk_id"],
            hashlib.sha256(CURRENT_PACKET.read_bytes()).hexdigest(),
        )

    assert state["source"]["whole_source_candidate_complete"] is True
    assert state["source"]["source_work_authorized"] is False
    assert state["authority"]["source_work_authorized"] is False


def test_send_records_malformed_response_without_creating_spend_successor(tmp_path, monkeypatch):
    spec = importlib.util.spec_from_file_location("m050_extraction_machine_send", MACHINE_TOOL)
    assert spec is not None and spec.loader is not None
    tool = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(tool)
    packet = tool.build_packet(ROOT, AUTHGRAM_CONFIG, "C0001")

    packet_path = tmp_path / "packet.json"
    state_path = tmp_path / "state.json"
    key_path = tmp_path / "key.txt"
    raw_path = tmp_path / "raw.json"
    outcome_path = tmp_path / "outcome.json"
    ledger_path = tmp_path / "run.jsonl"
    packet_path.write_bytes(tool.canonical_json_bytes(packet))
    config_target = tmp_path / packet["configuration_path"]
    config_target.parent.mkdir(parents=True)
    config_target.write_bytes(AUTHGRAM_CONFIG.read_bytes())
    for relative in _json(AUTHGRAM_CONFIG)["artifacts"].values():
        target = tmp_path / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes((ROOT / relative).read_bytes())
    state = _compile_state(source_id=packet["source_id"], spent="0.00")
    state["calibration"].update({
        "configuration": packet["configuration_path"],
        "pilot_chunk_id": packet["chunk_id"],
        "cache_miss_call_ceiling_usd": packet["cache_miss_call_ceiling_usd"],
    })
    state_path.write_text(json.dumps(state), encoding="utf-8")
    key_path.write_text("test-key", encoding="utf-8")

    class FakeResponse:
        status = 200
        headers = {"request-id": "test-request"}

        def __enter__(self):
            return self

        def __exit__(self, *_args):
            return False

        def read(self):
            return b"not-json"

    monkeypatch.setattr(tool.urllib.request, "urlopen", lambda *_args, **_kwargs: FakeResponse())
    args = SimpleNamespace(
        repo_root=str(tmp_path),
        packet=str(packet_path),
        expected_packet_sha256=hashlib.sha256(packet_path.read_bytes()).hexdigest(),
        compile_state="state.json",
        run_ledger=str(ledger_path),
        api_key_file=str(key_path),
        raw_response=str(raw_path),
        outcome=str(outcome_path),
    )
    assert tool.command_send(args) == 1
    assert raw_path.read_bytes() == b"not-json"
    assert _json(outcome_path)["provider_call_made"] is True
    assert _json(outcome_path)["canonical_spend_update_required"] is False
    assert read_run_ledger(ledger_path)[-1]["state"] == "call_captured"


def test_substantive_review_resolves_decision_required_outcome(tmp_path):
    spec = importlib.util.spec_from_file_location("m050_extraction_machine_review", MACHINE_TOOL)
    assert spec is not None and spec.loader is not None
    tool = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(tool)
    outcome_path = tmp_path / "outcome.json"
    ledger_path = tmp_path / "run.jsonl"
    outcome_path.write_text(json.dumps({
        "source_id": "S1",
        "chunk_id": "C0001",
        "mechanical_validation": {"passed": True, "decision_required": True},
    }), encoding="utf-8")
    append_run_ledger_event(ledger_path, {
        "state": "call_captured",
        "source_id": "S1",
        "chunk_id": "C0001",
        "outcome_sha256": hashlib.sha256(outcome_path.read_bytes()).hexdigest(),
    })
    args = SimpleNamespace(
        run_ledger=str(ledger_path),
        outcome=str(outcome_path),
        result="passed",
        reviewer="source reviewer",
        reason="Decision-required finding reviewed and resolved.",
    )
    assert tool.command_review(args) == 0
    assert read_run_ledger(ledger_path)[-1]["state"] == "review_passed"


def test_substantive_review_cannot_pass_mechanically_invalid_outcome(tmp_path):
    spec = importlib.util.spec_from_file_location("m050_extraction_machine_review_invalid", MACHINE_TOOL)
    assert spec is not None and spec.loader is not None
    tool = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(tool)
    outcome_path = tmp_path / "outcome.json"
    ledger_path = tmp_path / "run.jsonl"
    outcome_path.write_text(json.dumps({
        "source_id": "S1",
        "chunk_id": "C0001",
        "mechanical_validation": {"passed": False, "decision_required": True},
    }), encoding="utf-8")
    append_run_ledger_event(ledger_path, {
        "state": "call_captured",
        "source_id": "S1",
        "chunk_id": "C0001",
        "outcome_sha256": hashlib.sha256(outcome_path.read_bytes()).hexdigest(),
    })
    args = SimpleNamespace(
        run_ledger=str(ledger_path),
        outcome=str(outcome_path),
        result="passed",
        reviewer="source reviewer",
        reason="Must remain blocked.",
    )
    with pytest.raises(ContractError, match="mechanically invalid"):
        tool.command_review(args)
    assert read_run_ledger(ledger_path)[-1]["state"] == "call_captured"
