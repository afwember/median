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
from decimal import Decimal, ROUND_CEILING, ROUND_FLOOR
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
ENGINE_MODULE = ROOT / "m050/extraction/engine/src/median_gate5/extraction_machine.py"
ENGINE_TESTS = ROOT / "m050/extraction/engine/tests/test_extraction_machine.py"
HUMAN_EVIDENCE = ROOT / "m050/extraction/evidence/human-rulings"

LIVE_EXTRACTION_DIRS = {
    "accepted",
    "audit",
    "calibration",
    "control",
    "engine",
    "evidence",
    "runs",
}
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
IGNORED_RUNTIME_DIRS = {"__pycache__", ".pytest_cache", "build", "median_gate5.egg-info"}
RETIRED_PATTERNS = (
    "m050/extraction/control/M050_Active_Control_Index_v0_*_MEDIANv0_5_0.json",
    "m050/extraction/control/M050_Current_State_Checkpoint_v0_*_MEDIANv0_5_0.json",
    "m050/extraction/control/M050_Current_State_Checkpoint_v0_*_MEDIANv0_5_0.md",
    "m050/extraction/control/M050_New_Task_Bootstrap_v0_*_MEDIANv0_5_0.md",
    "m050/extraction/control/M050_Compile_Execution_Standard_v0_*_MEDIANv0_5_0.md",
    "m050/extraction/control/M050_Repository_Write_Authority_and_Freeze_Policy_v0_1_MEDIANv0_5_0.md",
    "m050/extraction/control/M050_Compile_Source_State_Matrix_v0_1_MEDIANv0_5_0.md",
    "m050/extraction/control/M050_Source_Atomization_Pilot_Calibration_Protocol_v0_*_MEDIANv0_5_0.md",
    "m050/tools/m050_guard_v0_*.py",
    "m050/extraction/audit/M050_*_Active_Lifecycle_Receipt_MEDIANv0_5_0.json",
    "m050/extraction/audit/spend-envelopes/*",
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


def read_jsonl(path: Path, label: str, errors: list[str]) -> list[dict]:
    try:
        values = [
            json.loads(line)
            for line in path.read_text(encoding="utf-8").splitlines()
            if line.strip()
        ]
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"{label} is invalid: {exc}")
        return []
    if any(not isinstance(value, dict) for value in values):
        errors.append(f"{label} contains a non-object event")
        return []
    return values


def bound_file(relative: object, label: str, errors: list[str]) -> Path | None:
    if not isinstance(relative, str) or not relative:
        errors.append(f"{label} path is absent")
        return None
    supplied = Path(relative)
    if supplied.is_absolute() or ".." in supplied.parts:
        errors.append(f"{label} path is not repository-relative: {relative}")
        return None
    target = (ROOT / supplied).resolve()
    try:
        target.relative_to(ROOT)
    except ValueError:
        errors.append(f"{label} path escapes the repository: {relative}")
        return None
    if target == ROOT / "m051" or (ROOT / "m051") in target.parents:
        errors.append(f"{label} path enters prohibited m051: {relative}")
        return None
    if not target.is_file():
        errors.append(f"{label} file is missing: {relative}")
        return None
    return target


def validate_accepted_candidate_records(
    candidate_records: list[dict],
    expected_records: list[tuple[str, dict]],
    errors: list[str],
) -> None:
    """Require exact accepted-atom coverage and candidate-wide unique identifiers."""
    if len(candidate_records) != len(expected_records):
        errors.append(
            "accepted candidate record coverage drifted: "
            f"expected {len(expected_records)}, found {len(candidate_records)}"
        )

    identifiers: list[tuple[str, str]] = []
    for index, candidate in enumerate(candidate_records):
        identifier = next(
            (
                (field, value)
                for field in ("proposal_id", "atom_id", "record_id")
                if isinstance((value := candidate.get(field)), str) and value
            ),
            None,
        )
        if identifier is None:
            errors.append(f"accepted candidate record {index + 1} lacks an identifier")
        else:
            identifiers.append(identifier)

    if len({field for field, _value in identifiers}) > 1:
        errors.append("accepted candidate identifier field is inconsistent")
    if len(identifiers) != len({value for _field, value in identifiers}):
        errors.append("accepted candidate record identifiers are not candidate-wide unique")

    for index, (candidate, (chunk_id, expected)) in enumerate(
        zip(candidate_records, expected_records), start=1
    ):
        reconstructed = dict(candidate)
        traced_chunk = reconstructed.pop("accepted_chunk_id", None)
        source_identifier = reconstructed.pop("source_proposal_id", None)
        if (traced_chunk is None) != (source_identifier is None):
            errors.append(f"accepted candidate record {index} has incomplete identifier trace")
            continue
        if traced_chunk is not None:
            if traced_chunk != chunk_id:
                errors.append(f"accepted candidate record {index} has incorrect chunk trace")
            if expected.get("proposal_id") != source_identifier:
                errors.append(f"accepted candidate record {index} has incorrect source identifier trace")
            reconstructed["proposal_id"] = source_identifier
        if reconstructed != expected:
            errors.append(f"accepted candidate semantic coverage drifted at record {index}")


def validate_candidate_acceptance(
    source: dict,
    config: dict,
    calibration: dict,
    accepted_ids: list[str],
    accepted_evidence: list[dict],
    errors: list[str],
) -> None:
    """Validate the established candidate/report pair for a completed source."""
    binding = calibration.get("candidate_acceptance")
    if not isinstance(binding, dict):
        errors.append("completed source lacks a hash-bound candidate/report pair")
        return
    required_binding_keys = {"candidate", "candidate_sha256", "report", "report_sha256"}
    if set(binding) != required_binding_keys:
        errors.append("candidate acceptance binding shape drifted")

    candidate_path = bound_file(binding.get("candidate"), "accepted candidate", errors)
    report_path = bound_file(binding.get("report"), "acceptance report", errors)
    if candidate_path is None or report_path is None:
        return
    if sha256_file(candidate_path) != binding.get("candidate_sha256"):
        errors.append("accepted candidate hash binding drifted")
    if sha256_file(report_path) != binding.get("report_sha256"):
        errors.append("acceptance report hash binding drifted")

    report = read_json(report_path, errors)
    if (
        report.get("source_id") != source.get("id")
        or report.get("source_sha256") != config.get("source_sha256")
        or report.get("approval") is not True
        or report.get("accepted_chunk_ids") != accepted_ids
        or report.get("candidate_path") != binding.get("candidate")
        or report.get("candidate_sha256") != binding.get("candidate_sha256")
    ):
        errors.append("acceptance report source or candidate binding drifted")

    expected_records: list[tuple[str, dict]] = []
    expected_inputs: list[dict] = []
    target_dispositions = 0
    no_substantive = 0
    for item in accepted_evidence:
        chunk_id = item.get("chunk_id")
        outcome_path = bound_file(item.get("outcome"), f"candidate outcome {chunk_id}", errors)
        ledger_path = bound_file(item.get("run_ledger"), f"candidate ledger {chunk_id}", errors)
        if outcome_path is None or ledger_path is None:
            continue
        outcome = read_json(outcome_path, errors)
        dispositions = outcome.get("structured_proposal", {}).get("dispositions", [])
        if not isinstance(dispositions, list):
            errors.append(f"accepted outcome dispositions are invalid: {chunk_id}")
            continue
        target_dispositions += len(dispositions)
        for disposition in dispositions:
            if disposition.get("kind") == "no_substantive_claim":
                no_substantive += 1
            atoms = disposition.get("atoms", [])
            if not isinstance(atoms, list) or any(not isinstance(atom, dict) for atom in atoms):
                errors.append(f"accepted outcome atoms are invalid: {chunk_id}")
                continue
            expected_records.extend((chunk_id, atom) for atom in atoms)
        outcome_hash = sha256_file(outcome_path)
        matching = [
            event for event in read_jsonl(ledger_path, f"candidate ledger {chunk_id}", errors)
            if event.get("chunk_id") == chunk_id
            and event.get("state") == "review_passed"
            and event.get("outcome_sha256") == outcome_hash
        ]
        if len(matching) != 1:
            errors.append(f"candidate review evidence is not unique: {chunk_id}")
            continue
        expected_inputs.append({
            "chunk_id": chunk_id,
            "outcome_path": item.get("outcome"),
            "outcome_sha256": outcome_hash,
            "review_event_id": matching[0].get("event_id"),
            "review_event_outcome_sha256": matching[0].get("outcome_sha256"),
        })

    candidate_records = read_jsonl(candidate_path, "accepted candidate", errors)
    validate_accepted_candidate_records(candidate_records, expected_records, errors)
    if report.get("accepted_inputs") != expected_inputs:
        errors.append("acceptance report evidence coverage drifted")
    for field, expected in {
        "chunks": len(accepted_ids),
        "target_dispositions": target_dispositions,
        "candidate_atoms": len(expected_records),
        "no_substantive_claim_dispositions": no_substantive,
    }.items():
        if report.get(field) != expected:
            errors.append(f"acceptance report exact coverage drifted: {field}")


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


def is_live_file(path: Path) -> bool:
    return path.name not in IGNORED_NAMES and not (set(path.parts) & IGNORED_RUNTIME_DIRS)


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


def validate_live_topology(errors: list[str]) -> None:
    extraction = ROOT / "m050/extraction"
    active_dirs = {
        item.relative_to(extraction).parts[0]
        for item in extraction.rglob("*")
        if item.is_file() and is_live_file(item)
    }
    if active_dirs != LIVE_EXTRACTION_DIRS:
        errors.append(
            "live extraction topology drifted: "
            f"expected {sorted(LIVE_EXTRACTION_DIRS)}, found {sorted(active_dirs)}"
        )
    for item in extraction.rglob("*.md"):
        if not item.is_file() or not is_live_file(item):
            continue
        relative = item.relative_to(extraction)
        allowed = (
            relative.as_posix() in {
                "engine/README.md",
                "control/source-identities/README.md",
            }
            or relative.parts[:1] == ("calibration",)
            or relative.parts[:3] == ("control", "source-identities", "cards")
            or (relative.parts[:1] == ("evidence",) and "source" in relative.parts)
        )
        if not allowed:
            errors.append(f"unclassified process-facing Markdown: {item.relative_to(ROOT)}")
    if (ROOT / "m050/archive").exists():
        errors.append("retired m050/archive directory has returned")


def validate_human_evidence(errors: list[str]) -> None:
    reconstruction = HUMAN_EVIDENCE / "reconstruction"
    report_path = reconstruction / "M050_Human_Rulings_Reconstruction_Report_v0_1_MEDIANv0_5_0.json"
    report = read_json(report_path, errors)
    expected = {
        "coordinate_ledger": reconstruction / "M050_Human_Rulings_Legacy_Atom_Coordinate_Ledger_v0_1_MEDIANv0_5_0.jsonl",
        "reference_rewrite_map": reconstruction / "M050_Human_Rulings_Active_to_Legacy_Reference_Rewrite_Map_v0_1_MEDIANv0_5_0.json",
        "registry": reconstruction / "M050_Human_Rulings_Section_and_Field_Registry_v0_1_MEDIANv0_5_0.json",
    }
    if (
        report.get("passed") is not True
        or report.get("legacy_record_count") != 173
        or report.get("ruling_count") != 41
        or report.get("complete_ruling_coverage") is not True
    ):
        errors.append("Human Rulings reconstruction boundary drifted")
    for name, target in expected.items():
        binding = report.get(name, {})
        if (
            binding.get("path") != target.relative_to(ROOT).as_posix()
            or not target.is_file()
            or binding.get("sha256") != sha256_file(target)
        ):
            errors.append(f"Human Rulings reconstruction binding drifted: {name}")


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
    allowed_keys = {"order", "source_id", "label", "pre_candidate_acceptance_control"}
    for item in sequence:
        if not set(item) <= allowed_keys:
            errors.append(f"processing order duplicates source state: {item.get('source_id')}")
        if not item.get("label"):
            errors.append(f"processing order label is absent: {item.get('source_id')}")


def expected_status(state: dict) -> str:
    dashboard = state.get("dashboard", {})
    try:
        remaining_display = Decimal(state.get("spend", {}).get("remaining_usd", "")).quantize(
            Decimal("0.01"), rounding=ROUND_FLOOR
        )
    except Exception:
        remaining_display = ""
    return (
        "# MEDIAN COMPILE — v0.5.0\n\n"
        f"{dashboard.get('updated_human', '')}<br>\n\n"
        "<!-- Derived dashboard only; M050_Compile_State_MEDIANv0_5_0.json is authoritative. -->\n\n"
        f"**STATUS:** {dashboard.get('status', '')}<br>\n"
        f"**PHASE:** {dashboard.get('phase', '')}<br>\n"
        f"**SOURCE:** {dashboard.get('source', '')}<br>\n"
        f"**CHUNK:** {dashboard.get('chunk', '')}<br>\n"
        f"**NOW:** {dashboard.get('now', '')}<br>\n"
        f"**NEXT:** {dashboard.get('next', '')}<br>\n"
        f"**SPEND REMAINING:** ${remaining_display}\n"
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


def validate_spend_and_status(state: dict, errors: list[str]) -> None:
    state_spend = state.get("spend", {})
    if "record" in state_spend:
        errors.append("canonical spend points to a redundant successor spend file")
    try:
        authorized = Decimal(state_spend.get("authorized_usd", ""))
        cumulative = Decimal(state_spend.get("cumulative_spent_usd", ""))
        remaining = Decimal(state_spend.get("remaining_usd", ""))
        rounded = cumulative.quantize(Decimal("0.01"), rounding=ROUND_CEILING)
    except Exception:
        errors.append("canonical cumulative budget is not decimal")
    else:
        if state_spend.get("active") is not True:
            errors.append("canonical cumulative budget is inactive")
        if cumulative < 0 or authorized < 0 or remaining < 0 or authorized - cumulative != remaining:
            errors.append("canonical cumulative budget arithmetic is inconsistent")
        if state_spend.get("display_usd_rounded_up") != f"{rounded:.2f}":
            errors.append("dashboard cost is not rounded upward to the cent")

    validate_timestamp(state, errors)
    if STATUS.read_text(encoding="utf-8") != expected_status(state):
        errors.append("STATUS does not exactly mirror canonical compile state")


def validate_pending_identity_card(
    source: dict,
    registered: dict,
    calibration: dict,
    latest: object,
    errors: list[str],
) -> None:
    """Validate the existing pre-configuration identity-approval boundary."""
    expected_keys = {
        "identity_card",
        "identity_card_sha256",
        "identity_card_approval_pending",
        "offline_gate_passed",
    }
    if set(calibration) != expected_keys:
        errors.append("pending identity calibration state contains non-identity machinery")
    if calibration.get("offline_gate_passed") is not False:
        errors.append("pending identity state claims an offline extraction gate")
    if latest is not None:
        errors.append("pending identity state retains a provider attempt")
    if (
        source.get("accepted_chunk_ids") != []
        or source.get("rejected_chunk_id") is not None
        or source.get("whole_source_candidate_complete") is not False
    ):
        errors.append("pending identity source has an extraction boundary")

    card_path = bound_file(calibration.get("identity_card"), "pending identity card", errors)
    if card_path is None:
        return
    if sha256_file(card_path) != calibration.get("identity_card_sha256"):
        errors.append("pending identity card hash binding drifted")
    text = card_path.read_text(encoding="utf-8")
    for required in (
        "Status: `PENDING_AUTHOR_APPROVAL`",
        "Lifecycle state: `identity_card_proposed`",
        "Author/root of authority: Asa Wember",
        f"| Source ID | `{source.get('id')}` |",
        f"| Path | `{registered.get('path')}` |",
        f"| SHA-256 | `{registered.get('sha256')}` |",
    ):
        if required not in text:
            errors.append(f"pending identity card lacks required binding: {required}")


def validate_authority_state(
    source: dict[str, Any], authority: dict[str, Any], errors: list[str]
) -> None:
    for prohibited in (
        "google_sheets_interaction_authorized",
        "semantic_acceptance_authorized",
        "mapping_authorized",
        "reconciliation_authorized",
        "compiled_prose_authorized",
    ):
        if authority.get(prohibited) is not False:
            errors.append(f"prohibited authority is active: {prohibited}")
    if source.get("source_work_authorized") is not authority.get("source_work_authorized"):
        errors.append("source-work authority disagrees between source and authority state")
    if "provider_call_authorized" in authority:
        errors.append("canonical authority stores redundant transaction-level provider permission")
    if authority.get("source_work_authorized") is True and authority.get("repository_writes_authorized") is not True:
        errors.append("active source work lacks the one-writer repository grant")
    if source.get("whole_source_candidate_complete") is True:
        if authority.get("source_work_authorized") is not False:
            errors.append("completed source retains source-work authority")
        if authority.get("repository_writes_authorized") is not False:
            errors.append("completed source has not completed formal Stopdown")


def validate_atomic_extraction_profile(errors: list[str]) -> None:
    state = read_json(STATE, errors)
    if state.get("schema_version") != "M050-COMPILE-STATE-1.0":
        errors.append("canonical compile-state schema drifted")
    matrix = read_json(MATRIX, errors)
    order = read_json(ORDER, errors)
    matrix_by_id = {item.get("source_id"): item for item in matrix.get("sources", [])}
    order_by_id = {item.get("source_id"): item for item in order.get("sequence", [])}
    completed_ids = state.get("progress", {}).get("completed_source_ids", [])
    if len(completed_ids) != len(set(completed_ids)) or not set(completed_ids) <= set(matrix_by_id):
        errors.append("canonical completed-source progress is duplicate or unregistered")
    compile_scope_ids = {
        source_id for source_id, item in matrix_by_id.items() if item.get("in_compile_scope") is True
    }
    legacy_seed_ids = {
        source_id
        for source_id, item in matrix_by_id.items()
        if item.get("current_state") == "atomized_legacy_seed"
    }
    if not legacy_seed_ids <= set(completed_ids):
        errors.append("canonical progress omits an atomized legacy seed")
    outstanding_ids = compile_scope_ids - set(completed_ids)
    outstanding_pre = {
        source_id
        for source_id in outstanding_ids
        if matrix_by_id[source_id].get("processing_phase") == "pre_reconciliation_atomization"
    }
    outstanding_later = outstanding_ids - outstanding_pre
    derived_corpus = {
        "registered_sources": len(matrix_by_id),
        "atomic_compile_exclusions": len(matrix_by_id) - len(compile_scope_ids),
        "compile_scope_sources": len(compile_scope_ids),
        "atomized_legacy_seed_sources": len(legacy_seed_ids),
        "outstanding_compile_scope_sources": len(outstanding_ids),
        "outstanding_pre_reconciliation_sources": len(outstanding_pre),
        "outstanding_later_or_conditional_sources": len(outstanding_later),
        "whole_corpus_atomization_complete": not outstanding_ids,
    }
    if state.get("corpus") != derived_corpus:
        errors.append("canonical corpus vector disagrees with completed-source progress")
    next_outstanding = next(
        (
            item.get("source_id")
            for item in order.get("sequence", [])
            if item.get("source_id") in outstanding_ids
        ),
        None,
    )
    source = state.get("source", {})
    source_id = source.get("id")
    registered = matrix_by_id.get(source_id)
    ordered = order_by_id.get(source_id)
    if not registered or not ordered:
        errors.append("active source is not registered in the canonical matrix and order")
        registered = {}
        ordered = {}
    source_complete = source.get("whole_source_candidate_complete") is True
    if source_complete:
        if source_id not in completed_ids:
            errors.append("completed active source is absent from canonical progress")
    elif source_id != next_outstanding:
        errors.append("active source is not the next outstanding source in canonical order")
    if source.get("compile_ordinal") != ordered.get("order"):
        errors.append("active source compile ordinal drifted")
    if registered.get("in_compile_scope") is not True:
        errors.append("active source is outside compile scope")

    authority = state.get("authority", {})
    validate_authority_state(source, authority, errors)

    calibration = state.get("calibration", {})
    if "provider_call_authorized" in calibration:
        errors.append("calibration stores redundant transaction-level provider permission")
    if calibration.get("identity_card_approval_pending") is True:
        validate_pending_identity_card(
            source, registered, calibration, state.get("latest_provider_attempt"), errors
        )
        validate_spend_and_status(state, errors)
        return
    if calibration.get("offline_gate_passed") is not True:
        errors.append("active packet lacks a completed offline calibration gate")

    config_path = bound_file(calibration.get("configuration"), "active configuration", errors)
    if config_path is None:
        return
    config = read_json(config_path, errors)
    if config.get("schema_version") != "M050-EXTRACTION-MACHINE-CONFIG-0.1":
        errors.append("active configuration schema drifted")
    if config.get("source_id") != source_id:
        errors.append("active configuration source ID disagrees with canonical state")
    if config.get("source_path") != registered.get("path"):
        errors.append("active configuration source path disagrees with source registry")
    if config.get("source_sha256") != registered.get("sha256"):
        errors.append("active configuration source hash disagrees with source registry")
    if config.get("allowed_streams") != registered.get("output_streams"):
        errors.append("active configuration streams disagree with source registry")

    required_artifacts = {
        "identity_card", "block_manifest", "disposition_ledger",
        "chunk_plan", "prompt", "response_schema",
    }
    artifacts = config.get("artifacts", {})
    artifact_hashes = config.get("artifact_sha256", {})
    if set(artifacts) != required_artifacts or set(artifact_hashes) != required_artifacts:
        errors.append("active configuration artifact classes drifted")
    resolved_artifacts: dict[str, Path] = {}
    for name in sorted(required_artifacts):
        target = bound_file(artifacts.get(name), f"configuration artifact {name}", errors)
        if target is None:
            continue
        resolved_artifacts[name] = target
        if sha256_file(target) != artifact_hashes.get(name):
            errors.append(f"configuration artifact binding drifted: {name}")
    card = resolved_artifacts.get("identity_card")
    if card is not None:
        card_text = card.read_text(encoding="utf-8")
        if "Status: `APPROVED`" not in card_text or "Author/root of authority: Asa Wember" not in card_text:
            errors.append("active identity card is not explicitly Asa-approved")
    execution = config.get("execution", {})
    if execution != {
        "cadence": "sequential_one_call_review",
        "next_chunk_requires_substantive_review_of_prior_chunk": True,
    }:
        errors.append("active configuration cadence drifted")
    provider = config.get("provider", {})
    if provider.get("cache_required") is not True or provider.get("cache_ttl") != "1h":
        errors.append("active configuration does not require one-hour Claude caching")

    accepted_ids = source.get("accepted_chunk_ids", [])
    accepted_evidence = calibration.get("accepted_evidence", [])
    if [item.get("chunk_id") for item in accepted_evidence] != accepted_ids:
        errors.append("accepted chunk evidence does not exactly cover the canonical boundary")
    for item in accepted_evidence:
        chunk_id = item.get("chunk_id")
        outcome_path = bound_file(item.get("outcome"), f"accepted outcome {chunk_id}", errors)
        ledger_path = bound_file(item.get("run_ledger"), f"accepted ledger {chunk_id}", errors)
        if outcome_path is None or ledger_path is None:
            continue
        outcome = read_json(outcome_path, errors)
        if (
            outcome.get("source_id") != source_id
            or outcome.get("chunk_id") != chunk_id
            or outcome.get("mechanical_validation", {}).get("passed") is not True
        ):
            errors.append(f"accepted outcome boundary drifted: {chunk_id}")
        matching = [
            event for event in read_jsonl(ledger_path, f"accepted ledger {chunk_id}", errors)
            if event.get("chunk_id") == chunk_id and event.get("state") == "review_passed"
        ]
        if len(matching) != 1 or matching[0].get("outcome_sha256") != sha256_file(outcome_path):
            errors.append(f"accepted review binding drifted: {chunk_id}")

    if source.get("whole_source_candidate_complete") is True:
        validate_candidate_acceptance(
            source, config, calibration, accepted_ids, accepted_evidence, errors
        )

    freeze_path = bound_file(calibration.get("freeze"), "active freeze", errors)
    compatibility_path = bound_file(
        calibration.get("compatibility_receipt"), "active compatibility receipt", errors
    )
    packet_path = bound_file(calibration.get("pilot_packet"), "active pilot packet", errors)
    ledger_path = bound_file(calibration.get("run_ledger"), "active run ledger", errors)
    latest = state.get("latest_provider_attempt")
    outcome_path = (
        bound_file(calibration.get("latest_outcome"), "latest outcome", errors)
        if latest
        else None
    )
    if None in (freeze_path, compatibility_path, packet_path, ledger_path):
        return
    if latest and outcome_path is None:
        return

    freeze = read_json(freeze_path, errors)
    compatibility = read_json(compatibility_path, errors)
    packet = read_json(packet_path, errors)
    outcome = read_json(outcome_path, errors) if outcome_path else {}
    pilot_chunk_id = calibration.get("pilot_chunk_id")
    binding = freeze.get("binding", {})
    chunk_plan = resolved_artifacts.get("chunk_plan")
    prompt = resolved_artifacts.get("prompt")
    if (
        binding.get("source_id") != source_id
        or binding.get("pilot_chunk_id") != pilot_chunk_id
        or binding.get("configuration_sha256") != sha256_file(config_path)
        or chunk_plan is None
        or binding.get("chunk_plan_sha256") != sha256_file(chunk_plan)
        or prompt is None
        or binding.get("prompt_sha256") != sha256_file(prompt)
        or binding.get("pilot_packet_sha256") != packet.get("packet_sha256")
        or binding.get("pilot_packet_file_sha256") != sha256_file(packet_path)
        or (
            not source_complete
            and binding.get("engine_module_sha256") != sha256_file(ENGINE_MODULE)
        )
        or (
            not source_complete
            and binding.get("engine_tests_sha256") != sha256_file(ENGINE_TESTS)
        )
    ):
        errors.append("active freeze binding drifted")
    if "authority" in freeze:
        errors.append("freeze stores redundant transaction-level authority")
    if freeze.get("pilot", {}).get("cache_miss_call_ceiling_usd") != calibration.get("cache_miss_call_ceiling_usd"):
        errors.append("freeze call ceiling disagrees with canonical state")
    offline_tests = calibration.get("offline_tests_passed")
    if (
        freeze.get("offline_verification", {}).get("offline_tests_passed") != offline_tests
        or compatibility.get("offline_verification", {}).get("offline_tests_passed") != offline_tests
    ):
        errors.append("offline test count disagrees across canonical calibration evidence")
    if "authority_boundary" in compatibility:
        errors.append("compatibility evidence stores redundant transaction-level authority")

    packet_body = dict(packet)
    packet_hash = packet_body.pop("packet_sha256", None)
    canonical_packet = (json.dumps(packet_body, sort_keys=True, separators=(",", ":"), ensure_ascii=False) + "\n").encode("utf-8")
    if packet_hash != hashlib.sha256(canonical_packet).hexdigest():
        errors.append("active packet internal hash drifted")
    payload = packet.get("payload", {})
    if (
        packet.get("source_id") != source_id
        or packet.get("chunk_id") != pilot_chunk_id
        or packet.get("configuration_path") != calibration.get("configuration")
        or packet.get("configuration_sha256") != sha256_file(config_path)
        or payload.get("required_target_disposition_count") != len(payload.get("target_blocks", []))
    ):
        errors.append("active packet boundary drifted")

    events = read_jsonl(ledger_path, "active run ledger", errors)
    if latest:
        validation = outcome.get("mechanical_validation") or {}
        outcome_mechanical_passed = validation.get("passed")
        if outcome_mechanical_passed is None and outcome.get("capture_error"):
            outcome_mechanical_passed = False
        usage = outcome.get("usage", {})
        if (
            outcome.get("source_id") != source_id
            or outcome.get("chunk_id") != latest.get("chunk_id")
            or outcome_mechanical_passed is not latest.get("mechanical_passed")
            or outcome.get("http_status") != latest.get("http_status")
            or outcome.get("stop_reason") != latest.get("stop_reason")
            or usage.get("output_tokens") != latest.get("output_tokens")
            or usage.get("cache_creation_input_tokens") != latest.get("cache_creation_input_tokens")
            or usage.get("cache_read_input_tokens") != latest.get("cache_read_input_tokens")
            or outcome.get("cost", {}).get("total_usd") != latest.get("exact_cost_usd")
        ):
            errors.append("latest provider attempt disagrees with canonical state")
        if latest.get("review_state") == "review_failed" and source.get("rejected_chunk_id") != latest.get("chunk_id"):
            errors.append("rejected chunk boundary disagrees with the latest failed review")
        if (
            not events
            or events[-1].get("state") != latest.get("review_state")
            or events[-1].get("outcome_sha256") != sha256_file(outcome_path)
        ):
            errors.append("active run ledger disagrees with the latest outcome")
    elif events:
        errors.append("run ledger contains events but canonical state has no latest provider attempt")

    compatibility_binding = compatibility.get("binding", {})
    current_compatibility_bindings = {
        "configuration_sha256": sha256_file(config_path),
        "prompt_sha256": sha256_file(prompt) if prompt else None,
    }
    if not source_complete:
        current_compatibility_bindings.update({
            "engine_module_sha256": sha256_file(ENGINE_MODULE),
            "engine_tests_sha256": sha256_file(ENGINE_TESTS),
        })
    for key, expected in current_compatibility_bindings.items():
        if key in compatibility_binding and compatibility_binding.get(key) != expected:
            errors.append(f"compatibility binding drifted: {key}")
    replays = compatibility.get("replays", {})
    replay_paths = calibration.get("compatibility_replays", {})
    if set(replays) != set(replay_paths):
        errors.append("compatibility replay inventory drifted")
    for name, relative in replay_paths.items():
        target = bound_file(relative, f"compatibility replay {name}", errors)
        if target is not None and replays.get(name, {}).get("sha256") != sha256_file(target):
            errors.append(f"compatibility replay binding drifted: {name}")

    validate_spend_and_status(state, errors)


def validate_active_phase(errors: list[str]) -> None:
    """Single replaceable phase-specific validation seam."""
    state = read_json(STATE, errors)
    if not state.get("dashboard", {}).get("phase", "").startswith("Atomic extraction"):
        errors.append("canonical state does not name the active atomic-extraction profile")
        return
    validate_human_evidence(errors)
    validate_atomic_extraction_profile(errors)


def validate_operating_contract(errors: list[str]) -> None:
    if OVERRIDE.exists() or OVERRIDE.is_symlink():
        errors.append("AGENTS.override.md exists")
    text = AGENTS.read_text(encoding="utf-8")
    for heading in (
        "## Conservation of System",
        "## Task roles and phase handoff",
        "## Phase model",
        "## Canonical controls",
        "## Authority model",
        "## Active phase profile — atomic extraction",
        "## STATUS contract",
    ):
        if heading not in text:
            errors.append(f"AGENTS omits required structural section: {heading}")
    if len(text.encode("utf-8")) > 32 * 1024:
        errors.append("AGENTS exceeds the 32 KiB root-instruction discovery limit")
    for pattern in RETIRED_PATTERNS:
        for target in ROOT.glob(pattern):
            errors.append(f"retired supervisory file remains active: {target.relative_to(ROOT)}")


def validate_json_integrity(errors: list[str]) -> tuple[int, int]:
    json_count = 0
    jsonl_count = 0
    for target in (ROOT / "m050/extraction").rglob("*.json"):
        if not is_live_file(target):
            continue
        try:
            json.loads(target.read_text(encoding="utf-8"))
            json_count += 1
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"invalid JSON {target.relative_to(ROOT)}: {exc}")
    for target in (ROOT / "m050/extraction").rglob("*.jsonl"):
        if not is_live_file(target):
            continue
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
    validate_live_topology(errors)
    validate_source_registry(errors)
    validate_operating_contract(errors)
    validate_active_phase(errors)
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
    state = read_json(STATE, [])
    source = state.get("source", {})
    spend = state.get("spend", {})
    accepted = ", ".join(source.get("accepted_chunk_ids", [])) or "none"
    rejected = source.get("rejected_chunk_id") or "none"
    corpus = state.get("corpus", {})
    print(
        "- corpus: "
        f"{corpus.get('registered_sources')} / {corpus.get('compile_scope_sources')} / "
        f"{corpus.get('atomized_legacy_seed_sources')} / "
        f"{corpus.get('outstanding_compile_scope_sources')} = "
        f"{corpus.get('outstanding_pre_reconciliation_sources')} + "
        f"{corpus.get('outstanding_later_or_conditional_sources')}"
    )
    print(f"- frozen files: {frozen_count}; immutable accepted artifacts: {immutable_count}")
    print("- live extraction topology: 7 directories; retired process families absent")
    print("- Human Rulings evidence: 173 reconstructed records across 41 rulings")
    print(
        f"- active source: {source.get('label')} ({source.get('id')}); "
        f"accepted {accepted}; rejected/frozen {rejected}"
    )
    print(
        f"- spend: ${spend.get('cumulative_spent_usd')} exact; "
        f"${spend.get('remaining_usd')} remaining; "
        f"${spend.get('display_usd_rounded_up')} display"
    )
    print(f"- JSON integrity: {json_count} JSON files and {jsonl_count} JSONL files")
    if args.with_tests:
        print("- offline regression suite: pass")
    return 0


if __name__ == "__main__":
    sys.exit(main())
