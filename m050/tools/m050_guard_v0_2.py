#!/usr/bin/env python3
"""Verify Gate 4 integrity plus the active MEDIAN Gate 5 offline foundation."""

from __future__ import annotations

import argparse
import ast
import hashlib
import json
import pathlib
import re
import subprocess
import sys


REPO_ROOT = pathlib.Path(__file__).resolve().parents[2]
LEGACY_GUARD = REPO_ROOT / "m050/tools/m050_guard.py"
ACTIVE_INDEX = REPO_ROOT / "m050/extraction/control/M050_Active_Control_Index_v0_6_MEDIANv0_5_0.json"
IDENTITY_APPROVAL_RECEIPT = REPO_ROOT / "m050/extraction/audit/M050_Extraction_Gate_5_Legacy_Source_Identity_Approval_Receipt_v0_1_MEDIANv0_5_0.json"
LEGACY_REPLAY_RECEIPT = REPO_ROOT / "m050/extraction/audit/M050_Extraction_Gate_5_Legacy_Replay_Milestone_Receipt_v0_1_MEDIANv0_5_0.json"
HUMAN_RULINGS_RECEIPT = REPO_ROOT / "m050/extraction/audit/M050_Extraction_Gate_5_Human_Rulings_Reconstruction_Receipt_v0_1_MEDIANv0_5_0.json"
REPAIR_CLOSURE_RECEIPT = REPO_ROOT / "m050/extraction/audit/M050_Extraction_Gate_5_Legacy_Repair_Closure_Receipt_v0_1_MEDIANv0_5_0.json"
ENGINE_ROOT = REPO_ROOT / "m050/extraction/engine"
LOCK_PATH = ENGINE_ROOT / "requirements.lock"
SCHEMA_PATH = ENGINE_ROOT / "src/median_gate5/schemas/gate5-artifacts.schema.json"
REGRESSION_PATH = ENGINE_ROOT / "fixtures/regression/manifest.json"
IGNORED_PARTS = {"__pycache__", ".pytest_cache"}
PROVIDER_MODULES = {"openai", "anthropic"}
LOCK_REQUIREMENT = re.compile(r"^[A-Za-z0-9_.-]+==[^\s\\]+\s*\\$")
LOCK_HASH = re.compile(r"^--hash=sha256:[0-9a-f]{64}$")


def sha256_file(path: pathlib.Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def content_id(prefix: str, value: object) -> str:
    canonical = json.dumps(
        value, ensure_ascii=False, allow_nan=False, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")
    return f"{prefix}_{hashlib.sha256(canonical).hexdigest()[:24]}"


def engine_snapshot() -> tuple[int, str]:
    digest = hashlib.sha256()
    files = sorted(
        path
        for path in ENGINE_ROOT.rglob("*")
        if path.is_file()
        and not any(part in IGNORED_PARTS or part.endswith(".egg-info") for part in path.parts)
        and path.suffix != ".pyc"
    )
    for path in files:
        relative = path.relative_to(REPO_ROOT).as_posix()
        digest.update(relative.encode("utf-8") + b"\0" + sha256_file(path).encode("ascii") + b"\n")
    return len(files), digest.hexdigest()


def validate_active_index(errors: list[str]) -> None:
    try:
        index = json.loads(ACTIVE_INDEX.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"active control index cannot be read: {exc}")
        return
    if index.get("execution_state") != "GATE_5_LEGACY_MECHANICAL_REPAIR_OVERLAY_COMPLETE":
        errors.append("active control index has unexpected execution state")
    if index.get("provider_call_authorized") is not False:
        errors.append("active control index does not explicitly prohibit provider calls")
    if index.get("google_sheets_interaction_authorized") is not False:
        errors.append("active control index does not preserve the Google Sheets pause")
    overlay = index.get("repair_state", {})
    if (
        overlay.get("raw_replay_queue_records") != 24
        or overlay.get("mechanically_dispositioned_queue_records") != 24
        or overlay.get("unresolved_grounding_or_coordinate_repairs") != 0
    ):
        errors.append("active control index has an unexpected repair state")
    for control in index.get("current_controls", []):
        relative = control.get("path")
        if not isinstance(relative, str) or not relative:
            errors.append("active control entry lacks a path")
            continue
        target = REPO_ROOT / relative
        if relative.endswith("/"):
            if not target.is_dir():
                errors.append(f"missing active control directory: {relative}")
        elif not target.is_file():
            errors.append(f"missing active control file: {relative}")


def validate_identity_approval(errors: list[str]) -> int:
    try:
        aggregate = json.loads(IDENTITY_APPROVAL_RECEIPT.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"identity approval receipt cannot be read: {exc}")
        return 0
    if aggregate.get("status") != "FOUR_LEGACY_SOURCE_IDENTITIES_APPROVED":
        errors.append("identity approval receipt has unexpected status")
    if aggregate.get("author_decision") != "approve all four":
        errors.append("identity approval receipt does not preserve the exact author decision")
    if aggregate.get("authority") != "Asa Wember":
        errors.append("identity approval receipt lacks author authority")
    if aggregate.get("provider_call_authorized") is not False:
        errors.append("identity approval receipt does not prohibit provider calls")
    cards = aggregate.get("approved_cards", [])
    if not isinstance(cards, list) or len(cards) != 4:
        errors.append("identity approval receipt must bind exactly four approved cards")
        return 0
    seen_sources: set[str] = set()
    for entry in cards:
        source_id = entry.get("source_id")
        if not isinstance(source_id, str) or source_id in seen_sources:
            errors.append(f"invalid or duplicate approved source ID: {source_id}")
            continue
        seen_sources.add(source_id)
        card_path = REPO_ROOT / entry.get("path", "")
        try:
            card = json.loads(card_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"approved identity card cannot be read for {source_id}: {exc}")
            continue
        if sha256_file(card_path) != entry.get("sha256"):
            errors.append(f"approved identity card hash mismatch: {source_id}")
        if (
            card.get("source_id") != source_id
            or card.get("card_id") != entry.get("card_id")
            or card.get("status") != "approved"
            or card.get("version") != 3
        ):
            errors.append(f"approved identity card metadata mismatch: {source_id}")
        card_body = {key: value for key, value in card.items() if key != "card_id"}
        if card.get("card_id") != content_id("sic", card_body):
            errors.append(f"approved identity card content ID mismatch: {source_id}")
        receipt_values: dict[str, dict] = {}
        for key, prior_state, new_state in (
            ("review_receipt", "draft", "reviewed"),
            ("approval_receipt", "reviewed", "approved"),
        ):
            binding = entry.get(key, {})
            receipt_path = REPO_ROOT / binding.get("path", "")
            try:
                receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
            except (OSError, json.JSONDecodeError) as exc:
                errors.append(f"{key} cannot be read for {source_id}: {exc}")
                continue
            receipt_values[key] = receipt
            if sha256_file(receipt_path) != binding.get("sha256"):
                errors.append(f"{key} hash mismatch: {source_id}")
            receipt_body = {name: value for name, value in receipt.items() if name != "receipt_id"}
            if receipt.get("receipt_id") != binding.get("receipt_id") or receipt.get(
                "receipt_id"
            ) != content_id("tr", receipt_body):
                errors.append(f"{key} content ID mismatch: {source_id}")
            if (
                receipt.get("machine") != "identity_card"
                or receipt.get("prior_state") != prior_state
                or receipt.get("new_state") != new_state
                or receipt.get("authority") != "Asa Wember"
            ):
                errors.append(f"{key} transition metadata mismatch: {source_id}")
        reviewed = entry.get("review_receipt", {})
        reviewed_receipt = receipt_values.get("review_receipt", {})
        approval = receipt_values.get("approval_receipt", {})
        if card.get("supersedes_card_id") != reviewed_receipt.get("artifact_id"):
            errors.append(f"approved card does not supersede the reviewed receipt target: {source_id}")
        if approval.get("artifact_id") != card.get("card_id"):
            errors.append(f"approval receipt targets the wrong card: {source_id}")
        if approval.get("predecessor_receipt_hash") != reviewed.get("sha256"):
            errors.append(f"approval receipt predecessor hash mismatch: {source_id}")
    return len(seen_sources)


def validate_legacy_replay(errors: list[str]) -> tuple[int, int]:
    try:
        milestone = json.loads(LEGACY_REPLAY_RECEIPT.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"legacy replay milestone receipt cannot be read: {exc}")
        return 0, 0
    if milestone.get("status") != "DETERMINISTIC_REPLAY_PASSED_REPAIR_QUEUE_REQUIRED":
        errors.append("legacy replay milestone receipt has unexpected status")
    if milestone.get("provider_call_authorized") is not False:
        errors.append("legacy replay milestone receipt does not prohibit provider calls")
    if milestone.get("external_model_calls") != 0 or milestone.get("accounted_cost_cents") != 0:
        errors.append("legacy replay milestone must record zero calls and zero cost")
    sources = milestone.get("sources", [])
    if not isinstance(sources, list) or len(sources) != 4:
        errors.append("legacy replay milestone must bind exactly four source reports")
        return 0, 0
    total_records = 0
    total_queue = 0
    seen_sources: set[str] = set()
    for entry in sources:
        source_id = entry.get("source_id")
        if not isinstance(source_id, str) or source_id in seen_sources:
            errors.append(f"invalid or duplicate replay source ID: {source_id}")
            continue
        seen_sources.add(source_id)
        bound_values: dict[str, tuple[pathlib.Path, dict]] = {}
        for key in ("ledger", "report"):
            binding = entry.get(key, {})
            path = REPO_ROOT / binding.get("path", "")
            if not path.is_file():
                errors.append(f"missing legacy replay {key}: {source_id}")
                continue
            if sha256_file(path) != binding.get("sha256"):
                errors.append(f"legacy replay {key} hash mismatch: {source_id}")
            bound_values[key] = (path, binding)
        if "ledger" not in bound_values or "report" not in bound_values:
            continue
        report_path, _ = bound_values["report"]
        try:
            report = json.loads(report_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            errors.append(f"invalid legacy replay report for {source_id}: {exc}")
            continue
        report_body = {
            key: value
            for key, value in report.items()
            if key not in {"schema_version", "replay_id"}
        }
        if report.get("replay_id") != entry.get("replay_id") or report.get(
            "replay_id"
        ) != content_id("lr", report_body):
            errors.append(f"legacy replay report content ID mismatch: {source_id}")
        if (
            report.get("source_id") != source_id
            or report.get("passed") is not True
            or report.get("migration_ready") is not False
            or report.get("provider_calls") != 0
            or report.get("accounted_cost_cents") != 0
        ):
            errors.append(f"legacy replay report metadata mismatch: {source_id}")
        ledger_path, ledger_binding = bound_values["ledger"]
        ledger_records: list[dict] = []
        try:
            for line in ledger_path.read_text(encoding="utf-8").splitlines():
                ledger_records.append(json.loads(line))
        except json.JSONDecodeError as exc:
            errors.append(f"invalid legacy replay ledger for {source_id}: {exc}")
            continue
        if report.get("ledger", {}).get("sha256") != ledger_binding.get("sha256"):
            errors.append(f"legacy replay report ledger binding mismatch: {source_id}")
        if len(ledger_records) != report.get("record_count") or len(ledger_records) != entry.get(
            "records"
        ):
            errors.append(f"legacy replay record count mismatch: {source_id}")
        record_ids: set[str] = set()
        for record in ledger_records:
            record_body = {
                key: value
                for key, value in record.items()
                if key not in {"schema_version", "replay_record_id"}
            }
            if record.get("replay_record_id") != content_id("lrr", record_body):
                errors.append(f"legacy replay record content ID mismatch: {source_id}")
                break
            if record.get("source_id") != source_id:
                errors.append(f"legacy replay record source mismatch: {source_id}")
                break
            legacy_id = record.get("legacy_record_id")
            if not isinstance(legacy_id, str) or legacy_id in record_ids:
                errors.append(f"invalid or duplicate legacy replay record ID: {source_id}")
                break
            record_ids.add(legacy_id)
        queue = report.get("review_queue_ids", [])
        failures = report.get("grounding_failure_ids", [])
        if failures:
            errors.append(f"legacy replay contains grounding failures: {source_id}")
        if len(queue) != entry.get("repair_queue"):
            errors.append(f"legacy replay repair queue count mismatch: {source_id}")
        total_records += len(ledger_records)
        total_queue += len(queue)
    aggregate = milestone.get("aggregate", {})
    if total_records != 913 or total_records != aggregate.get("records"):
        errors.append("legacy replay aggregate record count mismatch")
    if total_queue != 24 or total_queue != aggregate.get("repair_queue_records"):
        errors.append("legacy replay aggregate repair queue count mismatch")
    if aggregate.get("grounding_failures") != 0:
        errors.append("legacy replay aggregate contains grounding failures")
    return total_records, total_queue


def validate_human_rulings_reconstruction(errors: list[str]) -> tuple[int, int, int]:
    try:
        receipt = json.loads(HUMAN_RULINGS_RECEIPT.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"Human Rulings reconstruction receipt cannot be read: {exc}")
        return 0, 0, 0
    if receipt.get("status") != "HUMAN_RULINGS_RECONSTRUCTION_PASSED":
        errors.append("Human Rulings reconstruction receipt has unexpected status")
    if receipt.get("provider_call_authorized") is not False:
        errors.append("Human Rulings reconstruction receipt does not prohibit provider calls")
    if receipt.get("google_sheets_interactions") != 0:
        errors.append("Human Rulings reconstruction receipt violates the Google Sheets pause")
    if receipt.get("external_model_calls") != 0 or receipt.get("accounted_cost_cents") != 0:
        errors.append("Human Rulings reconstruction must record zero calls and zero cost")

    artifacts = receipt.get("artifacts", {})
    loaded: dict[str, tuple[pathlib.Path, object]] = {}
    for key in (
        "section_and_field_registry",
        "legacy_atom_coordinate_ledger",
        "reference_rewrite_map",
        "machine_reconstruction_report",
        "human_readable_report",
    ):
        binding = artifacts.get(key, {})
        path = REPO_ROOT / binding.get("path", "")
        if not path.is_file():
            errors.append(f"missing Human Rulings artifact: {key}")
            continue
        if sha256_file(path) != binding.get("sha256"):
            errors.append(f"Human Rulings artifact hash mismatch: {key}")
        if path.suffix == ".json":
            try:
                loaded[key] = (path, json.loads(path.read_text(encoding="utf-8")))
            except json.JSONDecodeError as exc:
                errors.append(f"invalid Human Rulings JSON artifact {key}: {exc}")
        else:
            loaded[key] = (path, None)

    registry_value = loaded.get("section_and_field_registry")
    rewrite_value = loaded.get("reference_rewrite_map")
    report_value = loaded.get("machine_reconstruction_report")
    coordinate_binding = artifacts.get("legacy_atom_coordinate_ledger", {})
    coordinate_path = REPO_ROOT / coordinate_binding.get("path", "")
    if not registry_value or not rewrite_value or not report_value or not coordinate_path.is_file():
        return 0, 0, 0
    registry = registry_value[1]
    rewrite_map = rewrite_value[1]
    report = report_value[1]
    if not isinstance(registry, dict) or not isinstance(rewrite_map, dict) or not isinstance(report, dict):
        errors.append("Human Rulings reconstruction JSON roots must be objects")
        return 0, 0, 0

    for value, id_key, prefix, label in (
        (registry, "registry_id", "hrr", "registry"),
        (rewrite_map, "rewrite_map_id", "hrrm", "rewrite map"),
        (report, "reconstruction_id", "hrrp", "reconstruction report"),
    ):
        body = {key: item for key, item in value.items() if key not in {"schema_version", id_key}}
        if value.get(id_key) != content_id(prefix, body):
            errors.append(f"Human Rulings {label} content ID mismatch")

    sections = registry.get("sections", [])
    field_count = sum(len(section.get("fields", [])) for section in sections)
    if registry.get("ruling_count") != 41 or len(sections) != 41 or field_count != 348:
        errors.append("Human Rulings registry coverage mismatch")
    ruling_ids = [section.get("section_id") for section in sections]
    if len(ruling_ids) != len(set(ruling_ids)):
        errors.append("Human Rulings registry contains duplicate ruling IDs")
    for section in sections:
        for field in section.get("fields", []):
            body = {key: item for key, item in field.items() if key != "field_id"}
            if field.get("field_id") != content_id("hrf", body):
                errors.append("Human Rulings field content ID mismatch")
                break

    coordinates: list[dict] = []
    try:
        for line in coordinate_path.read_text(encoding="utf-8").splitlines():
            coordinates.append(json.loads(line))
    except json.JSONDecodeError as exc:
        errors.append(f"invalid Human Rulings coordinate ledger: {exc}")
        return len(sections), field_count, 0
    record_ids: set[str] = set()
    reference_rewrite_records = 0
    for coordinate in coordinates:
        body = {
            key: value
            for key, value in coordinate.items()
            if key not in {"schema_version", "coordinate_record_id"}
        }
        if coordinate.get("coordinate_record_id") != content_id("hrc", body):
            errors.append("Human Rulings coordinate content ID mismatch")
            break
        record_id = coordinate.get("legacy_record_id")
        if not isinstance(record_id, str) or record_id in record_ids:
            errors.append("Human Rulings coordinate ledger has duplicate or invalid record IDs")
            break
        record_ids.add(record_id)
        legacy_coordinate = coordinate.get("legacy_coordinate", {})
        if legacy_coordinate.get("ruling_id") and not legacy_coordinate.get("field_labels"):
            errors.append(f"Human Rulings atom lacks its labeled-field link: {record_id}")
            break
        if coordinate.get("coordinate_status") == "active_reference_rewrite":
            reference_rewrite_records += 1
            if coordinate.get("active_coordinate") is not None or not coordinate.get("reference_rewrite_ids"):
                errors.append(f"invalid reference-rewrite coordinate: {record_id}")
                break
    if len(coordinates) != 173 or len(record_ids) != 173 or reference_rewrite_records != 6:
        errors.append("Human Rulings legacy-coordinate coverage mismatch")

    rewrites = rewrite_map.get("rewrites", [])
    rewrite_ids = {rewrite.get("rewrite_id") for rewrite in rewrites}
    for rewrite in rewrites:
        body = {key: value for key, value in rewrite.items() if key != "rewrite_id"}
        if rewrite.get("rewrite_id") != content_id("hrrw", body):
            errors.append("Human Rulings reference rewrite content ID mismatch")
            break
    if (
        rewrite_map.get("rewrite_count") != 24
        or len(rewrites) != 24
        or len(rewrite_ids) != 24
        or rewrite_map.get("legacy_only_record_count") != 6
        or len(rewrite_map.get("legacy_only_record_ids", [])) != 6
    ):
        errors.append("Human Rulings reference-rewrite coverage mismatch")

    for key in ("registry", "coordinate_ledger", "reference_rewrite_map"):
        report_binding = report.get(key, {})
        artifact_key = {
            "registry": "section_and_field_registry",
            "coordinate_ledger": "legacy_atom_coordinate_ledger",
            "reference_rewrite_map": "reference_rewrite_map",
        }[key]
        receipt_binding = artifacts.get(artifact_key, {})
        if (
            report_binding.get("path") != receipt_binding.get("path")
            or report_binding.get("sha256") != receipt_binding.get("sha256")
        ):
            errors.append(f"Human Rulings report binding mismatch: {key}")
    if (
        report.get("passed") is not True
        or report.get("ruling_count") != 41
        or report.get("field_count") != 348
        or report.get("legacy_record_count") != 173
        or report.get("legacy_only_record_count") != 6
        or report.get("provider_calls") != 0
        or report.get("accounted_cost_cents") != 0
    ):
        errors.append("Human Rulings reconstruction report metadata mismatch")
    return len(sections), field_count, len(coordinates)


def validate_repair_closure(errors: list[str]) -> int:
    try:
        receipt = json.loads(REPAIR_CLOSURE_RECEIPT.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"legacy repair closure receipt cannot be read: {exc}")
        return 0
    if receipt.get("status") != "LEGACY_MECHANICAL_REPAIR_OVERLAY_COMPLETE":
        errors.append("legacy repair closure receipt has unexpected status")
    if receipt.get("provider_call_authorized") is not False:
        errors.append("legacy repair closure receipt does not prohibit provider calls")
    if receipt.get("google_sheets_interactions") != 0:
        errors.append("legacy repair closure receipt violates the Google Sheets pause")
    if receipt.get("external_model_calls") != 0 or receipt.get("accounted_cost_cents") != 0:
        errors.append("legacy repair closure must record zero calls and zero cost")
    active_binding = receipt.get("active_control_index", {})
    if (
        active_binding.get("path") != str(ACTIVE_INDEX.relative_to(REPO_ROOT))
        or active_binding.get("sha256") != sha256_file(ACTIVE_INDEX)
    ):
        errors.append("legacy repair closure active-control binding mismatch")
    verification = receipt.get("verification", {})
    snapshot_files, snapshot_digest = engine_snapshot()
    if (
        verification.get("engine_files") != snapshot_files
        or verification.get("engine_digest") != snapshot_digest
        or verification.get("artifact_schema_sha256") != sha256_file(SCHEMA_PATH)
        or verification.get("regression_manifest_sha256") != sha256_file(REGRESSION_PATH)
        or verification.get("gate_5_guard_sha256") != sha256_file(pathlib.Path(__file__))
    ):
        errors.append("legacy repair closure verification snapshot mismatch")

    artifacts = receipt.get("artifacts", {})
    paths: dict[str, pathlib.Path] = {}
    for key in (
        "compound_disposition_ledger",
        "compound_disposition_report",
        "occurrence_resolution",
        "repair_closure_report",
        "human_readable_report",
    ):
        binding = artifacts.get(key, {})
        path = REPO_ROOT / binding.get("path", "")
        paths[key] = path
        if not path.is_file():
            errors.append(f"missing legacy repair closure artifact: {key}")
        elif sha256_file(path) != binding.get("sha256"):
            errors.append(f"legacy repair closure artifact hash mismatch: {key}")
    if not all(path.is_file() for path in paths.values()):
        return 0
    try:
        compound_report = json.loads(paths["compound_disposition_report"].read_text(encoding="utf-8"))
        occurrence = json.loads(paths["occurrence_resolution"].read_text(encoding="utf-8"))
        closure = json.loads(paths["repair_closure_report"].read_text(encoding="utf-8"))
        compound_records = [
            json.loads(line)
            for line in paths["compound_disposition_ledger"].read_text(encoding="utf-8").splitlines()
        ]
    except json.JSONDecodeError as exc:
        errors.append(f"invalid legacy repair closure JSON: {exc}")
        return 0

    for value, id_key, prefix, label in (
        (compound_report, "compound_report_id", "lcdr", "compound report"),
        (occurrence, "occurrence_resolution_id", "lor", "occurrence resolution"),
        (closure, "repair_closure_id", "lrc", "repair closure"),
    ):
        body = {key: item for key, item in value.items() if key not in {"schema_version", id_key}}
        if value.get(id_key) != content_id(prefix, body):
            errors.append(f"legacy {label} content ID mismatch")

    compound_ids: set[str] = set()
    for record in compound_records:
        body = {
            key: value
            for key, value in record.items()
            if key not in {"schema_version", "compound_disposition_id"}
        }
        if record.get("compound_disposition_id") != content_id("lcd", body):
            errors.append("legacy compound disposition content ID mismatch")
            break
        record_id = record.get("legacy_record_id")
        if not isinstance(record_id, str) or record_id in compound_ids:
            errors.append("legacy compound disposition has duplicate or invalid record IDs")
            break
        compound_ids.add(record_id)
        checks = record.get("structural_checks", {})
        if not checks or not all(value is True for value in checks.values()):
            errors.append(f"legacy compound structural checks did not all pass: {record_id}")
            break
        if (
            record.get("preservation_disposition")
            != "preserve_as_one_indivisible_legacy_compound"
            or record.get("risk_tier") != 2
            or record.get("semantic_review_performed") is not False
            or record.get("legacy_record_modified") is not False
            or record.get("split_performed") is not False
        ):
            errors.append(f"legacy compound disposition metadata mismatch: {record_id}")
            break
    if len(compound_records) != 17 or len(compound_ids) != 17:
        errors.append("legacy compound disposition coverage mismatch")
    if (
        compound_report.get("record_count") != 17
        or compound_report.get("tier_2_semantic_review_required") != 17
        or compound_report.get("semantic_reviews_performed") != 0
        or compound_report.get("legacy_records_modified_or_split") != 0
        or compound_report.get("passed") is not True
    ):
        errors.append("legacy compound report metadata mismatch")
    ledger_binding = compound_report.get("ledger", {})
    receipt_ledger = artifacts.get("compound_disposition_ledger", {})
    if (
        ledger_binding.get("path") != receipt_ledger.get("path")
        or ledger_binding.get("sha256") != receipt_ledger.get("sha256")
    ):
        errors.append("legacy compound report ledger binding mismatch")

    if (
        occurrence.get("legacy_record_id") != "ATOM-MSID-DIRECT-0062"
        or occurrence.get("original_occurrence_count") != 38
        or occurrence.get("pinned_range_occurrence_count") != 2
        or occurrence.get("pinned_range_whole_line_occurrence_count") != 1
        or occurrence.get("selected_span", {}).get("start_line") != 288
        or occurrence.get("selected_span", {}).get("end_line") != 288
        or occurrence.get("risk_tier") != 2
        or occurrence.get("semantic_review_performed") is not False
        or occurrence.get("legacy_record_modified") is not False
        or occurrence.get("replay_record_modified") is not False
    ):
        errors.append("legacy occurrence resolution metadata mismatch")

    coverage = receipt.get("coverage", {})
    if (
        closure.get("passed") is not True
        or closure.get("legacy_record_count") != 913
        or closure.get("raw_replay_queue_count") != 24
        or closure.get("mechanically_dispositioned_queue_count") != 24
        or closure.get("unresolved_grounding_or_coordinate_repairs") != 0
        or closure.get("replay_ledgers_byte_identical") != 4
        or closure.get("replay_reports_byte_identical") != 4
        or closure.get("semantic_acceptance_performed") is not False
        or closure.get("layer_e_migration_started") is not False
        or closure.get("legacy_or_replay_records_modified") != 0
        or coverage.get("mechanically_dispositioned_queue_records") != 24
        or coverage.get("unresolved_grounding_or_coordinate_repairs") != 0
    ):
        errors.append("legacy repair closure coverage mismatch")
    closure_compound = closure.get("compound_disposition_report", {})
    receipt_compound = artifacts.get("compound_disposition_report", {})
    closure_occurrence = closure.get("occurrence_resolution", {})
    receipt_occurrence = artifacts.get("occurrence_resolution", {})
    if (
        closure_compound.get("path") != receipt_compound.get("path")
        or closure_compound.get("sha256") != receipt_compound.get("sha256")
        or closure_occurrence.get("path") != receipt_occurrence.get("path")
        or closure_occurrence.get("sha256") != receipt_occurrence.get("sha256")
    ):
        errors.append("legacy repair closure artifact binding mismatch")
    return len(compound_ids) + 7


def validate_lock(errors: list[str]) -> None:
    if not LOCK_PATH.is_file():
        errors.append("Gate 5 requirements lock is missing")
        return
    significant = [
        line.strip()
        for line in LOCK_PATH.read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.lstrip().startswith("#")
    ]
    if len(significant) % 2:
        errors.append("requirements lock has an incomplete requirement/hash pair")
        return
    for index in range(0, len(significant), 2):
        requirement = significant[index]
        hash_line = significant[index + 1]
        if not LOCK_REQUIREMENT.match(requirement):
            errors.append(f"unlocked or malformed requirement: {requirement}")
        if not LOCK_HASH.match(hash_line):
            errors.append(f"missing or malformed requirement hash: {hash_line}")
        name = requirement.split("==", 1)[0].lower().replace("_", "-")
        if name in PROVIDER_MODULES:
            errors.append(f"provider SDK is prohibited in offline-core lock: {name}")


def validate_json_controls(errors: list[str]) -> int:
    count = 0
    for path in (SCHEMA_PATH, REGRESSION_PATH):
        try:
            json.loads(path.read_text(encoding="utf-8"))
            count += 1
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"invalid Gate 5 JSON control {path.relative_to(REPO_ROOT)}: {exc}")
    return count


def validate_offline_imports(errors: list[str]) -> None:
    package_root = ENGINE_ROOT / "src/median_gate5"
    for path in sorted(package_root.glob("*.py")):
        try:
            tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        except (OSError, SyntaxError) as exc:
            errors.append(f"cannot parse offline core module {path.name}: {exc}")
            continue
        for node in ast.walk(tree):
            imported: str | None = None
            if isinstance(node, ast.Import):
                for alias in node.names:
                    if alias.name.split(".", 1)[0] in PROVIDER_MODULES:
                        imported = alias.name
                        break
            elif isinstance(node, ast.ImportFrom) and node.module:
                if node.module.split(".", 1)[0] in PROVIDER_MODULES:
                    imported = node.module
            if imported:
                errors.append(f"offline core imports provider module {imported}: {path.name}")


def run_legacy_guard(skip_archive: bool, work_order: pathlib.Path | None) -> int:
    command = [sys.executable, str(LEGACY_GUARD)]
    if skip_archive:
        command.append("--skip-archive")
    if work_order:
        command.extend(["--work-order", str(work_order)])
    result = subprocess.run(command, cwd=REPO_ROOT, text=True, capture_output=True, check=False)
    if result.stdout:
        print(result.stdout.rstrip())
    if result.stderr:
        print(result.stderr.rstrip(), file=sys.stderr)
    return result.returncode


def run_tests() -> int:
    python = REPO_ROOT / ".venv/bin/python"
    if not python.is_file():
        print("Gate 5 test environment is missing: .venv/bin/python", file=sys.stderr)
        return 1
    result = subprocess.run(
        [str(python), "-m", "pytest", "m050/extraction/engine/tests", "-q"],
        cwd=REPO_ROOT,
        check=False,
    )
    return result.returncode


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--work-order", type=pathlib.Path)
    parser.add_argument("--skip-archive", action="store_true")
    parser.add_argument("--with-tests", action="store_true")
    args = parser.parse_args()

    if run_legacy_guard(args.skip_archive, args.work_order):
        print("M050 GATE 5 GUARD: FAIL — Gate 4 guard failed")
        return 1

    errors: list[str] = []
    validate_active_index(errors)
    approved_identity_cards = validate_identity_approval(errors)
    replay_records, replay_queue = validate_legacy_replay(errors)
    ruling_sections, ruling_fields, ruling_coordinates = validate_human_rulings_reconstruction(errors)
    mechanically_dispositioned = validate_repair_closure(errors)
    validate_lock(errors)
    json_controls = validate_json_controls(errors)
    validate_offline_imports(errors)
    file_count, digest = engine_snapshot()

    if args.with_tests and run_tests():
        errors.append("Gate 5 offline regression suite failed")

    if errors:
        print("M050 GATE 5 GUARD: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    print("M050 GATE 5 GUARD: PASS")
    print(f"- engine files: {file_count}")
    print(f"- engine digest: {digest}")
    print(f"- parsed JSON controls: {json_controls}")
    print(f"- approved identity cards: {approved_identity_cards}")
    print(f"- replayed legacy records: {replay_records}")
    print(f"- replay repair queue: {replay_queue}")
    print(f"- reconstructed Human Rulings sections: {ruling_sections}")
    print(f"- reconstructed Human Rulings fields: {ruling_fields}")
    print(f"- Human Rulings legacy coordinates: {ruling_coordinates}")
    print(f"- mechanically dispositioned replay queue: {mechanically_dispositioned}/24")
    print("- unresolved grounding or coordinate repairs: 0")
    print("- offline provider imports: 0")
    print("- provider calls: prohibited")
    if args.with_tests:
        print("- offline regression suite: pass")
    return 0


if __name__ == "__main__":
    sys.exit(main())
