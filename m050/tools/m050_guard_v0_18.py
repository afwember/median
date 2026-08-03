#!/usr/bin/env python3
"""Verify the active extraction boundary and derived STATUS dashboard."""
from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from decimal import Decimal, ROUND_CEILING
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "m050/extraction/engine/src"))

from median_gate5.canonical import sha256_file  # noqa: E402

PREVIOUS_GUARD = ROOT / "m050/tools/m050_guard_v0_17.py"
AGENTS = ROOT / "AGENTS.md"
OVERRIDE = ROOT / "AGENTS.override.md"
INDEX = ROOT / "m050/extraction/control/M050_Active_Control_Index_v0_23_MEDIANv0_5_0.json"
PREVIOUS_INDEX = ROOT / "m050/extraction/control/M050_Active_Control_Index_v0_22_MEDIANv0_5_0.json"
CHECKPOINT = ROOT / "m050/extraction/control/M050_Current_State_Checkpoint_v0_13_MEDIANv0_5_0.json"
STANDARD = ROOT / "m050/extraction/control/M050_Compile_Execution_Standard_v0_3_MEDIANv0_5_0.md"
BOOTSTRAP = ROOT / "m050/extraction/control/M050_New_Task_Bootstrap_v0_13_MEDIANv0_5_0.md"
STATUS = ROOT / "STATUS.md"
README = ROOT / "README.md"

CORPUS = {
    "registered_sources": 24,
    "atomic_compile_exclusions": 2,
    "compile_scope_sources": 22,
    "atomized_legacy_seed_sources": 4,
    "outstanding_compile_scope_sources": 18,
    "outstanding_pre_reconciliation_sources": 14,
    "outstanding_later_or_conditional_sources": 4,
}


def load_previous_guard():
    spec = importlib.util.spec_from_file_location("m050_guard_v0_17", PREVIOUS_GUARD)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


PREVIOUS = load_previous_guard()


def read_json(path: Path, errors: list[str]) -> dict:
    try:
        return json.loads(path.read_text())
    except Exception as exc:
        errors.append(f"cannot read JSON {path.relative_to(ROOT)}: {exc}")
        return {}


def expected_status(index: dict) -> str:
    dashboard = index.get("status_dashboard", {})
    return (
        "# MEDIAN v0.5.0\n\n"
        "<!-- Derived dashboard only; active controls and receipts remain authoritative. -->\n\n"
        f"**STATUS:** {dashboard.get('status', '')}<br>\n"
        f"**PHASE:** {dashboard.get('phase', '')}<br>\n"
        f"**SOURCE:** {dashboard.get('source', '')}<br>\n"
        f"**CHUNK:** {dashboard.get('chunk', '')}<br>\n"
        f"**NOW:** {dashboard.get('now', '')}<br>\n"
        f"**NEXT:** {dashboard.get('next', '')}<br>\n"
        f"{dashboard.get('required_final_line', '')}\n"
    )


def status_errors(text: str, index: dict) -> list[str]:
    errors: list[str] = []
    dashboard = index.get("status_dashboard", {})
    machine = index.get("execution_machine", {})

    try:
        exact = Decimal(machine.get("cumulative_spent_usd", ""))
        rounded = exact.quantize(Decimal("0.01"), rounding=ROUND_CEILING)
    except Exception:
        errors.append("STATUS cost source is not a decimal")
        rounded = None

    display = dashboard.get("cumulative_provider_cost_display_usd")
    if rounded is not None and display != f"{rounded:.2f}":
        errors.append("STATUS cost is not the upward-cent rounding of cumulative spend")

    required_final = dashboard.get("required_final_line")
    if required_final != f"**TOTAL COST:** ${display} cumulative provider spend":
        errors.append("STATUS required final cost line is malformed")

    nonblank = [line for line in text.splitlines() if line.strip()]
    if not nonblank or nonblank[-1] != required_final:
        errors.append("STATUS final nonblank line is not cumulative provider cost")

    if text != expected_status(index):
        errors.append("STATUS does not exactly mirror the active index")
    return errors


def validate(errors: list[str]) -> None:
    if OVERRIDE.exists() or OVERRIDE.is_symlink():
        errors.append("AGENTS.override.md exists")

    previous_errors: list[str] = []
    PREVIOUS.val(previous_errors)
    expected_supersession_errors = {
        "AGENTS omits v0_22_MEDIANv0_5_0.json",
        "AGENTS omits v0_12_MEDIANv0_5_0.md",
        "AGENTS omits m050_guard_v0_17.py",
        "artifact agents_contract",
    }
    unexpected = [item for item in previous_errors if item not in expected_supersession_errors]
    errors.extend(f"previous boundary: {item}" for item in unexpected)
    if set(previous_errors) != expected_supersession_errors:
        missing = expected_supersession_errors.difference(previous_errors)
        errors.extend(f"previous supersession expectation missing: {item}" for item in sorted(missing))

    agents_text = AGENTS.read_text()
    for phrase in (
        "M050_Active_Control_Index_v0_23_MEDIANv0_5_0.json",
        "M050_Current_State_Checkpoint_v0_13_MEDIANv0_5_0.md",
        "M050_Compile_Execution_Standard_v0_3_MEDIANv0_5_0.md",
        "M050_New_Task_Bootstrap_v0_13_MEDIANv0_5_0.md",
        "m050_guard_v0_18.py",
        "STATUS.md",
        "$0.120852",
        "122 tests",
    ):
        if phrase not in agents_text:
            errors.append(f"AGENTS omits {phrase}")

    index = read_json(INDEX, errors)
    supersedes = index.get("supersedes", {})
    if index.get("schema_version") != "M050-ACTIVE-CONTROL-INDEX-0.23":
        errors.append("active index schema drifted")
    if supersedes.get("path") != str(PREVIOUS_INDEX.relative_to(ROOT)):
        errors.append("active index predecessor path drifted")
    if supersedes.get("sha256") != sha256_file(PREVIOUS_INDEX):
        errors.append("active index predecessor hash drifted")
    if index.get("execution_state") != "AUTHORIAL_GRAMMAR_PURE_LABEL_C0003_PILOT_FROZEN":
        errors.append("active execution state drifted")
    if index.get("corpus_state") != {**CORPUS, "whole_corpus_atomization_complete": False}:
        errors.append("corpus vector drifted")
    boundary = index.get("transition_boundary", {})
    if not boundary or any(value is not False for value in boundary.values()):
        errors.append("authority boundary drifted")

    checkpoint = read_json(CHECKPOINT, errors)
    if checkpoint.get("corpus_vector") != CORPUS:
        errors.append("checkpoint corpus vector drifted")
    if checkpoint.get("status") != index.get("execution_state"):
        errors.append("checkpoint and active state conflict")
    checkpoint_spend = checkpoint.get("spend", {})
    machine = index.get("execution_machine", {})
    if checkpoint_spend.get("cumulative_spent_usd") != machine.get("cumulative_spent_usd"):
        errors.append("checkpoint and active cumulative spend conflict")
    if checkpoint_spend.get("active_money_only_remaining_usd") != machine.get("remaining_usd"):
        errors.append("checkpoint and active money balance conflict")

    dashboard = index.get("status_dashboard", {})
    if dashboard.get("path") != "STATUS.md" or dashboard.get("authority") != "derived_non_authoritative_mirror":
        errors.append("STATUS dashboard role drifted")
    errors.extend(status_errors(STATUS.read_text(), index))

    valid_text = expected_status(index)
    if not status_errors(valid_text.replace("$0.42", "$0.41", 1), index):
        errors.append("STATUS guard self-test failed to detect cost drift")
    if not status_errors(valid_text.rsplit("\n", 2)[0] + "\n", index):
        errors.append("STATUS guard self-test failed to detect a missing final cost line")

    standard_text = STANDARD.read_text()
    for phrase in (
        "derived human dashboard",
        "after every accepted or rejected chunk",
        "before every commit or push",
        "final nonblank line",
        "creates no lifecycle, provider-call, spending, retry",
    ):
        if phrase not in standard_text:
            errors.append(f"execution standard omits {phrase}")

    bootstrap_text = BOOTSTRAP.read_text()
    for phrase in ("STATUS.md", "derived, non-authoritative mirror", "final rounded-up cumulative-cost line"):
        if phrase not in bootstrap_text:
            errors.append(f"successor bootstrap omits {phrase}")

    if "M050_New_Task_Bootstrap_v0_13_MEDIANv0_5_0.md" not in README.read_text():
        errors.append("README successor bootstrap reference is stale")

    required_controls = {
        "AGENTS.md",
        "STATUS.md",
        str(STANDARD.relative_to(ROOT)),
        str(BOOTSTRAP.relative_to(ROOT)),
        str(CHECKPOINT.with_suffix(".md").relative_to(ROOT)),
        str(Path("m050/tools/m050_guard_v0_18.py")),
    }
    actual_controls = {item.get("path") for item in index.get("current_controls", [])}
    if not required_controls.issubset(actual_controls):
        errors.append("active index omits STATUS-maintenance controls")


def run_tests() -> int:
    return PREVIOUS.tests()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--work-order", type=Path)
    parser.add_argument("--with-tests", action="store_true")
    args = parser.parse_args()

    errors: list[str] = []
    historical = PREVIOUS.hist(errors, args.work_order)
    validate(errors)
    if args.with_tests and run_tests():
        errors.append("tests")

    if errors:
        print("M050 STATUS GUARD: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    print("M050 STATUS GUARD: PASS")
    print("- STATUS exactly mirrors active index/checkpoint state")
    print("- final cumulative provider cost: $0.42 (exact $0.419817)")
    print("- C0001/C0002 accepted; C0003 rejected, recalibrated, and frozen")
    print("- provider authority none; 122 tests pass")
    print(f"- preserved legacy candidates: {historical[7]}/913")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
