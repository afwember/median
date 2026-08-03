#!/usr/bin/env python3
"""Verify the complete-corpus MEDIAN Gate 5 corrective checkpoint."""

from __future__ import annotations

import argparse
import importlib.util
import json
from pathlib import Path
import sys

import yaml


REPO_ROOT = Path(__file__).resolve().parents[2]
ENGINE_SRC = REPO_ROOT / "m050/extraction/engine/src"
sys.path.insert(0, str(ENGINE_SRC))

from median_gate5.canonical import sha256_file  # noqa: E402
from median_gate5.corpus import derive_compile_source_state  # noqa: E402


PRIOR_GUARD_PATH = REPO_ROOT / "m050/tools/m050_guard_v0_4.py"
GATE_2 = REPO_ROOT / "m050/extraction/audit/M050_Extraction_Gate_2_Source_Disposition_v0_1_MEDIANv0_5_0.yaml"
ACTIVE_INDEX = REPO_ROOT / "m050/extraction/control/M050_Active_Control_Index_v0_10_MEDIANv0_5_0.json"
MATRIX = REPO_ROOT / "m050/extraction/control/M050_Compile_Source_State_Matrix_v0_1_MEDIANv0_5_0.json"
MATRIX_REPORT = REPO_ROOT / "m050/extraction/control/M050_Compile_Source_State_Matrix_v0_1_MEDIANv0_5_0.md"
CHECKPOINT = REPO_ROOT / "m050/extraction/control/M050_Current_State_Checkpoint_v0_1_MEDIANv0_5_0.json"
CHECKPOINT_REPORT = REPO_ROOT / "m050/extraction/control/M050_Current_State_Checkpoint_v0_1_MEDIANv0_5_0.md"
BOOTSTRAP = REPO_ROOT / "m050/extraction/control/M050_New_Task_Bootstrap_v0_1_MEDIANv0_5_0.md"
CORRECTION_REPORT = REPO_ROOT / "m050/extraction/audit/M050_Extraction_Gate_5_Corpus_Scope_Correction_Report_v0_1_MEDIANv0_5_0.md"
CORRECTION_RECEIPT = REPO_ROOT / "m050/extraction/audit/M050_Extraction_Gate_5_Corpus_Scope_Correction_Receipt_v0_1_MEDIANv0_5_0.json"
AGENTS = REPO_ROOT / "AGENTS.md"
MATRIX_GENERATOR = REPO_ROOT / "m050/tools/m050_build_compile_source_state.py"
EXPECTED_SUMMARY = {
    "registered_sources": 24,
    "atomic_compile_exclusions": 2,
    "compile_scope_sources": 22,
    "atomized_legacy_seed_sources": 4,
    "outstanding_compile_scope_sources": 18,
    "outstanding_pre_reconciliation_sources": 14,
    "outstanding_later_or_conditional_sources": 4,
}


def _load_prior_guard():
    spec = importlib.util.spec_from_file_location("m050_guard_v0_4", PRIOR_GUARD_PATH)
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


def validate_historical_foundation(errors: list[str], work_order: Path | None) -> tuple:
    if PRIOR.PRIOR.run_legacy_guard(True, work_order):
        errors.append("Gate 4 guard failed")
        return (0,) * 15
    PRIOR.PRIOR.validate_active_index(errors)
    approved_identity_cards = PRIOR.PRIOR.validate_identity_approval(errors)
    replay_records, replay_queue = PRIOR.PRIOR.validate_legacy_replay(errors)
    ruling_sections, ruling_fields, ruling_coordinates = PRIOR.PRIOR.validate_human_rulings_reconstruction(errors)
    mechanically_dispositioned = PRIOR.PRIOR.validate_repair_closure(errors)
    migration_errors: list[str] = []
    migration_candidates, compound_review_records, retrospective_blocks = PRIOR.PRIOR.validate_layer_e_migration(migration_errors)
    errors.extend(
        error
        for error in migration_errors
        if error != "historical Layer E migration verification snapshot mismatch"
    )
    relocated_evidence = PRIOR.validate_retired_archive(errors)
    PRIOR.validate_active_index(errors)
    review_errors: list[str] = []
    review_bundles, uncovered_blocks, transitions, preserved_compounds = PRIOR.validate_review_plan(review_errors)
    errors.extend(
        error
        for error in review_errors
        if error != "semantic review planning receipt engine snapshot mismatch"
    )
    PRIOR.PRIOR.validate_lock(errors)
    PRIOR.PRIOR.validate_json_controls(errors)
    PRIOR.PRIOR.validate_offline_imports(errors)
    return (
        approved_identity_cards,
        replay_records,
        replay_queue,
        ruling_sections,
        ruling_fields,
        ruling_coordinates,
        mechanically_dispositioned,
        migration_candidates,
        compound_review_records,
        retrospective_blocks,
        relocated_evidence,
        review_bundles,
        uncovered_blocks,
        transitions,
        preserved_compounds,
    )


def validate_matrix(errors: list[str]) -> dict:
    matrix = read_json(MATRIX, errors)
    try:
        gate_2 = yaml.safe_load(GATE_2.read_text(encoding="utf-8"))
        expected = derive_compile_source_state(
            gate_2,
            manifest_path=GATE_2.relative_to(REPO_ROOT).as_posix(),
            manifest_sha256=sha256_file(GATE_2),
        )
    except Exception as exc:
        errors.append(f"cannot derive complete corpus state: {exc}")
        return matrix
    if matrix != expected:
        errors.append("committed compile source matrix differs from authoritative Gate 2 derivation")
    if matrix.get("summary") != EXPECTED_SUMMARY:
        errors.append("complete corpus vector is not 24 / 22 / 4 / 18 = 14 + 4")
    if len(matrix.get("sources", [])) != 24:
        errors.append("compile source matrix does not contain all 24 source rows")
    constraints = matrix.get("transition_constraints", {})
    if not constraints or any(value is not False for value in constraints.values()):
        errors.append("compile source matrix authorizes a prohibited incomplete-corpus transition")
    return matrix


def validate_active_index(errors: list[str]) -> dict:
    index = read_json(ACTIVE_INDEX, errors)
    if index.get("execution_state") != "GATE_5_LEGACY_SEED_4_OF_22_PRESERVED_CORPUS_ATOMIZATION_INCOMPLETE":
        errors.append("active control index has unexpected whole-corpus execution state")
    if index.get("corpus_state") != {**EXPECTED_SUMMARY, "whole_corpus_atomization_complete": False}:
        errors.append("active control index corpus vector drifted")
    legacy = index.get("legacy_seed_state", {})
    if (
        legacy.get("source_count") != 4
        or legacy.get("mechanically_valid_candidates") != 913
        or legacy.get("candidate_review_bundles") != 181
        or legacy.get("execution_authorized") is not False
        or legacy.get("classification") != "PRESERVED_DORMANT_PARTIAL_LEGACY_REVIEW_PLANNING"
    ):
        errors.append("legacy subset is not preserved as dormant partial planning")
    boundary = index.get("transition_boundary", {})
    if not boundary or any(value is not False for value in boundary.values()):
        errors.append("active control index authorizes a prohibited incomplete-corpus transition")
    if index.get("provider_call_authorized") is not False:
        errors.append("active control index does not prohibit provider calls")
    if index.get("google_sheets_interaction_authorized") is not False:
        errors.append("active control index does not preserve the Google Sheets pause")
    for control in index.get("current_controls", []):
        relative = control.get("path")
        if not isinstance(relative, str) or not relative:
            errors.append("active control entry lacks a path")
            continue
        target = REPO_ROOT / relative
        if relative.endswith("/"):
            exists = target.is_dir()
        else:
            exists = target.is_file()
        if not exists:
            errors.append(f"missing v0.10 active control: {relative}")
    return index


def validate_bindings(container: dict, key: str, artifacts: dict[str, Path], errors: list[str]) -> None:
    bindings = container.get(key, {})
    for name, path in artifacts.items():
        binding = bindings.get(name, {})
        relative = path.relative_to(REPO_ROOT).as_posix()
        if binding.get("path") != relative:
            errors.append(f"{key} path binding mismatch: {name}")
        elif not path.is_file() or binding.get("sha256") != sha256_file(path):
            errors.append(f"{key} hash binding mismatch: {name}")


def validate_checkpoint(errors: list[str]) -> dict:
    checkpoint = read_json(CHECKPOINT, errors)
    if checkpoint.get("status") != "CORPUS_ATOMIZATION_INCOMPLETE_HANDOFF_READY":
        errors.append("current-state checkpoint has unexpected status")
    if checkpoint.get("predecessor_commit") != "41d529982f00b2a239628ccf1ee108081776b7dd":
        errors.append("current-state checkpoint predecessor commit drifted")
    if checkpoint.get("corpus_vector") != EXPECTED_SUMMARY:
        errors.append("current-state checkpoint corpus vector drifted")
    if checkpoint.get("successor_authority") != "READ_ONLY_UNTIL_EXPLICIT_AUTHOR_TRANSFER":
        errors.append("current-state checkpoint grants successor write authority")
    validate_bindings(
        checkpoint,
        "artifacts",
        {
            "agents_contract": AGENTS,
            "active_control_index": ACTIVE_INDEX,
            "gate_2_source_disposition": GATE_2,
            "source_state_matrix": MATRIX,
            "source_state_report": MATRIX_REPORT,
            "source_state_generator": MATRIX_GENERATOR,
            "checkpoint_report": CHECKPOINT_REPORT,
            "new_task_bootstrap": BOOTSTRAP,
            "correction_report": CORRECTION_REPORT,
        },
        errors,
    )
    return checkpoint


def validate_correction_receipt(errors: list[str]) -> None:
    receipt = read_json(CORRECTION_RECEIPT, errors)
    if receipt.get("status") != "CORPUS_SCOPE_CORRECTED_HANDOFF_PACKAGE_VERIFIED":
        errors.append("corpus-scope correction receipt has unexpected status")
    if receipt.get("corpus_vector") != EXPECTED_SUMMARY:
        errors.append("corpus-scope correction receipt vector drifted")
    validate_bindings(
        receipt,
        "artifacts",
        {
            "agents_contract": AGENTS,
            "active_control_index": ACTIVE_INDEX,
            "gate_2_source_disposition": GATE_2,
            "source_state_matrix": MATRIX,
            "source_state_report": MATRIX_REPORT,
            "source_state_generator": MATRIX_GENERATOR,
            "current_state_checkpoint": CHECKPOINT,
            "checkpoint_report": CHECKPOINT_REPORT,
            "new_task_bootstrap": BOOTSTRAP,
            "correction_report": CORRECTION_REPORT,
        },
        errors,
    )
    verification = receipt.get("verification", {})
    engine_files, engine_digest = PRIOR.PRIOR.engine_snapshot()
    if verification.get("engine_files") != engine_files or verification.get("engine_digest") != engine_digest:
        errors.append("corpus-scope correction receipt engine snapshot mismatch")
    if verification.get("gate_5_guard_sha256") != sha256_file(Path(__file__)):
        errors.append("corpus-scope correction receipt guard hash mismatch")
    if verification.get("regression_cases") != 53:
        errors.append("corpus-scope correction receipt regression count drifted")
    if verification.get("offline_tests") != 87:
        errors.append("corpus-scope correction receipt test count drifted")
    if receipt.get("provider_calls") != 0 or receipt.get("google_sheets_interactions") != 0:
        errors.append("corrective operation crossed a paused external boundary")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--work-order", type=Path)
    parser.add_argument("--with-tests", action="store_true")
    args = parser.parse_args()
    errors: list[str] = []
    historical = validate_historical_foundation(errors, args.work_order)
    validate_matrix(errors)
    validate_active_index(errors)
    validate_checkpoint(errors)
    validate_correction_receipt(errors)
    engine_files, engine_digest = PRIOR.PRIOR.engine_snapshot()
    if args.with_tests and PRIOR.PRIOR.run_tests():
        errors.append("Gate 5 offline regression suite failed")
    if errors:
        print("M050 GATE 5 COMPLETE-CORPUS GUARD: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1
    print("M050 GATE 5 COMPLETE-CORPUS GUARD: PASS")
    print(f"- corpus vector: 24 registered / 22 compile / 4 atomized / 18 outstanding = 14 + 4")
    print(f"- engine files: {engine_files}")
    print(f"- engine digest: {engine_digest}")
    print(f"- approved legacy identity cards: {historical[0]}")
    print(f"- preserved legacy candidates: {historical[7]}/913")
    print(f"- preserved legacy review bundles: {historical[11]}/181")
    print(f"- preserved legacy review transitions: {historical[13]}/913")
    print("- legacy review queues: dormant")
    print("- semantic reviews: 0")
    print("- accepted evidence: 0")
    print("- mapping/reconciliation/compiled prose: prohibited")
    print("- provider calls: prohibited")
    print("- Google Sheets: paused")
    if args.with_tests:
        print("- offline regression suite: pass")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
