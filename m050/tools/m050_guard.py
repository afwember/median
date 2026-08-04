#!/usr/bin/env python3
"""Validate the current MEDIAN v0.5.0 compile without historical guard chains."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from datetime import datetime
from decimal import Decimal, ROUND_CEILING
from pathlib import Path
from typing import Iterable
from zoneinfo import ZoneInfo


ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / "m050/extraction/control/M050_Compile_State_MEDIANv0_5_0.json"
STATUS = ROOT / "STATUS.md"
AGENTS = ROOT / "AGENTS.md"
OVERRIDE = ROOT / "AGENTS.override.md"
FROZEN = ROOT / "m050/extraction/control/M050_Frozen_Corpus_Manifest_v0_1_MEDIANv0_5_0.json"
GATE_2 = ROOT / "m050/extraction/audit/M050_Extraction_Gate_2_Source_Disposition_v0_1_MEDIANv0_5_0.yaml"
MATRIX = ROOT / "m050/extraction/control/M050_Compile_Source_State_Matrix_v0_1_MEDIANv0_5_0.json"
ORDER = ROOT / "m050/extraction/control/M050_Compile_Source_Processing_Order_v0_1_MEDIANv0_5_0.json"
MIGRATION_RECEIPT = ROOT / "m050/extraction/audit/M050_Extraction_Gate_5_Layer_E_Legacy_Migration_Receipt_v0_1_MEDIANv0_5_0.json"
ARCHIVE_RETIREMENT_RECEIPT = ROOT / "m050/extraction/audit/M050_Extraction_Gate_5_Archive_Retirement_Receipt_v0_1_MEDIANv0_5_0.json"
RELOCATION_MANIFEST = ROOT / "m050/extraction/evidence/legacy/M050_Legacy_Evidence_Relocation_Manifest_v0_1_MEDIANv0_5_0.json"
CONFIG = ROOT / "m050/extraction/control/M050_Authorial_Grammar_Extraction_Machine_Config_v0_6_MEDIANv0_5_0.json"
PROMPT = ROOT / "m050/extraction/calibration/authorial-grammar/M050_Authorial_Grammar_Extraction_Prompt_v0_5_MEDIANv0_5_0.md"
FREEZE = ROOT / "m050/extraction/calibration/authorial-grammar/M050_Authorial_Grammar_Target_Coverage_C0003_Pilot_Freeze_Proposal_v0_11_MEDIANv0_5_0.json"
COMPATIBILITY = ROOT / "m050/extraction/audit/M050_Authorial_Grammar_Target_Coverage_Recalibration_Compatibility_Receipt_v0_6_MEDIANv0_5_0.json"
OUTCOME = ROOT / "m050/extraction/runs/authorial-grammar-pure-label-calibration/M050_Authorial_Grammar_Pure_Label_C0003_Outcome_v0_10_MEDIANv0_5_0.json"
LEDGER = ROOT / "m050/extraction/runs/authorial-grammar-pure-label-calibration/M050_Authorial_Grammar_Pure_Label_Pilot_Run_Ledger_v0_10_MEDIANv0_5_0.jsonl"
SPEND = ROOT / "m050/extraction/audit/spend-envelopes/M050_Provider_Spend_Envelope_001_After_Pure_Label_C0003_Pilot_v0_9_MEDIANv0_5_0.json"
PACKET_DIR = ROOT / "m050/extraction/runs/authorial-grammar-target-coverage-calibration"
PILOT_PACKET = PACKET_DIR / "M050_Authorial_Grammar_Target_Coverage_C0003_Call_Packet_v0_11_MEDIANv0_5_0.json"
CHUNK_PLAN = ROOT / "m050/extraction/control/M050_Authorial_Grammar_Section_Aware_Chunk_Plan_v0_3_MEDIANv0_5_0.json"
ENGINE_MODULE = ROOT / "m050/extraction/engine/src/median_gate5/extraction_machine.py"
ENGINE_TESTS = ROOT / "m050/extraction/engine/tests/test_extraction_machine.py"

CORPUS = {
    "registered_sources": 24,
    "atomic_compile_exclusions": 2,
    "compile_scope_sources": 22,
    "atomized_legacy_seed_sources": 4,
    "outstanding_compile_scope_sources": 18,
    "outstanding_pre_reconciliation_sources": 14,
    "outstanding_later_or_conditional_sources": 4,
}
IGNORED_NAMES = {".DS_Store"}
RETIRED_PATTERNS = (
    "m050/extraction/control/M050_Active_Control_Index_v0_*_MEDIANv0_5_0.json",
    "m050/extraction/control/M050_Current_State_Checkpoint_v0_*_MEDIANv0_5_0.json",
    "m050/extraction/control/M050_Current_State_Checkpoint_v0_*_MEDIANv0_5_0.md",
    "m050/extraction/control/M050_New_Task_Bootstrap_v0_*_MEDIANv0_5_0.md",
    "m050/extraction/control/M050_Compile_Execution_Standard_v0_*_MEDIANv0_5_0.md",
    "m050/extraction/control/M050_Repository_Write_Authority_and_Freeze_Policy_v0_1_MEDIANv0_5_0.md",
    "m050/extraction/control/M050_Compile_Source_State_Matrix_v0_1_MEDIANv0_5_0.md",
    "m050/tools/m050_guard_v0_*.py",
)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def read_json(path: Path, errors: list[str]) -> dict:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"cannot read JSON {path.relative_to(ROOT)}: {exc}")
        return {}
    if not isinstance(value, dict):
        errors.append(f"JSON root is not an object: {path.relative_to(ROOT)}")
        return {}
    return value


def relative_files(roots: Iterable[str]) -> set[str]:
    found: set[str] = set()
    for root_text in roots:
        source_root = ROOT / root_text
        if not source_root.is_dir():
            continue
        for item in source_root.rglob("*"):
            if item.is_file() and item.name not in IGNORED_NAMES:
                found.add(item.relative_to(ROOT).as_posix())
    return found


def gate2_registered_sources() -> dict[str, tuple[str, str]]:
    records: dict[str, tuple[str, str]] = {}
    current: dict[str, str] = {}
    in_sources = False
    for raw_line in GATE_2.read_text(encoding="utf-8").splitlines():
        if raw_line == "sources:":
            in_sources = True
            continue
        if in_sources and raw_line and not raw_line.startswith(" "):
            break
        if not in_sources:
            continue
        stripped = raw_line.strip()
        if stripped.startswith("- source_id: "):
            if {"source_id", "path", "sha256"} <= current.keys():
                records[current["source_id"]] = (current["path"], current["sha256"])
            current = {"source_id": stripped.split(": ", 1)[1]}
        elif stripped.startswith("path: "):
            current["path"] = stripped.split(": ", 1)[1]
        elif stripped.startswith("sha256: "):
            current["sha256"] = stripped.split(": ", 1)[1]
    if {"source_id", "path", "sha256"} <= current.keys():
        records[current["source_id"]] = (current["path"], current["sha256"])
    return records


def validate_frozen_corpus(errors: list[str]) -> tuple[int, int]:
    manifest = read_json(FROZEN, errors)
    frozen_files = manifest.get("frozen_files", [])
    expected = {item.get("path"): item.get("sha256") for item in frozen_files}
    registered = {
        item.get("source_id"): (item.get("path"), item.get("sha256"))
        for item in frozen_files
        if item.get("kind") == "registered_source"
    }
    if gate2_registered_sources() != registered:
        errors.append("Gate 2 source disposition disagrees with the frozen manifest")
    actual = relative_files(manifest.get("source_roots", []))
    for relative in sorted(set(expected) - actual):
        errors.append(f"missing frozen source: {relative}")
    for relative in sorted(actual - set(expected)):
        errors.append(f"unregistered file in frozen source root: {relative}")
    for relative, expected_hash in expected.items():
        target = ROOT / str(relative)
        if target.is_file() and sha256_file(target) != expected_hash:
            errors.append(f"frozen source hash mismatch: {relative}")

    immutable = manifest.get("immutable_accepted_files", [])
    for binding in immutable:
        target = ROOT / binding.get("path", "")
        if not target.is_file() or sha256_file(target) != binding.get("sha256"):
            errors.append(f"immutable accepted artifact drifted: {binding.get('path')}")

    return len(expected), len(immutable)


def validate_archive_retirement(errors: list[str]) -> int:
    if (ROOT / "m050/archive").exists():
        errors.append("retired m050/archive directory has returned")
    frozen = read_json(FROZEN, errors)
    manifest = read_json(RELOCATION_MANIFEST, errors)
    receipt = read_json(ARCHIVE_RETIREMENT_RECEIPT, errors)
    if manifest.get("status") != "ACTIVE_ARCHIVE_RETIRED":
        errors.append("legacy-evidence relocation manifest is not active")
    retired = manifest.get("retired_archive_snapshot", {})
    expected = frozen.get("archive_snapshot", {})
    for key in (
        "root",
        "file_count_excluding_ds_store",
        "total_bytes",
        "ordered_path_and_sha256_digest",
    ):
        if retired.get(key) != expected.get(key):
            errors.append(f"retired archive snapshot drifted: {key}")
    original_paths: set[str] = set()
    relocated_paths: set[str] = set()
    for item in manifest.get("relocations", []):
        original = item.get("original_path")
        relocated = item.get("relocated_path")
        if not isinstance(original, str) or not original.startswith("m050/archive/"):
            errors.append(f"invalid retired archive identifier: {original}")
            continue
        if not isinstance(relocated, str) or not relocated.startswith("m050/extraction/evidence/legacy/"):
            errors.append(f"invalid relocated evidence path: {relocated}")
            continue
        if original in original_paths or relocated in relocated_paths:
            errors.append("duplicate legacy-evidence relocation")
            continue
        original_paths.add(original)
        relocated_paths.add(relocated)
        target = ROOT / relocated
        if not target.is_file() or sha256_file(target) != item.get("sha256"):
            errors.append(f"relocated legacy evidence drifted: {relocated}")
    if len(original_paths) != 12 or len(relocated_paths) != 12:
        errors.append("legacy-evidence relocation coverage is not 12 files")
    if receipt.get("status") != "ARCHIVE_RETIRED_EVIDENCE_RELOCATED":
        errors.append("archive-retirement receipt status drifted")
    if receipt.get("authority") != "Asa Wember":
        errors.append("archive-retirement receipt lacks author authority")
    if receipt.get("bindings", {}).get("relocation_manifest", {}).get("sha256") != sha256_file(
        RELOCATION_MANIFEST
    ):
        errors.append("archive-retirement relocation binding drifted")
    verification = receipt.get("verification", {})
    if (
        verification.get("relocated_evidence_files") != 12
        or verification.get("relocated_evidence_hash_mismatches") != 0
        or verification.get("retired_archive_present") is not False
    ):
        errors.append("archive-retirement verification boundary drifted")
    return len(relocated_paths)


def validate_legacy_evidence(errors: list[str]) -> int:
    receipt = read_json(MIGRATION_RECEIPT, errors)
    if receipt.get("status") != "LAYER_E_LEGACY_MIGRATION_CANDIDATES_COMPLETE":
        errors.append("legacy migration receipt status drifted")
    if receipt.get("provider_call_authorized") is not False:
        errors.append("legacy migration receipt permits provider calls")
    if receipt.get("external_model_calls") != 0 or receipt.get("accounted_cost_cents") != 0:
        errors.append("legacy migration receipt cost boundary drifted")

    artifacts = receipt.get("artifacts", {})
    required = (
        "migration_candidates",
        "compound_review_inventory",
        "transition_control",
        "migration_report",
        "crossing_block_ledger",
        "human_rulings_block_ledger",
        "msid_block_ledger",
        "pa_block_ledger",
        "human_readable_report",
    )
    resolved: dict[str, Path] = {}
    for name in required:
        binding = artifacts.get(name, {})
        target = ROOT / binding.get("path", "")
        resolved[name] = target
        if not target.is_file() or sha256_file(target) != binding.get("sha256"):
            errors.append(f"legacy evidence artifact drifted: {name}")
    if any(not target.is_file() for target in resolved.values()):
        return 0

    try:
        candidates = [
            json.loads(line)
            for line in resolved["migration_candidates"].read_text(encoding="utf-8").splitlines()
            if line.strip()
        ]
        inventory = [
            json.loads(line)
            for line in resolved["compound_review_inventory"].read_text(encoding="utf-8").splitlines()
            if line.strip()
        ]
        transition = json.loads(resolved["transition_control"].read_text(encoding="utf-8"))
        report = json.loads(resolved["migration_report"].read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        errors.append(f"legacy evidence JSON invalid: {exc}")
        return 0

    ids = [item.get("legacy_record_id") for item in candidates]
    if len(candidates) != 913 or len(set(ids)) != 913 or any(not isinstance(item, str) for item in ids):
        errors.append("legacy migration candidate coverage is not 913 unique records")
    for candidate in candidates:
        if (
            candidate.get("state") != "mechanically_valid"
            or candidate.get("acceptance_state") != "not_accepted"
            or candidate.get("review_state") != "pending"
            or candidate.get("mapping_state") != "not_started"
            or candidate.get("reconciliation_state") != "not_started"
        ):
            errors.append(f"legacy candidate crossed its dormant boundary: {candidate.get('legacy_record_id')}")
            break
    inventory_ids = [item.get("legacy_record_id") for item in inventory]
    if len(inventory) != 139 or len(set(inventory_ids)) != 139:
        errors.append("legacy compound review inventory drifted")
    if (
        transition.get("permitted_next_state") != "semantic_review_pending"
        or transition.get("direct_acceptance_from_mechanically_valid_prohibited") is not True
        or transition.get("mapping_authorized") is not False
        or transition.get("reconciliation_authorized") is not False
        or transition.get("compilation_authorized") is not False
    ):
        errors.append("legacy transition boundary drifted")
    if (
        report.get("passed") is not True
        or report.get("migration_candidate_count") != 913
        or report.get("accepted_evidence_records") != 0
        or report.get("semantic_reviews_performed") != 0
    ):
        errors.append("legacy migration report drifted")
    return len(set(ids))


def validate_source_registry(errors: list[str]) -> None:
    matrix = read_json(MATRIX, errors)
    order = read_json(ORDER, errors)
    if matrix.get("summary") != CORPUS or len(matrix.get("sources", [])) != 24:
        errors.append("source matrix corpus vector drifted")
    sequence = order.get("sequence", [])
    matrix_by_id = {item.get("source_id"): item for item in matrix.get("sources", [])}
    if [item.get("order") for item in sequence] != list(range(1, 25)):
        errors.append("processing order ordinals drifted")
    if len({item.get("source_id") for item in sequence}) != 24 or set(matrix_by_id) != {
        item.get("source_id") for item in sequence
    }:
        errors.append("processing order source coverage drifted")
    if order.get("next_source", {}).get("source_id") != "M050-SRC-AUTHORIAL-GRAMMAR-001":
        errors.append("next source drifted")
    if len(order.get("outstanding_pre_reconciliation_order", [])) != 14:
        errors.append("pre-reconciliation processing queue drifted")


def expected_status(state: dict) -> str:
    dashboard = state.get("dashboard", {})
    display = state.get("spend", {}).get("display_usd_rounded_up", "")
    return (
        "# MEDIAN COMPILE — v0.5.0\n\n"
        f"**UPDATED:** {dashboard.get('updated_human', '')}<br>\n\n"
        "<!-- Derived dashboard only; M050_Compile_State_MEDIANv0_5_0.json is authoritative. -->\n\n"
        f"**STATUS:** {dashboard.get('status', '')}<br>\n"
        f"**PHASE:** {dashboard.get('phase', '')}<br>\n"
        f"**SOURCE:** {dashboard.get('source', '')}<br>\n"
        f"**CHUNK:** {dashboard.get('chunk', '')}<br>\n"
        f"**NOW:** {dashboard.get('now', '')}<br>\n"
        f"**NEXT:** {dashboard.get('next', '')}<br>\n"
        f"**TOTAL COST:** ${display} cumulative provider spend\n"
    )


def validate_timestamp(state: dict, errors: list[str]) -> None:
    try:
        exact = datetime.fromisoformat(state.get("updated", ""))
    except ValueError:
        errors.append("canonical state timestamp is not ISO-8601 to the second")
        return
    if exact.microsecond:
        errors.append("canonical state timestamp is not rounded to the nearest second")
    eastern = exact.astimezone(ZoneInfo("America/New_York"))
    expected = (
        f"{eastern.strftime('%B')} {eastern.day}, {eastern.year} at "
        f"{eastern.strftime('%I').lstrip('0')}:{eastern.strftime('%M:%S %p %Z')}"
    )
    if state.get("dashboard", {}).get("updated_human") != expected:
        errors.append("human STATUS timestamp disagrees with canonical ISO timestamp")


def validate_current_boundary(errors: list[str]) -> None:
    state = read_json(STATE, errors)
    config = read_json(CONFIG, errors)
    freeze = read_json(FREEZE, errors)
    compatibility = read_json(COMPATIBILITY, errors)
    outcome = read_json(OUTCOME, errors)
    spend = read_json(SPEND, errors)

    if state.get("schema_version") != "M050-COMPILE-STATE-1.0":
        errors.append("canonical compile-state schema drifted")
    if state.get("execution_state") != "AUTHORIAL_GRAMMAR_TARGET_COVERAGE_C0003_PILOT_FROZEN":
        errors.append("current execution state drifted")
    if state.get("corpus") != {**CORPUS, "whole_corpus_atomization_complete": False}:
        errors.append("canonical corpus vector drifted")
    source = state.get("source", {})
    if (
        source.get("id") != "M050-SRC-AUTHORIAL-GRAMMAR-001"
        or source.get("accepted_chunk_ids") != ["C0001", "C0002"]
        or source.get("rejected_chunk_id") != "C0003"
        or source.get("source_work_authorized") is not False
    ):
        errors.append("current source boundary drifted")
    authority = state.get("authority", {})
    if not authority or any(value is not False for value in authority.values()):
        errors.append("current authority boundary drifted")

    calibration = state.get("calibration", {})
    if (
        calibration.get("generated_chunk_count") != 13
        or calibration.get("target_blocks_per_chunk") != 20
        or calibration.get("pilot_chunk_id") != "C0003"
        or calibration.get("cache_miss_call_ceiling_usd") != "0.12354"
        or calibration.get("provider_call_authorized") is not False
    ):
        errors.append("current calibration boundary drifted")
    for key in ("configuration", "freeze", "compatibility_receipt", "run_ledger"):
        target = ROOT / calibration.get(key, "")
        if not target.is_file():
            errors.append(f"canonical calibration path is missing: {key}")

    if config.get("status") != "OFFLINE_TARGET_COVERAGE_RECALIBRATION_REQUIRES_PILOT":
        errors.append("configuration state drifted")
    policy = config.get("lean_structural_policy", {})
    if (
        policy.get("exact_target_disposition_coverage_required") is not True
        or policy.get("dependent_example_bodies_remain_disposition_required") is not True
    ):
        errors.append("target-coverage policy drifted")
    for name, relative in config.get("artifacts", {}).items():
        target = ROOT / relative
        if not target.is_file() or sha256_file(target) != config.get("artifact_sha256", {}).get(name):
            errors.append(f"configuration artifact binding drifted: {name}")
    prompt_text = PROMPT.read_text(encoding="utf-8")
    for phrase in (
        "exactly `required_target_disposition_count`",
        "block IDs match the supplied `target_blocks`",
        "never removes or excuses its dependent target body",
    ):
        if phrase not in prompt_text:
            errors.append(f"prompt omits target-coverage rule: {phrase}")

    binding = freeze.get("binding", {})
    pilot_packet = read_json(PILOT_PACKET, errors)
    if (
        binding.get("source_id") != "M050-SRC-AUTHORIAL-GRAMMAR-001"
        or binding.get("pilot_chunk_id") != "C0003"
        or binding.get("configuration_sha256") != sha256_file(CONFIG)
        or binding.get("chunk_plan_sha256") != sha256_file(CHUNK_PLAN)
        or binding.get("prompt_sha256") != sha256_file(PROMPT)
        or binding.get("pilot_packet_sha256") != pilot_packet.get("packet_sha256")
        or binding.get("pilot_packet_file_sha256") != sha256_file(PILOT_PACKET)
        or binding.get("engine_module_sha256") != sha256_file(ENGINE_MODULE)
        or binding.get("engine_tests_sha256") != sha256_file(ENGINE_TESTS)
    ):
        errors.append("frozen C0003 binding drifted")
    if freeze.get("authority", {}).get("provider_call_authorized") is not False:
        errors.append("frozen C0003 incorrectly carries provider authority")
    if freeze.get("pilot", {}).get("cache_miss_call_ceiling_usd") != "0.12354":
        errors.append("frozen C0003 ceiling drifted")

    validation = outcome.get("mechanical_validation", {})
    outcome_errors = " ".join(validation.get("errors", []))
    if validation.get("passed") is not False or "B00085" not in outcome_errors or "B00121" not in outcome_errors:
        errors.append("captured C0003 coverage defect drifted")
    if validation.get("checks", {}).get("required_disposition_errors") != 0:
        errors.append("captured C0003 structural-rule evidence drifted")
    if outcome.get("cost", {}).get("total_usd") != "0.056146":
        errors.append("captured C0003 exact cost drifted")

    try:
        events = [json.loads(line) for line in LEDGER.read_text(encoding="utf-8").splitlines() if line.strip()]
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"run ledger invalid: {exc}")
        events = []
    if len(events) != 2 or events[-1].get("state") != "review_failed" or events[-1].get("outcome_sha256") != sha256_file(OUTCOME):
        errors.append("rejected-pilot ledger drifted")

    packets = sorted(PACKET_DIR.glob("*_Call_Packet_v0_11_MEDIANv0_5_0.json"))
    if len(packets) != 13:
        errors.append("target-coverage packet count drifted")
    for packet_path in packets:
        packet = read_json(packet_path, errors)
        if packet.get("configuration_sha256") != sha256_file(CONFIG):
            errors.append(f"packet configuration binding drifted: {packet_path.name}")
        payload = packet.get("payload", {})
        if payload.get("required_target_disposition_count") != len(payload.get("target_blocks", [])):
            errors.append(f"packet target count drifted: {packet_path.name}")

    replays = compatibility.get("replays", {})
    if (
        replays.get("accepted_c0001", {}).get("passed") is not True
        or replays.get("accepted_c0002", {}).get("passed") is not True
        or replays.get("rejected_c0003", {}).get("missing_target_count") != 2
    ):
        errors.append("target-coverage compatibility replay drifted")

    state_spend = state.get("spend", {})
    if (
        spend.get("spent_usd") != state_spend.get("cumulative_spent_usd")
        or spend.get("remaining_usd") != state_spend.get("remaining_usd")
        or spend.get("authorized_usd") != state_spend.get("authorized_usd")
    ):
        errors.append("canonical spend disagrees with spend evidence")
    try:
        rounded = Decimal(state_spend.get("cumulative_spent_usd", "")).quantize(
            Decimal("0.01"), rounding=ROUND_CEILING
        )
    except Exception:
        errors.append("canonical cumulative spend is not decimal")
    else:
        if state_spend.get("display_usd_rounded_up") != f"{rounded:.2f}":
            errors.append("dashboard cost is not rounded upward to the cent")

    validate_timestamp(state, errors)
    if STATUS.read_text(encoding="utf-8") != expected_status(state):
        errors.append("STATUS does not exactly mirror canonical compile state")


def validate_operating_contract(errors: list[str]) -> None:
    if OVERRIDE.exists() or OVERRIDE.is_symlink():
        errors.append("AGENTS.override.md exists")
    text = AGENTS.read_text(encoding="utf-8")
    for phrase in (
        "Conservation of Process",
        "Conservation of Representation",
        "Conservation of Mandate",
        "M050_Compile_State_MEDIANv0_5_0.json",
        "m050/tools/m050_guard.py",
        "Starting the next source always",
        "A normal compile operation has no process delta",
    ):
        if phrase not in text:
            errors.append(f"AGENTS omits required control: {phrase}")
    for pattern in RETIRED_PATTERNS:
        for target in ROOT.glob(pattern):
            errors.append(f"retired supervisory file remains active: {target.relative_to(ROOT)}")


def validate_json_integrity(errors: list[str]) -> tuple[int, int]:
    json_count = 0
    jsonl_count = 0
    for target in (ROOT / "m050/extraction").rglob("*.json"):
        try:
            json.loads(target.read_text(encoding="utf-8"))
            json_count += 1
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"invalid JSON {target.relative_to(ROOT)}: {exc}")
    for target in (ROOT / "m050/extraction").rglob("*.jsonl"):
        try:
            for line in target.read_text(encoding="utf-8").splitlines():
                if line.strip():
                    json.loads(line)
            jsonl_count += 1
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"invalid JSONL {target.relative_to(ROOT)}: {exc}")
    return json_count, jsonl_count


def validate_work_order(path: Path | None, errors: list[str]) -> None:
    if path is None:
        return
    data = read_json(path.resolve(), errors)
    candidates: list[str] = []
    for key in ("source_path", "path", "input_path"):
        if isinstance(data.get(key), str):
            candidates.append(data[key])
    if isinstance(data.get("input_paths"), list):
        candidates.extend(item for item in data["input_paths"] if isinstance(item, str))
    contaminated = [item for item in candidates if item == "m051" or item.startswith("m051/")]
    if contaminated:
        errors.append("work order contains prohibited m051 input")


def run_tests() -> int:
    return subprocess.run(
        [str(ROOT / ".venv/bin/python"), "-m", "pytest", "m050/extraction/engine/tests", "-q"],
        cwd=ROOT,
        check=False,
    ).returncode


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--work-order", type=Path)
    parser.add_argument("--with-tests", action="store_true")
    args = parser.parse_args()

    errors: list[str] = []
    frozen_count, immutable_count = validate_frozen_corpus(errors)
    relocated_count = validate_archive_retirement(errors)
    legacy_count = validate_legacy_evidence(errors)
    validate_source_registry(errors)
    validate_operating_contract(errors)
    validate_current_boundary(errors)
    json_count, jsonl_count = validate_json_integrity(errors)
    validate_work_order(args.work_order, errors)
    if args.with_tests and run_tests():
        errors.append("offline regression suite failed")

    if errors:
        print("M050 COMPILE GUARD: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    print("M050 COMPILE GUARD: PASS")
    print("- corpus: 24 / 22 / 4 / 18 = 14 + 4")
    print(f"- frozen files: {frozen_count}; immutable accepted artifacts: {immutable_count}")
    print(f"- retired archive absent; compact relocated evidence: {relocated_count}/12")
    print(f"- preserved dormant legacy candidates: {legacy_count}/913")
    print("- Authorial Grammar C0001/C0002 accepted; C0003 frozen and unauthorized")
    print("- spend: $0.475963 exact; $1.524037 remaining; $0.48 display")
    print(f"- JSON integrity: {json_count} JSON files and {jsonl_count} JSONL files")
    if args.with_tests:
        print("- offline regression suite: pass")
    return 0


if __name__ == "__main__":
    sys.exit(main())
