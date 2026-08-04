import copy
from decimal import Decimal
import hashlib
import importlib.util
import json
from pathlib import Path
from types import SimpleNamespace

import pytest

from median_gate5.errors import ContractError
from median_gate5.extraction_machine import (
    anthropic_usage_cost,
    append_run_ledger_event,
    build_anthropic_request,
    build_chunk_payload,
    build_generic_response_schema,
    build_generic_source_prompt,
    conservative_call_ceiling,
    debit_spend_envelope,
    draft_block_dispositions,
    extract_anthropic_structured_response,
    read_run_ledger,
    plan_source_chunks,
    require_authorized_chunk,
    require_run_ready_for_next_call,
    spend_preflight,
    validate_extraction_response,
)


ROOT = Path(__file__).parents[4]
AUTHGRAM = ROOT / "m050/extraction/calibration/authorial-grammar"
MACHINE_TOOL = ROOT / "m050/tools/m050_extraction_machine_v0_1.py"
AUTHGRAM_CONFIG = ROOT / "m050/extraction/control/M050_Authorial_Grammar_Extraction_Machine_Config_v0_6_MEDIANv0_5_0.json"
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
        response_schema={"type": "object"},
        payload={"source_id": "S", "target_blocks": []},
        model="claude-sonnet-5",
        reasoning_effort="low",
        maximum_output_tokens=6000,
        cache_ttl="1h",
    )
    assert request["system"][0] == {
        "type": "text",
        "text": "Stable source policy",
    }
    assert request["system"][1]["text"].startswith("BOUND_RESPONSE_SCHEMA\n")
    assert request["system"][1]["cache_control"] == {
        "type": "ephemeral",
        "ttl": "1h",
    }
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


def _envelope():
    return {
        "authority": "Asa Wember",
        "scope": "provider_spend_only",
        "active": True,
        "authorized_usd": "2.00",
        "spent_usd": "1.92",
    }


def _release():
    return {
        "state": "source_run_authorized",
        "authority": "Asa Wember",
        "provider_call_limit": 5,
        "authorized_chunk_ids": ["C0001", "C0002", "C0003", "C0004", "C0005"],
        "execution_cadence": "sequential_one_call_review",
        "revoked": False,
        "binding": {
            "source_id": "S1",
            "configuration_sha256": "c" * 64,
            "model": "claude-sonnet-5",
            "reasoning_effort": "low",
            "cache_ttl": "1h",
        },
    }


def _required_binding():
    return {
        "configuration_sha256": "c" * 64,
        "model": "claude-sonnet-5",
        "reasoning_effort": "low",
        "cache_ttl": "1h",
    }


def test_money_envelope_does_not_replace_lifecycle_authority():
    request = build_anthropic_request(
        prompt="policy",
        response_schema={"type": "object"},
        payload={"source_id": "S1"},
        model="claude-sonnet-5",
        reasoning_effort="low",
        maximum_output_tokens=100,
        cache_ttl="1h",
    )
    ceiling = conservative_call_ceiling(request, _pricing())
    uncached_request = copy.deepcopy(request)
    uncached_request["system"][-1].pop("cache_control")
    assert ceiling > conservative_call_ceiling(uncached_request, _pricing())
    result = spend_preflight(
        envelope=_envelope(),
        lifecycle_receipt=_release(),
        source_id="S1",
        completed_calls=0,
        call_ceiling_usd=ceiling,
        required_binding=_required_binding(),
    )
    assert Decimal(result["remaining_after_reservation_usd"]) >= 0

    invalid = _release()
    invalid["state"] = "pilot_accepted"
    with pytest.raises(ContractError, match="lifecycle"):
        spend_preflight(
            envelope=_envelope(),
            lifecycle_receipt=invalid,
            source_id="S1",
            completed_calls=0,
            call_ceiling_usd=ceiling,
            required_binding=_required_binding(),
        )


def test_envelope_halts_before_next_call_and_debits_exact_actual_cost():
    with pytest.raises(ContractError, match="cannot cover"):
        spend_preflight(
            envelope=_envelope(),
            lifecycle_receipt=_release(),
            source_id="S1",
            completed_calls=0,
            call_ceiling_usd=Decimal("0.081"),
            required_binding=_required_binding(),
        )
    updated = debit_spend_envelope(_envelope(), "0.06984")
    assert updated["spent_usd"] == "1.98984"
    assert updated["remaining_usd"] == "0.01016"
    assert _envelope()["spent_usd"] == "1.92"


def test_cross_source_or_revoked_release_never_inherits_authority():
    with pytest.raises(ContractError, match="does not cover"):
        spend_preflight(
            envelope=_envelope(),
            lifecycle_receipt=_release(),
            source_id="S2",
            completed_calls=0,
            call_ceiling_usd=Decimal("0.01"),
            required_binding=_required_binding(),
        )
    revoked = copy.deepcopy(_release())
    revoked["revoked"] = True
    with pytest.raises(ContractError, match="revoked"):
        spend_preflight(
            envelope=_envelope(),
            lifecycle_receipt=revoked,
            source_id="S1",
            completed_calls=0,
            call_ceiling_usd=Decimal("0.01"),
            required_binding=_required_binding(),
        )


def test_lifecycle_receipt_must_bind_exact_machine_configuration():
    release = _release()
    release["binding"]["cache_ttl"] = "5m"
    with pytest.raises(ContractError, match="exact execution configuration"):
        spend_preflight(
            envelope=_envelope(),
            lifecycle_receipt=release,
            source_id="S1",
            completed_calls=0,
            call_ceiling_usd=Decimal("0.01"),
            required_binding=_required_binding(),
        )


def test_compact_run_ledger_blocks_until_review_and_verifies_chain(tmp_path):
    ledger = tmp_path / "run.jsonl"
    assert require_run_ready_for_next_call(read_run_ledger(ledger), "S1") == 0
    captured = append_run_ledger_event(
        ledger,
        {"state": "call_captured", "source_id": "S1", "chunk_id": "C0001"},
    )
    assert captured["sequence"] == 1
    with pytest.raises(ContractError, match="prior outcome"):
        require_run_ready_for_next_call(read_run_ledger(ledger), "S1")
    reviewed = append_run_ledger_event(
        ledger,
        {"state": "review_passed", "source_id": "S1", "chunk_id": "C0001"},
    )
    assert reviewed["predecessor_event_sha256"]
    assert require_run_ready_for_next_call(read_run_ledger(ledger), "S1") == 1
    with pytest.raises(ContractError, match="another source"):
        require_run_ready_for_next_call(read_run_ledger(ledger), "S2")


def test_lifecycle_receipt_binds_exact_chunk_order_and_call_limit():
    release = _release()
    require_authorized_chunk(release, "C0001", 0)
    require_authorized_chunk(release, "C0003", 2)
    with pytest.raises(ContractError, match="next authorized chunk"):
        require_authorized_chunk(release, "C0003", 1)
    release["provider_call_limit"] = 4
    with pytest.raises(ContractError, match="does not match"):
        require_authorized_chunk(release, "C0001", 0)


def test_authorial_full_plan_prepares_source_agnostically_with_stable_cache_prefix(tmp_path):
    spec = importlib.util.spec_from_file_location("m050_extraction_machine", MACHINE_TOOL)
    assert spec is not None and spec.loader is not None
    tool = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(tool)

    target_ids = []
    context_ids = []
    excluded_ids = []
    stable_systems = []
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
        target_ids.extend(chunk_targets)
        context_ids.extend(chunk_context)
        excluded_ids.extend(chunk_excluded)
        stable_systems.append(packet["provider_request"]["system"])

    manifest = _json(ROOT / config["artifacts"]["block_manifest"])
    primary_ids = [block_id for chunk in plan["chunks"] for block_id in chunk["block_ids"]]
    assert primary_ids == [block["block_id"] for block in manifest["blocks"]]
    assert len(target_ids) == len(set(target_ids)) == 228
    assert len(excluded_ids) == len(set(excluded_ids)) == 280
    assert all(len(packet["payload"]["target_blocks"]) <= 20 for packet in packets)
    assert plan["quantization"]["generated_chunk_count"] == len(chunk_ids) == 13
    assert plan["quantization"]["chunk_count_is_input"] is False
    assert context_ids
    assert all(system == stable_systems[0] for system in stable_systems)
    assert stable_systems[0][-1]["cache_control"] == {
        "type": "ephemeral",
        "ttl": "1h",
    }

    lifecycle = {
        "state": "source_run_authorized",
        "authority": "Asa Wember",
        "provider_call_limit": len(chunk_ids),
        "authorized_chunk_ids": chunk_ids,
        "execution_cadence": "sequential_one_call_review",
        "revoked": False,
        "binding": {
            "source_id": packets[0]["source_id"],
            "configuration_sha256": packets[0]["configuration_sha256"],
            "model": packets[0]["binding"]["model"],
            "reasoning_effort": packets[0]["binding"]["reasoning_effort"],
            "cache_ttl": packets[0]["binding"]["cache_ttl"],
        },
    }
    envelope = {
        "authority": "Asa Wember",
        "scope": "provider_spend_only",
        "active": True,
        "authorized_usd": "2.00",
        "spent_usd": "0.00",
    }
    preflight = tool._preflight(packets[0], envelope, lifecycle, tmp_path / "run.jsonl")
    assert preflight["reserved_call_ceiling_usd"] == packets[0]["cache_miss_call_ceiling_usd"]
    with pytest.raises(ContractError, match="next authorized chunk"):
        tool._preflight(packets[1], envelope, lifecycle, tmp_path / "run.jsonl")


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
    assert request["system"][-1]["cache_control"]["ttl"] == "1h"
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
    approval = repo / "m050/extraction/audit/card-approved.json"
    source.parent.mkdir(parents=True)
    card.parent.mkdir(parents=True)
    approval.parent.mkdir(parents=True)
    source.write_text("# Test source\n\nA rule applies.\n", encoding="utf-8")
    card.write_text("# Approved boundary\n\nOnly this source is in scope.\n", encoding="utf-8")
    card_sha256 = hashlib.sha256(card.read_bytes()).hexdigest()
    approval.write_text(
        json.dumps(
            {
                "machine": "identity_card",
                "new_state": "approved",
                "authority": "Asa Wember",
                "artifact_id": "sic_" + card_sha256[:24],
            }
        ),
        encoding="utf-8",
    )
    base = "m050/extraction/onboarding/test"
    args = SimpleNamespace(
        repo_root=str(repo),
        source_id="M050-SRC-TEST-SPEC-001",
        source_path="m050/docs/spec.md",
        identity_card="m050/extraction/control/card.md",
        identity_approval_receipt="m050/extraction/audit/card-approved.json",
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
    assert config["execution"]["provider_calls_authorized"] is False
    loaded, paths = tool.load_config(repo, repo / f"{base}/config.json")
    assert loaded["source_id"] == "M050-SRC-TEST-SPEC-001"
    assert set(paths) == {
        "identity_card", "identity_approval_receipt", "block_manifest",
        "disposition_ledger", "chunk_plan", "prompt", "response_schema",
    }


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


def test_send_consumes_call_and_halts_on_malformed_success_response(tmp_path, monkeypatch):
    spec = importlib.util.spec_from_file_location("m050_extraction_machine_send", MACHINE_TOOL)
    assert spec is not None and spec.loader is not None
    tool = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(tool)
    packet = tool.build_packet(ROOT, AUTHGRAM_CONFIG, "C0001")

    packet_path = tmp_path / "packet.json"
    envelope_path = tmp_path / "spend.json"
    release_path = tmp_path / "release.json"
    key_path = tmp_path / "key.txt"
    raw_path = tmp_path / "raw.json"
    outcome_path = tmp_path / "outcome.json"
    successor_path = tmp_path / "spend-next.json"
    ledger_path = tmp_path / "run.jsonl"
    packet_path.write_bytes(tool.canonical_json_bytes(packet))
    envelope_path.write_text(json.dumps({
        "authority": "Asa Wember", "scope": "provider_spend_only",
        "active": True, "authorized_usd": "2.00", "spent_usd": "0.00",
    }), encoding="utf-8")
    release_path.write_text(json.dumps({
        "state": "source_run_authorized",
        "authority": "Asa Wember",
        "provider_call_limit": 1,
        "authorized_chunk_ids": ["C0001"],
        "execution_cadence": "sequential_one_call_review",
        "revoked": False,
        "binding": {
            "source_id": packet["source_id"],
            "configuration_sha256": packet["configuration_sha256"],
            "model": packet["binding"]["model"],
            "reasoning_effort": packet["binding"]["reasoning_effort"],
            "cache_ttl": packet["binding"]["cache_ttl"],
        },
    }), encoding="utf-8")
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
        packet=str(packet_path),
        expected_packet_sha256=hashlib.sha256(packet_path.read_bytes()).hexdigest(),
        spend_envelope=str(envelope_path),
        successor_spend_envelope=str(successor_path),
        lifecycle_receipt=str(release_path),
        run_ledger=str(ledger_path),
        api_key_file=str(key_path),
        raw_response=str(raw_path),
        outcome=str(outcome_path),
    )
    assert tool.command_send(args) == 1
    assert raw_path.read_bytes() == b"not-json"
    assert _json(outcome_path)["authorization_consumed"] is True
    successor = _json(successor_path)
    assert successor["active"] is False
    assert successor["halt_reason"] == "invalid_provider_response_cost_reconciliation_required"
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
