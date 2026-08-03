import copy
from collections import Counter
import hashlib
import importlib.util
import json
from pathlib import Path

import jsonschema

from median_gate5.calibration import require_source_readiness
from median_gate5.validation import (
    validate_atoms,
    validate_block_dispositions,
)


REPO_ROOT = Path(__file__).resolve().parents[4]
SOURCE_ID = "M050-SRC-AUTHORIAL-GRAMMAR-001"
SOURCE = REPO_ROOT / "m050/docs/v0.5/governance/M050_Authorial_Grammar_Orthography_and_Prose_Style_Guide_v0_1_MEDIANv0_5_0.md"
MANIFEST = REPO_ROOT / "m050/extraction/control/source-identities/blocks/M050_Authorial_Grammar_Block_Manifest_v0_1_MEDIANv0_5_0.json"
PLAN = REPO_ROOT / "m050/extraction/control/M050_Authorial_Grammar_Section_Aware_Chunk_Plan_v0_1_MEDIANv0_5_0.json"
LEDGER = REPO_ROOT / "m050/extraction/calibration/authorial-grammar/M050_Authorial_Grammar_Block_Disposition_Ledger_v0_1_MEDIANv0_5_0.jsonl"
PROFILE = REPO_ROOT / "m050/extraction/calibration/authorial-grammar/M050_Authorial_Grammar_Offline_Readiness_Profile_v0_1_MEDIANv0_5_0.json"
PROMPT = REPO_ROOT / "m050/extraction/calibration/authorial-grammar/M050_Authorial_Grammar_Extraction_Prompt_v0_1_MEDIANv0_5_0.md"
RESPONSE_SCHEMA = REPO_ROOT / "m050/extraction/calibration/authorial-grammar/M050_Authorial_Grammar_Extraction_Response_Schema_v0_2_MEDIANv0_5_0.json"
PILOTS = REPO_ROOT / "m050/extraction/calibration/authorial-grammar/pilots"
VALIDATOR = REPO_ROOT / "m050/tools/m050_validate_source_pilot_v0_2.py"
R5_PROMPT = REPO_ROOT / "m050/extraction/calibration/authorial-grammar/M050_Authorial_Grammar_Extraction_Prompt_v0_2_MEDIANv0_5_0.md"
R5_SCHEMA = REPO_ROOT / "m050/extraction/calibration/authorial-grammar/M050_Authorial_Grammar_Pilot_001_R5_Response_Schema_v0_5_MEDIANv0_5_0.json"
R5_VALIDATOR = REPO_ROOT / "m050/tools/m050_validate_source_pilot_v0_3.py"
R6_SCHEMA = REPO_ROOT / "m050/extraction/calibration/authorial-grammar/M050_Authorial_Grammar_Pilot_001_R6_Response_Schema_v0_6_MEDIANv0_5_0.json"


def _load_validator():
    spec = importlib.util.spec_from_file_location("m050_source_pilot_validator", VALIDATOR)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def _load_module(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def _json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def _ledger():
    return [json.loads(line) for line in LEDGER.read_text(encoding="utf-8").splitlines()]


def _fixture():
    manifest = _json(MANIFEST)
    block = next(item for item in manifest["blocks"] if item["ordinal"] == 383)
    proposal = {
        "schema_version": "M050-EVIDENCE-PROPOSAL-0.1",
        "proposal_set_id": "offline-fake-valid-001",
        "request_id": "offline-not-sent-001",
        "source_id": SOURCE_ID,
        "dispositions": [
            {
                "block_id": block["block_id"],
                "kind": "atoms",
                "atoms": [
                    {
                        "proposal_id": "offline-proposal-001",
                        "source_id": SOURCE_ID,
                        "block_id": block["block_id"],
                        "exact_source_text": "status: PROVISIONAL",
                        "normalized_claim": "Mechanics-teaching Narrative italics have PROVISIONAL status.",
                        "claim_kind": "authorial_convention_status",
                        "stream": "evidence_authorial_rule",
                    }
                ],
            }
        ],
    }
    return manifest, block, proposal


def _validate_profile_constraints(proposal, blocks, *, allowed_block_ids):
    errors = []
    if proposal.get("source_id") != SOURCE_ID:
        errors.append("proposal source_id violates source profile")
    by_id = {block["block_id"]: block for block in blocks}
    proposal_ids = []
    for disposition in proposal.get("dispositions", []):
        block_id = disposition.get("block_id")
        if block_id not in allowed_block_ids:
            errors.append(f"block outside source profile: {block_id}")
        statuses = {
            marker.split(":", 1)[-1].strip().upper()
            for marker in by_id.get(block_id, {}).get("status_markers", [])
        }
        for atom in disposition.get("atoms", []):
            proposal_ids.append(str(atom.get("proposal_id")))
            if atom.get("source_id") != SOURCE_ID:
                errors.append("atom source_id violates source profile")
            if atom.get("stream") != "evidence_authorial_rule":
                errors.append("atom stream violates source profile")
            normalized = str(atom.get("normalized_claim", "")).upper()
            for status in statuses:
                if status not in normalized:
                    errors.append(f"status qualifier {status} missing from atom")
    duplicates = [key for key, count in Counter(proposal_ids).items() if count > 1]
    if duplicates:
        errors.append("duplicate proposal IDs")
    return {"passed": not errors, "errors": errors}


def test_authorial_profile_binds_complete_source_and_accounts_every_block():
    manifest = _json(MANIFEST)
    profile = _json(PROFILE)
    ledger = _ledger()
    source_bytes = SOURCE.read_bytes()
    assert hashlib.sha256(source_bytes).hexdigest() == profile["source_sha256"]
    assert "".join(block["text"] for block in manifest["blocks"]) == source_bytes.decode()
    assert len(manifest["blocks"]) == len(ledger) == 590
    assert {block["block_id"] for block in manifest["blocks"]} == {
        item["block_id"] for item in ledger
    }
    counts = profile["structural_accounting"]
    assert counts["total_blocks"] == sum(
        counts[key] for key in ("eligible_blocks", "excluded_blocks", "context_only_blocks")
    )
    assert all(item["disposition"] == "excluded" for item in ledger[-14:])
    assert next(item for item in ledger if "__B00383_" in item["block_id"])["disposition"] == "eligible"
    require_source_readiness(profile)


def test_section_plan_covers_blocks_once_and_keeps_provisional_section_together():
    manifest = _json(MANIFEST)
    plan = _json(PLAN)
    planned = [block_id for chunk in plan["chunks"] for block_id in chunk["block_ids"]]
    assert planned == [block["block_id"] for block in manifest["blocks"]]
    assert len(plan["chunks"]) == 5
    provisional_id = next(
        block["block_id"] for block in manifest["blocks"] if block["ordinal"] == 383
    )
    section_start = next(
        block["block_id"] for block in manifest["blocks"] if block["ordinal"] == 367
    )
    section_end = next(
        block["block_id"] for block in manifest["blocks"] if block["ordinal"] == 405
    )
    chunk = next(item for item in plan["chunks"] if provisional_id in item["block_ids"])
    assert section_start in chunk["block_ids"] and section_end in chunk["block_ids"]


def test_prompt_and_schema_enforce_source_only_authorial_stream():
    prompt = PROMPT.read_text(encoding="utf-8")
    schema = _json(RESPONSE_SCHEMA)
    jsonschema.Draft202012Validator.check_schema(schema)
    assert "Allowed source: `M050-SRC-AUTHORIAL-GRAMMAR-001` only" in prompt
    assert "Allowed stream: `evidence_authorial_rule` only" in prompt
    assert "No source text is embedded" in prompt
    _, _, proposal = _fixture()
    jsonschema.validate(proposal, schema)
    prohibited_provider_keywords = {"if", "then", "else", "allOf"}

    def keys(value):
        if isinstance(value, dict):
            for key, child in value.items():
                yield key
                yield from keys(child)
        elif isinstance(value, list):
            for child in value:
                yield from keys(child)

    assert prohibited_provider_keywords.isdisjoint(keys(schema))


def test_valid_fake_response_passes_grounding_profile_and_status_gates():
    manifest, block, proposal = _fixture()
    profiled_block = {**block, "claim_bearing": True}
    assert validate_block_dispositions([profiled_block], proposal["dispositions"])["passed"]
    assert validate_atoms(SOURCE_ID, [block], proposal["dispositions"])["passed"]
    assert _validate_profile_constraints(
        proposal,
        manifest["blocks"],
        allowed_block_ids={item["block_id"] for item in _ledger() if item["disposition"] == "eligible"},
    )["passed"]


def test_malformed_fake_responses_fail_closed():
    manifest, block, proposal = _fixture()
    allowed = {item["block_id"] for item in _ledger() if item["disposition"] == "eligible"}

    wrong_stream = copy.deepcopy(proposal)
    wrong_stream["dispositions"][0]["atoms"][0]["stream"] = "evidence_game_semantic"
    result = _validate_profile_constraints(
        wrong_stream, manifest["blocks"], allowed_block_ids=allowed,
    )
    assert not result["passed"] and any("stream" in error for error in result["errors"])

    lost_status = copy.deepcopy(proposal)
    lost_status["dispositions"][0]["atoms"][0]["normalized_claim"] = "Narrative italics are required."
    result = _validate_profile_constraints(
        lost_status, manifest["blocks"], allowed_block_ids=allowed,
    )
    assert not result["passed"] and any("PROVISIONAL" in error for error in result["errors"])

    foreign = copy.deepcopy(proposal)
    foreign["source_id"] = "M050-SRC-HUMAN-RULINGS-001"
    foreign["dispositions"][0]["atoms"][0]["source_id"] = "M050-SRC-HUMAN-RULINGS-001"
    result = _validate_profile_constraints(
        foreign, manifest["blocks"], allowed_block_ids=allowed,
    )
    assert not result["passed"] and any("source_id" in error for error in result["errors"])

    ungrounded = copy.deepcopy(proposal)
    ungrounded["dispositions"][0]["atoms"][0]["exact_source_text"] = "invented text"
    assert not validate_atoms(SOURCE_ID, [block], ungrounded["dispositions"])["passed"]

    change_block = next(item for item in manifest["blocks"] if item["ordinal"] == 580)
    excluded = copy.deepcopy(proposal)
    excluded["dispositions"][0]["block_id"] = change_block["block_id"]
    excluded["dispositions"][0]["atoms"][0]["block_id"] = change_block["block_id"]
    result = _validate_profile_constraints(
        excluded, manifest["blocks"], allowed_block_ids=allowed,
    )
    assert not result["passed"] and any("outside source profile" in error for error in result["errors"])


def test_frozen_request_candidates_are_exact_source_only_claude_low_requests():
    ledger = {item["block_id"]: item for item in _ledger()}
    for number in (1, 2, 3):
        stem = f"M050_Authorial_Grammar_Pilot_{number:03d}"
        payload_path = PILOTS / f"{stem}_Payload_v0_1_MEDIANv0_5_0.json"
        request_path = PILOTS / f"{stem}_Anthropic_Request_v0_1_MEDIANv0_5_0.json"
        payload = _json(payload_path)
        request = _json(request_path)
        assert request["model"] == "claude-sonnet-5"
        assert request["thinking"] == {"type": "adaptive"}
        assert request["output_config"]["effort"] == "low"
        assert request["output_config"]["format"]["type"] == "json_schema"
        assert "temperature" not in request and "top_p" not in request and "tools" not in request
        assert len(request["messages"]) == 1 and request["messages"][0]["role"] == "user"
        expected_content = (
            "SOURCE_BLOCKS\n"
            + json.dumps(payload, sort_keys=True, separators=(",", ":"))
            + "\nEND_SOURCE_BLOCKS"
        )
        assert request["messages"][0]["content"] == expected_content
        assert payload["source_id"] == SOURCE_ID
        assert all(block["block_id"].startswith(SOURCE_ID + "__") for block in payload["blocks"])
        assert all(ledger[block["block_id"]]["disposition"] != "excluded" for block in payload["blocks"])
        assert "M050-SRC-HUMAN-RULINGS-001" not in request["messages"][0]["content"]


def test_r2_request_uses_provider_supported_schema_and_preserves_exact_payload():
    payload = _json(PILOTS / "M050_Authorial_Grammar_Pilot_001_R2_Payload_v0_2_MEDIANv0_5_0.json")
    request = _json(PILOTS / "M050_Authorial_Grammar_Pilot_001_R2_Anthropic_Request_v0_2_MEDIANv0_5_0.json")
    assert payload["pilot_id"] == "M050-AUTHGRAM-PILOT-001-R2"
    assert request["model"] == "claude-sonnet-5"
    assert request["output_config"]["effort"] == "low"
    provider_schema = request["output_config"]["format"]["schema"]
    serialized_schema = json.dumps(provider_schema, sort_keys=True)
    assert all(f'"{keyword}"' not in serialized_schema for keyword in ("if", "then", "else", "allOf"))
    assert request["messages"][0]["content"] == (
        "SOURCE_BLOCKS\n"
        + json.dumps(payload, sort_keys=True, separators=(",", ":"))
        + "\nEND_SOURCE_BLOCKS"
    )


def test_r3_request_expands_only_bound_output_allowance_under_new_cap():
    r2 = _json(PILOTS / "M050_Authorial_Grammar_Pilot_001_R2_Anthropic_Request_v0_2_MEDIANv0_5_0.json")
    r3 = _json(PILOTS / "M050_Authorial_Grammar_Pilot_001_R3_Anthropic_Request_v0_3_MEDIANv0_5_0.json")
    payload = _json(PILOTS / "M050_Authorial_Grammar_Pilot_001_R3_Payload_v0_3_MEDIANv0_5_0.json")
    assert r3["max_tokens"] == 12000
    assert r3["model"] == r2["model"] == "claude-sonnet-5"
    assert r3["thinking"] == r2["thinking"] == {"type": "adaptive"}
    assert r3["output_config"] == r2["output_config"]
    assert r3["system"] == r2["system"]
    assert r3["messages"][0]["content"] == (
        "SOURCE_BLOCKS\n"
        + json.dumps(payload, sort_keys=True, separators=(",", ":"))
        + "\nEND_SOURCE_BLOCKS"
    )


def test_r4_request_targets_established_six_thousand_token_regime():
    payload = _json(PILOTS / "M050_Authorial_Grammar_Pilot_001_R4_Payload_v0_4_MEDIANv0_5_0.json")
    request = _json(PILOTS / "M050_Authorial_Grammar_Pilot_001_R4_Anthropic_Request_v0_4_MEDIANv0_5_0.json")
    assert payload["pilot_id"] == "M050-AUTHGRAM-PILOT-001-R4"
    assert payload["ordinal_range"] == [77, 170]
    assert sum(block["structural_disposition"] == "eligible" for block in payload["blocks"]) == 27
    assert request["max_tokens"] == 6000
    assert request["model"] == "claude-sonnet-5"
    assert request["output_config"]["effort"] == "low"
    assert request["messages"][0]["content"] == (
        "SOURCE_BLOCKS\n"
        + json.dumps(payload, sort_keys=True, separators=(",", ":"))
        + "\nEND_SOURCE_BLOCKS"
    )


def test_r5_schema_payload_and_prompt_force_complete_target_only_output():
    schema = _json(R5_SCHEMA)
    payload = _json(PILOTS / "M050_Authorial_Grammar_Pilot_001_R5_Payload_v0_5_MEDIANv0_5_0.json")
    request = _json(PILOTS / "M050_Authorial_Grammar_Pilot_001_R5_Anthropic_Request_v0_5_MEDIANv0_5_0.json")
    prompt = R5_PROMPT.read_text(encoding="utf-8")
    dispositions = schema["properties"]["dispositions"]
    item = dispositions["items"]
    assert dispositions["minItems"] == dispositions["maxItems"] == 27
    assert "atoms" in item["required"]
    assert "excluded" not in item["properties"]["kind"]["enum"]
    assert len(payload["target_blocks"]) == 27
    assert len(payload["context_blocks"]) == 19
    assert "blocks" not in payload
    target_ids = {block["block_id"] for block in payload["target_blocks"]}
    context_ids = {block["block_id"] for block in payload["context_blocks"]}
    assert target_ids.isdisjoint(context_ids)
    assert "Never return a disposition for a context block" in prompt
    assert "Return exactly one disposition for every target block" in prompt
    assert request["max_tokens"] == 6000
    assert request["output_config"]["format"]["schema"] == {
        key: value for key, value in schema.items() if key not in {"$schema", "$id"}
    }
    assert request["messages"][0]["content"] == (
        "SOURCE_BLOCKS\n"
        + json.dumps(payload, sort_keys=True, separators=(",", ":"))
        + "\nEND_SOURCE_BLOCKS"
    )


def test_r5_validator_accepts_complete_empty_arrays_and_rejects_all_contract_defects():
    validator = _load_module(R5_VALIDATOR, "m050_r5_validator")
    payload = _json(PILOTS / "M050_Authorial_Grammar_Pilot_001_R5_Payload_v0_5_MEDIANv0_5_0.json")
    schema = _json(R5_SCHEMA)
    response = {
        "schema_version": "M050-EVIDENCE-PROPOSAL-0.1",
        "proposal_set_id": "offline-r5-complete",
        "request_id": "offline-not-sent-r5",
        "source_id": SOURCE_ID,
        "dispositions": [
            {"block_id": block["block_id"], "kind": "review_required", "atoms": []}
            for block in payload["target_blocks"]
        ],
    }
    assert validator.validate_pilot_response(payload, response, schema)["passed"]

    missing = copy.deepcopy(response)
    missing["dispositions"].pop()
    assert not validator.validate_pilot_response(payload, missing, schema)["passed"]

    context = copy.deepcopy(response)
    context["dispositions"][0]["block_id"] = payload["context_blocks"][0]["block_id"]
    result = validator.validate_pilot_response(payload, context, schema)
    assert not result["passed"] and any("context-only" in error for error in result["errors"])

    empty_atoms = copy.deepcopy(response)
    empty_atoms["dispositions"][0]["kind"] = "atoms"
    result = validator.validate_pilot_response(payload, empty_atoms, schema)
    assert not result["passed"] and any("lacks atoms" in error for error in result["errors"])

    nonempty_review = copy.deepcopy(response)
    target = payload["target_blocks"][0]
    nonempty_review["dispositions"][0]["atoms"] = [{
        "proposal_id": "offline-r5-invalid-atom",
        "source_id": SOURCE_ID,
        "block_id": target["block_id"],
        "exact_source_text": target["text"].strip(),
        "normalized_claim": "Offline test only.",
        "claim_kind": "offline_test",
        "stream": "evidence_authorial_rule",
    }]
    result = validator.validate_pilot_response(payload, nonempty_review, schema)
    assert not result["passed"] and any("non-atoms disposition carries atoms" in error for error in result["errors"])


def test_r6_provider_schema_uses_supported_constraints_and_local_exact_coverage():
    validator = _load_module(R5_VALIDATOR, "m050_r6_validator")
    schema = _json(R6_SCHEMA)
    payload = _json(PILOTS / "M050_Authorial_Grammar_Pilot_001_R6_Payload_v0_6_MEDIANv0_5_0.json")
    request = _json(PILOTS / "M050_Authorial_Grammar_Pilot_001_R6_Anthropic_Request_v0_6_MEDIANv0_5_0.json")
    dispositions = schema["properties"]["dispositions"]
    assert dispositions.get("minItems") == 1
    assert "maxItems" not in dispositions
    serialized = json.dumps(request["output_config"]["format"]["schema"], sort_keys=True)
    assert all(f'"{keyword}"' not in serialized for keyword in (
        "if", "then", "else", "allOf", "maxItems", "minLength", "maxLength"
    ))
    assert payload["required_target_disposition_count"] == len(payload["target_blocks"]) == 27
    response = {
        "schema_version": "M050-EVIDENCE-PROPOSAL-0.1",
        "proposal_set_id": "offline-r6-complete",
        "request_id": "offline-not-sent-r6",
        "source_id": SOURCE_ID,
        "dispositions": [
            {"block_id": block["block_id"], "kind": "review_required", "atoms": []}
            for block in payload["target_blocks"]
        ],
    }
    assert validator.validate_pilot_response(payload, response, schema)["passed"]
    incomplete = copy.deepcopy(response)
    incomplete["dispositions"] = incomplete["dispositions"][:3]
    result = validator.validate_pilot_response(payload, incomplete, schema)
    assert not result["passed"] and any("coverage" in error for error in result["errors"])


def test_bound_pilot_validator_passes_complete_fake_and_fails_context_disposition():
    validator = _load_validator()
    payload = _json(PILOTS / "M050_Authorial_Grammar_Pilot_002_Payload_v0_1_MEDIANv0_5_0.json")
    schema = _json(RESPONSE_SCHEMA)
    eligible = [
        block for block in payload["blocks"]
        if block["structural_disposition"] == "eligible"
    ]
    response = {
        "schema_version": "M050-EVIDENCE-PROPOSAL-0.1",
        "proposal_set_id": "offline-complete-fake-002",
        "request_id": "offline-not-sent-002",
        "source_id": SOURCE_ID,
        "dispositions": [
            {"block_id": block["block_id"], "kind": "review_required"}
            for block in eligible
        ],
    }
    assert validator.validate_pilot_response(payload, response, schema)["passed"]
    context = next(
        block for block in payload["blocks"]
        if block["structural_disposition"] == "context_only"
    )
    malformed = copy.deepcopy(response)
    malformed["dispositions"].append(
        {"block_id": context["block_id"], "kind": "no_substantive_claim"}
    )
    result = validator.validate_pilot_response(payload, malformed, schema)
    assert not result["passed"]
    assert any("context-only" in error or "coverage" in error for error in result["errors"])

    conditional = copy.deepcopy(response)
    conditional["dispositions"][0]["atoms"] = [_fixture()[2]["dispositions"][0]["atoms"][0]]
    result = validator.validate_pilot_response(payload, conditional, schema)
    assert not result["passed"]
    assert any("non-atoms disposition carries atoms" in error for error in result["errors"])
