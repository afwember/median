from __future__ import annotations

from collections import Counter
import json
from pathlib import Path
import re
from typing import Any

from .canonical import canonical_json_bytes, content_id, sha256_bytes, sha256_file
from .errors import ContractError, IntegrityError
from .normalization import locate_quote
from .schema import validate_artifact


REPLAY_VERSION = "M050-LEGACY-REPLAY-0.1"
LINE_LOCATION = re.compile(r"^L(?P<start>[0-9]{5})-L(?P<end>[0-9]{5})$")


def _repo_path(repo_root: Path, relative: str) -> Path:
    target = (repo_root / relative).resolve()
    try:
        target.relative_to(repo_root.resolve())
    except ValueError as exc:
        raise IntegrityError(f"legacy replay binding escapes repository: {relative}") from exc
    if relative == "m051" or relative.startswith("m051/"):
        raise IntegrityError(f"m051 input is prohibited: {relative}")
    if not target.is_file():
        raise IntegrityError(f"legacy replay binding is not a file: {relative}")
    return target


def _require_binding(repo_root: Path, binding: dict[str, Any]) -> Path:
    path = _repo_path(repo_root, binding.get("path", ""))
    actual = sha256_file(path)
    if actual != binding.get("sha256"):
        raise IntegrityError(f"legacy replay binding hash mismatch: {binding.get('path', '')}")
    return path


def _read_jsonl(path: Path) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not line.strip():
            raise ContractError(f"blank JSONL line at {path}:{line_number}")
        value = json.loads(line)
        if not isinstance(value, dict):
            raise ContractError(f"JSONL record is not an object at {path}:{line_number}")
        records.append(value)
    return records


def canonical_jsonl_bytes(records: list[dict[str, Any]]) -> bytes:
    return b"".join(canonical_json_bytes(record) + b"\n" for record in records)


def _occurrences(text: str, quotation: str) -> list[tuple[int, int]]:
    matches: list[tuple[int, int]] = []
    start = 0
    while True:
        index = text.find(quotation, start)
        if index < 0:
            return matches
        matches.append((index, index + len(quotation)))
        start = index + 1


def _line_bounds(text: str, location: str) -> tuple[int, int] | None:
    match = LINE_LOCATION.fullmatch(location)
    if not match:
        return None
    start_line = int(match.group("start"))
    end_line = int(match.group("end"))
    lines = text.splitlines(keepends=True)
    if start_line < 1 or end_line < start_line or end_line > len(lines):
        return None
    return sum(len(line) for line in lines[: start_line - 1]), sum(
        len(line) for line in lines[:end_line]
    )


def _select_occurrence(
    text: str, quotation: str, location: str
) -> tuple[tuple[int, int] | None, int, bool]:
    matches = _occurrences(text, quotation)
    if len(matches) == 1:
        return matches[0], 1, False
    bounds = _line_bounds(text, location)
    if len(matches) > 1 and bounds is not None:
        bounded = [
            match
            for match in matches
            if match[0] >= bounds[0] and match[1] <= bounds[1]
        ]
        if len(bounded) == 1:
            return bounded[0], len(matches), True
    return None, len(matches), False


def _overlapping_blocks(
    blocks: list[dict[str, Any]], span: tuple[int, int]
) -> list[str]:
    start, end = span
    return [
        block["block_id"]
        for block in blocks
        if block.get("block_type") != "whitespace"
        and block["start"] < end
        and block["end"] > start
    ]


def replay_record(
    *,
    source_id: str,
    active_source_text: str,
    active_source_sha256: str,
    blocks: list[dict[str, Any]],
    legacy_record: dict[str, Any],
    legacy_source_text: str | None = None,
    legacy_source_sha256: str | None = None,
) -> dict[str, Any]:
    legacy_record_id = legacy_record.get("atom_id")
    location = legacy_record.get("source_location")
    quotation = legacy_record.get("exact_source_text")
    if not all(isinstance(value, str) and value for value in (legacy_record_id, location, quotation)):
        raise ContractError("legacy record requires non-empty atom_id, source_location, and exact_source_text")
    if legacy_record.get("source_id") != source_id:
        raise ContractError(f"legacy record source_id mismatch: {legacy_record_id}")

    span, occurrence_count, line_applied = _select_occurrence(
        active_source_text, quotation, location
    )
    block_ids: list[str] = []
    normalization_events: list[str] = []
    role = "active_frozen_source"
    source_sha256 = active_source_sha256
    if span is not None:
        block_ids = _overlapping_blocks(blocks, span)
        if not block_ids:
            status = "exact_active_unassigned"
            disposition = "grounding_failure"
        elif len(block_ids) == 1:
            status = (
                "exact_single_block_location_disambiguated"
                if line_applied
                else "exact_single_block"
            )
            disposition = "eligible"
        else:
            status = "exact_cross_block"
            disposition = "boundary_review_required"
    elif occurrence_count > 1:
        status = "exact_active_ambiguous"
        disposition = "occurrence_review_required"
    else:
        legacy_span = None
        legacy_occurrences = 0
        legacy_line_applied = False
        if legacy_source_text is not None:
            legacy_span, legacy_occurrences, legacy_line_applied = _select_occurrence(
                legacy_source_text, quotation, location
            )
        if legacy_span is not None:
            role = "legacy_extraction_source"
            source_sha256 = legacy_source_sha256 or ""
            occurrence_count = legacy_occurrences
            line_applied = legacy_line_applied
            status = "exact_legacy_source_only"
            disposition = "active_to_legacy_reference_rewrite_required"
        elif legacy_occurrences > 1:
            role = "legacy_extraction_source"
            source_sha256 = legacy_source_sha256 or ""
            occurrence_count = legacy_occurrences
            status = "exact_legacy_ambiguous"
            disposition = "occurrence_review_required"
        else:
            normalized: list[tuple[dict[str, Any], Any]] = []
            for block in blocks:
                try:
                    normalized.append((block, locate_quote(block["text"], quotation)))
                except Exception:
                    continue
            if len(normalized) == 1:
                block, located = normalized[0]
                block_ids = [block["block_id"]]
                normalization_events = list(located.transformations)
                status = "normalized_single_block"
                disposition = "eligible"
                occurrence_count = 1
            elif len(normalized) > 1:
                block_ids = [block["block_id"] for block, _ in normalized]
                status = "normalized_active_ambiguous"
                disposition = "occurrence_review_required"
                occurrence_count = len(normalized)
            else:
                status = "not_grounded"
                disposition = "grounding_failure"
                occurrence_count = 0

    body = {
        "legacy_record_id": legacy_record_id,
        "source_id": source_id,
        "source_location": location,
        "quote_sha256": sha256_bytes(quotation.encode("utf-8")),
        "grounding_source_role": role,
        "grounding_source_sha256": source_sha256,
        "grounding_status": status,
        "block_ids": block_ids,
        "source_occurrence_count": occurrence_count,
        "line_location_applied": line_applied,
        "normalization_events": normalization_events,
        "migration_disposition": disposition,
    }
    result = {
        "schema_version": "M050-LEGACY-REPLAY-RECORD-0.1",
        "replay_record_id": content_id("lrr", body),
        **body,
    }
    validate_artifact("legacy_replay_record", result)
    return result


def build_legacy_replay(
    *,
    repo_root: Path,
    card: dict[str, Any],
    card_path: Path,
    block_manifest: dict[str, Any],
    block_manifest_path: Path,
    ledger_relative_path: str,
) -> tuple[bytes, dict[str, Any]]:
    repo_root = repo_root.resolve()
    validate_artifact("source_identity_card_v0_2", card)
    validate_artifact("block_manifest", block_manifest)
    if card.get("status") != "approved":
        raise ContractError("legacy replay requires an approved source identity card")
    if card.get("source_id") != block_manifest.get("source_id"):
        raise ContractError("identity card and block manifest source IDs differ")
    if card.get("source_sha256") != block_manifest.get("source_sha256"):
        raise ContractError("identity card and block manifest source hashes differ")

    expected_card = _repo_path(repo_root, str(card_path.resolve().relative_to(repo_root)))
    expected_block = _require_binding(repo_root, card["block_manifest_binding"])
    if expected_card != card_path.resolve():
        raise IntegrityError("supplied identity card path does not resolve inside the repository")
    if expected_block != block_manifest_path.resolve():
        raise IntegrityError("supplied block manifest does not match the card binding")

    active_source = _repo_path(repo_root, card["source_path"])
    if sha256_file(active_source) != card["source_sha256"]:
        raise IntegrityError("active source hash does not match the approved identity card")
    candidate_binding = card["legacy_extraction"]["candidate"]
    report_binding = card["legacy_extraction"]["acceptance_report"]
    candidate_path = _require_binding(repo_root, candidate_binding)
    acceptance_path = _require_binding(repo_root, report_binding)
    acceptance = json.loads(acceptance_path.read_text(encoding="utf-8"))
    if not isinstance(acceptance, dict):
        raise ContractError("legacy acceptance report root must be an object")
    if acceptance.get("source_id") != card["source_id"]:
        raise ContractError("legacy acceptance report source_id mismatch")
    reported_candidate_hash = acceptance.get("candidate_sha256") or acceptance.get(
        "candidate_atoms_sha256"
    )
    if reported_candidate_hash != candidate_binding["sha256"]:
        raise IntegrityError("legacy acceptance report candidate hash mismatch")

    legacy_source_text = None
    legacy_source_sha256 = None
    source_bindings = card["legacy_extraction"]["source_bindings"]
    for binding in source_bindings:
        source_path = _require_binding(repo_root, binding)
        if binding["role"] == "legacy_extraction_source":
            legacy_source_text = source_path.read_text(encoding="utf-8", errors="strict")
            legacy_source_sha256 = binding["sha256"]

    records = _read_jsonl(candidate_path)
    expected_count = card["legacy_extraction"]["record_count"]
    if len(records) != expected_count:
        raise IntegrityError(
            f"legacy candidate record count mismatch: expected {expected_count}, found {len(records)}"
        )
    record_ids = [record.get("atom_id") for record in records]
    if any(not isinstance(record_id, str) or not record_id for record_id in record_ids):
        raise ContractError("legacy candidate contains an empty or non-string atom_id")
    if len(record_ids) != len(set(record_ids)):
        raise ContractError("legacy candidate contains duplicate atom_id values")
    distinct_locations = {record.get("source_location") for record in records}
    if len(distinct_locations) != card["legacy_extraction"]["distinct_source_locations"]:
        raise IntegrityError("legacy candidate distinct source-location count mismatch")

    active_text = active_source.read_text(encoding="utf-8", errors="strict")
    ledger = [
        replay_record(
            source_id=card["source_id"],
            active_source_text=active_text,
            active_source_sha256=card["source_sha256"],
            blocks=block_manifest["blocks"],
            legacy_record=record,
            legacy_source_text=legacy_source_text,
            legacy_source_sha256=legacy_source_sha256,
        )
        for record in records
    ]
    ledger_bytes = canonical_jsonl_bytes(ledger)
    status_counts = dict(sorted(Counter(item["grounding_status"] for item in ledger).items()))
    disposition_counts = dict(
        sorted(Counter(item["migration_disposition"] for item in ledger).items())
    )
    grounding_failures = [
        item["legacy_record_id"]
        for item in ledger
        if item["migration_disposition"] == "grounding_failure"
    ]
    review_queue = [
        item["legacy_record_id"]
        for item in ledger
        if item["migration_disposition"] != "eligible"
    ]
    ledger_binding = {
        "path": ledger_relative_path,
        "sha256": sha256_bytes(ledger_bytes),
        "role": "deterministic_legacy_replay_ledger",
    }
    body = {
        "replay_version": REPLAY_VERSION,
        "source_id": card["source_id"],
        "identity_card": {
            "path": str(card_path.resolve().relative_to(repo_root)),
            "sha256": sha256_file(card_path),
            "role": "approved_source_identity_card",
        },
        "block_manifest": card["block_manifest_binding"],
        "legacy_candidate": candidate_binding,
        "legacy_acceptance_report": report_binding,
        "source_bindings": source_bindings,
        "ledger": ledger_binding,
        "record_count": len(ledger),
        "distinct_legacy_record_ids": len(record_ids),
        "status_counts": status_counts,
        "disposition_counts": disposition_counts,
        "review_queue_ids": review_queue,
        "grounding_failure_ids": grounding_failures,
        "input_integrity_passed": True,
        "passed": not grounding_failures,
        "migration_ready": not review_queue,
        "provider_calls": 0,
        "accounted_cost_cents": 0,
    }
    report = {
        "schema_version": "M050-LEGACY-REPLAY-REPORT-0.1",
        "replay_id": content_id("lr", body),
        **body,
    }
    validate_artifact("legacy_replay_report", report)
    return ledger_bytes, report
