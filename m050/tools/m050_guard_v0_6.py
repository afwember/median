#!/usr/bin/env python3
"""Verify the MEDIAN Gate 5 calibration-provisioning amendment."""

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


PRIOR_GUARD_PATH = REPO_ROOT / "m050/tools/m050_guard_v0_5.py"
AGENTS_OVERRIDE = REPO_ROOT / "AGENTS.override.md"
ACTIVE_INDEX = REPO_ROOT / "m050/extraction/control/M050_Active_Control_Index_v0_11_MEDIANv0_5_0.json"
GATE_2 = REPO_ROOT / "m050/extraction/audit/M050_Extraction_Gate_2_Source_Disposition_v0_1_MEDIANv0_5_0.yaml"
MATRIX = REPO_ROOT / "m050/extraction/control/M050_Compile_Source_State_Matrix_v0_1_MEDIANv0_5_0.json"
MATRIX_REPORT = REPO_ROOT / "m050/extraction/control/M050_Compile_Source_State_Matrix_v0_1_MEDIANv0_5_0.md"
TRACKER = REPO_ROOT / "m050/extraction/progress/M050_Document_Processing_Tracker_v0_1_MEDIANv0_5_0.xlsx"
ORDER = REPO_ROOT / "m050/extraction/control/M050_Compile_Source_Processing_Order_v0_1_MEDIANv0_5_0.json"
PROTOCOL = REPO_ROOT / "m050/extraction/control/M050_Source_Atomization_Pilot_Calibration_Protocol_v0_1_MEDIANv0_5_0.md"
CHECKPOINT = REPO_ROOT / "m050/extraction/control/M050_Current_State_Checkpoint_v0_2_MEDIANv0_5_0.json"
CHECKPOINT_REPORT = REPO_ROOT / "m050/extraction/control/M050_Current_State_Checkpoint_v0_2_MEDIANv0_5_0.md"
BOOTSTRAP = REPO_ROOT / "m050/extraction/control/M050_New_Task_Bootstrap_v0_2_MEDIANv0_5_0.md"
AMENDMENT_REPORT = REPO_ROOT / "m050/extraction/audit/M050_Atomization_Calibration_Provisioning_Amendment_Report_v0_1_MEDIANv0_5_0.md"
OVERSIGHT_AUDIT = REPO_ROOT / "m050/extraction/audit/M050_Compile_Provisioning_Categorical_Oversight_Audit_v0_1_MEDIANv0_5_0.md"
ARCHIVE_SCAN = REPO_ROOT / "m050/extraction/audit/M050_Post_Cleanup_External_Archive_Recovery_Scan_v0_1_MEDIANv0_5_0.md"
AMENDMENT_RECEIPT = REPO_ROOT / "m050/extraction/audit/M050_Atomization_Calibration_Provisioning_Amendment_Receipt_v0_1_MEDIANv0_5_0.json"
CALIBRATION_MODULE = REPO_ROOT / "m050/extraction/engine/src/median_gate5/calibration.py"
PREDECESSOR_INDEX = REPO_ROOT / "m050/extraction/control/M050_Active_Control_Index_v0_10_MEDIANv0_5_0.json"
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
EXPECTED_TRACKER_SHA256 = "7a05dbcfeadf7a012a8ea00987ab6138a35d9b6c71cb70df82e44ef69cfa778c"
EXPECTED_GATE_2_SHA256 = "f460dd7c3ebf2df9344ee58aa8f650c3314af436b7684bf6cd2bf674fef5bf63"
EXPECTED_REGRESSION_CASES = 65
EXPECTED_OFFLINE_TESTS = 99


def _load_prior_guard():
    spec = importlib.util.spec_from_file_location("m050_guard_v0_5", PRIOR_GUARD_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load predecessor Gate 5 guard")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


PRIOR = _load_prior_guard()


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


def validate_bindings(container: dict, key: str, artifacts: dict[str, Path], errors: list[str]) -> None:
    bindings = container.get(key, {})
    for name, path in artifacts.items():
        binding = bindings.get(name, {})
        relative = path.relative_to(REPO_ROOT).as_posix()
        if binding.get("path") != relative:
            errors.append(f"{key} path binding mismatch: {name}")
        elif not path.is_file() or binding.get("sha256") != sha256_file(path):
            errors.append(f"{key} hash binding mismatch: {name}")


def validate_historical_foundation(errors: list[str], work_order: Path | None) -> tuple:
    historical = PRIOR.validate_historical_foundation(errors, work_order)
    PRIOR.validate_matrix(errors)
    PRIOR.validate_active_index(errors)
    PRIOR.validate_checkpoint(errors)
    receipt_errors: list[str] = []
    PRIOR.validate_correction_receipt(receipt_errors)
    errors.extend(
        error
        for error in receipt_errors
        if error != "corpus-scope correction receipt engine snapshot mismatch"
    )
    return historical


def validate_processing_order(errors: list[str]) -> dict:
    order = read_json(ORDER, errors)
    matrix = read_json(MATRIX, errors)
    if not TRACKER.is_file() or sha256_file(TRACKER) != EXPECTED_TRACKER_SHA256:
        errors.append("processing tracker hash drifted from recovered source order authority")
    if not GATE_2.is_file() or sha256_file(GATE_2) != EXPECTED_GATE_2_SHA256:
        errors.append("Gate 2 disposition hash drifted from processing order authority")
    authority = order.get("authority", {})
    if authority.get("sequence_source_sha256") != EXPECTED_TRACKER_SHA256:
        errors.append("processing order does not bind the recovered tracker sequence")
    if authority.get("disposition_source_sha256") != EXPECTED_GATE_2_SHA256:
        errors.append("processing order does not bind Gate 2 disposition authority")

    sequence = order.get("sequence", [])
    sources = matrix.get("sources", [])
    by_id = {source.get("source_id"): source for source in sources}
    if [item.get("order") for item in sequence] != list(range(1, 25)):
        errors.append("processing order is not an exact 1-through-24 sequence")
    sequence_ids = [item.get("source_id") for item in sequence]
    if len(sequence_ids) != 24 or len(set(sequence_ids)) != 24 or set(sequence_ids) != set(by_id):
        errors.append("processing order does not exactly cover the 24 Gate 2 sources")
    for item in sequence:
        source = by_id.get(item.get("source_id"), {})
        if (
            item.get("matrix_position") != source.get("position")
            or item.get("current_state") != source.get("current_state")
            or item.get("processing_phase") != source.get("processing_phase")
        ):
            errors.append(f"processing order state drift: {item.get('source_id')}")
    expected_queue = [
        source_id
        for source_id in sequence_ids
        if by_id.get(source_id, {}).get("current_state") == "outstanding"
        and by_id.get(source_id, {}).get("processing_phase") == "pre_reconciliation_atomization"
    ]
    if len(expected_queue) != 14 or order.get("outstanding_pre_reconciliation_order") != expected_queue:
        errors.append("processing order does not preserve the exact 14-source pre-reconciliation queue")
    if order.get("next_source", {}).get("source_id") != EXPECTED_NEXT or expected_queue[:1] != [EXPECTED_NEXT]:
        errors.append("processing order does not identify Authorial Grammar as next")
    authorial_control = sequence[0].get("pre_candidate_acceptance_control", {}) if sequence else {}
    if (
        authorial_control.get("higher_authority_source_id") != "M050-SRC-HUMAN-RULINGS-001"
        or authorial_control.get("provider_prompt_inclusion") != "prohibited"
        or "Layer E semantic acceptance" not in authorial_control.get("effect", "")
    ):
        errors.append("processing order omits the recovered Authorial Grammar conformance boundary")
    constraints = order.get("transition_constraints", {})
    if not constraints or any(value is not False for value in constraints.values()):
        errors.append("processing order authorizes a prohibited transition")
    return order


def validate_active_index(errors: list[str]) -> dict:
    index = read_json(ACTIVE_INDEX, errors)
    if index.get("execution_state") != "GATE_5_PILOT_CALIBRATION_PROTOCOL_PROVISIONED_CORPUS_ATOMIZATION_INCOMPLETE":
        errors.append("active v0.11 execution state drifted")
    if index.get("corpus_state") != {**EXPECTED_SUMMARY, "whole_corpus_atomization_complete": False}:
        errors.append("active v0.11 corpus vector drifted")
    calibration = index.get("calibration_state", {})
    expected_false = {
        "prior_source_authority_transfers",
        "pilot_acceptance_releases_full_source",
        "source_extraction_acceptance_is_layer_e_semantic_acceptance",
    }
    expected_true = {
        "protocol_provisioned",
        "applies_to_every_new_source",
        "approved_identity_card_required_before_offline_dry_run",
        "offline_dry_run_required",
        "representative_pilot_required",
        "perfect_for_release_required",
        "separate_author_full_source_release_required",
        "stoppable_chunk_execution_required",
        "defect_revokes_source_run",
        "whole_document_gate_required",
        "source_only_prompt_firewall_required",
        "embedded_media_disposition_required",
        "complete_configuration_binding_required",
    }
    if any(calibration.get(key) is not False for key in expected_false):
        errors.append("active v0.11 calibration state grants an unsafe implicit transition")
    if any(calibration.get(key) is not True for key in expected_true):
        errors.append("active v0.11 calibration state omits a mandatory gate")
    if (
        calibration.get("currently_selected_source") is not None
        or calibration.get("current_state") != "unstarted_read_only"
        or calibration.get("default_execution_cadence") != "sequential_one_call_review"
    ):
        errors.append("active v0.11 claims source work or a non-sequential default")
    boundary = index.get("transition_boundary", {})
    if not boundary or any(value is not False for value in boundary.values()):
        errors.append("active v0.11 authorizes a prohibited transition")
    if index.get("provider_call_authorized") is not False or index.get("google_sheets_interaction_authorized") is not False:
        errors.append("active v0.11 crossed a paused external boundary")
    for control in index.get("current_controls", []):
        relative = control.get("path")
        if not isinstance(relative, str) or not relative or not (REPO_ROOT / relative).is_file():
            errors.append(f"missing v0.11 active control: {relative}")
    return index


def validate_checkpoint(errors: list[str]) -> dict:
    checkpoint = read_json(CHECKPOINT, errors)
    if checkpoint.get("status") != "CALIBRATION_PROVISIONING_AMENDED_HANDOFF_READY":
        errors.append("amended checkpoint has unexpected status")
    if checkpoint.get("predecessor_commit") != "bfcb55847533f183a52831b51afefe23d9e5d981":
        errors.append("amended checkpoint predecessor commit drifted")
    if checkpoint.get("corpus_vector") != EXPECTED_SUMMARY:
        errors.append("amended checkpoint corpus vector drifted")
    if checkpoint.get("next_source_id") != EXPECTED_NEXT:
        errors.append("amended checkpoint next source drifted")
    if checkpoint.get("successor_authority") != "READ_ONLY_UNTIL_EXPLICIT_AUTHOR_TRANSFER":
        errors.append("amended checkpoint grants successor write authority")
    validate_bindings(
        checkpoint,
        "artifacts",
        {
            "agents_override": AGENTS_OVERRIDE,
            "active_control_index": ACTIVE_INDEX,
            "gate_2_source_disposition": GATE_2,
            "source_state_matrix": MATRIX,
            "source_state_report": MATRIX_REPORT,
            "document_processing_tracker": TRACKER,
            "source_processing_order": ORDER,
            "calibration_protocol": PROTOCOL,
            "checkpoint_report": CHECKPOINT_REPORT,
            "new_task_bootstrap": BOOTSTRAP,
            "amendment_report": AMENDMENT_REPORT,
            "categorical_oversight_audit": OVERSIGHT_AUDIT,
            "external_archive_recovery_scan": ARCHIVE_SCAN,
            "calibration_module": CALIBRATION_MODULE,
        },
        errors,
    )
    return checkpoint


def validate_amendment_receipt(errors: list[str]) -> None:
    receipt = read_json(AMENDMENT_RECEIPT, errors)
    if receipt.get("status") != "CALIBRATION_PROVISIONING_AMENDMENT_VERIFIED":
        errors.append("calibration amendment receipt has unexpected status")
    if receipt.get("corpus_vector") != EXPECTED_SUMMARY or receipt.get("next_source_id") != EXPECTED_NEXT:
        errors.append("calibration amendment receipt corpus/order state drifted")
    if receipt.get("historical_predecessor_index_sha256") != sha256_file(PREDECESSOR_INDEX):
        errors.append("calibration amendment receipt predecessor binding drifted")
    validate_bindings(
        receipt,
        "artifacts",
        {
            "agents_override": AGENTS_OVERRIDE,
            "active_control_index": ACTIVE_INDEX,
            "gate_2_source_disposition": GATE_2,
            "source_state_matrix": MATRIX,
            "document_processing_tracker": TRACKER,
            "source_processing_order": ORDER,
            "calibration_protocol": PROTOCOL,
            "current_state_checkpoint": CHECKPOINT,
            "checkpoint_report": CHECKPOINT_REPORT,
            "new_task_bootstrap": BOOTSTRAP,
            "amendment_report": AMENDMENT_REPORT,
            "categorical_oversight_audit": OVERSIGHT_AUDIT,
            "external_archive_recovery_scan": ARCHIVE_SCAN,
            "calibration_module": CALIBRATION_MODULE,
            "active_guard": Path(__file__),
        },
        errors,
    )
    verification = receipt.get("verification", {})
    engine_files, engine_digest = PRIOR.PRIOR.PRIOR.engine_snapshot()
    if verification.get("engine_files") != engine_files or verification.get("engine_digest") != engine_digest:
        errors.append("calibration amendment receipt engine snapshot mismatch")
    if verification.get("regression_cases") != EXPECTED_REGRESSION_CASES:
        errors.append("calibration amendment receipt regression count drifted")
    if verification.get("offline_tests") != EXPECTED_OFFLINE_TESTS:
        errors.append("calibration amendment receipt test count drifted")
    if receipt.get("provider_calls") != 0 or receipt.get("google_sheets_interactions") != 0:
        errors.append("calibration amendment crossed a paused external boundary")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--work-order", type=Path)
    parser.add_argument("--with-tests", action="store_true")
    args = parser.parse_args()
    errors: list[str] = []
    historical = validate_historical_foundation(errors, args.work_order)
    validate_processing_order(errors)
    validate_active_index(errors)
    validate_checkpoint(errors)
    validate_amendment_receipt(errors)
    engine_files, engine_digest = PRIOR.PRIOR.PRIOR.engine_snapshot()
    if args.with_tests and PRIOR.PRIOR.PRIOR.run_tests():
        errors.append("Gate 5 offline regression suite failed")
    if errors:
        print("M050 GATE 5 CALIBRATION-PROVISIONING GUARD: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1
    print("M050 GATE 5 CALIBRATION-PROVISIONING GUARD: PASS")
    print("- corpus vector: 24 registered / 22 compile / 4 atomized / 18 outstanding = 14 + 4")
    print("- next source: Authorial Grammar (identity card only after author transfer)")
    print("- source order: 24/24 bound to tracker and Gate 2")
    print("- pilot acceptance: does not release full source")
    print("- execution cadence: sequential one-call/review; defects revoke release")
    print(f"- engine files: {engine_files}")
    print(f"- engine digest: {engine_digest}")
    print(f"- preserved legacy candidates: {historical[7]}/913")
    print("- semantic review/mapping/reconciliation/compiled prose: prohibited")
    print("- provider calls: prohibited")
    print("- Google Sheets: paused")
    if args.with_tests:
        print("- offline regression suite: pass")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
