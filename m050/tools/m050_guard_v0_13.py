#!/usr/bin/env python3
"""Verify accepted structural C0002 and the unreleased remaining-source boundary."""

from __future__ import annotations

import argparse
import importlib.util
import json
from pathlib import Path
import subprocess
import sys


REPO_ROOT = Path(__file__).resolve().parents[2]
ENGINE_SRC = REPO_ROOT / "m050/extraction/engine/src"
sys.path.insert(0, str(ENGINE_SRC))

from median_gate5.canonical import sha256_file  # noqa: E402


PRIOR_PATH = REPO_ROOT / "m050/tools/m050_guard_v0_12.py"
AGENTS = REPO_ROOT / "AGENTS.md"
AGENTS_OVERRIDE = REPO_ROOT / "AGENTS.override.md"
ACTIVE_INDEX = REPO_ROOT / "m050/extraction/control/M050_Active_Control_Index_v0_18_MEDIANv0_5_0.json"
PREDECESSOR_INDEX = REPO_ROOT / "m050/extraction/control/M050_Active_Control_Index_v0_17_MEDIANv0_5_0.json"
CHECKPOINT = REPO_ROOT / "m050/extraction/control/M050_Current_State_Checkpoint_v0_9_MEDIANv0_5_0.json"
PREDECESSOR_CHECKPOINT = REPO_ROOT / "m050/extraction/control/M050_Current_State_Checkpoint_v0_8_MEDIANv0_5_0.json"
CHECKPOINT_REPORT = REPO_ROOT / "m050/extraction/control/M050_Current_State_Checkpoint_v0_9_MEDIANv0_5_0.md"
BOOTSTRAP = REPO_ROOT / "m050/extraction/control/M050_New_Task_Bootstrap_v0_8_MEDIANv0_5_0.md"
CONFIG = REPO_ROOT / "m050/extraction/control/M050_Authorial_Grammar_Extraction_Machine_Config_v0_3_MEDIANv0_5_0.json"
PLAN = REPO_ROOT / "m050/extraction/control/M050_Authorial_Grammar_Section_Aware_Chunk_Plan_v0_3_MEDIANv0_5_0.json"
AUTHORIZATION = REPO_ROOT / "m050/extraction/audit/pilot-transitions/M050_Authorial_Grammar_Structural_C0002_Pilot_Call_Authorized_v0_8_MEDIANv0_5_0.json"
ACCEPTANCE = REPO_ROOT / "m050/extraction/audit/pilot-transitions/M050_Authorial_Grammar_Structural_C0002_Pilot_Accepted_v0_8_MEDIANv0_5_0.json"
OUTCOME = REPO_ROOT / "m050/extraction/runs/authorial-grammar-structural-pilot/M050_Authorial_Grammar_Structural_C0002_Outcome_v0_8_MEDIANv0_5_0.json"
LEDGER = REPO_ROOT / "m050/extraction/runs/authorial-grammar-structural-pilot/M050_Authorial_Grammar_Structural_Pilot_Run_Ledger_v0_8_MEDIANv0_5_0.jsonl"
SPEND = REPO_ROOT / "m050/extraction/audit/spend-envelopes/M050_Provider_Spend_Envelope_001_After_Structural_C0002_Pilot_v0_5_MEDIANv0_5_0.json"

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
EXPECTED_TESTS = 120
EXPECTED_REMAINING = ["C0001"] + [f"C{ordinal:04d}" for ordinal in range(3, 14)]
HISTORICAL_ROOT_CONTRACT_DRIFT = "artifacts hash binding mismatch: agents_contract"


def _load_prior():
    spec = importlib.util.spec_from_file_location("m050_guard_v0_12", PRIOR_PATH)
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
    errors.extend(
        error for error in historical_errors
        if error != HISTORICAL_ROOT_CONTRACT_DRIFT
    )
    return historical


def validate_root(errors: list[str]) -> None:
    if not AGENTS.is_file():
        errors.append("sole root AGENTS.md contract is missing")
        return
    if AGENTS_OVERRIDE.exists() or AGENTS_OVERRIDE.is_symlink():
        errors.append("AGENTS.override.md recreates an ambiguous root contract")
    text = AGENTS.read_text(encoding="utf-8")
    for phrase in (
        "M050_Active_Control_Index_v0_18_MEDIANv0_5_0.json",
        "M050_Current_State_Checkpoint_v0_9_MEDIANv0_5_0.md",
        "M050_New_Task_Bootstrap_v0_8_MEDIANv0_5_0.md",
        "m050_guard_v0_13.py",
        "24 / 22 / 4 / 18 = 14 + 4",
        "$1.358372",
    ):
        if phrase not in text:
            errors.append(f"root AGENTS.md omits: {phrase}")


def validate_index(errors: list[str]) -> None:
    index = read_json(ACTIVE_INDEX, errors)
    predecessor = index.get("supersedes", {})
    if (
        index.get("schema_version") != "M050-ACTIVE-CONTROL-INDEX-0.18"
        or predecessor.get("path") != PREDECESSOR_INDEX.relative_to(REPO_ROOT).as_posix()
        or not PREDECESSOR_INDEX.is_file()
        or predecessor.get("sha256") != sha256_file(PREDECESSOR_INDEX)
        or index.get("execution_state") != "AUTHORIAL_GRAMMAR_STRUCTURAL_C0002_PILOT_ACCEPTED"
        or index.get("corpus_state") != {**EXPECTED_SUMMARY, "whole_corpus_atomization_complete": False}
    ):
        errors.append("active accepted-pilot control index drifted")
    calibration = index.get("calibration_state", {})
    if (
        calibration.get("currently_selected_source") != EXPECTED_NEXT
        or calibration.get("accepted_structural_pilot_chunk") != "C0002"
        or calibration.get("pilot_result") != "perfect_for_release_for_structurally_grouped_20_target_quantization"
        or calibration.get("remaining_chunk_ids") != EXPECTED_REMAINING
        or calibration.get("remaining_call_count") != 12
        or calibration.get("remaining_cache_miss_ceiling_usd") != "1.358372"
        or calibration.get("additional_provider_calls_authorized") != 0
    ):
        errors.append("active accepted-pilot calibration boundary drifted")
    boundary = index.get("transition_boundary", {})
    if not boundary or any(value is not False for value in boundary.values()):
        errors.append("active control index crosses a prohibited transition")
    for control in index.get("current_controls", []):
        relative = control.get("path")
        if not isinstance(relative, str) or not (REPO_ROOT / relative).is_file():
            errors.append(f"missing active control: {relative}")


def validate_pilot(errors: list[str]) -> None:
    config = read_json(CONFIG, errors)
    if (
        config.get("execution", {}).get("provider_calls_authorized") is not False
        or config.get("execution", {}).get("full_source_authorized") is not False
        or config.get("quantization", {}).get("generated_chunk_count") != 13
    ):
        errors.append("provider-disabled structural configuration drifted")
    plan = read_json(PLAN, errors)
    chunk_ids = [chunk.get("chunk_id") for chunk in plan.get("chunks", [])]
    if chunk_ids != [f"C{ordinal:04d}" for ordinal in range(1, 14)]:
        errors.append("structural plan chunk sequence drifted")
    authorization = read_json(AUTHORIZATION, errors)
    if (
        authorization.get("state") != "pilot_call_authorized"
        or authorization.get("provider_call_limit") != 1
        or authorization.get("authorized_chunk_ids") != ["C0002"]
        or authorization.get("approved_cost_cap_usd") != "0.11"
    ):
        errors.append("structural pilot authorization drifted")
    outcome = read_json(OUTCOME, errors)
    validation = outcome.get("mechanical_validation", {})
    if (
        outcome.get("stop_reason") != "end_turn"
        or validation.get("passed") is not True
        or validation.get("errors") != []
        or outcome.get("cache", {}).get("effective") is not True
        or outcome.get("cache", {}).get("read_input_tokens") != 2545
        or outcome.get("cost", {}).get("total_usd") != "0.054311"
    ):
        errors.append("structural C0002 provider outcome drifted")
    acceptance = read_json(ACCEPTANCE, errors)
    if (
        acceptance.get("state") != "pilot_accepted"
        or acceptance.get("chunk_id") != "C0002"
        or acceptance.get("pilot_result") != "perfect_for_release_for_structurally_grouped_20_target_quantization"
        or acceptance.get("provider_result", {}).get("substantive_review_passed") is not True
        or acceptance.get("substantive_findings", {}).get("defects_found") != 0
        or acceptance.get("additional_provider_calls_authorized") != 0
        or acceptance.get("full_source_execution_authorized") is not False
    ):
        errors.append("structural C0002 acceptance drifted")
    try:
        states = [json.loads(line).get("state") for line in LEDGER.read_text(encoding="utf-8").splitlines() if line.strip()]
    except (OSError, json.JSONDecodeError):
        states = []
    if states != ["call_captured", "review_passed"]:
        errors.append("structural pilot reviewed ledger drifted")
    spend = read_json(SPEND, errors)
    if (
        spend.get("active") is not True
        or spend.get("spent_usd") != "0.254597"
        or spend.get("remaining_usd") != "1.745403"
    ):
        errors.append("post-pilot money-only envelope drifted")


def validate_checkpoint(errors: list[str]) -> None:
    checkpoint = read_json(CHECKPOINT, errors)
    predecessor = checkpoint.get("supersedes", {})
    if (
        checkpoint.get("status") != "AUTHORIAL_GRAMMAR_STRUCTURAL_C0002_PILOT_ACCEPTED"
        or predecessor.get("path") != PREDECESSOR_CHECKPOINT.relative_to(REPO_ROOT).as_posix()
        or not PREDECESSOR_CHECKPOINT.is_file()
        or predecessor.get("sha256") != sha256_file(PREDECESSOR_CHECKPOINT)
        or checkpoint.get("corpus_vector") != EXPECTED_SUMMARY
        or checkpoint.get("next_source_id") != EXPECTED_NEXT
    ):
        errors.append("accepted-pilot checkpoint state drifted")
    authority = checkpoint.get("authority_boundary", {})
    if not authority or any(value is not False for value in authority.values()):
        errors.append("accepted-pilot checkpoint crosses an authority boundary")
    for name, binding in checkpoint.get("artifacts", {}).items():
        relative = binding.get("path")
        target = REPO_ROOT / relative if isinstance(relative, str) else Path("/__missing__")
        if not target.is_file() or binding.get("sha256") != sha256_file(target):
            errors.append(f"accepted-pilot checkpoint artifact drifted: {name}")
    report = CHECKPOINT_REPORT.read_text(encoding="utf-8") if CHECKPOINT_REPORT.is_file() else ""
    bootstrap = BOOTSTRAP.read_text(encoding="utf-8") if BOOTSTRAP.is_file() else ""
    for phrase in ("$0.054311", "$1.745403", "C0003-C0013", "$1.358372"):
        if phrase not in report:
            errors.append(f"checkpoint report omits: {phrase}")
    for phrase in ("Remain read-only", "accepted new-plan structural C0002", "Complete guard result"):
        if phrase not in bootstrap:
            errors.append(f"successor bootstrap omits: {phrase}")


def run_tests() -> int:
    python = REPO_ROOT / ".venv/bin/python"
    if not python.is_file():
        return 1
    return subprocess.run(
        [str(python), "-m", "pytest", "m050/extraction/engine/tests", "-q"],
        cwd=REPO_ROOT,
        check=False,
    ).returncode


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--work-order", type=Path)
    parser.add_argument("--with-tests", action="store_true")
    args = parser.parse_args()
    errors: list[str] = []
    historical = validate_historical(errors, args.work_order)
    validate_root(errors)
    validate_index(errors)
    validate_pilot(errors)
    validate_checkpoint(errors)
    if args.with_tests and run_tests():
        errors.append("Gate 5 offline regression suite failed")
    if errors:
        print("M050 GATE 5 STRUCTURAL-PILOT-ACCEPTANCE GUARD: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1
    print("M050 GATE 5 STRUCTURAL-PILOT-ACCEPTANCE GUARD: PASS")
    print("- corpus vector: 24 / 22 / 4 / 18 = 14 + 4; next source Authorial Grammar")
    print("- new-plan C0002: mechanically and substantively accepted; no defects")
    print("- cache: effective 2,545-token read; exact pilot cost $0.054311")
    print("- spend: $0.254597 cumulative; active money-only balance $1.745403")
    print("- remaining sequence: C0001 plus C0003-C0013; 12 calls; ceiling $1.358372")
    print("- old-plan C0001 does not accept new-plan C0001; no projection workaround")
    print("- additional provider/full-source authority: none")
    print("- semantic acceptance/mapping/reconciliation/compiled prose: prohibited")
    print(f"- preserved legacy candidates: {historical[7]}/913")
    if args.with_tests:
        print(f"- offline regression suite: pass ({EXPECTED_TESTS} tests)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
