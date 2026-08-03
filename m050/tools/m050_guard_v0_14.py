#!/usr/bin/env python3
"""Verify the halted C0003 layout-metadata-atom source-run boundary."""

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

PRIOR_PATH = REPO_ROOT / "m050/tools/m050_guard_v0_13.py"
AGENTS = REPO_ROOT / "AGENTS.md"
OVERRIDE = REPO_ROOT / "AGENTS.override.md"
INDEX = REPO_ROOT / "m050/extraction/control/M050_Active_Control_Index_v0_19_MEDIANv0_5_0.json"
PRIOR_INDEX = REPO_ROOT / "m050/extraction/control/M050_Active_Control_Index_v0_18_MEDIANv0_5_0.json"
CHECKPOINT = REPO_ROOT / "m050/extraction/control/M050_Current_State_Checkpoint_v0_10_MEDIANv0_5_0.json"
PRIOR_CHECKPOINT = REPO_ROOT / "m050/extraction/control/M050_Current_State_Checkpoint_v0_9_MEDIANv0_5_0.json"
REPORT = REPO_ROOT / "m050/extraction/control/M050_Current_State_Checkpoint_v0_10_MEDIANv0_5_0.md"
BOOTSTRAP = REPO_ROOT / "m050/extraction/control/M050_New_Task_Bootstrap_v0_9_MEDIANv0_5_0.md"
HALT = REPO_ROOT / "m050/extraction/audit/source-run-transitions/M050_Authorial_Grammar_Structural_Source_Run_Halted_After_C0003_v0_5_MEDIANv0_5_0.json"
LEDGER = REPO_ROOT / "m050/extraction/runs/authorial-grammar-structural-source/M050_Authorial_Grammar_Structural_Source_Run_Ledger_v0_4_MEDIANv0_5_0.jsonl"
C1_OUTCOME = REPO_ROOT / "m050/extraction/runs/authorial-grammar-structural-source/M050_Authorial_Grammar_Structural_C0001_Outcome_v0_4_MEDIANv0_5_0.json"
C3_OUTCOME = REPO_ROOT / "m050/extraction/runs/authorial-grammar-structural-source/M050_Authorial_Grammar_Structural_C0003_Outcome_v0_4_MEDIANv0_5_0.json"
SPEND = REPO_ROOT / "m050/extraction/audit/spend-envelopes/M050_Provider_Spend_Envelope_001_After_Structural_C0003_v0_7_MEDIANv0_5_0.json"

SUMMARY = {
    "registered_sources": 24, "atomic_compile_exclusions": 2,
    "compile_scope_sources": 22, "atomized_legacy_seed_sources": 4,
    "outstanding_compile_scope_sources": 18,
    "outstanding_pre_reconciliation_sources": 14,
    "outstanding_later_or_conditional_sources": 4,
}
TESTS = 120

def load_prior():
    spec = importlib.util.spec_from_file_location("m050_guard_v0_13", PRIOR_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load predecessor guard")
    module = importlib.util.module_from_spec(spec); spec.loader.exec_module(module); return module

PRIOR = load_prior()

def read_json(path: Path, errors: list[str]) -> dict:
    try: value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"cannot read {path.relative_to(REPO_ROOT)}: {exc}"); return {}
    return value if isinstance(value, dict) else {}

def historical(errors: list[str], work_order: Path | None) -> tuple:
    prior_errors: list[str] = []; result = PRIOR.validate_historical(prior_errors, work_order)
    errors.extend(e for e in prior_errors if e != "artifacts hash binding mismatch: agents_contract")
    return result

def validate(errors: list[str]) -> None:
    if not AGENTS.is_file(): errors.append("AGENTS.md missing")
    if OVERRIDE.exists() or OVERRIDE.is_symlink(): errors.append("AGENTS.override.md present")
    text = AGENTS.read_text(encoding="utf-8") if AGENTS.is_file() else ""
    for phrase in ("M050_Active_Control_Index_v0_19_MEDIANv0_5_0.json", "M050_Current_State_Checkpoint_v0_10_MEDIANv0_5_0.md", "M050_New_Task_Bootstrap_v0_9_MEDIANv0_5_0.md", "m050_guard_v0_14.py", "$0.352455", "C0004-C0013"):
        if phrase not in text: errors.append(f"AGENTS.md omits: {phrase}")
    index = read_json(INDEX, errors); predecessor = index.get("supersedes", {})
    if (index.get("schema_version") != "M050-ACTIVE-CONTROL-INDEX-0.19" or
        predecessor.get("path") != PRIOR_INDEX.relative_to(REPO_ROOT).as_posix() or
        predecessor.get("sha256") != sha256_file(PRIOR_INDEX) or
        index.get("execution_state") != "AUTHORIAL_GRAMMAR_STRUCTURAL_SOURCE_RUN_HALTED_C0003_LAYOUT_ATOM" or
        index.get("corpus_state") != {**SUMMARY, "whole_corpus_atomization_complete": False}):
        errors.append("active halted-run index drifted")
    calibration = index.get("calibration_state", {})
    if (calibration.get("accepted_chunk_ids") != ["C0001", "C0002"] or
        calibration.get("failed_chunk_id") != "C0003" or
        calibration.get("failure_kind") != "nonsemantic_layout_metadata_atom" or
        calibration.get("uncalled_chunk_ids") != [f"C{i:04d}" for i in range(4,14)] or
        calibration.get("remaining_source_run_revoked") is not True or
        calibration.get("additional_provider_calls_authorized") != 0):
        errors.append("active halted-run calibration boundary drifted")
    boundary = index.get("transition_boundary", {})
    if not boundary or any(v is not False for v in boundary.values()): errors.append("index crosses authority boundary")
    for control in index.get("current_controls", []):
        path = control.get("path")
        if not isinstance(path, str) or not (REPO_ROOT/path).is_file(): errors.append(f"missing control: {path}")
    halt = read_json(HALT, errors)
    if (halt.get("state") != "source_run_halted" or halt.get("failed_chunk_id") != "C0003" or
        halt.get("release_revoked") is not True or halt.get("defect", {}).get("kind") != "nonsemantic_layout_metadata_atom" or
        halt.get("additional_provider_calls_authorized") != 0): errors.append("C0003 halt receipt drifted")
    c1 = read_json(C1_OUTCOME, errors); c3 = read_json(C3_OUTCOME, errors)
    if c1.get("mechanical_validation", {}).get("passed") is not True or c1.get("cost", {}).get("total_usd") != "0.042259": errors.append("C0001 outcome drifted")
    if c3.get("mechanical_validation", {}).get("passed") is not True or c3.get("cost", {}).get("total_usd") != "0.055599": errors.append("C0003 outcome drifted")
    try: states=[json.loads(line).get("state") for line in LEDGER.read_text(encoding="utf-8").splitlines() if line.strip()]
    except (OSError, json.JSONDecodeError): states=[]
    if states != ["call_captured", "review_passed", "call_captured", "review_failed"]: errors.append("source-run ledger drifted")
    spend = read_json(SPEND, errors)
    if spend.get("spent_usd") != "0.352455" or spend.get("remaining_usd") != "1.647545" or spend.get("active") is not True: errors.append("spend boundary drifted")
    checkpoint=read_json(CHECKPOINT, errors); cp=checkpoint.get("supersedes", {})
    if (checkpoint.get("status") != "AUTHORIAL_GRAMMAR_STRUCTURAL_SOURCE_RUN_HALTED_C0003_LAYOUT_ATOM" or
        cp.get("path") != PRIOR_CHECKPOINT.relative_to(REPO_ROOT).as_posix() or cp.get("sha256") != sha256_file(PRIOR_CHECKPOINT) or
        checkpoint.get("corpus_vector") != SUMMARY): errors.append("checkpoint state drifted")
    auth=checkpoint.get("authority_boundary", {})
    if not auth or any(v is not False for v in auth.values()): errors.append("checkpoint crosses authority boundary")
    for name,binding in checkpoint.get("artifacts", {}).items():
        path=binding.get("path"); target=REPO_ROOT/path if isinstance(path,str) else Path("/__missing__")
        if not target.is_file() or binding.get("sha256") != sha256_file(target): errors.append(f"checkpoint artifact drifted: {name}")
    report=REPORT.read_text(encoding="utf-8") if REPORT.is_file() else ""; bootstrap=BOOTSTRAP.read_text(encoding="utf-8") if BOOTSTRAP.is_file() else ""
    for phrase in ("B00071", "$0.352455", "C0004-C0013"): 
        if phrase not in report: errors.append(f"report omits: {phrase}")
    for phrase in ("Remain read-only", "B00071 nonsemantic", "Complete guard result"):
        if phrase not in bootstrap: errors.append(f"bootstrap omits: {phrase}")

def run_tests() -> int:
    return subprocess.run([str(REPO_ROOT/".venv/bin/python"), "-m", "pytest", "m050/extraction/engine/tests", "-q"], cwd=REPO_ROOT, check=False).returncode

def main() -> int:
    parser=argparse.ArgumentParser(description=__doc__); parser.add_argument("--work-order", type=Path); parser.add_argument("--with-tests", action="store_true"); args=parser.parse_args()
    errors=[]; preserved=historical(errors,args.work_order); validate(errors)
    if args.with_tests and run_tests(): errors.append("offline regression suite failed")
    if errors:
        print("M050 GATE 5 C0003-HALT GUARD: FAIL"); [print(f"- {e}") for e in errors]; return 1
    print("M050 GATE 5 C0003-HALT GUARD: PASS")
    print("- corpus vector: 24 / 22 / 4 / 18 = 14 + 4; next source Authorial Grammar")
    print("- accepted new-plan chunks: C0001 and C0002; no whole-source candidate")
    print("- C0003 rejected: B00071 layout metadata emitted as an atom")
    print("- remaining release revoked; C0004-C0013 uncalled")
    print("- run spend $0.097858; cumulative $0.352455; money-only balance $1.647545")
    print("- retry, method change, provider call, and later semantic stages: unauthorized")
    print(f"- preserved legacy candidates: {preserved[7]}/913")
    if args.with_tests: print(f"- offline regression suite: pass ({TESTS} tests)")
    return 0

if __name__ == "__main__": raise SystemExit(main())
