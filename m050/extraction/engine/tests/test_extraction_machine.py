import copy
from datetime import datetime
from decimal import Decimal
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
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
GUARD = ROOT / "m050/tools/m050_guard.py"
HOME_CONFIG = ROOT / "m050/extraction/control/M050_Home_Extraction_Machine_Config_v0_1_MEDIANv0_5_0.json"
RENDER_STATUS = ROOT / "m050/tools/m050_render_status.py"
HOME_REPORT = ROOT / "m050/extraction/accepted/home/M050_Home_Full_Extraction_Acceptance_Report_v0_1_MEDIANv0_5_0.json"
HOME_LEDGER = "m050/extraction/runs/home-pilot/M050_Home_Run_Ledger_v0_1_MEDIANv0_5_0.jsonl"
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


def _guard_module():
    spec = importlib.util.spec_from_file_location("m050_guard_for_tests", GUARD)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _render_status_module():
    spec = importlib.util.spec_from_file_location(
        "m050_render_status_for_tests", RENDER_STATUS
    )
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    tool_path = str(RENDER_STATUS.parent)
    sys.path.insert(0, tool_path)
    try:
        spec.loader.exec_module(module)
    finally:
        sys.path.remove(tool_path)
    return module


def _home_acceptance_fixture():
    report = _json(HOME_REPORT)
    source = {
        "id": report["source_id"],
        "accepted_chunk_ids": report["accepted_chunk_ids"],
    }
    calibration = {
        "accepted_evidence": [
            {
                "chunk_id": item["chunk_id"],
                "outcome": item["outcome_path"],
                "run_ledger": HOME_LEDGER,
            }
            for item in report["accepted_inputs"]
        ],
        "candidate_acceptance": {
            "candidate": report["candidate_path"],
            "candidate_sha256": report["candidate_sha256"],
            "report": HOME_REPORT.relative_to(ROOT).as_posix(),
            "report_sha256": hashlib.sha256(HOME_REPORT.read_bytes()).hexdigest(),
        },
    }
    return source, _json(HOME_CONFIG), calibration


def test_completed_source_has_exact_hash_bound_candidate_acceptance():
    guard = _guard_module()
    source, config, calibration = _home_acceptance_fixture()
    errors = []
    guard.validate_candidate_acceptance(
        source,
        config,
        calibration,
        source["accepted_chunk_ids"],
        calibration["accepted_evidence"],
        errors,
    )
    assert errors == []


def test_completed_source_rejects_missing_candidate_acceptance_pair():
    guard = _guard_module()
    source, config, calibration = _home_acceptance_fixture()
    calibration.pop("candidate_acceptance")
    errors = []
    guard.validate_candidate_acceptance(
        source,
        config,
        calibration,
        source["accepted_chunk_ids"],
        calibration["accepted_evidence"],
        errors,
    )
    assert errors == ["completed source lacks a hash-bound candidate/report pair"]


def test_accepted_candidate_rejects_missing_coverage_and_duplicate_identifiers():
    guard = _guard_module()
    expected = [
        ("C0001", {"proposal_id": "P1", "source_id": "S1"}),
        ("C0002", {"proposal_id": "P1", "source_id": "S1"}),
    ]
    candidate = [{"proposal_id": "P1", "source_id": "S1"}]
    errors = []
    guard.validate_accepted_candidate_records(candidate, expected, errors)
    assert any("coverage drifted" in error for error in errors)

    candidate = [
        {"proposal_id": "P1", "source_id": "S1"},
        {"proposal_id": "P1", "source_id": "S1"},
    ]
    errors = []
    guard.validate_accepted_candidate_records(candidate, expected, errors)
    assert "accepted candidate record identifiers are not candidate-wide unique" in errors


def test_pending_identity_card_is_hash_bound_and_has_no_extraction_boundary(tmp_path, monkeypatch):
    guard = _guard_module()
    monkeypatch.setattr(guard, "ROOT", tmp_path)
    relative = "m050/extraction/control/source-identities/cards/test.md"
    card = tmp_path / relative
    card.parent.mkdir(parents=True)
    source = {
        "id": "M050-SRC-TEST-001",
        "accepted_chunk_ids": [],
        "rejected_chunk_id": None,
        "whole_source_candidate_complete": False,
    }
    registered = {"path": "m050/docs/test.md", "sha256": "a" * 64}
    card.write_text(
        "Status: `PENDING_AUTHOR_APPROVAL`\n"
        "Lifecycle state: `identity_card_proposed`\n"
        "Author/root of authority: Asa Wember\n"
        "| Source ID | `M050-SRC-TEST-001` |\n"
        "| Path | `m050/docs/test.md` |\n"
        f"| SHA-256 | `{'a' * 64}` |\n",
        encoding="utf-8",
    )
    calibration = {
        "identity_card": relative,
        "identity_card_sha256": hashlib.sha256(card.read_bytes()).hexdigest(),
        "identity_card_approval_pending": True,
        "offline_gate_passed": False,
    }
    errors = []
    guard.validate_pending_identity_card(source, registered, calibration, None, errors)
    assert errors == []

    calibration["identity_card_sha256"] = "b" * 64
    errors = []
    guard.validate_pending_identity_card(source, registered, calibration, None, errors)
    assert errors == ["pending identity card hash binding drifted"]


def test_completed_source_requires_formal_stopdown_authority():
    guard = _guard_module()
    source = {
        "source_work_authorized": False,
        "whole_source_candidate_complete": True,
    }
    authority = {
        "repository_writes_authorized": False,
        "source_work_authorized": False,
        "google_sheets_interaction_authorized": False,
        "semantic_acceptance_authorized": False,
        "mapping_authorized": False,
        "reconciliation_authorized": False,
        "compiled_prose_authorized": False,
    }
    errors = []
    guard.validate_authority_state(source, authority, errors)
    assert errors == []

    authority["repository_writes_authorized"] = True
    errors = []
    guard.validate_authority_state(source, authority, errors)
    assert errors == ["completed source has not completed formal Stopdown"]

    source["source_work_authorized"] = True
    authority["source_work_authorized"] = True
    errors = []
    guard.validate_authority_state(source, authority, errors)
    assert errors == [
        "completed source retains source-work authority",
        "completed source has not completed formal Stopdown",
    ]


def test_active_source_retains_one_writer_authority():
    guard = _guard_module()
    source = {
        "source_work_authorized": True,
        "whole_source_candidate_complete": False,
    }
    authority = {
        "repository_writes_authorized": True,
        "source_work_authorized": True,
        "google_sheets_interaction_authorized": False,
        "semantic_acceptance_authorized": False,
        "mapping_authorized": False,
        "reconciliation_authorized": False,
        "compiled_prose_authorized": False,
    }
    errors = []
    guard.validate_authority_state(source, authority, errors)
    assert errors == []


def test_status_uses_unlabeled_timestamp_and_safe_remaining_balance():
    guard = _guard_module()
    state = {
        "dashboard": {
            "updated_human": "August 4, 2026 at 5:46:07 PM EDT",
            "status": "Stopped",
            "phase": "Atomic extraction",
            "source": "Away",
            "chunk": "Complete",
            "now": "Candidate accepted",
            "next": "Await authorization",
        },
        "spend": {
            "remaining_usd": "0.6576584",
            "display_usd_rounded_up": "9.03",
        },
    }
    status = guard.expected_status(state)
    assert "**UPDATED:**" not in status
    assert "August 4, 2026 at 5:46:07 PM EDT<br>" in status
    assert status.endswith("**SPEND REMAINING:** $0.65\n")
    assert "TOTAL COST" not in status


def test_status_renderer_rounds_and_updates_canonical_timestamp(tmp_path):
    renderer = _render_status_module()
    state_path = tmp_path / "state.json"
    status_path = tmp_path / "STATUS.md"
    state = {
        "updated": "2026-01-01T00:00:00-05:00",
        "dashboard": {
            "updated_human": "stale",
            "status": "Stopped",
            "phase": "Atomic extraction",
            "source": "Personal Items",
            "chunk": "C0015",
            "now": "Stopped",
            "next": "Await authorization",
        },
        "spend": {"remaining_usd": "0.2745620"},
    }
    state_path.write_text(json.dumps(state), encoding="utf-8")
    renderer.render_status(
        state_path,
        status_path,
        now=datetime.fromisoformat("2026-08-05T09:12:13.600000-04:00"),
    )
    updated = _json(state_path)
    assert updated["updated"] == "2026-08-05T09:12:14-04:00"
    assert updated["dashboard"]["updated_human"] == (
        "August 5, 2026 at 9:12:14 AM EDT"
    )
    assert status_path.read_text(encoding="utf-8") == renderer.expected_status(updated)


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


def test_generic_prompt_promotes_only_concise_cross_source_invariants():
    boundary = "Extract this source's claims within its approved identity boundary."
    prompt = build_generic_source_prompt(
        "M050-SRC-TEST-001", ["evidence_game_semantic"], boundary
    )

    assert boundary in prompt
    assert "input-ordered disposition block-ID set must exactly equal `target_blocks`" in prompt
    assert "none missing, repeated, or partial" in prompt
    assert "byte-for-byte" in prompt
    assert "target-block substring that occurs exactly once" in prompt
    assert "Expand repeated or nested terms with adjacent text until unique" in prompt
    assert "actual target-block\ncharacters" in prompt
    assert "never literal backslash Unicode-escape spellings" in prompt
    assert "retains\nmarkup and escaping" not in prompt
    assert "Preserve smart quotes exactly" not in prompt
    assert "Include interrupting markup or split the atom" in prompt
    assert "required_disposition" in prompt
    assert "after verifying exactly\n`required_target_disposition_count` dispositions" in prompt
    assert "`no_substantive_claim` requires empty `atoms`" in prompt
    assert "Kind `atoms` requires nonempty\n`atoms`" in prompt
    assert "all other kinds require empty `atoms`" in prompt
    assert "every nonempty semantic cell" in prompt
    assert "stages,\nactions, and results" in prompt
    assert "never infer a relationship between\nadjacent cells" in prompt
    assert "No exact span crosses a semicolon; each side gets its own atom" in prompt
    assert "Copy every authored slash into the normalized claim" in prompt
    assert "never replace it with a word unless the source defines that meaning" in prompt
    assert "document-control metadata carry no substantive atom" in prompt
    assert "target block ID plus local atom ordinal" in prompt
    assert "proposal IDs must remain source-unique" in prompt
    assert "never samples, placeholders, or dummy `x`" in prompt
    assert "never abbreviate the target set" in prompt
    assert "Exact spans uniquely ground core assertions" in prompt
    assert "Separate claims only when each remains independently grounded and self-contained" in prompt
    assert "Preserve coordinated subjects or effects in one atom" in prompt
    assert "share a predicate, subject, condition, or relationship" in prompt
    assert "Split independent same-subject effects" not in prompt
    assert "A subject or label alone never grounds an\nimported predicate" in prompt
    assert "Start each normalized claim with `exact_source_text`" in prompt
    assert "For self-containment" in prompt
    assert "resolve pronouns and subjectless exact-text prefixes" in prompt
    assert "explicit governing subjects" in prompt
    assert "parent headings\nmay supply only necessary status or scope" in prompt
    assert "Never paraphrase, gloss, define, compare, infer, or complete implied meaning" in prompt
    assert "Parent headings are context, never atoms" in prompt
    assert "Normalized claims may add explicit, unambiguous qualifiers" not in prompt
    assert "Never repair source text or invent identifiers, statuses, owners, or\nauthorities" in prompt
    assert "cost, staffing, and effect" not in prompt
    assert "dedicated Home" not in prompt
    assert len(prompt.split()) < 450


def test_active_prompt_equals_generated_generic_prompt():
    state = _json(COMPILE_STATE)
    if state["calibration"].get("identity_card_approval_pending") is True:
        return
    config = _json(ROOT / state["calibration"]["configuration"])
    identity = (ROOT / config["artifacts"]["identity_card"]).read_text(encoding="utf-8")
    active = (ROOT / config["artifacts"]["prompt"]).read_text(encoding="utf-8")
    generated = build_generic_source_prompt(
        config["source_id"], config["allowed_streams"], identity
    )
    assert active == generated
    assert "\\n" not in active


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


def test_request_keeps_output_schema_stable_and_bound_contract_exact():
    source_id = "M050-SRC-TEST-001"
    first_ids = [
        f"{source_id}__B00001_aaaaaaaaaaaa",
        f"{source_id}__B00002_bbbbbbbbbbbb",
    ]
    second_ids = [f"{source_id}__B00003_cccccccccccc"]
    schema = build_generic_response_schema(source_id, ["evidence_game_semantic"])

    def request_for(target_ids):
        return build_anthropic_request(
            prompt="Stable source policy",
            response_schema=schema,
            payload={
                "source_id": source_id,
                "required_target_disposition_count": len(target_ids),
                "target_blocks": [
                    {"block_id": block_id} for block_id in target_ids
                ],
            },
            model="claude-sonnet-5",
            reasoning_effort="low",
            maximum_output_tokens=6000,
            cache_ttl="1h",
        )

    first = request_for(first_ids)
    second = request_for(second_ids)
    assert first["output_config"] == second["output_config"]
    assert first["system"][0] == second["system"][0]
    assert first["system"][1] != second["system"][1]
    assert first["messages"] != second["messages"]

    dispositions = first["output_config"]["format"]["schema"]["properties"][
        "dispositions"
    ]
    expected_pattern = f"^{source_id}__B[0-9]{{5}}_[0-9a-f]{{12}}$"
    assert dispositions["items"]["properties"]["block_id"] == {
        "type": "string",
        "pattern": expected_pattern,
    }
    atoms = dispositions["items"]["properties"]["atoms"]
    assert atoms["items"]["properties"]["block_id"] == {
        "type": "string",
        "pattern": expected_pattern,
    }

    bound_text = first["system"][1]["text"]
    bound_schema = json.loads(
        bound_text.removeprefix("BOUND_RESPONSE_SCHEMA\n").removesuffix(
            "\nEND_BOUND_RESPONSE_SCHEMA"
        )
    )
    bound_dispositions = bound_schema["properties"]["dispositions"]
    assert bound_dispositions["items"]["properties"]["block_id"] == {
        "enum": first_ids
    }
    bound_atoms = bound_dispositions["items"]["properties"]["atoms"]
    assert bound_atoms["items"]["properties"]["block_id"] == {
        "enum": first_ids
    }


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


def _smart_quote_grounding_report(exact_source_text):
    source_text = "A brief note such as “Twig takes focus - Sire’s Hat” may appear.\n"
    payload = {
        "source_id": "S1",
        "target_blocks": [{
            "block_id": "B1", "block_type": "paragraph",
            "text": source_text, "status_markers": [],
        }],
        "context_blocks": [],
        "excluded_block_ids": [],
    }
    response = {
        "schema_version": "M050-EVIDENCE-PROPOSAL-0.1",
        "proposal_set_id": "smart-quote-test",
        "request_id": "smart-quote-test",
        "source_id": "S1",
        "dispositions": [{
            "block_id": "B1",
            "kind": "atoms",
            "atoms": [{
                "proposal_id": "P1",
                "source_id": "S1",
                "block_id": "B1",
                "exact_source_text": exact_source_text,
                "normalized_claim": "A note may say Twig takes focus - Sire’s Hat.",
                "claim_kind": "example",
                "stream": "allowed",
            }],
        }],
    }
    return validate_extraction_response(
        payload=payload,
        response=response,
        response_schema=build_generic_response_schema("S1", ["allowed"]),
        allowed_streams=["allowed"],
    )


def test_validator_grounds_actual_source_smart_quotes_after_json_decoding():
    report = _smart_quote_grounding_report(
        "“Twig takes focus - Sire’s Hat”"
    )
    assert report["passed"] is True


def test_validator_rejects_literal_unicode_escape_spellings_after_json_decoding():
    report = _smart_quote_grounding_report(
        "\\u201cTwig takes focus - Sire\\u2019s Hat\\u201d"
    )
    assert report["passed"] is False
    assert any("exact contiguous grounding" in error for error in report["errors"])


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


def test_validator_requires_authored_slashes_in_normalized_claims():
    payload = {
        "source_id": "S1",
        "target_blocks": [{
            "block_id": "B1", "block_type": "paragraph",
            "text": "Ledge Loft / Open Flight Shelf\n", "status_markers": [],
        }],
        "context_blocks": [],
        "excluded_block_ids": [],
    }
    schema = build_generic_response_schema("S1", ["allowed"])
    atom = {
        "proposal_id": "P1", "source_id": "S1", "block_id": "B1",
        "exact_source_text": "Ledge Loft / Open Flight Shelf",
        "normalized_claim": "The House is Ledge Loft or Open Flight Shelf.",
        "claim_kind": "attribute", "stream": "allowed",
    }
    response = {
        "schema_version": "M050-EVIDENCE-PROPOSAL-0.1",
        "proposal_set_id": "slash-test", "request_id": "slash-test",
        "source_id": "S1",
        "dispositions": [{"block_id": "B1", "kind": "atoms", "atoms": [atom]}],
    }
    rejected = validate_extraction_response(
        payload=payload, response=response, response_schema=schema,
        allowed_streams=["allowed"],
    )
    assert rejected["passed"] is False
    assert rejected["checks"]["relationship_preservation_errors"] == 1

    atom["normalized_claim"] = "The House is Ledge Loft / Open Flight Shelf."
    accepted = validate_extraction_response(
        payload=payload, response=response, response_schema=schema,
        allowed_streams=["allowed"],
    )
    assert accepted["passed"] is True
    assert accepted["checks"]["relationship_preservation_errors"] == 0


def test_validator_ignores_html_tag_slashes_in_relationship_check():
    payload = {
        "source_id": "S1",
        "target_blocks": [{
            "block_id": "B1", "block_type": "paragraph",
            "text": "STATUS<br /> COMPLETE\n", "status_markers": [],
        }],
        "context_blocks": [],
        "excluded_block_ids": [],
    }
    schema = build_generic_response_schema("S1", ["allowed"])
    atom = {
        "proposal_id": "P1", "source_id": "S1", "block_id": "B1",
        "exact_source_text": "STATUS<br /> COMPLETE",
        "normalized_claim": "Document status is COMPLETE.",
        "claim_kind": "status", "stream": "allowed",
    }
    response = {
        "schema_version": "M050-EVIDENCE-PROPOSAL-0.1",
        "proposal_set_id": "html-slash-test", "request_id": "html-slash-test",
        "source_id": "S1",
        "dispositions": [{"block_id": "B1", "kind": "atoms", "atoms": [atom]}],
    }
    accepted = validate_extraction_response(
        payload=payload, response=response, response_schema=schema,
        allowed_streams=["allowed"],
    )
    assert accepted["passed"] is True
    assert accepted["checks"]["relationship_preservation_errors"] == 0


def test_validator_requires_semicolon_clauses_to_be_separate_atoms():
    payload = {
        "source_id": "S1",
        "target_blocks": [{
            "block_id": "B1", "block_type": "paragraph",
            "text": "The Healer values calm; a Crafter brings salvage.\n",
            "status_markers": [],
        }],
        "context_blocks": [],
        "excluded_block_ids": [],
    }
    schema = build_generic_response_schema("S1", ["allowed"])
    atoms = [{
        "proposal_id": "P1", "source_id": "S1", "block_id": "B1",
        "exact_source_text": "The Healer values calm; a Crafter brings salvage.",
        "normalized_claim": "The Healer values calm while a Crafter brings salvage.",
        "claim_kind": "relationship", "stream": "allowed",
    }]
    response = {
        "schema_version": "M050-EVIDENCE-PROPOSAL-0.1",
        "proposal_set_id": "semicolon-test", "request_id": "semicolon-test",
        "source_id": "S1",
        "dispositions": [{"block_id": "B1", "kind": "atoms", "atoms": atoms}],
    }
    rejected = validate_extraction_response(
        payload=payload, response=response, response_schema=schema,
        allowed_streams=["allowed"],
    )
    assert rejected["passed"] is False
    assert rejected["checks"]["atomicity_errors"] == 1

    response["dispositions"][0]["atoms"] = [
        {**atoms[0], "exact_source_text": "The Healer values calm",
         "normalized_claim": "The Healer values calm."},
        {**atoms[0], "proposal_id": "P2",
         "exact_source_text": "a Crafter brings salvage.",
         "normalized_claim": "A Crafter brings salvage."},
    ]
    accepted = validate_extraction_response(
        payload=payload, response=response, response_schema=schema,
        allowed_streams=["allowed"],
    )
    assert accepted["passed"] is True


def test_payload_marks_generic_table_header_and_delimiter_non_substantive():
    rows = [
        ("B1", "| **Card family** | **Function** | **Example** |\n"),
        ("B2", "|---|---|---|\n"),
        ("B3", "| Arrival | A Presence arrives | Hawk pass |\n"),
    ]
    manifest = {
        "source_id": "S1", "source_sha256": "a" * 64,
        "blocks": [
            {"block_id": block_id, "block_type": "table_row", "text": value,
             "status_markers": []}
            for block_id, value in rows
        ],
    }
    payload = build_chunk_payload(
        manifest,
        [{"block_id": block_id, "disposition": "eligible"} for block_id, _ in rows],
        {"chunk_id": "C0001", "block_ids": [block_id for block_id, _ in rows]},
    )
    targets = {item["block_id"]: item for item in payload["target_blocks"]}
    for block_id in ("B1", "B2"):
        assert targets[block_id]["structural_role"] == "table_header_or_delimiter"
        assert targets[block_id]["required_disposition"] == "no_substantive_claim"
    assert "required_disposition" not in targets["B3"]


def test_payload_marks_contents_navigation_non_substantive():
    manifest = {
        "source_id": "S1",
        "source_sha256": "b" * 64,
        "blocks": [
            {
                "block_id": "B1",
                "block_type": "paragraph",
                "parent_heading": "## Contents\n",
                "text": "1. Purpose and Scope\n",
                "status_markers": [],
            },
            {
                "block_id": "B2",
                "block_type": "paragraph",
                "parent_heading": "# Purpose and Scope\n",
                "text": "This source defines its bounded purpose.\n",
                "status_markers": [],
            },
        ],
    }
    payload = build_chunk_payload(
        manifest,
        [
            {"block_id": "B1", "disposition": "eligible"},
            {"block_id": "B2", "disposition": "eligible"},
        ],
        {"chunk_id": "C0001", "block_ids": ["B1", "B2"]},
    )
    targets = {item["block_id"]: item for item in payload["target_blocks"]}
    assert targets["B1"]["structural_role"] == "contents_navigation"
    assert targets["B1"]["required_disposition"] == "no_substantive_claim"
    assert "required_disposition" not in targets["B2"]


def test_payload_exposes_existing_parent_heading_to_its_target():
    manifest = {
        "source_id": "S1",
        "source_sha256": "c" * 64,
        "blocks": [
            {
                "block_id": "B1",
                "block_type": "paragraph",
                "parent_heading": "## Explicitly deferred work\n",
                "text": "- Registry publication.\n",
                "status_markers": [],
            },
        ],
    }
    payload = build_chunk_payload(
        manifest,
        [{"block_id": "B1", "disposition": "eligible"}],
        {"chunk_id": "C0001", "block_ids": ["B1"]},
    )
    assert payload["target_blocks"][0]["parent_heading"] == (
        "## Explicitly deferred work\n"
    )


def test_payload_marks_generic_document_end_marker_non_substantive():
    manifest = {
        "source_id": "S1",
        "source_sha256": "d" * 64,
        "blocks": [
            {
                "block_id": "B1",
                "block_type": "paragraph",
                "text": "<!--@22¶4-->\nEND OF SPECIFICATION\n",
                "status_markers": [],
            },
            {
                "block_id": "B2",
                "block_type": "paragraph",
                "text": "The specification ends when its completion condition is met.\n",
                "status_markers": [],
            },
        ],
    }
    payload = build_chunk_payload(
        manifest,
        [
            {"block_id": "B1", "disposition": "eligible"},
            {"block_id": "B2", "disposition": "eligible"},
        ],
        {"chunk_id": "C0001", "block_ids": ["B1", "B2"]},
    )
    targets = {item["block_id"]: item for item in payload["target_blocks"]}
    assert targets["B1"]["structural_role"] == "document_end_marker"
    assert targets["B1"]["required_disposition"] == "no_substantive_claim"
    assert "required_disposition" not in targets["B2"]


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


def test_payload_marks_entire_document_control_table_non_substantive():
    rows = [
        ("B1", "| **Document field** | **Specification** |\n"),
        ("B2", "|---|---|\n"),
        ("B3", "| Version | 1.0 |\n"),
        ("B4", "| Precedence | New work leads old work |\n"),
    ]
    manifest = {
        "source_id": "S1", "source_sha256": "c" * 64,
        "blocks": [
            {"block_id": block_id, "block_type": "table_row", "text": value,
             "status_markers": []}
            for block_id, value in rows
        ],
    }
    payload = build_chunk_payload(
        manifest,
        [{"block_id": block_id, "disposition": "eligible"} for block_id, _ in rows],
        {"chunk_id": "C0001", "block_ids": [block_id for block_id, _ in rows]},
    )
    assert all(
        target["structural_role"] == "document_control_metadata"
        and target["required_disposition"] == "no_substantive_claim"
        for target in payload["target_blocks"]
    )


def test_procedural_table_requires_separate_action_and_result_atoms():
    rows = [
        ("B1", "| **Beat** | **Player attention** | **Possible result** |\n"),
        ("B2", "|---|---|---|\n"),
        ("B3", "| Read | Watch traffic | A window becomes legible |\n"),
    ]
    manifest = {
        "source_id": "S1", "source_sha256": "d" * 64,
        "blocks": [{"block_id": key, "block_type": "table_row", "text": value,
                    "status_markers": []} for key, value in rows],
    }
    payload = build_chunk_payload(
        manifest,
        [{"block_id": key, "disposition": "eligible"} for key, _ in rows],
        {"chunk_id": "C0001", "block_ids": [key for key, _ in rows]},
    )
    body = payload["target_blocks"][2]
    assert body["structural_role"] == "procedural_stage_action_result"
    assert body["minimum_atoms"] == 2
    schema = build_generic_response_schema("S1", ["allowed"])
    response = {
        "schema_version": "M050-EVIDENCE-PROPOSAL-0.1", "proposal_set_id": "p",
        "request_id": "r", "source_id": "S1",
        "dispositions": [
            {"block_id": "B1", "kind": "no_substantive_claim", "atoms": []},
            {"block_id": "B2", "kind": "no_substantive_claim", "atoms": []},
            {"block_id": "B3", "kind": "atoms", "atoms": [{
                "proposal_id": "p1", "source_id": "S1", "block_id": "B3",
                "exact_source_text": "Watch traffic", "normalized_claim": "Watch traffic.",
                "claim_kind": "mechanic", "stream": "allowed",
            }]},
        ],
    }
    rejected = validate_extraction_response(
        payload=payload, response=response, response_schema=schema,
        allowed_streams=["allowed"],
    )
    assert rejected["passed"] is False
    assert rejected["checks"]["atomicity_errors"] == 1


def test_outcome_table_derives_minimum_atoms_from_semicolon_effects():
    rows = [
        ("B1", "| **Outcome class** | **World-state expression** |\n"),
        ("B2", "|---|---|\n"),
        ("B3", "| Delay | Day spent; weather worsens; margin narrows. |\n"),
    ]
    manifest = {
        "source_id": "S1", "source_sha256": "e" * 64,
        "blocks": [{"block_id": key, "block_type": "table_row", "text": value,
                    "status_markers": []} for key, value in rows],
    }
    payload = build_chunk_payload(
        manifest,
        [{"block_id": key, "disposition": "eligible"} for key, _ in rows],
        {"chunk_id": "C0001", "block_ids": [key for key, _ in rows]},
    )
    body = payload["target_blocks"][2]
    assert body["structural_role"] == "independent_table_columns"
    assert body["minimum_atoms"] == 3


def test_independent_table_columns_derive_minimum_atoms():
    rows = [
        ("B1", "| **Option** | **Meaning** | **Constraint** |\n"),
        ("B2", "|---|---|---|\n"),
        ("B3", "| TAKE | Gather now | Carry is finite; renewal may fall. |\n"),
    ]
    manifest = {
        "source_id": "S1", "source_sha256": "f" * 64,
        "blocks": [{"block_id": key, "block_type": "table_row", "text": value,
                    "status_markers": []} for key, value in rows],
    }
    payload = build_chunk_payload(
        manifest,
        [{"block_id": key, "disposition": "eligible"} for key, _ in rows],
        {"chunk_id": "C0001", "block_ids": [key for key, _ in rows]},
    )
    body = payload["target_blocks"][2]
    assert body["structural_role"] == "independent_table_columns"
    assert body["minimum_atoms"] == 3


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


@pytest.mark.parametrize(
    "transport_error",
    [
        "URLError:workspace DNS unavailable",
        "HTTPError:529",
        "TimeoutError:The read operation timed out",
    ],
)
def test_compact_run_ledger_allows_same_packet_after_reviewed_transient_failure(
    tmp_path, transport_error
):
    ledger = tmp_path / "run.jsonl"
    append_run_ledger_event(
        ledger,
        {
            "state": "call_captured",
            "source_id": "S1",
            "chunk_id": "C0001",
            "packet_file_sha256": "a" * 64,
            "outcome_sha256": "o" * 64,
            "mechanical_passed": False,
            "transport_error": transport_error,
        },
    )
    append_run_ledger_event(
        ledger,
        {
            "state": "review_failed",
            "source_id": "S1",
            "chunk_id": "C0001",
            "outcome_sha256": "o" * 64,
        },
    )

    assert require_run_ready_for_next_call(
        read_run_ledger(ledger), "S1", "C0001", "a" * 64
    ) == 1


def test_compact_run_ledger_allows_one_same_packet_retry_after_provider_refusal(
    tmp_path,
):
    ledger = tmp_path / "run.jsonl"
    refusal_error = "ContractError:Anthropic response did not end cleanly: refusal"
    append_run_ledger_event(
        ledger,
        {
            "state": "call_captured",
            "source_id": "S1",
            "chunk_id": "C0001",
            "packet_file_sha256": "a" * 64,
            "outcome_sha256": "o" * 64,
            "mechanical_passed": False,
            "capture_error": refusal_error,
        },
    )
    append_run_ledger_event(
        ledger,
        {
            "state": "review_failed",
            "source_id": "S1",
            "chunk_id": "C0001",
            "outcome_sha256": "o" * 64,
        },
    )

    assert require_run_ready_for_next_call(
        read_run_ledger(ledger), "S1", "C0001", "a" * 64
    ) == 1

    append_run_ledger_event(
        ledger,
        {
            "state": "call_captured",
            "source_id": "S1",
            "chunk_id": "C0001",
            "packet_file_sha256": "a" * 64,
            "outcome_sha256": "p" * 64,
            "mechanical_passed": False,
            "capture_error": refusal_error,
        },
    )
    append_run_ledger_event(
        ledger,
        {
            "state": "review_failed",
            "source_id": "S1",
            "chunk_id": "C0001",
            "outcome_sha256": "p" * 64,
        },
    )

    with pytest.raises(ContractError, match="must be corrected"):
        require_run_ready_for_next_call(
            read_run_ledger(ledger), "S1", "C0001", "a" * 64
        )


@pytest.mark.parametrize(
    "transport_error",
    [
        "URLError:timed out",
        "ConnectionResetError:connection reset by peer",
        "HTTPError:503",
    ],
)
def test_compact_run_ledger_blocks_same_packet_after_other_transport_failures(
    tmp_path, transport_error
):
    ledger = tmp_path / "run.jsonl"
    append_run_ledger_event(
        ledger,
        {
            "state": "call_captured",
            "source_id": "S1",
            "chunk_id": "C0001",
            "packet_file_sha256": "a" * 64,
            "outcome_sha256": "o" * 64,
            "mechanical_passed": False,
            "transport_error": transport_error,
        },
    )
    append_run_ledger_event(
        ledger,
        {
            "state": "review_failed",
            "source_id": "S1",
            "chunk_id": "C0001",
            "outcome_sha256": "o" * 64,
        },
    )

    with pytest.raises(ContractError, match="must be corrected"):
        require_run_ready_for_next_call(
            read_run_ledger(ledger), "S1", "C0001", "a" * 64
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


def test_generic_prompt_requires_each_independent_table_cell_to_ground_its_own_claim():
    prompt = build_generic_source_prompt(
        "M050-SRC-TEST-001",
        ["evidence_game_semantic"],
        "Extract only the bound source.",
    )
    assert "requires exact source text from its own\ncell" in prompt
    assert "never ground a ruling or consequence only in another cell" in prompt


def test_generic_prompt_requires_substantive_list_items_without_cross_block_import():
    prompt = build_generic_source_prompt(
        "M050-SRC-TEST-001",
        ["evidence_game_semantic"],
        "Extract only the bound source.",
    )
    assert "Authored\nlist items are substantive targets" in prompt
    assert "atomize their own text" in prompt


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

    assert packet["source_id"] in state["progress"]["completed_source_ids"]
    assert state["source"]["id"] != packet["source_id"]


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

    observed = {}

    def fake_urlopen(*_args, **kwargs):
        observed["timeout"] = kwargs["timeout"]
        return FakeResponse()

    monkeypatch.setattr(tool.urllib.request, "urlopen", fake_urlopen)
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
    assert observed["timeout"] == 180
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


def test_substantive_review_rejects_shell_interpolation_artifact(tmp_path):
    spec = importlib.util.spec_from_file_location(
        "m050_extraction_machine_review_shell_artifact", MACHINE_TOOL
    )
    assert spec is not None and spec.loader is not None
    tool = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(tool)
    outcome_path = tmp_path / "outcome.json"
    ledger_path = tmp_path / "run.jsonl"
    outcome_path.write_text(json.dumps({
        "source_id": "S1",
        "chunk_id": "C0001",
        "mechanical_validation": {"passed": True, "decision_required": False},
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
        result="failed",
        reviewer="source reviewer",
        reason="Remaining /bin/zsh.1830290 cannot cover the ceiling.",
    )

    with pytest.raises(ContractError, match="shell-interpolation artifact"):
        tool.command_review(args)
    assert read_run_ledger(ledger_path)[-1]["state"] == "call_captured"


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
