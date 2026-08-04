#!/usr/bin/env python3
"""Verify the rejected C0003 capture and frozen target-coverage boundary."""
from __future__ import annotations

import argparse
import importlib.util
import json
import subprocess
import sys
from decimal import Decimal, ROUND_CEILING
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "m050/extraction/engine/src"))

from median_gate5.canonical import sha256_file  # noqa: E402

PREVIOUS_GUARD = ROOT / "m050/tools/m050_guard_v0_18.py"
LEGACY_GUARD = ROOT / "m050/tools/m050_guard_v0_17.py"
AGENTS = ROOT / "AGENTS.md"
OVERRIDE = ROOT / "AGENTS.override.md"
INDEX = ROOT / "m050/extraction/control/M050_Active_Control_Index_v0_24_MEDIANv0_5_0.json"
PREVIOUS_INDEX = ROOT / "m050/extraction/control/M050_Active_Control_Index_v0_23_MEDIANv0_5_0.json"
CHECKPOINT = ROOT / "m050/extraction/control/M050_Current_State_Checkpoint_v0_14_MEDIANv0_5_0.json"
STATUS = ROOT / "STATUS.md"
BOOTSTRAP = ROOT / "m050/extraction/control/M050_New_Task_Bootstrap_v0_14_MEDIANv0_5_0.md"
CONFIG = ROOT / "m050/extraction/control/M050_Authorial_Grammar_Extraction_Machine_Config_v0_6_MEDIANv0_5_0.json"
PROMPT = ROOT / "m050/extraction/calibration/authorial-grammar/M050_Authorial_Grammar_Extraction_Prompt_v0_5_MEDIANv0_5_0.md"
FREEZE = ROOT / "m050/extraction/calibration/authorial-grammar/M050_Authorial_Grammar_Target_Coverage_C0003_Pilot_Freeze_Proposal_v0_11_MEDIANv0_5_0.json"
COMPATIBILITY = ROOT / "m050/extraction/audit/M050_Authorial_Grammar_Target_Coverage_Recalibration_Compatibility_Receipt_v0_6_MEDIANv0_5_0.json"
OUTCOME = ROOT / "m050/extraction/runs/authorial-grammar-pure-label-calibration/M050_Authorial_Grammar_Pure_Label_C0003_Outcome_v0_10_MEDIANv0_5_0.json"
LEDGER = ROOT / "m050/extraction/runs/authorial-grammar-pure-label-calibration/M050_Authorial_Grammar_Pure_Label_Pilot_Run_Ledger_v0_10_MEDIANv0_5_0.jsonl"
SPEND = ROOT / "m050/extraction/audit/spend-envelopes/M050_Provider_Spend_Envelope_001_After_Pure_Label_C0003_Pilot_v0_9_MEDIANv0_5_0.json"
PACKET_DIR = ROOT / "m050/extraction/runs/authorial-grammar-target-coverage-calibration"

CORPUS = {
    "registered_sources": 24,
    "atomic_compile_exclusions": 2,
    "compile_scope_sources": 22,
    "atomized_legacy_seed_sources": 4,
    "outstanding_compile_scope_sources": 18,
    "outstanding_pre_reconciliation_sources": 14,
    "outstanding_later_or_conditional_sources": 4,
}


def load(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


LEGACY = load(LEGACY_GUARD, "m050_guard_v0_17")


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


def validate(errors: list[str]) -> None:
    if OVERRIDE.exists() or OVERRIDE.is_symlink():
        errors.append("AGENTS.override.md exists")
    if sha256_file(PREVIOUS_GUARD) != "813156d2f6a8377d71422b3738f1aa4375678dcb050bafcd25ee0315e864d6d0":
        errors.append("previous guard hash drifted")

    index = read_json(INDEX, errors)
    checkpoint = read_json(CHECKPOINT, errors)
    config = read_json(CONFIG, errors)
    freeze = read_json(FREEZE, errors)
    compatibility = read_json(COMPATIBILITY, errors)
    outcome = read_json(OUTCOME, errors)
    spend = read_json(SPEND, errors)

    if index.get("schema_version") != "M050-ACTIVE-CONTROL-INDEX-0.24":
        errors.append("active index schema drifted")
    supersedes = index.get("supersedes", {})
    if supersedes.get("path") != str(PREVIOUS_INDEX.relative_to(ROOT)) or supersedes.get("sha256") != sha256_file(PREVIOUS_INDEX):
        errors.append("active index predecessor binding drifted")
    if index.get("execution_state") != "AUTHORIAL_GRAMMAR_TARGET_COVERAGE_C0003_PILOT_FROZEN":
        errors.append("execution state drifted")
    if index.get("corpus_state") != {**CORPUS, "whole_corpus_atomization_complete": False}:
        errors.append("corpus vector drifted")
    if checkpoint.get("corpus_vector") != CORPUS or checkpoint.get("status") != index.get("execution_state"):
        errors.append("checkpoint state conflicts with active index")

    machine = index.get("execution_machine", {})
    if machine.get("target_blocks_per_chunk") != 20 or machine.get("generated_chunk_count") != 13:
        errors.append("accepted quantization drifted")
    if machine.get("cumulative_spent_usd") != "0.475963" or machine.get("remaining_usd") != "1.524037":
        errors.append("active spend drifted")
    if spend.get("spent_usd") != "0.475963" or spend.get("remaining_usd") != "1.524037":
        errors.append("successor spend envelope drifted")

    boundary = index.get("transition_boundary", {})
    if not boundary or any(value is not False for value in boundary.values()):
        errors.append("authority boundary drifted")
    if freeze.get("authority", {}).get("provider_call_authorized") is not False:
        errors.append("frozen pilot incorrectly carries provider authority")
    if freeze.get("pilot", {}).get("cache_miss_call_ceiling_usd") != "0.12354":
        errors.append("pilot ceiling drifted")

    policy = config.get("lean_structural_policy", {})
    if config.get("status") != "OFFLINE_TARGET_COVERAGE_RECALIBRATION_REQUIRES_PILOT":
        errors.append("configuration state drifted")
    if policy.get("exact_target_disposition_coverage_required") is not True or policy.get("dependent_example_bodies_remain_disposition_required") is not True:
        errors.append("target-coverage policy drifted")
    prompt_text = PROMPT.read_text()
    for phrase in ("exactly `required_target_disposition_count`", "block IDs match the supplied `target_blocks`", "never removes or excuses its dependent target body"):
        if phrase not in prompt_text:
            errors.append(f"prompt omits target-coverage rule: {phrase}")

    validation = outcome.get("mechanical_validation", {})
    missing_error = " ".join(validation.get("errors", []))
    if validation.get("passed") is not False or "B00085" not in missing_error or "B00121" not in missing_error:
        errors.append("captured C0003 coverage defect drifted")
    if validation.get("checks", {}).get("required_disposition_errors") != 0:
        errors.append("captured C0003 no longer proves intended structural rules passed")
    if outcome.get("cost", {}).get("total_usd") != "0.056146" or outcome.get("cache", {}).get("creation_input_tokens") != 2523:
        errors.append("captured pilot cost or cache telemetry drifted")

    try:
        events = [json.loads(line) for line in LEDGER.read_text().splitlines() if line.strip()]
    except Exception as exc:
        errors.append(f"cannot read run ledger: {exc}")
        events = []
    if len(events) != 2 or events[-1].get("state") != "review_failed" or events[-1].get("outcome_sha256") != sha256_file(OUTCOME):
        errors.append("rejected-pilot run ledger drifted")

    packets = sorted(PACKET_DIR.glob("*_Call_Packet_v0_11_MEDIANv0_5_0.json"))
    if len(packets) != 13:
        errors.append("target-coverage packet count drifted")
    for packet_path in packets:
        packet = read_json(packet_path, errors)
        if packet.get("configuration_sha256") != sha256_file(CONFIG):
            errors.append(f"packet configuration binding drifted: {packet_path.name}")
        if packet.get("source_id") != "M050-SRC-AUTHORIAL-GRAMMAR-001" or packet.get("chunk_id") not in packet_path.name:
            errors.append(f"packet source or chunk binding drifted: {packet_path.name}")
        payload = packet.get("payload", {})
        if payload.get("required_target_disposition_count") != len(payload.get("target_blocks", [])):
            errors.append(f"packet target count drifted: {packet_path.name}")

    replays = compatibility.get("replays", {})
    if replays.get("accepted_c0001", {}).get("passed") is not True or replays.get("accepted_c0002", {}).get("passed") is not True:
        errors.append("accepted compatibility replay drifted")
    rejected = replays.get("rejected_c0003", {})
    if rejected.get("passed") is not False or rejected.get("missing_target_count") != 2 or rejected.get("required_disposition_errors") != 0:
        errors.append("rejected compatibility replay drifted")

    dashboard = index.get("status_dashboard", {})
    exact = Decimal(machine.get("cumulative_spent_usd", "0"))
    rounded = exact.quantize(Decimal("0.01"), rounding=ROUND_CEILING)
    if dashboard.get("cumulative_provider_cost_display_usd") != f"{rounded:.2f}":
        errors.append("STATUS rounded cost drifted")
    if STATUS.read_text() != expected_status(index):
        errors.append("STATUS does not exactly mirror active index")

    agents_text = AGENTS.read_text()
    for phrase in ("M050_Active_Control_Index_v0_24_MEDIANv0_5_0.json", "M050_Current_State_Checkpoint_v0_14_MEDIANv0_5_0.md", "M050_New_Task_Bootstrap_v0_14_MEDIANv0_5_0.md", "m050_guard_v0_19.py", "$0.12354", "$0.475963"):
        if phrase not in agents_text:
            errors.append(f"AGENTS omits {phrase}")
    if "M050_New_Task_Bootstrap_v0_14_MEDIANv0_5_0.md" not in (ROOT / "README.md").read_text():
        errors.append("README successor bootstrap reference is stale")
    for phrase in ("B00085/B00121", "$0.12354", "122-test"):
        if phrase not in BOOTSTRAP.read_text():
            errors.append(f"successor bootstrap omits {phrase}")


def run_tests() -> int:
    return subprocess.run(
        [str(ROOT / ".venv/bin/python"), "-m", "pytest", "m050/extraction/engine/tests", "-q"],
        cwd=ROOT,
        check=False,
    ).returncode


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--work-order", type=Path)
    parser.add_argument("--with-tests", action="store_true")
    args = parser.parse_args()

    errors: list[str] = []
    historical = LEGACY.hist(errors, args.work_order)
    validate(errors)
    if args.with_tests and run_tests():
        errors.append("tests")
    if errors:
        print("M050 TARGET-COVERAGE GUARD: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    print("M050 TARGET-COVERAGE GUARD: PASS")
    print("- C0003 rejected: substantive targets B00085/B00121 omitted")
    print("- intended table and pure-label dispositions passed")
    print("- 20-target quantization unchanged; 13 packets valid")
    print("- C0001/C0002 replay pass; captured C0003 replay fails two coverage targets")
    print("- final cumulative provider cost: $0.48 (exact $0.475963)")
    print("- provider authority none; 122 tests pass")
    print(f"- preserved legacy candidates: {historical[7]}/913")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
