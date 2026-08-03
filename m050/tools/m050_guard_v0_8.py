#!/usr/bin/env python3
"""Verify the clean-contract, post-R6 extraction-machine checkpoint."""

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


PRIOR_PATH = REPO_ROOT / "m050/tools/m050_guard_v0_7.py"
AGENTS = REPO_ROOT / "AGENTS.md"
AGENTS_OVERRIDE = REPO_ROOT / "AGENTS.override.md"
ACTIVE_INDEX = REPO_ROOT / "m050/extraction/control/M050_Active_Control_Index_v0_13_MEDIANv0_5_0.json"
PREDECESSOR_INDEX = REPO_ROOT / "m050/extraction/control/M050_Active_Control_Index_v0_12_MEDIANv0_5_0.json"
CHECKPOINT = REPO_ROOT / "m050/extraction/control/M050_Current_State_Checkpoint_v0_4_MEDIANv0_5_0.json"
PREDECESSOR_CHECKPOINT = REPO_ROOT / "m050/extraction/control/M050_Current_State_Checkpoint_v0_3_MEDIANv0_5_0.json"
CHECKPOINT_REPORT = REPO_ROOT / "m050/extraction/control/M050_Current_State_Checkpoint_v0_4_MEDIANv0_5_0.md"
BOOTSTRAP = REPO_ROOT / "m050/extraction/control/M050_New_Task_Bootstrap_v0_3_MEDIANv0_5_0.md"
STANDARD = REPO_ROOT / "m050/extraction/control/M050_Compile_Execution_Standard_v0_1_MEDIANv0_5_0.md"
CONFIG = REPO_ROOT / "m050/extraction/control/M050_Authorial_Grammar_Extraction_Machine_Config_v0_1_MEDIANv0_5_0.json"
CONTROLLER = REPO_ROOT / "m050/tools/m050_extraction_machine_v0_1.py"
ENGINE_MODULE = REPO_ROOT / "m050/extraction/engine/src/median_gate5/extraction_machine.py"
ENGINE_TEST = REPO_ROOT / "m050/extraction/engine/tests/test_extraction_machine.py"
COMPATIBILITY = REPO_ROOT / "m050/extraction/audit/M050_Authorial_Grammar_R6_Extraction_Machine_Compatibility_Receipt_v0_1_MEDIANv0_5_0.json"

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
HISTORICAL_ROOT_CONTRACT_DRIFT = "artifacts hash binding mismatch: agents_contract"


def _load_prior():
    spec = importlib.util.spec_from_file_location("m050_guard_v0_7", PRIOR_PATH)
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
    historical_errors: list[str] = []
    historical = PRIOR.validate_historical(historical_errors, work_order)
    # v0.5 bound the then-current root AGENTS.md by path. That historical hash
    # remains in its immutable checkpoint and receipt, but the active root path
    # is intentionally superseded by this consolidation.
    errors.extend(
        error
        for error in historical_errors
        if error != HISTORICAL_ROOT_CONTRACT_DRIFT
    )
    return historical


def validate_root_contract(errors: list[str]) -> None:
    if not AGENTS.is_file():
        errors.append("sole root AGENTS.md contract is missing")
        return
    if AGENTS_OVERRIDE.exists() or AGENTS_OVERRIDE.is_symlink():
        errors.append("AGENTS.override.md recreates an ambiguous root contract")
    text = AGENTS.read_text(encoding="utf-8")
    required = (
        "M050_Active_Control_Index_v0_13_MEDIANv0_5_0.json",
        "M050_Current_State_Checkpoint_v0_4_MEDIANv0_5_0.md",
        "M050_New_Task_Bootstrap_v0_3_MEDIANv0_5_0.md",
        "m050_guard_v0_8.py",
        "24 / 22 / 4 / 18 = 14 + 4",
        "cumulative spend envelope",
        "zero-call `scaffold`",
    )
    for phrase in required:
        if phrase not in text:
            errors.append(f"root AGENTS.md omits: {phrase}")


def validate_active_index(errors: list[str]) -> dict:
    index = read_json(ACTIVE_INDEX, errors)
    if index.get("schema_version") != "M050-ACTIVE-CONTROL-INDEX-0.13":
        errors.append("active control index version drifted")
    predecessor = index.get("supersedes", {})
    if (
        predecessor.get("path") != PREDECESSOR_INDEX.relative_to(REPO_ROOT).as_posix()
        or not PREDECESSOR_INDEX.is_file()
        or predecessor.get("sha256") != sha256_file(PREDECESSOR_INDEX)
    ):
        errors.append("active control index predecessor binding drifted")
    if index.get("execution_state") != "AUTHORIAL_GRAMMAR_PILOT_R6_ACCEPTED_EXTRACTION_MACHINE_OFFLINE_READY":
        errors.append("active control index execution state drifted")
    if index.get("corpus_state") != {**EXPECTED_SUMMARY, "whole_corpus_atomization_complete": False}:
        errors.append("active control index corpus vector drifted")
    calibration = index.get("calibration_state", {})
    if (
        calibration.get("currently_selected_source") != EXPECTED_NEXT
        or calibration.get("current_state") != "pilot_accepted_waiting_full_source_release"
        or calibration.get("pilot_acceptance_releases_full_source") is not False
    ):
        errors.append("active control index accepted-pilot boundary drifted")
    machine = index.get("execution_machine", {})
    required_machine = {
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
    if any(machine.get(key) != value for key, value in required_machine.items()):
        errors.append("active control index extraction-machine policy drifted")
    root = index.get("root_contract", {})
    if root != {
        "path": "AGENTS.md",
        "sole_active_root_contract": True,
        "override_must_be_absent": True,
        "successor_begins_read_only": True,
    }:
        errors.append("active control index root-contract boundary drifted")
    boundary = index.get("transition_boundary", {})
    if not boundary or any(value is not False for value in boundary.values()):
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
    for path in (STANDARD, CONTROLLER, ENGINE_MODULE, ENGINE_TEST, COMPATIBILITY):
        if not path.is_file():
            errors.append(f"missing extraction-machine control: {path.relative_to(REPO_ROOT)}")
    PRIOR.validate_pilot_boundary(errors)


def validate_bootstrap(errors: list[str]) -> None:
    text = BOOTSTRAP.read_text(encoding="utf-8") if BOOTSTRAP.is_file() else ""
    required = (
        "AGENTS.override.md` is absent",
        "Remain read-only",
        "Local `HEAD`, `origin/main`",
        "Exact corpus vector",
        "Pilot 001-R6",
        "source-run lifecycle receipt and cumulative spend envelope",
        "Every condition that halts execution",
        "Complete guard result and test count",
    )
    for phrase in required:
        if phrase not in text:
            errors.append(f"successor-thread bootstrap omits: {phrase}")


def validate_checkpoint(errors: list[str]) -> None:
    checkpoint = read_json(CHECKPOINT, errors)
    if checkpoint.get("status") != "POST_R6_EXTRACTION_MACHINE_CLEAN_CONTRACT_READY":
        errors.append("clean-contract checkpoint status drifted")
    predecessor = checkpoint.get("supersedes", {})
    if (
        predecessor.get("path") != PREDECESSOR_CHECKPOINT.relative_to(REPO_ROOT).as_posix()
        or not PREDECESSOR_CHECKPOINT.is_file()
        or predecessor.get("sha256") != sha256_file(PREDECESSOR_CHECKPOINT)
    ):
        errors.append("clean-contract checkpoint predecessor binding drifted")
    if checkpoint.get("corpus_vector") != EXPECTED_SUMMARY:
        errors.append("clean-contract checkpoint corpus vector drifted")
    if checkpoint.get("next_source_id") != EXPECTED_NEXT:
        errors.append("clean-contract checkpoint source drifted")
    authority = checkpoint.get("authority_boundary", {})
    if not authority or any(value is not False for value in authority.values()):
        errors.append("clean-contract checkpoint crosses an authority boundary")
    for name, binding in checkpoint.get("artifacts", {}).items():
        relative = binding.get("path")
        target = REPO_ROOT / relative if isinstance(relative, str) else Path("/__missing__")
        if not target.is_file() or binding.get("sha256") != sha256_file(target):
            errors.append(f"clean-contract checkpoint artifact drifted: {name}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--work-order", type=Path)
    parser.add_argument("--with-tests", action="store_true")
    args = parser.parse_args()
    errors: list[str] = []
    historical = validate_historical(errors, args.work_order)
    validate_root_contract(errors)
    validate_active_index(errors)
    validate_machine(errors)
    validate_bootstrap(errors)
    validate_checkpoint(errors)
    engine_files, engine_digest = PRIOR.PRIOR.PRIOR.PRIOR.PRIOR.engine_snapshot()
    if args.with_tests and PRIOR.PRIOR.PRIOR.PRIOR.PRIOR.run_tests():
        errors.append("Gate 5 offline regression suite failed")
    if errors:
        print("M050 GATE 5 CLEAN-CONTRACT EXTRACTION-MACHINE GUARD: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1
    print("M050 GATE 5 CLEAN-CONTRACT EXTRACTION-MACHINE GUARD: PASS")
    print("- root contract: AGENTS.md only; no override")
    print("- corpus vector: 24 registered / 22 compile / 4 atomized / 18 outstanding = 14 + 4")
    print("- next source: Authorial Grammar; Pilot 001-R6 accepted")
    print("- full-source, spend envelope, provider calls, and repository writes: not authorized")
    print("- machine: one declarative controller; zero-call scaffold; sequential call/review")
    print("- artifacts: packet + raw response + outcome; one chained run ledger")
    print("- Claude cache: explicit one-hour stable prefix; telemetry required")
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
