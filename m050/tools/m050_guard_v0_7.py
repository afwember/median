#!/usr/bin/env python3
"""Verify the post-R6 source-agnostic extraction-machine checkpoint."""

from __future__ import annotations

import argparse
import importlib.util
import json
from pathlib import Path
import sys


REPO_ROOT = Path(__file__).resolve().parents[2]
ENGINE_SRC = REPO_ROOT / "m050/extraction/engine/src"
sys.path.insert(0, str(ENGINE_SRC))

from median_gate5.canonical import sha256_file  # noqa: E402


PRIOR_PATH = REPO_ROOT / "m050/tools/m050_guard_v0_6.py"
ACTIVE_INDEX = REPO_ROOT / "m050/extraction/control/M050_Active_Control_Index_v0_12_MEDIANv0_5_0.json"
PREDECESSOR_INDEX = REPO_ROOT / "m050/extraction/control/M050_Active_Control_Index_v0_11_MEDIANv0_5_0.json"
CHECKPOINT = REPO_ROOT / "m050/extraction/control/M050_Current_State_Checkpoint_v0_3_MEDIANv0_5_0.json"
CHECKPOINT_REPORT = REPO_ROOT / "m050/extraction/control/M050_Current_State_Checkpoint_v0_3_MEDIANv0_5_0.md"
STANDARD = REPO_ROOT / "m050/extraction/control/M050_Compile_Execution_Standard_v0_1_MEDIANv0_5_0.md"
CONFIG = REPO_ROOT / "m050/extraction/control/M050_Authorial_Grammar_Extraction_Machine_Config_v0_1_MEDIANv0_5_0.json"
CONTROLLER = REPO_ROOT / "m050/tools/m050_extraction_machine_v0_1.py"
ENGINE_MODULE = REPO_ROOT / "m050/extraction/engine/src/median_gate5/extraction_machine.py"
ENGINE_TEST = REPO_ROOT / "m050/extraction/engine/tests/test_extraction_machine.py"
COMPATIBILITY = REPO_ROOT / "m050/extraction/audit/M050_Authorial_Grammar_R6_Extraction_Machine_Compatibility_Receipt_v0_1_MEDIANv0_5_0.json"
AGENTS_OVERRIDE = REPO_ROOT / "AGENTS.override.md"
PILOT_ACCEPTED = REPO_ROOT / "m050/extraction/audit/pilot-transitions/M050_Authorial_Grammar_Pilot_001_R6_Accepted_Transition_v0_6_MEDIANv0_5_0.json"
R6_PAYLOAD = REPO_ROOT / "m050/extraction/calibration/authorial-grammar/pilots/M050_Authorial_Grammar_Pilot_001_R6_Payload_v0_6_MEDIANv0_5_0.json"
R6_PROPOSAL = REPO_ROOT / "m050/extraction/calibration/authorial-grammar/pilots/M050_Authorial_Grammar_Pilot_001_R6_Structured_Proposal_v0_6_MEDIANv0_5_0.json"
R6_SCHEMA = REPO_ROOT / "m050/extraction/calibration/authorial-grammar/M050_Authorial_Grammar_Pilot_001_R6_Response_Schema_v0_6_MEDIANv0_5_0.json"

EXPECTED_SUMMARY = {
    "registered_sources": 24,
    "atomic_compile_exclusions": 2,
    "compile_scope_sources": 22,
    "atomized_legacy_seed_sources": 4,
    "outstanding_compile_scope_sources": 18,
    "outstanding_pre_reconciliation_sources": 14,
    "outstanding_later_or_conditional_sources": 4,
}
EXPECTED_NEXT = "M050-SRC-AUTHORIAL-GRAMMAR-001"
EXPECTED_TESTS = 115


def _load_prior():
    spec = importlib.util.spec_from_file_location("m050_guard_v0_6", PRIOR_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load predecessor guard")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


PRIOR = _load_prior()


def read_json(path: Path, errors: list[str]) -> dict:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"cannot read JSON {path.relative_to(REPO_ROOT)}: {exc}")
        return {}
    if not isinstance(value, dict):
        errors.append(f"JSON root is not an object: {path.relative_to(REPO_ROOT)}")
        return {}
    return value


def validate_historical(errors: list[str], work_order: Path | None) -> tuple:
    historical = PRIOR.validate_historical_foundation(errors, work_order)
    PRIOR.validate_processing_order(errors)
    return historical


def validate_active_index(errors: list[str]) -> dict:
    index = read_json(ACTIVE_INDEX, errors)
    if index.get("schema_version") != "M050-ACTIVE-CONTROL-INDEX-0.12":
        errors.append("active control index version drifted")
    predecessor = index.get("supersedes", {})
    if (
        predecessor.get("path") != str(PREDECESSOR_INDEX.relative_to(REPO_ROOT))
        or not PREDECESSOR_INDEX.is_file()
        or predecessor.get("sha256") != sha256_file(PREDECESSOR_INDEX)
    ):
        errors.append("active control index predecessor binding drifted")
    expected_corpus = {**EXPECTED_SUMMARY, "whole_corpus_atomization_complete": False}
    if index.get("corpus_state") != expected_corpus:
        errors.append("active control index corpus vector drifted")
    calibration = index.get("calibration_state", {})
    if (
        calibration.get("currently_selected_source") != EXPECTED_NEXT
        or calibration.get("current_state") != "pilot_accepted_waiting_full_source_release"
        or calibration.get("pilot_acceptance_releases_full_source") is not False
    ):
        errors.append("active control index misstates the accepted-pilot boundary")
    machine = index.get("execution_machine", {})
    required = {
        "source_specific_workers_permitted": False,
        "declarative_source_configuration_required": True,
        "zero_call_source_scaffold_required": True,
        "claude_cache_ttl": "1h",
        "cache_telemetry_required": True,
        "default_spend_increment_usd": "2.00",
        "spend_envelope_scope": "provider_spend_only",
        "spend_envelope_authorized": False,
        "ordinary_per_call_artifacts": 3,
        "chained_run_ledger_required": True,
        "authorized_chunk_sequence_required": True,
        "prior_review_pass_required": True,
    }
    if any(machine.get(key) != value for key, value in required.items()):
        errors.append("active control index extraction-machine policy drifted")
    boundary = index.get("transition_boundary", {})
    if boundary.get("offline_machine_writes_authorized") is not True:
        errors.append("active control index omits offline machine authority")
    prohibited = {key: value for key, value in boundary.items() if key != "offline_machine_writes_authorized"}
    if not prohibited or any(value is not False for value in prohibited.values()):
        errors.append("active control index crosses a prohibited transition")
    for control in index.get("current_controls", []):
        relative = control.get("path")
        if not isinstance(relative, str) or not (REPO_ROOT / relative).is_file():
            errors.append(f"missing active control: {relative}")
    if index.get("provider_call_authorized") is not False:
        errors.append("active control index authorizes a provider call")
    return index


def validate_machine(errors: list[str]) -> None:
    config = read_json(CONFIG, errors)
    if config.get("schema_version") != "M050-EXTRACTION-MACHINE-CONFIG-0.1":
        errors.append("Authorial machine configuration version drifted")
        return
    if config.get("source_id") != EXPECTED_NEXT:
        errors.append("Authorial machine configuration source drifted")
    provider = config.get("provider", {})
    if (
        provider.get("model") != "claude-sonnet-5"
        or provider.get("reasoning_effort") != "low"
        or provider.get("cache_ttl") != "1h"
        or provider.get("cache_required") is not True
    ):
        errors.append("Authorial machine provider/cache binding drifted")
    execution = config.get("execution", {})
    if (
        execution.get("provider_calls_authorized") is not False
        or execution.get("full_source_authorized") is not False
        or execution.get("spend_envelope_authorized") is not False
        or execution.get("next_chunk_requires_substantive_review_of_prior_chunk") is not True
    ):
        errors.append("Authorial machine configuration crosses an authority boundary")
    for name, relative in config.get("artifacts", {}).items():
        target = REPO_ROOT / relative
        if not target.is_file() or config.get("artifact_sha256", {}).get(name) != sha256_file(target):
            errors.append(f"Authorial machine artifact binding drifted: {name}")
    approval_path = config.get("artifacts", {}).get("identity_approval_receipt")
    card_path = config.get("artifacts", {}).get("identity_card")
    if isinstance(approval_path, str) and isinstance(card_path, str):
        approval = read_json(REPO_ROOT / approval_path, errors)
        card_sha256 = sha256_file(REPO_ROOT / card_path) if (REPO_ROOT / card_path).is_file() else ""
        if (
            approval.get("machine") != "identity_card"
            or approval.get("new_state") != "approved"
            or approval.get("authority") != "Asa Wember"
            or approval.get("artifact_id") != "sic_" + card_sha256[:24]
        ):
            errors.append("Authorial machine identity-card approval binding drifted")
    else:
        errors.append("Authorial machine omits identity-card approval bindings")

    standard = STANDARD.read_text(encoding="utf-8") if STANDARD.is_file() else ""
    for phrase in (
        "one execution configuration per source",
        "provider_spend_only",
        "one-hour caching",
        "three artifacts",
        "Routine append-only runtime capture does not rerun the entire repository suite",
    ):
        if phrase not in standard:
            errors.append(f"compile execution standard omits: {phrase}")
    agents = AGENTS_OVERRIDE.read_text(encoding="utf-8") if AGENTS_OVERRIDE.is_file() else ""
    if STANDARD.relative_to(REPO_ROOT).as_posix() not in agents or "m050_guard_v0_7.py" not in agents:
        errors.append("AGENTS override does not cold-start the active execution standard/guard")
    for path in (CONTROLLER, ENGINE_MODULE, ENGINE_TEST):
        if not path.is_file():
            errors.append(f"missing extraction-machine implementation: {path.relative_to(REPO_ROOT)}")
    controller_text = CONTROLLER.read_text(encoding="utf-8") if CONTROLLER.is_file() else ""
    if 'sub.add_parser("scaffold")' not in controller_text:
        errors.append("extraction-machine controller omits zero-call source scaffold")


def validate_pilot_boundary(errors: list[str]) -> None:
    pilot = read_json(PILOT_ACCEPTED, errors)
    if (
        pilot.get("state") != "pilot_accepted"
        or pilot.get("pilot_result") != "perfect_for_release_as_representative_pilot"
        or pilot.get("mechanical_validation_passed") is not True
        or pilot.get("substantive_review_passed") is not True
        or pilot.get("full_source_execution_authorized") is not False
        or pilot.get("additional_provider_calls_authorized") != 0
    ):
        errors.append("accepted Authorial R6 pilot boundary drifted")
    for path in (R6_PAYLOAD, R6_PROPOSAL, R6_SCHEMA):
        if not path.is_file():
            errors.append(f"missing R6 compatibility artifact: {path.relative_to(REPO_ROOT)}")
    compatibility = read_json(COMPATIBILITY, errors)
    if (
        compatibility.get("status") != "OFFLINE_COMPATIBILITY_VERIFIED"
        or compatibility.get("source_id") != EXPECTED_NEXT
        or compatibility.get("offline_replay", {}).get("passed") is not True
        or compatibility.get("offline_replay", {}).get("decision_required") is not False
        or compatibility.get("successor_machine", {}).get("cache_ttl") != "1h"
        or compatibility.get("successor_machine", {}).get("cache_telemetry_required_on_first_live_call") is not True
        or compatibility.get("limits", {}).get("provider_calls") != 0
        or compatibility.get("limits", {}).get("full_source_execution_authorized") is not False
    ):
        errors.append("R6 generic-machine compatibility receipt drifted")
    accepted_binding = compatibility.get("accepted_pilot_receipt", {})
    if (
        accepted_binding.get("path") != PILOT_ACCEPTED.relative_to(REPO_ROOT).as_posix()
        or accepted_binding.get("sha256") != sha256_file(PILOT_ACCEPTED)
    ):
        errors.append("R6 compatibility receipt accepted-pilot binding drifted")
    saved = compatibility.get("saved_artifacts", {})
    expected_saved = {
        "payload_sha256": sha256_file(R6_PAYLOAD),
        "structured_proposal_sha256": sha256_file(R6_PROPOSAL),
        "response_schema_sha256": sha256_file(R6_SCHEMA),
    }
    if any(saved.get(key) != value for key, value in expected_saved.items()):
        errors.append("R6 compatibility receipt saved-artifact binding drifted")
    successor = compatibility.get("successor_machine", {})
    expected_successor = {
        "configuration_sha256": sha256_file(CONFIG),
        "controller_sha256": sha256_file(CONTROLLER),
        "engine_module_sha256": sha256_file(ENGINE_MODULE),
    }
    if any(successor.get(key) != value for key, value in expected_successor.items()):
        errors.append("R6 compatibility receipt successor-machine binding drifted")


def validate_checkpoint(errors: list[str]) -> None:
    checkpoint = read_json(CHECKPOINT, errors)
    if checkpoint.get("status") != "POST_R6_EXTRACTION_MACHINE_OFFLINE_READY":
        errors.append("post-R6 checkpoint status drifted")
    if checkpoint.get("corpus_vector") != EXPECTED_SUMMARY:
        errors.append("post-R6 checkpoint corpus vector drifted")
    if checkpoint.get("next_source_id") != EXPECTED_NEXT:
        errors.append("post-R6 checkpoint source drifted")
    authority = checkpoint.get("authority_boundary", {})
    if (
        authority.get("provider_calls_authorized") is not False
        or authority.get("full_source_authorized") is not False
        or authority.get("spend_envelope_authorized") is not False
    ):
        errors.append("post-R6 checkpoint crosses an authority boundary")
    for name, binding in checkpoint.get("artifacts", {}).items():
        relative = binding.get("path")
        target = REPO_ROOT / relative if isinstance(relative, str) else Path("/__missing__")
        if not target.is_file() or binding.get("sha256") != sha256_file(target):
            errors.append(f"post-R6 checkpoint artifact drifted: {name}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--work-order", type=Path)
    parser.add_argument("--with-tests", action="store_true")
    args = parser.parse_args()
    errors: list[str] = []
    historical = validate_historical(errors, args.work_order)
    validate_active_index(errors)
    validate_machine(errors)
    validate_pilot_boundary(errors)
    validate_checkpoint(errors)
    engine_files, engine_digest = PRIOR.PRIOR.PRIOR.PRIOR.engine_snapshot()
    test_count = None
    if args.with_tests:
        test_count = PRIOR.PRIOR.PRIOR.PRIOR.run_tests()
        if test_count:
            errors.append("Gate 5 offline regression suite failed")
    if errors:
        print("M050 GATE 5 EXTRACTION-MACHINE GUARD: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1
    print("M050 GATE 5 EXTRACTION-MACHINE GUARD: PASS")
    print("- corpus vector: 24 registered / 22 compile / 4 atomized / 18 outstanding = 14 + 4")
    print("- next source: Authorial Grammar; Pilot 001-R6 accepted")
    print("- full-source and provider calls: not authorized")
    print("- machine: one declarative controller; sequential call/review")
    print("- artifacts: packet + raw response + outcome; one chained run ledger")
    print("- Claude cache: explicit one-hour stable prefix; telemetry required")
    print("- spend: independent cumulative money envelope; currently unauthorized")
    print(f"- engine files: {engine_files}")
    print(f"- engine digest: {engine_digest}")
    print(f"- preserved legacy candidates: {historical[7]}/913")
    print("- semantic acceptance/mapping/reconciliation/compiled prose: prohibited")
    print("- Google Sheets: paused")
    if args.with_tests:
        print(f"- offline regression suite: pass ({EXPECTED_TESTS} expected tests)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
