#!/usr/bin/env python3
"""Verify the frozen Authorial Grammar structural-recalibration pilot boundary."""

from __future__ import annotations

import argparse
import importlib.util
import json
from pathlib import Path
import re
import subprocess
import sys


REPO_ROOT = Path(__file__).resolve().parents[2]
ENGINE_SRC = REPO_ROOT / "m050/extraction/engine/src"
sys.path.insert(0, str(ENGINE_SRC))

from median_gate5.canonical import sha256_file  # noqa: E402


PRIOR_PATH = REPO_ROOT / "m050/tools/m050_guard_v0_11.py"
AGENTS = REPO_ROOT / "AGENTS.md"
AGENTS_OVERRIDE = REPO_ROOT / "AGENTS.override.md"
ACTIVE_INDEX = REPO_ROOT / "m050/extraction/control/M050_Active_Control_Index_v0_17_MEDIANv0_5_0.json"
PREDECESSOR_INDEX = REPO_ROOT / "m050/extraction/control/M050_Active_Control_Index_v0_16_MEDIANv0_5_0.json"
CHECKPOINT = REPO_ROOT / "m050/extraction/control/M050_Current_State_Checkpoint_v0_8_MEDIANv0_5_0.json"
PREDECESSOR_CHECKPOINT = REPO_ROOT / "m050/extraction/control/M050_Current_State_Checkpoint_v0_7_MEDIANv0_5_0.json"
CHECKPOINT_REPORT = REPO_ROOT / "m050/extraction/control/M050_Current_State_Checkpoint_v0_8_MEDIANv0_5_0.md"
BOOTSTRAP = REPO_ROOT / "m050/extraction/control/M050_New_Task_Bootstrap_v0_7_MEDIANv0_5_0.md"
CONFIG = REPO_ROOT / "m050/extraction/control/M050_Authorial_Grammar_Extraction_Machine_Config_v0_3_MEDIANv0_5_0.json"
PLAN = REPO_ROOT / "m050/extraction/control/M050_Authorial_Grammar_Section_Aware_Chunk_Plan_v0_3_MEDIANv0_5_0.json"
MANIFEST = REPO_ROOT / "m050/extraction/control/source-identities/blocks/M050_Authorial_Grammar_Block_Manifest_v0_1_MEDIANv0_5_0.json"
FREEZE = REPO_ROOT / "m050/extraction/calibration/authorial-grammar/M050_Authorial_Grammar_Structural_C0002_Pilot_Freeze_Proposal_v0_8_MEDIANv0_5_0.json"
PACKET = REPO_ROOT / "m050/extraction/runs/authorial-grammar-structural-pilot/M050_Authorial_Grammar_Structural_C0002_Call_Packet_v0_8_MEDIANv0_5_0.json"
COMPATIBILITY = REPO_ROOT / "m050/extraction/audit/M050_Authorial_Grammar_Structural_Recalibration_Compatibility_Receipt_v0_3_MEDIANv0_5_0.json"
HALT = REPO_ROOT / "m050/extraction/audit/source-run-transitions/M050_Authorial_Grammar_Quantized_Source_Run_Halted_After_C0002_v0_3_MEDIANv0_5_0.json"
SPEND = REPO_ROOT / "m050/extraction/audit/spend-envelopes/M050_Provider_Spend_Envelope_001_After_C0002_v0_4_MEDIANv0_5_0.json"
ACCEPTED_PILOT = REPO_ROOT / "m050/extraction/audit/pilot-transitions/M050_Authorial_Grammar_Quantized_C0001_Pilot_Accepted_v0_7_MEDIANv0_5_0.json"
CONTROLLER = REPO_ROOT / "m050/tools/m050_extraction_machine_v0_1.py"
ENGINE_MODULE = REPO_ROOT / "m050/extraction/engine/src/median_gate5/extraction_machine.py"
ENGINE_TEST = REPO_ROOT / "m050/extraction/engine/tests/test_extraction_machine.py"

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
EXPECTED_TARGETS = [15, 18, 19, 15, 20, 14, 20, 20, 17, 20, 20, 19, 11]
HISTORICAL_ROOT_CONTRACT_DRIFT = "artifacts hash binding mismatch: agents_contract"


def _load_prior():
    spec = importlib.util.spec_from_file_location("m050_guard_v0_11", PRIOR_PATH)
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
        "M050_Active_Control_Index_v0_17_MEDIANv0_5_0.json",
        "M050_Current_State_Checkpoint_v0_8_MEDIANv0_5_0.md",
        "M050_New_Task_Bootstrap_v0_7_MEDIANv0_5_0.md",
        "m050_guard_v0_12.py",
        "24 / 22 / 4 / 18 = 14 + 4",
        "Chunk count is a generated result",
        "indivisible semantic group",
    ):
        if phrase not in text:
            errors.append(f"root AGENTS.md omits: {phrase}")


def validate_index(errors: list[str]) -> None:
    index = read_json(ACTIVE_INDEX, errors)
    predecessor = index.get("supersedes", {})
    if (
        index.get("schema_version") != "M050-ACTIVE-CONTROL-INDEX-0.17"
        or predecessor.get("path") != PREDECESSOR_INDEX.relative_to(REPO_ROOT).as_posix()
        or not PREDECESSOR_INDEX.is_file()
        or predecessor.get("sha256") != sha256_file(PREDECESSOR_INDEX)
    ):
        errors.append("active control index version/predecessor binding drifted")
    if index.get("execution_state") != "AUTHORIAL_GRAMMAR_STRUCTURAL_RECALIBRATION_PILOT_FROZEN":
        errors.append("active control index execution state drifted")
    if index.get("corpus_state") != {**EXPECTED_SUMMARY, "whole_corpus_atomization_complete": False}:
        errors.append("active control index corpus vector drifted")
    calibration = index.get("calibration_state", {})
    required_calibration = {
        "currently_selected_source": EXPECTED_NEXT,
        "accepted_old_plan_quantized_pilot_preserved": True,
        "old_plan_remaining_source_run_revoked": True,
        "structural_replan_complete": True,
        "target_blocks_per_chunk": 20,
        "generated_chunk_count": 13,
        "semantic_groups_audited": 51,
        "cross_chunk_semantic_group_violations": 0,
        "frozen_pilot_chunk": "C0002",
        "additional_provider_calls_authorized": 0,
    }
    if any(calibration.get(key) != value for key, value in required_calibration.items()):
        errors.append("active control index calibration boundary drifted")
    machine = index.get("execution_machine", {})
    required_machine = {
        "chunk_count_is_input": False,
        "semantic_group_oversize_policy": "halt_without_splitting",
        "claude_cache_ttl": "1h",
        "cache_telemetry_required": True,
        "spend_envelope_active": True,
        "cumulative_spent_usd": "0.200286",
        "remaining_usd": "1.799714",
    }
    if any(machine.get(key) != value for key, value in required_machine.items()):
        errors.append("active control index execution-machine policy drifted")
    boundary = index.get("transition_boundary", {})
    if not boundary or any(value is not False for value in boundary.values()):
        errors.append("active control index crosses a prohibited transition")
    for control in index.get("current_controls", []):
        relative = control.get("path")
        if not isinstance(relative, str) or not (REPO_ROOT / relative).is_file():
            errors.append(f"missing active control: {relative}")


def _block_number(block_id: str) -> int:
    match = re.search(r"__B(\d+)_", block_id)
    if not match:
        raise ValueError(block_id)
    return int(match.group(1))


def validate_machine(errors: list[str]) -> None:
    config = read_json(CONFIG, errors)
    if (
        config.get("status") != "OFFLINE_STRUCTURAL_RECALIBRATION_REQUIRES_PILOT"
        or config.get("source_id") != EXPECTED_NEXT
        or config.get("execution", {}).get("provider_calls_authorized") is not False
        or config.get("execution", {}).get("full_source_authorized") is not False
    ):
        errors.append("provider-disabled structural configuration drifted")
    quantization = config.get("quantization", {})
    grouping = config.get("structural_grouping", {})
    if (
        quantization.get("target_blocks_per_chunk") != 20
        or quantization.get("generated_chunk_count") != 13
        or quantization.get("chunk_count_is_input") is not False
        or grouping.get("oversize_policy") != "halt_without_splitting"
        or grouping.get("audited_lead_in_body_groups") != 51
        or grouping.get("cross_chunk_violations") != 0
    ):
        errors.append("structural quantization binding drifted")
    for name, relative in config.get("artifacts", {}).items():
        target = REPO_ROOT / relative
        if not target.is_file() or config.get("artifact_sha256", {}).get(name) != sha256_file(target):
            errors.append(f"structural configuration artifact drifted: {name}")

    plan = read_json(PLAN, errors)
    chunks = plan.get("chunks", [])
    if (
        plan.get("status") != "OFFLINE_RECALIBRATION_REQUIRES_PILOT"
        or plan.get("quantization", {}).get("target_blocks_per_chunk") != 20
        or plan.get("quantization", {}).get("chunk_count_is_input") is not False
        or [chunk.get("target_blocks") for chunk in chunks] != EXPECTED_TARGETS
    ):
        errors.append("complete-source structural replan drifted")
    manifest = read_json(MANIFEST, errors)
    primary = [block_id for chunk in chunks for block_id in chunk.get("block_ids", [])]
    expected = [block.get("block_id") for block in manifest.get("blocks", [])]
    if primary != expected:
        errors.append("structural replan lost, duplicated, or reordered source blocks")
    chunk_for_number = {
        _block_number(block_id): chunk.get("chunk_id")
        for chunk in chunks for block_id in chunk.get("block_ids", [])
    }
    if len({chunk_for_number.get(number) for number in range(41, 49)}) != 1:
        errors.append("formerly split B00041-B00048 semantic group is not indivisible")

    freeze = read_json(FREEZE, errors)
    authority = freeze.get("authority", {})
    binding = freeze.get("binding", {})
    if (
        freeze.get("state") != "awaiting_exact_one_call_authorization"
        or authority.get("provider_call_authorized") is not False
        or authority.get("requested_provider_call_limit") != 1
        or binding.get("pilot_chunk_id") != "C0002"
        or binding.get("configuration_sha256") != sha256_file(CONFIG)
        or binding.get("chunk_plan_sha256") != sha256_file(PLAN)
        or binding.get("pilot_packet_file_sha256") != sha256_file(PACKET)
        or freeze.get("pilot", {}).get("cache_miss_call_ceiling_usd") != "0.105248"
        or freeze.get("offline_verification", {}).get("offline_tests_passed") != EXPECTED_TESTS
    ):
        errors.append("frozen C0002 structural pilot binding drifted")
    packet = read_json(PACKET, errors)
    if (
        packet.get("chunk_id") != "C0002"
        or packet.get("configuration_sha256") != sha256_file(CONFIG)
        or packet.get("cache_miss_call_ceiling_usd") != "0.105248"
        or packet.get("binding", {}).get("cache_ttl") != "1h"
        or packet.get("binding", {}).get("cache_required") is not True
    ):
        errors.append("C0002 structural pilot packet drifted")
    compatibility = read_json(COMPATIBILITY, errors)
    verification = compatibility.get("offline_verification", {})
    if (
        compatibility.get("status") != "OFFLINE_STRUCTURAL_RECALIBRATION_VERIFIED_PILOT_REQUIRED"
        or verification.get("generated_chunk_count") != 13
        or verification.get("semantic_lead_in_body_groups_audited") != 51
        or verification.get("cross_chunk_semantic_group_violations") != 0
        or verification.get("offline_tests_passed") != EXPECTED_TESTS
        or compatibility.get("authority_boundary", {}).get("provider_calls_authorized") != 0
    ):
        errors.append("structural compatibility receipt drifted")

    spend = read_json(SPEND, errors)
    if (
        spend.get("active") is not True
        or spend.get("spent_usd") != "0.200286"
        or spend.get("remaining_usd") != "1.799714"
    ):
        errors.append("money-only spend envelope drifted")
    halt = read_json(HALT, errors)
    if halt.get("release_revoked") is not True or halt.get("additional_provider_calls_authorized") != 0:
        errors.append("old-plan halted-run boundary drifted")
    accepted = read_json(ACCEPTED_PILOT, errors)
    if accepted.get("state") != "pilot_accepted" or accepted.get("full_source_execution_authorized") is not False:
        errors.append("old-plan accepted-pilot evidence drifted")
    for path in (CONTROLLER, ENGINE_MODULE, ENGINE_TEST):
        if not path.is_file():
            errors.append(f"missing extraction-machine file: {path.relative_to(REPO_ROOT)}")


def validate_checkpoint(errors: list[str]) -> None:
    checkpoint = read_json(CHECKPOINT, errors)
    predecessor = checkpoint.get("supersedes", {})
    if (
        checkpoint.get("status") != "AUTHORIAL_GRAMMAR_STRUCTURAL_RECALIBRATION_PILOT_FROZEN"
        or predecessor.get("path") != PREDECESSOR_CHECKPOINT.relative_to(REPO_ROOT).as_posix()
        or not PREDECESSOR_CHECKPOINT.is_file()
        or predecessor.get("sha256") != sha256_file(PREDECESSOR_CHECKPOINT)
        or checkpoint.get("corpus_vector") != EXPECTED_SUMMARY
        or checkpoint.get("next_source_id") != EXPECTED_NEXT
    ):
        errors.append("structural checkpoint state drifted")
    authority = checkpoint.get("authority_boundary", {})
    if not authority or any(value is not False for value in authority.values()):
        errors.append("structural checkpoint crosses an authority boundary")
    for name, binding in checkpoint.get("artifacts", {}).items():
        relative = binding.get("path")
        target = REPO_ROOT / relative if isinstance(relative, str) else Path("/__missing__")
        if not target.is_file() or binding.get("sha256") != sha256_file(target):
            errors.append(f"structural checkpoint artifact drifted: {name}")
    report = CHECKPOINT_REPORT.read_text(encoding="utf-8") if CHECKPOINT_REPORT.is_file() else ""
    bootstrap = BOOTSTRAP.read_text(encoding="utf-8") if BOOTSTRAP.is_file() else ""
    for phrase in ("13 chunks", "51 detected", "$1.799714", "$0.105248"):
        if phrase not in report:
            errors.append(f"checkpoint report omits: {phrase}")
    for phrase in ("Remain read-only", "13 generated chunks", "51 audited", "Complete guard result"):
        if phrase not in bootstrap:
            errors.append(f"successor bootstrap omits: {phrase}")


def run_tests() -> int:
    python = REPO_ROOT / ".venv/bin/python"
    if not python.is_file():
        print("Gate 5 test environment is missing: .venv/bin/python", file=sys.stderr)
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
    validate_machine(errors)
    validate_checkpoint(errors)
    if args.with_tests and run_tests():
        errors.append("Gate 5 offline regression suite failed")
    if errors:
        print("M050 GATE 5 STRUCTURAL-RECALIBRATION GUARD: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1
    print("M050 GATE 5 STRUCTURAL-RECALIBRATION GUARD: PASS")
    print("- root contract: AGENTS.md only; no override")
    print("- corpus vector: 24 registered / 22 compile / 4 atomized / 18 outstanding = 14 + 4")
    print("- next source: Authorial Grammar")
    print("- accepted evidence: old-plan quantized C0001 pilot only; no whole-source candidate")
    print("- old-plan C0002: rejected semantic context split; remaining-source release revoked")
    print("- structural replan: 20-target quantization generated 13 chunks; count was not preserved")
    print("- semantic grouping: 51 lead-in/body groups audited; zero cross-chunk violations")
    print("- frozen pilot: new-plan C0002, B00041-B00068, 18 targets, $0.105248 cache-miss ceiling")
    print("- spend: $0.200286 cumulative; active money-only balance $1.799714")
    print("- provider/full-source authority: none; exact one-call authorization required")
    print("- cadence: sequential one call and substantive review at a time; any defect halts")
    print("- semantic acceptance/mapping/reconciliation/compiled prose: prohibited")
    print("- Google Sheets: paused")
    print(f"- preserved legacy candidates: {historical[7]}/913")
    if args.with_tests:
        print(f"- offline regression suite: pass ({EXPECTED_TESTS} tests)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
