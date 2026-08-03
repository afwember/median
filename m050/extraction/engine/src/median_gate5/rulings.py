from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from difflib import SequenceMatcher
import json
from pathlib import Path
import re
from typing import Any

import yaml

from .canonical import canonical_json_bytes, content_id, sha256_bytes, sha256_file
from .errors import ContractError, IntegrityError
from .legacy import canonical_jsonl_bytes, select_occurrence
from .schema import validate_artifact


RECONSTRUCTION_VERSION = "M050-HUMAN-RULINGS-RECONSTRUCTION-0.1"
HEADING = re.compile(r"^(?P<marks>#{1,6})\s+(?P<title>.+?)\s*$")
RULING_HEADING = re.compile(r"^(?P<id>HR-[A-Z0-9-]+)\s+—\s+(?P<title>.+)$")
OPEN_HEADING = re.compile(r"^(?P<id>OPEN-[A-Z0-9-]+)\s+—\s+(?P<title>.+)$")
FIELD = re.compile(r"^- \*\*(?P<label>[^*]+):\*\*\s*(?P<value>.*?)(?:\r?\n)?$")
REQUIRED_RULING_FIELDS = {
    "Date",
    "Class",
    "Status",
    "Normalized ruling",
    "Authority effect",
    "Affected sources",
    "Semantic scope",
}
EXACT_HUMAN_LABELS = {"Exact statement", "Exact statements", "Exact question"}


@dataclass(frozen=True)
class FieldSpan:
    label: str
    value: str
    start: int
    end: int
    value_start: int
    value_end: int
    start_line: int
    end_line: int


@dataclass(frozen=True)
class SectionSpan:
    section_id: str
    kind: str
    level: int
    title: str
    heading: str
    start: int
    end: int
    start_line: int
    end_line: int
    fields: tuple[FieldSpan, ...]


def _line_data(text: str) -> tuple[list[str], list[int]]:
    lines = text.splitlines(keepends=True)
    offsets = [0]
    for line in lines:
        offsets.append(offsets[-1] + len(line))
    return lines, offsets


def _slug(title: str) -> str:
    value = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
    return value or "untitled"


def parse_ledger(text: str) -> list[SectionSpan]:
    lines, offsets = _line_data(text)
    headings: list[tuple[int, int, int, str, str, str]] = []
    for index, line in enumerate(lines):
        match = HEADING.match(line.rstrip("\r\n"))
        if not match:
            continue
        level = len(match.group("marks"))
        heading_title = match.group("title")
        ruling = RULING_HEADING.fullmatch(heading_title)
        open_item = OPEN_HEADING.fullmatch(heading_title)
        if ruling:
            section_id = ruling.group("id")
            title = ruling.group("title")
            kind = "ruling"
        elif open_item:
            section_id = open_item.group("id")
            title = open_item.group("title")
            kind = "open_item"
        else:
            section_id = f"REGION-{_slug(heading_title).upper()}"
            title = heading_title
            kind = "document_region"
        headings.append((index, offsets[index], level, section_id, kind, title))

    sections: list[SectionSpan] = []
    for position, (line_index, start, level, section_id, kind, title) in enumerate(headings):
        end = len(text)
        for next_heading in headings[position + 1 :]:
            if next_heading[2] <= level:
                end = next_heading[1]
                break
        field_starts: list[tuple[int, int, str, int]] = []
        for field_index in range(line_index + 1, len(lines)):
            field_start = offsets[field_index]
            if field_start >= end:
                break
            match = FIELD.match(lines[field_index])
            if not match:
                continue
            field_starts.append(
                (
                    field_index,
                    field_start,
                    match.group("label"),
                    field_start + match.start("value"),
                )
            )
        fields: list[FieldSpan] = []
        for field_position, (field_index, field_start, label, raw_value_start) in enumerate(field_starts):
            raw_field_end = (
                field_starts[field_position + 1][1]
                if field_position + 1 < len(field_starts)
                else end
            )
            value_chunk = text[raw_value_start:raw_field_end]
            left_trim = len(value_chunk) - len(value_chunk.lstrip())
            right_trim = len(value_chunk) - len(value_chunk.rstrip())
            value_start = raw_value_start + left_trim
            value_end = raw_field_end - right_trim
            if value_end <= value_start:
                raise IntegrityError(f"empty labeled field {section_id}:{label}")
            field_end = value_end
            fields.append(
                FieldSpan(
                    label=label,
                    value=text[value_start:value_end],
                    start=field_start,
                    end=field_end,
                    value_start=value_start,
                    value_end=value_end,
                    start_line=field_index + 1,
                    end_line=text.count("\n", 0, max(value_start, value_end - 1)) + 1,
                )
            )
        end_line = text.count("\n", 0, max(start, end - 1)) + 1
        sections.append(
            SectionSpan(
                section_id=section_id,
                kind=kind,
                level=level,
                title=title,
                heading=lines[line_index].rstrip("\r\n"),
                start=start,
                end=end,
                start_line=line_index + 1,
                end_line=end_line,
                fields=tuple(fields),
            )
        )
    return sections


def _ruling_sections(sections: list[SectionSpan]) -> list[SectionSpan]:
    return [section for section in sections if section.kind == "ruling"]


def _validate_ruling_topology(sections: list[SectionSpan], *, source_role: str) -> None:
    rulings = _ruling_sections(sections)
    if len(rulings) != 41:
        raise IntegrityError(f"{source_role} ledger must contain exactly 41 HR sections")
    ids = [section.section_id for section in rulings]
    if len(ids) != len(set(ids)):
        raise IntegrityError(f"{source_role} ledger contains duplicate HR IDs")
    for section in rulings:
        labels = [field.label for field in section.fields]
        missing = sorted(REQUIRED_RULING_FIELDS - set(labels))
        if missing:
            raise IntegrityError(
                f"{source_role} {section.section_id} lacks required fields: {', '.join(missing)}"
            )
        exact_count = sum(label in EXACT_HUMAN_LABELS for label in labels)
        if exact_count != 1:
            raise IntegrityError(
                f"{source_role} {section.section_id} must contain exactly one exact-human field"
            )
        if len(labels) != len(set(labels)):
            raise IntegrityError(f"{source_role} {section.section_id} repeats a field label")


def _smallest_section(sections: list[SectionSpan], span: tuple[int, int]) -> SectionSpan:
    start, end = span
    candidates = [
        section
        for section in sections
        if section.start <= start and section.end >= end
    ]
    if not candidates:
        raise IntegrityError(f"source span {start}:{end} is outside every ledger section")
    return max(candidates, key=lambda section: section.level)


def _field_labels(section: SectionSpan, span: tuple[int, int]) -> list[str]:
    start, end = span
    return [
        field.label
        for field in section.fields
        if field.value_start < end and field.value_end > start
    ]


def _line_range(text: str, span: tuple[int, int]) -> tuple[int, int]:
    start, end = span
    return text.count("\n", 0, start) + 1, text.count("\n", 0, max(start, end - 1)) + 1


def _coordinate(
    *, text: str, source_role: str, source_sha256: str, sections: list[SectionSpan], span: tuple[int, int]
) -> dict[str, Any]:
    section = _smallest_section(sections, span)
    start_line, end_line = _line_range(text, span)
    return {
        "source_role": source_role,
        "source_sha256": source_sha256,
        "start": span[0],
        "end": span[1],
        "start_line": start_line,
        "end_line": end_line,
        "section_id": section.section_id,
        "section_kind": section.kind,
        "ruling_id": section.section_id if section.kind == "ruling" else None,
        "field_labels": _field_labels(section, span),
    }


def _section_dict(section: SectionSpan, text: str) -> dict[str, Any]:
    fields = []
    for ordinal, field in enumerate(section.fields, start=1):
        raw_line = text[field.start : field.end]
        body = {
            "ordinal": ordinal,
            "label": field.label,
            "value": field.value,
            "start": field.start,
            "end": field.end,
            "value_start": field.value_start,
            "value_end": field.value_end,
            "start_line": field.start_line,
            "end_line": field.end_line,
            "raw_sha256": sha256_bytes(raw_line.encode("utf-8")),
            "value_sha256": sha256_bytes(field.value.encode("utf-8")),
        }
        fields.append({"field_id": content_id("hrf", body), **body})
    body = {
        "section_id": section.section_id,
        "section_kind": section.kind,
        "title": section.title,
        "heading": section.heading,
        "start": section.start,
        "end": section.end,
        "start_line": section.start_line,
        "end_line": section.end_line,
        "raw_sha256": sha256_bytes(text[section.start : section.end].encode("utf-8")),
        "fields": fields,
    }
    return {"registry_section_id": content_id("hrs", body), **body}


def _read_jsonl(path: Path) -> list[dict[str, Any]]:
    values: list[dict[str, Any]] = []
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not line.strip():
            raise ContractError(f"blank JSONL line at {path}:{line_number}")
        value = json.loads(line)
        if not isinstance(value, dict):
            raise ContractError(f"non-object JSONL record at {path}:{line_number}")
        values.append(value)
    return values


def _bound_file(repo_root: Path, binding: dict[str, Any]) -> Path:
    path = (repo_root / binding.get("path", "")).resolve()
    try:
        path.relative_to(repo_root)
    except ValueError as exc:
        raise IntegrityError("Human Rulings binding escapes the repository") from exc
    if not path.is_file() or sha256_file(path) != binding.get("sha256"):
        raise IntegrityError(f"Human Rulings binding is missing or changed: {binding.get('path', '')}")
    return path


def _rewrite_lines(
    *,
    legacy_text: str,
    active_text: str,
    legacy_sections: list[SectionSpan],
    active_sections: list[SectionSpan],
    legacy_sha256: str,
    active_sha256: str,
    legacy_records: list[dict[str, Any]],
    legacy_spans: dict[str, tuple[int, int]],
    replay_by_id: dict[str, dict[str, Any]],
) -> list[dict[str, Any]]:
    legacy_lines, legacy_offsets = _line_data(legacy_text)
    active_lines, active_offsets = _line_data(active_text)
    matcher = SequenceMatcher(a=legacy_lines, b=active_lines, autojunk=False)
    rewrites: list[dict[str, Any]] = []
    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        if tag == "equal":
            continue
        if tag != "replace" or (i2 - i1) != (j2 - j1):
            raise IntegrityError("reference rewrite must preserve one-for-one line topology")
        for legacy_index, active_index in zip(range(i1, i2), range(j1, j2), strict=True):
            legacy_raw = legacy_lines[legacy_index].rstrip("\r\n")
            active_raw = active_lines[active_index].rstrip("\r\n")
            legacy_span = (legacy_offsets[legacy_index], legacy_offsets[legacy_index] + len(legacy_raw))
            active_span = (active_offsets[active_index], active_offsets[active_index] + len(active_raw))
            covered = sorted(
                record["atom_id"]
                for record in legacy_records
                if legacy_spans[record["atom_id"]][0] < legacy_span[1]
                and legacy_spans[record["atom_id"]][1] > legacy_span[0]
            )
            legacy_only = [
                record_id
                for record_id in covered
                if replay_by_id[record_id]["migration_disposition"]
                == "active_to_legacy_reference_rewrite_required"
            ]
            body = {
                "rewrite_kind": "gate_4_source_identity_reference_rewrite",
                "legacy_text": legacy_raw,
                "active_text": active_raw,
                "legacy_line_sha256": sha256_bytes(legacy_raw.encode("utf-8")),
                "active_line_sha256": sha256_bytes(active_raw.encode("utf-8")),
                "legacy_coordinate": _coordinate(
                    text=legacy_text,
                    source_role="legacy_extraction_source",
                    source_sha256=legacy_sha256,
                    sections=legacy_sections,
                    span=legacy_span,
                ),
                "active_coordinate": _coordinate(
                    text=active_text,
                    source_role="active_frozen_source",
                    source_sha256=active_sha256,
                    sections=active_sections,
                    span=active_span,
                ),
                "covered_legacy_record_ids": covered,
                "resolved_legacy_only_record_ids": legacy_only,
            }
            rewrites.append({"rewrite_id": content_id("hrrw", body), **body})
    return rewrites


def build_human_rulings_reconstruction(
    *,
    repo_root: Path,
    card: dict[str, Any],
    card_path: Path,
    replay_ledger_path: Path,
    replay_report: dict[str, Any],
    replay_report_path: Path,
    migration_receipt_path: Path,
    registry_relative_path: str,
    coordinate_ledger_relative_path: str,
    rewrite_map_relative_path: str,
) -> tuple[dict[str, Any], bytes, dict[str, Any], dict[str, Any]]:
    repo_root = repo_root.resolve()
    validate_artifact("source_identity_card_v0_2", card)
    validate_artifact("legacy_replay_report", replay_report)
    if card.get("status") != "approved" or card.get("source_id") != "M050-SRC-HUMAN-RULINGS-001":
        raise ContractError("reconstruction requires the approved Human Rulings identity card")
    if replay_report.get("source_id") != card["source_id"] or replay_report.get("passed") is not True:
        raise ContractError("reconstruction requires the passed Human Rulings replay report")
    for supplied_path, label in (
        (card_path, "identity card"),
        (replay_ledger_path, "replay ledger"),
        (replay_report_path, "replay report"),
        (migration_receipt_path, "migration receipt"),
    ):
        try:
            supplied_path.resolve().relative_to(repo_root)
        except ValueError as exc:
            raise IntegrityError(f"Human Rulings {label} escapes the repository") from exc
        if not supplied_path.is_file():
            raise IntegrityError(f"Human Rulings {label} is not a file")
    if sha256_file(replay_ledger_path) != replay_report["ledger"]["sha256"]:
        raise IntegrityError("Human Rulings replay ledger hash mismatch")
    if replay_report["ledger"]["path"] != str(replay_ledger_path.resolve().relative_to(repo_root)):
        raise IntegrityError("supplied Human Rulings replay ledger path differs from its report binding")

    source_bindings = {binding["role"]: binding for binding in card["legacy_extraction"]["source_bindings"]}
    active_binding = source_bindings.get("active_frozen_source")
    legacy_binding = source_bindings.get("legacy_extraction_source")
    if not active_binding or not legacy_binding:
        raise ContractError("Human Rulings card must bind active and legacy source roles")
    active_path = _bound_file(repo_root, active_binding)
    legacy_path = _bound_file(repo_root, legacy_binding)
    candidate_path = _bound_file(repo_root, card["legacy_extraction"]["candidate"])
    active_text = active_path.read_text(encoding="utf-8")
    legacy_text = legacy_path.read_text(encoding="utf-8")
    active_sections = parse_ledger(active_text)
    legacy_sections = parse_ledger(legacy_text)
    _validate_ruling_topology(active_sections, source_role="active")
    _validate_ruling_topology(legacy_sections, source_role="legacy")
    active_rulings = _ruling_sections(active_sections)
    legacy_rulings = _ruling_sections(legacy_sections)
    if [section.section_id for section in active_rulings] != [section.section_id for section in legacy_rulings]:
        raise IntegrityError("active and legacy ruling ID topology differs")
    if [[field.label for field in section.fields] for section in active_rulings] != [
        [field.label for field in section.fields] for section in legacy_rulings
    ]:
        raise IntegrityError("active and legacy ruling field topology differs")

    migration_receipt = yaml.safe_load(migration_receipt_path.read_text(encoding="utf-8"))
    if not isinstance(migration_receipt, dict) or migration_receipt.get("status") != "EXECUTED":
        raise ContractError("Gate 4 source-identity migration receipt is not executed")
    if migration_receipt.get("originals_preserved") is not True or migration_receipt.get("deletions_performed") != 0:
        raise IntegrityError("Gate 4 migration receipt does not preserve the required source boundary")

    legacy_records = _read_jsonl(candidate_path)
    replay_records = _read_jsonl(replay_ledger_path)
    replay_by_id = {record["legacy_record_id"]: record for record in replay_records}
    if len(replay_by_id) != len(replay_records) or len(legacy_records) != 173:
        raise IntegrityError("Human Rulings reconstruction requires 173 distinct replay records")
    if {record["atom_id"] for record in legacy_records} != set(replay_by_id):
        raise IntegrityError("legacy candidate and replay ledger record IDs differ")

    legacy_spans: dict[str, tuple[int, int]] = {}
    for record in legacy_records:
        span, _, _ = select_occurrence(
            legacy_text, record["exact_source_text"], record["source_location"]
        )
        if span is None:
            raise IntegrityError(f"legacy quotation is not uniquely grounded: {record['atom_id']}")
        legacy_spans[record["atom_id"]] = span

    rewrites = _rewrite_lines(
        legacy_text=legacy_text,
        active_text=active_text,
        legacy_sections=legacy_sections,
        active_sections=active_sections,
        legacy_sha256=legacy_binding["sha256"],
        active_sha256=active_binding["sha256"],
        legacy_records=legacy_records,
        legacy_spans=legacy_spans,
        replay_by_id=replay_by_id,
    )
    rewrite_by_record: dict[str, list[str]] = {}
    for rewrite in rewrites:
        for record_id in rewrite["resolved_legacy_only_record_ids"]:
            rewrite_by_record.setdefault(record_id, []).append(rewrite["rewrite_id"])

    coordinates: list[dict[str, Any]] = []
    for record in legacy_records:
        record_id = record["atom_id"]
        replay = replay_by_id[record_id]
        legacy_coordinate = _coordinate(
            text=legacy_text,
            source_role="legacy_extraction_source",
            source_sha256=legacy_binding["sha256"],
            sections=legacy_sections,
            span=legacy_spans[record_id],
        )
        active_span, _, _ = select_occurrence(
            active_text, record["exact_source_text"], record["source_location"]
        )
        active_coordinate = (
            _coordinate(
                text=active_text,
                source_role="active_frozen_source",
                source_sha256=active_binding["sha256"],
                sections=active_sections,
                span=active_span,
            )
            if active_span is not None
            else None
        )
        rewrite_ids = sorted(rewrite_by_record.get(record_id, []))
        status = "active_exact" if active_coordinate else "active_reference_rewrite"
        if status == "active_reference_rewrite" and not rewrite_ids:
            raise IntegrityError(f"legacy-only record lacks a reference rewrite: {record_id}")
        body = {
            "legacy_record_id": record_id,
            "replay_record_id": replay["replay_record_id"],
            "source_id": card["source_id"],
            "quote_sha256": replay["quote_sha256"],
            "coordinate_status": status,
            "legacy_coordinate": legacy_coordinate,
            "active_coordinate": active_coordinate,
            "reference_rewrite_ids": rewrite_ids,
            "compound_record_preserved": len(replay["block_ids"]) > 1,
            "replay_migration_disposition": replay["migration_disposition"],
        }
        coordinate = {
            "schema_version": "M050-HUMAN-RULINGS-ATOM-COORDINATE-0.1",
            "coordinate_record_id": content_id("hrc", body),
            **body,
        }
        validate_artifact("human_rulings_atom_coordinate", coordinate)
        coordinates.append(coordinate)

    coordinate_bytes = canonical_jsonl_bytes(coordinates)
    registry_body = {
        "reconstruction_version": RECONSTRUCTION_VERSION,
        "source_id": card["source_id"],
        "active_source": active_binding,
        "legacy_source": legacy_binding,
        "ruling_count": len(active_rulings),
        "open_item_count": len([section for section in active_sections if section.kind == "open_item"]),
        "field_count": sum(len(section.fields) for section in active_rulings),
        "ruling_ids": [section.section_id for section in active_rulings],
        "sections": [_section_dict(section, active_text) for section in active_rulings],
    }
    registry = {
        "schema_version": "M050-HUMAN-RULINGS-SECTION-REGISTRY-0.1",
        "registry_id": content_id("hrr", registry_body),
        **registry_body,
    }
    validate_artifact("human_rulings_section_registry", registry)

    receipt_binding = {
        "path": str(migration_receipt_path.resolve().relative_to(repo_root)),
        "sha256": sha256_file(migration_receipt_path),
        "role": "gate_4_source_identity_migration_receipt",
    }
    rewrite_body = {
        "reconstruction_version": RECONSTRUCTION_VERSION,
        "source_id": card["source_id"],
        "legacy_source": legacy_binding,
        "active_source": active_binding,
        "migration_receipt": receipt_binding,
        "rewrite_count": len(rewrites),
        "legacy_only_record_count": len(rewrite_by_record),
        "legacy_only_record_ids": sorted(rewrite_by_record),
        "rewrites": rewrites,
    }
    rewrite_map = {
        "schema_version": "M050-HUMAN-RULINGS-REFERENCE-REWRITE-MAP-0.1",
        "rewrite_map_id": content_id("hrrm", rewrite_body),
        **rewrite_body,
    }
    validate_artifact("human_rulings_reference_rewrite_map", rewrite_map)

    ruling_linked = sum(
        coordinate["legacy_coordinate"]["ruling_id"] is not None for coordinate in coordinates
    )
    field_linked = sum(bool(coordinate["legacy_coordinate"]["field_labels"]) for coordinate in coordinates)
    status_counts = dict(sorted(Counter(item["coordinate_status"] for item in coordinates).items()))
    report_body = {
        "reconstruction_version": RECONSTRUCTION_VERSION,
        "source_id": card["source_id"],
        "identity_card": {
            "path": str(card_path.resolve().relative_to(repo_root)),
            "sha256": sha256_file(card_path),
            "role": "approved_source_identity_card",
        },
        "replay_report": {
            "path": str(replay_report_path.resolve().relative_to(repo_root)),
            "sha256": sha256_file(replay_report_path),
            "role": "passed_legacy_replay_report",
        },
        "migration_receipt": receipt_binding,
        "registry": {
            "path": registry_relative_path,
            "sha256": sha256_bytes(canonical_json_bytes(registry) + b"\n"),
            "role": "active_ruling_section_and_field_registry",
        },
        "coordinate_ledger": {
            "path": coordinate_ledger_relative_path,
            "sha256": sha256_bytes(coordinate_bytes),
            "role": "legacy_atom_ruling_and_field_coordinate_ledger",
        },
        "reference_rewrite_map": {
            "path": rewrite_map_relative_path,
            "sha256": sha256_bytes(canonical_json_bytes(rewrite_map) + b"\n"),
            "role": "deterministic_active_to_legacy_reference_rewrite_map",
        },
        "ruling_count": len(active_rulings),
        "field_count": registry["field_count"],
        "legacy_record_count": len(coordinates),
        "ruling_linked_record_count": ruling_linked,
        "document_region_record_count": len(coordinates) - ruling_linked,
        "field_linked_record_count": field_linked,
        "coordinate_status_counts": status_counts,
        "reference_rewrite_count": len(rewrites),
        "legacy_only_record_count": len(rewrite_by_record),
        "complete_ruling_coverage": len(active_rulings) == 41,
        "complete_legacy_record_coverage": len(coordinates) == 173,
        "complete_reference_rewrite_coverage": len(rewrite_by_record) == 6,
        "exact_human_wording_preserved": True,
        "legacy_records_modified_or_split": 0,
        "provider_calls": 0,
        "accounted_cost_cents": 0,
        "passed": len(active_rulings) == 41 and len(coordinates) == 173 and len(rewrite_by_record) == 6,
    }
    report = {
        "schema_version": "M050-HUMAN-RULINGS-RECONSTRUCTION-REPORT-0.1",
        "reconstruction_id": content_id("hrrp", report_body),
        **report_body,
    }
    validate_artifact("human_rulings_reconstruction_report", report)
    return registry, coordinate_bytes, rewrite_map, report
