from __future__ import annotations

from collections import Counter
import json
from pathlib import Path
from typing import Any

from .canonical import canonical_json_bytes, content_id, sha256_bytes, sha256_file
from .errors import ContractError, IntegrityError
from .legacy import (
    build_legacy_replay,
    canonical_jsonl_bytes,
    exact_occurrences,
    line_bounds,
    overlapping_blocks,
    select_occurrence,
)
from .schema import validate_artifact


COMPOUND_DISPOSITION_VERSION = "M050-LEGACY-COMPOUND-DISPOSITION-0.1"


def _repo_file(repo_root: Path, relative: str) -> Path:
    path = (repo_root / relative).resolve()
    try:
        path.relative_to(repo_root)
    except ValueError as exc:
        raise IntegrityError(f"repair binding escapes repository: {relative}") from exc
    if relative == "m051" or relative.startswith("m051/"):
        raise IntegrityError(f"m051 input is prohibited: {relative}")
    if not path.is_file():
        raise IntegrityError(f"repair binding is not a file: {relative}")
    return path


def _bound_file(repo_root: Path, binding: dict[str, Any]) -> Path:
    path = _repo_file(repo_root, binding.get("path", ""))
    if sha256_file(path) != binding.get("sha256"):
        raise IntegrityError(f"repair binding hash mismatch: {binding.get('path', '')}")
    return path


def _read_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ContractError(f"JSON root must be an object: {path}")
    return value


def _read_jsonl(path: Path) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not line.strip():
            raise ContractError(f"blank JSONL line at {path}:{line_number}")
        value = json.loads(line)
        if not isinstance(value, dict):
            raise ContractError(f"non-object JSONL record at {path}:{line_number}")
        records.append(value)
    return records


def _line_range(text: str, span: tuple[int, int]) -> tuple[int, int]:
    start, end = span
    return text.count("\n", 0, start) + 1, text.count("\n", 0, max(start, end - 1)) + 1


def _verify_milestone(milestone: dict[str, Any]) -> None:
    if milestone.get("status") != "DETERMINISTIC_REPLAY_PASSED_REPAIR_QUEUE_REQUIRED":
        raise ContractError("compound disposition requires the passed legacy replay milestone")
    aggregate = milestone.get("aggregate", {})
    if (
        aggregate.get("records") != 913
        or aggregate.get("cross_block_records") != 17
        or aggregate.get("grounding_failures") != 0
    ):
        raise IntegrityError("legacy replay milestone has unexpected aggregate counts")
    if milestone.get("external_model_calls") != 0 or milestone.get("accounted_cost_cents") != 0:
        raise IntegrityError("legacy replay milestone must remain offline and zero-cost")


def build_compound_dispositions(
    *,
    repo_root: Path,
    replay_milestone: dict[str, Any],
    replay_milestone_path: Path,
    ledger_relative_path: str,
) -> tuple[bytes, dict[str, Any]]:
    repo_root = repo_root.resolve()
    _verify_milestone(replay_milestone)
    try:
        replay_milestone_path.resolve().relative_to(repo_root)
    except ValueError as exc:
        raise IntegrityError("legacy replay milestone path escapes repository") from exc

    dispositions: list[dict[str, Any]] = []
    source_summaries: list[dict[str, Any]] = []
    for source_entry in replay_milestone.get("sources", []):
        source_id = source_entry.get("source_id")
        replay_ledger_path = _bound_file(repo_root, source_entry.get("ledger", {}))
        replay_report_path = _bound_file(repo_root, source_entry.get("report", {}))
        replay_report = _read_json(replay_report_path)
        validate_artifact("legacy_replay_report", replay_report)
        if replay_report.get("source_id") != source_id or replay_report.get("passed") is not True:
            raise IntegrityError(f"invalid replay report for compound repair: {source_id}")

        card_path = _bound_file(repo_root, replay_report["identity_card"])
        card = _read_json(card_path)
        validate_artifact("source_identity_card_v0_2", card)
        if card.get("status") != "approved" or card.get("source_id") != source_id:
            raise ContractError(f"compound repair requires approved identity card: {source_id}")
        manifest_path = _bound_file(repo_root, replay_report["block_manifest"])
        manifest = _read_json(manifest_path)
        validate_artifact("block_manifest", manifest)
        blocks = manifest["blocks"]
        block_by_id = {block["block_id"]: block for block in blocks}

        active_binding = next(
            (
                binding
                for binding in card["legacy_extraction"]["source_bindings"]
                if binding["role"] == "active_frozen_source"
            ),
            None,
        )
        if active_binding is None:
            raise ContractError(f"compound repair lacks active source binding: {source_id}")
        active_source_path = _bound_file(repo_root, active_binding)
        source_text = active_source_path.read_text(encoding="utf-8")
        candidate_path = _bound_file(repo_root, card["legacy_extraction"]["candidate"])
        candidate_records = _read_jsonl(candidate_path)
        candidate_by_id = {record.get("atom_id"): record for record in candidate_records}
        if len(candidate_by_id) != len(candidate_records):
            raise IntegrityError(f"legacy candidate has duplicate record IDs: {source_id}")
        replay_records = _read_jsonl(replay_ledger_path)
        cross_block = [
            record for record in replay_records if record.get("grounding_status") == "exact_cross_block"
        ]

        for replay_record in cross_block:
            record_id = replay_record["legacy_record_id"]
            candidate = candidate_by_id.get(record_id)
            if not candidate:
                raise IntegrityError(f"cross-block replay record lacks legacy candidate: {record_id}")
            quotation = candidate.get("exact_source_text")
            location = candidate.get("source_location")
            if not isinstance(quotation, str) or not quotation or not isinstance(location, str):
                raise ContractError(f"invalid cross-block legacy candidate: {record_id}")
            span, occurrence_count, line_applied = select_occurrence(source_text, quotation, location)
            if span is None or occurrence_count != 1 or line_applied:
                raise IntegrityError(f"cross-block quotation is not uniquely exact: {record_id}")
            computed_ids = overlapping_blocks(blocks, span)
            if computed_ids != replay_record["block_ids"]:
                raise IntegrityError(f"cross-block replay block sequence drifted: {record_id}")
            selected = [block_by_id[block_id] for block_id in computed_ids]
            ordinals = [block["ordinal"] for block in selected]
            block_types = {block["block_type"] for block in selected}
            headings = {block.get("parent_heading") for block in selected}
            status_contexts = {tuple(block.get("status_markers", [])) for block in selected}
            local_dispositions = {block.get("local_disposition") for block in selected}
            local_reasons = {block.get("local_reason_code") for block in selected}
            checks = {
                "unique_exact_source_span": True,
                "contiguous_raw_quotation": source_text[span[0] : span[1]] == quotation,
                "replay_block_sequence_exact": computed_ids == replay_record["block_ids"],
                "consecutive_non_whitespace_blocks": ordinals
                == list(range(ordinals[0], ordinals[0] + len(ordinals))),
                "contiguous_block_partition": all(
                    left["end"] == right["start"] for left, right in zip(selected, selected[1:])
                ),
                "homogeneous_block_type": len(block_types) == 1,
                "shared_parent_heading": len(headings) == 1,
                "shared_status_context": len(status_contexts) == 1,
                "all_blocks_locally_eligible": local_dispositions == {"eligible"}
                and local_reasons == {"claim_bearing_content"},
                "interior_blocks_fully_covered": all(
                    span[0] <= block["start"] and span[1] >= block["end"]
                    for block in selected[1:-1]
                ),
            }
            if not all(checks.values()):
                failed = sorted(name for name, passed in checks.items() if not passed)
                raise IntegrityError(
                    f"cross-block compound fails deterministic boundary checks {record_id}: {', '.join(failed)}"
                )
            start_line, end_line = _line_range(source_text, span)
            body = {
                "legacy_record_id": record_id,
                "replay_record_id": replay_record["replay_record_id"],
                "source_id": source_id,
                "source_sha256": active_binding["sha256"],
                "source_location": location,
                "quote_sha256": replay_record["quote_sha256"],
                "legacy_candidate_record_sha256": sha256_bytes(canonical_json_bytes(candidate)),
                "source_span": {
                    "start": span[0],
                    "end": span[1],
                    "start_line": start_line,
                    "end_line": end_line,
                    "first_block_offset": span[0] - selected[0]["start"],
                    "last_block_end_offset": selected[-1]["end"] - span[1],
                },
                "ordered_block_ids": computed_ids,
                "ordered_block_ordinals": ordinals,
                "block_type": next(iter(block_types)),
                "parent_heading": next(iter(headings)) or "<document-root>",
                "status_context": list(next(iter(status_contexts))),
                "structural_checks": checks,
                "boundary_resolution": "contiguous_same_section_homogeneous_block_sequence",
                "preservation_disposition": "preserve_as_one_indivisible_legacy_compound",
                "migration_state": "mechanically_valid_pending_tier_2_semantic_review",
                "review_requirement": "exhaustive_independent_semantic_review_in_compound_bundle",
                "risk_tier": 2,
                "semantic_review_performed": False,
                "legacy_record_modified": False,
                "split_performed": False,
            }
            disposition = {
                "schema_version": "M050-LEGACY-COMPOUND-DISPOSITION-RECORD-0.1",
                "compound_disposition_id": content_id("lcd", body),
                **body,
            }
            validate_artifact("legacy_compound_disposition_record", disposition)
            dispositions.append(disposition)
        source_summaries.append(
            {
                "source_id": source_id,
                "cross_block_records": len(cross_block),
                "mechanically_valid_compounds": len(cross_block),
                "tier_2_review_required": len(cross_block),
            }
        )

    dispositions.sort(key=lambda item: (item["source_id"], item["legacy_record_id"]))
    if len(dispositions) != 17 or len({item["legacy_record_id"] for item in dispositions}) != 17:
        raise IntegrityError("compound disposition must account for exactly 17 distinct records")
    ledger_bytes = canonical_jsonl_bytes(dispositions)
    disposition_counts = dict(
        sorted(Counter(item["preservation_disposition"] for item in dispositions).items())
    )
    body = {
        "compound_disposition_version": COMPOUND_DISPOSITION_VERSION,
        "replay_milestone": {
            "path": str(replay_milestone_path.resolve().relative_to(repo_root)),
            "sha256": sha256_file(replay_milestone_path),
            "role": "passed_legacy_replay_milestone",
        },
        "ledger": {
            "path": ledger_relative_path,
            "sha256": sha256_bytes(ledger_bytes),
            "role": "source_preserving_cross_block_compound_disposition_ledger",
        },
        "record_count": len(dispositions),
        "distinct_legacy_record_ids": len({item["legacy_record_id"] for item in dispositions}),
        "source_summaries": source_summaries,
        "disposition_counts": disposition_counts,
        "all_exact_contiguous": all(
            item["structural_checks"]["contiguous_raw_quotation"] for item in dispositions
        ),
        "all_block_sequences_exact": all(
            item["structural_checks"]["replay_block_sequence_exact"] for item in dispositions
        ),
        "all_preserved_as_indivisible_compounds": all(
            item["preservation_disposition"] == "preserve_as_one_indivisible_legacy_compound"
            for item in dispositions
        ),
        "tier_2_semantic_review_required": len(dispositions),
        "semantic_reviews_performed": 0,
        "legacy_records_modified_or_split": 0,
        "provider_calls": 0,
        "accounted_cost_cents": 0,
        "passed": True,
    }
    report = {
        "schema_version": "M050-LEGACY-COMPOUND-DISPOSITION-REPORT-0.1",
        "compound_report_id": content_id("lcdr", body),
        **body,
    }
    validate_artifact("legacy_compound_disposition_report", report)
    return ledger_bytes, report


def _whole_line_matches(
    text: str, matches: list[tuple[int, int]], bounds: tuple[int, int]
) -> list[tuple[int, int]]:
    selected: list[tuple[int, int]] = []
    for start, end in matches:
        if start < bounds[0] or end > bounds[1]:
            continue
        line_start = text.rfind("\n", 0, start) + 1
        newline = text.find("\n", end)
        line_end = len(text) if newline < 0 else newline
        if line_end > line_start and text[line_end - 1] == "\r":
            line_end -= 1
        if start == line_start and end == line_end:
            selected.append((start, end))
    return selected


def build_occurrence_resolution(
    *,
    repo_root: Path,
    replay_milestone: dict[str, Any],
    replay_milestone_path: Path,
) -> dict[str, Any]:
    repo_root = repo_root.resolve()
    _verify_milestone(replay_milestone)
    ambiguous: list[tuple[dict[str, Any], dict[str, Any], dict[str, Any], dict[str, Any]]] = []
    for source_entry in replay_milestone.get("sources", []):
        replay_report = _read_json(_bound_file(repo_root, source_entry.get("report", {})))
        card = _read_json(_bound_file(repo_root, replay_report["identity_card"]))
        replay_records = _read_jsonl(_bound_file(repo_root, source_entry.get("ledger", {})))
        candidate_records = _read_jsonl(
            _bound_file(repo_root, card["legacy_extraction"]["candidate"])
        )
        candidate_by_id = {record.get("atom_id"): record for record in candidate_records}
        manifest = _read_json(_bound_file(repo_root, replay_report["block_manifest"]))
        for replay_record in replay_records:
            if replay_record.get("grounding_status") == "exact_active_ambiguous":
                candidate = candidate_by_id.get(replay_record["legacy_record_id"])
                if not candidate:
                    raise IntegrityError("ambiguous replay record lacks its legacy candidate")
                ambiguous.append((source_entry, replay_record, candidate, {"card": card, "manifest": manifest}))
    if len(ambiguous) != 1:
        raise IntegrityError("occurrence repair requires exactly one active-source ambiguity")

    source_entry, replay_record, candidate, controls = ambiguous[0]
    card = controls["card"]
    manifest = controls["manifest"]
    active_binding = next(
        binding
        for binding in card["legacy_extraction"]["source_bindings"]
        if binding["role"] == "active_frozen_source"
    )
    source_path = _bound_file(repo_root, active_binding)
    source_text = source_path.read_text(encoding="utf-8")
    quotation = candidate["exact_source_text"]
    location = candidate["source_location"]
    matches = exact_occurrences(source_text, quotation)
    bounds = line_bounds(source_text, location)
    if bounds is None:
        raise IntegrityError("ambiguous record lacks a valid pinned line range")
    bounded = [match for match in matches if match[0] >= bounds[0] and match[1] <= bounds[1]]
    whole_line = _whole_line_matches(source_text, matches, bounds)
    if len(matches) != replay_record["source_occurrence_count"] or len(whole_line) != 1:
        raise IntegrityError("pinned whole-line occurrence does not resolve uniquely")
    selected = whole_line[0]
    block_ids = overlapping_blocks(manifest["blocks"], selected)
    if len(block_ids) != 1:
        raise IntegrityError("resolved whole-line occurrence must belong to exactly one block")
    block = next(item for item in manifest["blocks"] if item["block_id"] == block_ids[0])
    start_line, end_line = _line_range(source_text, selected)
    body = {
        "legacy_record_id": replay_record["legacy_record_id"],
        "replay_record_id": replay_record["replay_record_id"],
        "source_id": source_entry["source_id"],
        "source_sha256": active_binding["sha256"],
        "source_location": location,
        "quote_sha256": replay_record["quote_sha256"],
        "legacy_candidate_record_sha256": sha256_bytes(canonical_json_bytes(candidate)),
        "original_occurrence_count": len(matches),
        "pinned_range_occurrence_count": len(bounded),
        "pinned_range_whole_line_occurrence_count": len(whole_line),
        "selected_span": {
            "start": selected[0],
            "end": selected[1],
            "start_line": start_line,
            "end_line": end_line,
        },
        "selected_block_id": block["block_id"],
        "selected_block_ordinal": block["ordinal"],
        "selected_block_type": block["block_type"],
        "parent_heading": block.get("parent_heading") or "<document-root>",
        "selection_rule": "unique_exact_whole_line_match_within_pinned_source_line_range",
        "resolution_disposition": "exact_occurrence_resolved_without_replay_mutation",
        "migration_state": "mechanically_valid_pending_tier_2_ontology_review",
        "review_requirement": "exhaustive_independent_semantic_review_in_ontology_bundle",
        "risk_tier": 2,
        "semantic_review_performed": False,
        "legacy_record_modified": False,
        "replay_record_modified": False,
        "provider_calls": 0,
        "accounted_cost_cents": 0,
    }
    resolution = {
        "schema_version": "M050-LEGACY-OCCURRENCE-RESOLUTION-0.1",
        "occurrence_resolution_id": content_id("lor", body),
        **body,
    }
    validate_artifact("legacy_occurrence_resolution", resolution)
    return resolution


def build_repair_closure(
    *,
    repo_root: Path,
    replay_milestone: dict[str, Any],
    replay_milestone_path: Path,
    human_reconstruction_report_path: Path,
    compound_report_path: Path,
    occurrence_resolution_path: Path,
) -> dict[str, Any]:
    repo_root = repo_root.resolve()
    _verify_milestone(replay_milestone)
    supplied = (
        human_reconstruction_report_path,
        compound_report_path,
        occurrence_resolution_path,
    )
    for path in supplied:
        try:
            path.resolve().relative_to(repo_root)
        except ValueError as exc:
            raise IntegrityError("repair closure input escapes repository") from exc
        if not path.is_file():
            raise IntegrityError(f"repair closure input is not a file: {path}")

    human_report = _read_json(human_reconstruction_report_path)
    compound_report = _read_json(compound_report_path)
    occurrence_resolution = _read_json(occurrence_resolution_path)
    validate_artifact("human_rulings_reconstruction_report", human_report)
    validate_artifact("legacy_compound_disposition_report", compound_report)
    validate_artifact("legacy_occurrence_resolution", occurrence_resolution)
    if human_report.get("passed") is not True or compound_report.get("passed") is not True:
        raise ContractError("repair closure requires passed reconstruction and compound reports")

    rewrite_map_path = _bound_file(repo_root, human_report["reference_rewrite_map"])
    rewrite_map = _read_json(rewrite_map_path)
    validate_artifact("human_rulings_reference_rewrite_map", rewrite_map)
    rewrite_ids = set(rewrite_map["legacy_only_record_ids"])
    compound_ledger_path = _bound_file(repo_root, compound_report["ledger"])
    compound_records = _read_jsonl(compound_ledger_path)
    for record in compound_records:
        validate_artifact("legacy_compound_disposition_record", record)
    compound_ids = {record["legacy_record_id"] for record in compound_records}
    occurrence_ids = {occurrence_resolution["legacy_record_id"]}
    if rewrite_ids & compound_ids or rewrite_ids & occurrence_ids or compound_ids & occurrence_ids:
        raise IntegrityError("repair disposition sets overlap")
    repaired_ids = rewrite_ids | compound_ids | occurrence_ids

    raw_queue_ids: set[str] = set()
    reproducibility: list[dict[str, Any]] = []
    for source_entry in replay_milestone["sources"]:
        existing_report_path = _bound_file(repo_root, source_entry["report"])
        existing_ledger_path = _bound_file(repo_root, source_entry["ledger"])
        existing_report = _read_json(existing_report_path)
        raw_queue_ids.update(existing_report["review_queue_ids"])
        card_path = _bound_file(repo_root, existing_report["identity_card"])
        manifest_path = _bound_file(repo_root, existing_report["block_manifest"])
        card = _read_json(card_path)
        manifest = _read_json(manifest_path)
        rebuilt_ledger, rebuilt_report = build_legacy_replay(
            repo_root=repo_root,
            card=card,
            card_path=card_path,
            block_manifest=manifest,
            block_manifest_path=manifest_path,
            ledger_relative_path=existing_report["ledger"]["path"],
        )
        ledger_identical = rebuilt_ledger == existing_ledger_path.read_bytes()
        report_identical = rebuilt_report == existing_report
        if not ledger_identical or not report_identical:
            raise IntegrityError(
                f"legacy replay is not byte reproducible after repairs: {source_entry['source_id']}"
            )
        reproducibility.append(
            {
                "source_id": source_entry["source_id"],
                "records": existing_report["record_count"],
                "raw_repair_queue_records": len(existing_report["review_queue_ids"]),
                "ledger_byte_identical": ledger_identical,
                "report_byte_identical": report_identical,
            }
        )
    if len(raw_queue_ids) != 24 or repaired_ids != raw_queue_ids:
        missing = sorted(raw_queue_ids - repaired_ids)
        extra = sorted(repaired_ids - raw_queue_ids)
        raise IntegrityError(
            f"repair overlay does not exactly cover raw replay queue; missing={missing}, extra={extra}"
        )

    def binding(path: Path, role: str) -> dict[str, str]:
        return {
            "path": str(path.resolve().relative_to(repo_root)),
            "sha256": sha256_file(path),
            "role": role,
        }

    body = {
        "replay_milestone": binding(
            replay_milestone_path, "passed_legacy_replay_milestone"
        ),
        "human_rulings_reconstruction_report": binding(
            human_reconstruction_report_path,
            "passed_human_rulings_reconstruction_report",
        ),
        "compound_disposition_report": binding(
            compound_report_path, "passed_cross_block_compound_disposition_report"
        ),
        "occurrence_resolution": binding(
            occurrence_resolution_path, "pinned_whole_line_occurrence_resolution"
        ),
        "reproducibility": reproducibility,
        "legacy_record_count": sum(item["records"] for item in reproducibility),
        "raw_replay_queue_count": len(raw_queue_ids),
        "reference_rewrite_repairs": len(rewrite_ids),
        "cross_block_compound_repairs": len(compound_ids),
        "ambiguous_occurrence_repairs": len(occurrence_ids),
        "mechanically_dispositioned_queue_count": len(repaired_ids),
        "unresolved_grounding_or_coordinate_repairs": 0,
        "replay_ledgers_byte_identical": len(reproducibility),
        "replay_reports_byte_identical": len(reproducibility),
        "mechanical_repair_overlay_complete": True,
        "semantic_acceptance_performed": False,
        "layer_e_migration_started": False,
        "legacy_or_replay_records_modified": 0,
        "provider_calls": 0,
        "accounted_cost_cents": 0,
        "passed": True,
    }
    closure = {
        "schema_version": "M050-LEGACY-REPAIR-CLOSURE-REPORT-0.1",
        "repair_closure_id": content_id("lrc", body),
        **body,
    }
    validate_artifact("legacy_repair_closure_report", closure)
    return closure
