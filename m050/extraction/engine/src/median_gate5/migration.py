from __future__ import annotations

from collections import Counter, defaultdict
import json
from pathlib import Path
import re
from typing import Any

from .canonical import canonical_json_bytes, content_id, sha256_bytes, sha256_file
from .errors import ContractError, IntegrityError
from .legacy import canonical_jsonl_bytes, overlapping_blocks
from .risk import classify_review_risk
from .schema import validate_artifact


MIGRATION_VERSION = "M050-LAYER-E-LEGACY-MIGRATION-0.1"
COMPOUND_REVIEW_PATTERN = re.compile(r"\.\s+(?=[A-Z])")
LEGACY_PROPOSAL_FIELDS = (
    "source_declared_class",
    "adjudicated_class",
    "primary_msid_candidate",
    "related_msid_candidates",
    "semantic_relation",
    "register",
    "operator",
    "mode",
    "record_status",
    "msid_status",
    "authority_scope",
    "authority_effect",
    "supersedes",
    "notes",
)
NON_IMPORTED_FIELDS = ("conformance_basis", "cross_source_support", "conflicts_with")
SOURCE_BASELINE_TIERS = {
    "M050-SRC-PA-001": 2,
    "M050-SRC-HUMAN-RULINGS-001": 2,
    "M050-SRC-MSID-GRAMMAR-001": 2,
}


def is_compound_review_quote(text: str) -> bool:
    """Reproduce the Gate 3 multi-sentence review indicator exactly."""
    return bool(COMPOUND_REVIEW_PATTERN.search(text))


def _repo_file(repo_root: Path, binding: dict[str, Any]) -> Path:
    relative = binding.get("path", "")
    target = (repo_root / relative).resolve()
    try:
        target.relative_to(repo_root)
    except ValueError as exc:
        raise IntegrityError(f"migration binding escapes repository: {relative}") from exc
    if relative == "m051" or relative.startswith("m051/"):
        raise IntegrityError(f"m051 input is prohibited: {relative}")
    if not target.is_file():
        raise IntegrityError(f"migration binding is not a file: {relative}")
    if sha256_file(target) != binding.get("sha256"):
        raise IntegrityError(f"migration binding hash mismatch: {relative}")
    return target


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


def _verify_repair_closure(closure: dict[str, Any]) -> None:
    validate_artifact("legacy_repair_closure_report", closure)
    if not (
        closure.get("passed")
        and closure.get("mechanical_repair_overlay_complete")
        and closure.get("legacy_record_count") == 913
        and closure.get("mechanically_dispositioned_queue_count") == 24
        and closure.get("unresolved_grounding_or_coordinate_repairs") == 0
        and closure.get("semantic_acceptance_performed") is False
        and closure.get("layer_e_migration_started") is False
    ):
        raise IntegrityError("Layer E migration requires the complete zero-error repair closure")


def _expanded_status_regions(
    card: dict[str, Any], blocks: list[dict[str, Any]]
) -> dict[str, list[dict[str, str]]]:
    by_id = {block["block_id"]: block for block in blocks}
    by_ordinal = {block["ordinal"]: block for block in blocks}
    memberships: dict[str, list[dict[str, str]]] = defaultdict(list)
    last_ordinal = max(by_ordinal)
    for region in card.get("mixed_status_regions", []):
        region_blocks = [by_id.get(block_id) for block_id in region["block_ids"]]
        if any(block is None for block in region_blocks):
            raise IntegrityError(f"identity status region references an unknown block: {region['label']}")
        ordinals = [block["ordinal"] for block in region_blocks if block is not None]
        start, end = min(ordinals), max(ordinals)
        handling = region["handling"].lower()
        if len(ordinals) == 1 and region["status"] == "change_record":
            end = last_ordinal
        if region["status"] == "silent" and "full endnote" in handling:
            end = last_ordinal
        for ordinal in range(start, end + 1):
            block = by_ordinal[ordinal]
            memberships[block["block_id"]].append(
                {
                    "label": region["label"],
                    "status": region["status"],
                    "handling": region["handling"],
                }
            )
    return memberships


def _candidate_risk(
    source_id: str,
    blocks: list[dict[str, Any]],
    quotation: str,
    status_regions: list[dict[str, str]],
    compound_flag: bool,
    repair_ids: list[str],
) -> tuple[int, list[str]]:
    tier = SOURCE_BASELINE_TIERS.get(source_id, 3)
    signals: set[str] = set()
    if tier == 2:
        signals.add("constitutional_ontology_or_ruling_reconstruction")
    for block in blocks:
        risk = classify_review_risk(block, {"normalized_claim": quotation})
        if source_id == "M050-SRC-CROSSING-001":
            tier = min(tier, risk["risk_tier"])
        signals.update(risk["signals"])
    if compound_flag:
        tier = min(tier, 2)
        signals.add("gate_3_compound_review_queue")
    if repair_ids:
        tier = min(tier, 2)
        signals.add("mechanical_repair_lineage")
    exceptional = {region["status"] for region in status_regions} & {
        "open",
        "provisional",
        "historical",
        "silent",
        "process_only",
        "change_record",
    }
    if exceptional:
        tier = 1
        signals.add("explicit_nonsettled_or_non_normative_status_region")
    return tier, sorted(signals)


def _review_requirement(tier: int) -> str:
    return {
        1: "author_decision_required_before_normative_use",
        2: "exhaustive_independent_semantic_review_and_bundle_approval",
        3: "deterministic_checks_plus_risk_weighted_sampling",
    }[tier]


def _artifact_binding(path: str, data: bytes, role: str) -> dict[str, str]:
    return {"path": path, "sha256": sha256_bytes(data), "role": role}


def build_layer_e_legacy_migration(
    *,
    repo_root: Path,
    repair_closure: dict[str, Any],
    repair_closure_path: Path,
    candidate_relative_path: str,
    compound_relative_path: str,
    block_ledger_relative_paths: dict[str, str],
) -> tuple[bytes, bytes, dict[str, bytes], dict[str, Any]]:
    repo_root = repo_root.resolve()
    _verify_repair_closure(repair_closure)
    try:
        repair_closure_path.resolve().relative_to(repo_root)
    except ValueError as exc:
        raise IntegrityError("repair closure path escapes repository") from exc
    if _read_json(repair_closure_path) != repair_closure:
        raise IntegrityError("supplied repair closure does not match its bound file")

    milestone = _read_json(_repo_file(repo_root, repair_closure["replay_milestone"]))
    compound_report = _read_json(_repo_file(repo_root, repair_closure["compound_disposition_report"]))
    compound_records = _read_jsonl(_repo_file(repo_root, compound_report["ledger"]))
    compound_by_legacy = {record["legacy_record_id"]: record for record in compound_records}
    occurrence = _read_json(_repo_file(repo_root, repair_closure["occurrence_resolution"]))
    occurrence_by_legacy = {occurrence["legacy_record_id"]: occurrence}

    human_report = _read_json(
        _repo_file(repo_root, repair_closure["human_rulings_reconstruction_report"])
    )
    coordinate_binding = human_report["coordinate_ledger"]
    human_coordinates = _read_jsonl(_repo_file(repo_root, coordinate_binding))
    human_coordinate_by_legacy = {record["legacy_record_id"]: record for record in human_coordinates}
    rewrite_map = _read_json(_repo_file(repo_root, human_report["reference_rewrite_map"]))
    rewrite_by_id = {record["rewrite_id"]: record for record in rewrite_map["rewrites"]}

    migration_records: list[dict[str, Any]] = []
    compound_inventory: list[dict[str, Any]] = []
    block_ledgers: dict[str, bytes] = {}
    source_summaries: list[dict[str, Any]] = []
    global_seen: set[str] = set()

    for source_entry in milestone["sources"]:
        source_id = source_entry["source_id"]
        if source_id not in block_ledger_relative_paths:
            raise ContractError(f"missing output block-ledger path for {source_id}")
        replay_report = _read_json(_repo_file(repo_root, source_entry["report"]))
        replay_records = _read_jsonl(_repo_file(repo_root, source_entry["ledger"]))
        replay_by_legacy = {record["legacy_record_id"]: record for record in replay_records}
        card_path = _repo_file(repo_root, replay_report["identity_card"])
        card = _read_json(card_path)
        manifest = _read_json(_repo_file(repo_root, replay_report["block_manifest"]))
        blocks = manifest["blocks"]
        block_by_id = {block["block_id"]: block for block in blocks}
        regions_by_block = _expanded_status_regions(card, blocks)
        legacy_path = _repo_file(repo_root, replay_report["legacy_candidate"])
        legacy_records = _read_jsonl(legacy_path)
        if len(legacy_records) != source_entry["records"]:
            raise IntegrityError(f"legacy record count drift: {source_id}")

        source_candidates: list[dict[str, Any]] = []
        candidate_ids_by_block: dict[str, list[str]] = defaultdict(list)
        gate_3_compound_count = 0
        structural_compound_count = 0
        for legacy_record in legacy_records:
            legacy_id = legacy_record["atom_id"]
            if legacy_id in global_seen:
                raise IntegrityError(f"duplicate legacy record ID across sources: {legacy_id}")
            global_seen.add(legacy_id)
            replay = replay_by_legacy.get(legacy_id)
            if replay is None:
                raise IntegrityError(f"legacy record lacks replay lineage: {legacy_id}")
            quotation = legacy_record["exact_source_text"]
            quote_sha256 = sha256_bytes(quotation.encode("utf-8"))
            if replay["quote_sha256"] != quote_sha256:
                raise IntegrityError(f"quotation hash drift: {legacy_id}")

            repair_ids: list[str] = []
            effective_block_ids = list(replay["block_ids"])
            coordinate_record_id: str | None = None
            if legacy_id in compound_by_legacy:
                compound = compound_by_legacy[legacy_id]
                repair_ids.append(compound["compound_disposition_id"])
                effective_block_ids = list(compound["ordered_block_ids"])
            if legacy_id in occurrence_by_legacy:
                repair = occurrence_by_legacy[legacy_id]
                repair_ids.append(repair["occurrence_resolution_id"])
                effective_block_ids = [repair["selected_block_id"]]
            if source_id == "M050-SRC-HUMAN-RULINGS-001":
                coordinate = human_coordinate_by_legacy.get(legacy_id)
                if coordinate is None:
                    raise IntegrityError(f"Human Rulings record lacks reconstructed coordinate: {legacy_id}")
                coordinate_record_id = coordinate["coordinate_record_id"]
                repair_ids.extend(coordinate["reference_rewrite_ids"])
                if not effective_block_ids:
                    active_coordinate = coordinate.get("active_coordinate")
                    active_coordinates = [active_coordinate] if active_coordinate is not None else [
                        rewrite_by_id[rewrite_id]["active_coordinate"]
                        for rewrite_id in coordinate["reference_rewrite_ids"]
                        if rewrite_id in rewrite_by_id
                    ]
                    if not active_coordinates:
                        raise IntegrityError(f"Human Rulings record lacks active repair coordinate: {legacy_id}")
                    effective_block_ids = list(
                        dict.fromkeys(
                            block_id
                            for active in active_coordinates
                            for block_id in overlapping_blocks(
                                blocks, (active["start"], active["end"])
                            )
                        )
                    )
            if not effective_block_ids or any(block_id not in block_by_id for block_id in effective_block_ids):
                raise IntegrityError(f"migration record lacks valid effective block coordinates: {legacy_id}")

            selected_blocks = [block_by_id[block_id] for block_id in effective_block_ids]
            status_regions = sorted(
                {
                    (region["label"], region["status"], region["handling"])
                    for block_id in effective_block_ids
                    for region in regions_by_block.get(block_id, [])
                }
            )
            status_region_records = [
                {"label": label, "status": status, "handling": handling}
                for label, status, handling in status_regions
            ]
            compound_flag = is_compound_review_quote(quotation)
            if compound_flag:
                gate_3_compound_count += 1
            structural_compound = legacy_id in compound_by_legacy
            if structural_compound:
                structural_compound_count += 1
            risk_tier, risk_signals = _candidate_risk(
                source_id,
                selected_blocks,
                quotation,
                status_region_records,
                compound_flag,
                repair_ids,
            )
            legacy_record_hash = sha256_bytes(canonical_json_bytes(legacy_record))
            evidence_identity = {
                "source_id": source_id,
                "grounding_source_sha256": replay["grounding_source_sha256"],
                "source_location": legacy_record["source_location"],
                "quote_sha256": quote_sha256,
                "effective_block_ids": effective_block_ids,
                "legacy_record_id": legacy_id,
            }
            evidence_id = content_id("e", evidence_identity)
            body = {
                "evidence_id": evidence_id,
                "state": "mechanically_valid",
                "acceptance_state": "not_accepted",
                "review_state": "pending",
                "risk_tier": risk_tier,
                "risk_signals": risk_signals,
                "review_requirement": _review_requirement(risk_tier),
                "source_id": source_id,
                "source_identity_card_id": card["card_id"],
                "active_source_sha256": card["source_sha256"],
                "grounding_source_role": replay["grounding_source_role"],
                "grounding_source_sha256": replay["grounding_source_sha256"],
                "source_location": legacy_record["source_location"],
                "exact_source_text": quotation,
                "quote_sha256": quote_sha256,
                "effective_block_ids": effective_block_ids,
                "explicit_status_regions": status_region_records,
                "allowed_streams": card["allowed_streams"],
                "assigned_stream": None,
                "normalized_claim": None,
                "controlled_claim_kind": None,
                "legacy_record_id": legacy_id,
                "legacy_candidate_record_sha256": legacy_record_hash,
                "legacy_proposals": {
                    field: legacy_record.get(field) for field in LEGACY_PROPOSAL_FIELDS
                },
                "non_imported_legacy_fields": [
                    {
                        "field": field,
                        "payload_sha256": sha256_bytes(
                            canonical_json_bytes(legacy_record.get(field))
                        ),
                    }
                    for field in NON_IMPORTED_FIELDS
                ],
                "legacy_semantic_fields_imported": False,
                "replay_record_id": replay["replay_record_id"],
                "replay_grounding_status": replay["grounding_status"],
                "repair_disposition_ids": sorted(set(repair_ids)),
                "human_rulings_coordinate_record_id": coordinate_record_id,
                "gate_3_compound_review_flag": compound_flag,
                "mapping_state": "not_started",
                "reconciliation_state": "not_started",
                "acceptance_receipt_id": None,
            }
            candidate = {
                "schema_version": "M050-LAYER-E-LEGACY-MIGRATION-CANDIDATE-0.1",
                "migration_candidate_id": content_id("lemc", body),
                **body,
            }
            validate_artifact("layer_e_legacy_migration_candidate", candidate)
            source_candidates.append(candidate)
            for block_id in effective_block_ids:
                candidate_ids_by_block[block_id].append(candidate["migration_candidate_id"])

            if compound_flag or structural_compound:
                review_reasons = []
                if compound_flag:
                    review_reasons.append("gate_3_multi_sentence_indicator")
                if structural_compound:
                    review_reasons.append("cross_block_structural_compound")
                inventory_body = {
                    "migration_candidate_id": candidate["migration_candidate_id"],
                    "evidence_id": evidence_id,
                    "legacy_record_id": legacy_id,
                    "source_id": source_id,
                    "source_location": legacy_record["source_location"],
                    "quote_sha256": quote_sha256,
                    "review_reasons": review_reasons,
                    "gate_3_indicator_pattern": (
                        r"\.\s+(?=[A-Z])" if compound_flag else None
                    ),
                    "minimum_review_tier": 2,
                    "candidate_risk_tier": risk_tier,
                    "review_state": "pending",
                    "split_performed": False,
                }
                inventory = {
                    "schema_version": "M050-LEGACY-COMPOUND-REVIEW-INVENTORY-RECORD-0.1",
                    "compound_review_id": content_id("lcri", inventory_body),
                    **inventory_body,
                }
                validate_artifact("legacy_compound_review_inventory_record", inventory)
                compound_inventory.append(inventory)

        migration_records.extend(source_candidates)

        identity_exclusions = {item["block_id"]: item for item in card["exclusions"]}
        ledger_records: list[dict[str, Any]] = []
        for block in blocks:
            candidate_ids = sorted(candidate_ids_by_block.get(block["block_id"], []))
            status_regions = regions_by_block.get(block["block_id"], [])
            non_normative_status = any(
                region["status"] in {"silent", "process_only", "change_record"}
                for region in status_regions
            )
            if candidate_ids and non_normative_status:
                disposition = "review_required_legacy_candidate_in_non_normative_region"
                reason = "identity_card_non_normative_region_contains_legacy_candidate"
            elif candidate_ids and block["local_disposition"] == "review_required":
                disposition = "review_required_legacy_candidate_in_locally_flagged_block"
                reason = block["local_reason_code"]
            elif candidate_ids:
                disposition = "legacy_migration_candidate_support"
                reason = "one_or_more_mechanically_valid_legacy_candidates_reference_block"
            elif block["local_disposition"] == "excluded":
                disposition = "excluded"
                reason = block["local_reason_code"]
            elif block["local_disposition"] == "context_only":
                disposition = "context_only"
                reason = block["local_reason_code"]
            elif non_normative_status:
                disposition = "excluded_identity_non_normative_region"
                reason = "identity_card_silent_process_or_change_record_region"
            else:
                disposition = "review_required_no_legacy_candidate"
                reason = "eligible_block_has_no_legacy_migration_candidate"
            ledger_body = {
                "source_id": source_id,
                "block_id": block["block_id"],
                "block_sha256": block["raw_sha256"],
                "block_ordinal": block["ordinal"],
                "block_type": block["block_type"],
                "claim_bearing": block["claim_bearing"],
                "local_disposition": block["local_disposition"],
                "local_reason_code": block["local_reason_code"],
                "explicit_status_regions": status_regions,
                "identity_exclusion_id": (
                    identity_exclusions.get(block["block_id"], {}).get("exclusion_id")
                ),
                "migration_candidate_ids": candidate_ids,
                "terminal_disposition": disposition,
                "reason_code": reason,
                "review_state": "pending" if disposition.startswith("review_required") else "mechanically_accounted",
            }
            ledger_record = {
                "schema_version": "M050-RETROSPECTIVE-BLOCK-DISPOSITION-0.1",
                "block_disposition_id": content_id("rbd", ledger_body),
                **ledger_body,
            }
            validate_artifact("retrospective_block_disposition", ledger_record)
            ledger_records.append(ledger_record)
        ledger_bytes = canonical_jsonl_bytes(ledger_records)
        block_ledgers[source_id] = ledger_bytes
        source_summaries.append(
            {
                "source_id": source_id,
                "legacy_records": len(legacy_records),
                "migration_candidates": len(source_candidates),
                "compound_review_records": sum(
                    1 for item in compound_inventory if item["source_id"] == source_id
                ),
                "gate_3_multi_sentence_records": gate_3_compound_count,
                "cross_block_structural_compounds": structural_compound_count,
                "blocks": len(blocks),
                "block_disposition_counts": dict(
                    sorted(Counter(item["terminal_disposition"] for item in ledger_records).items())
                ),
                "risk_tier_counts": {
                    str(key): value
                    for key, value in sorted(Counter(item["risk_tier"] for item in source_candidates).items())
                },
                "block_ledger": _artifact_binding(
                    block_ledger_relative_paths[source_id],
                    ledger_bytes,
                    "retrospective_block_and_exclusion_disposition_ledger",
                ),
            }
        )

    migration_records.sort(key=lambda item: (item["source_id"], item["legacy_record_id"]))
    compound_inventory.sort(key=lambda item: (item["source_id"], item["legacy_record_id"]))
    if len(migration_records) != 913 or len({item["legacy_record_id"] for item in migration_records}) != 913:
        raise IntegrityError("Layer E migration must account for exactly 913 unique legacy records")
    expected_compounds = {
        "M050-SRC-CROSSING-001": 2,
        "M050-SRC-HUMAN-RULINGS-001": 21,
        "M050-SRC-MSID-GRAMMAR-001": 31,
        "M050-SRC-PA-001": 69,
    }
    actual_gate_3_compounds = Counter(
        item["source_id"]
        for item in compound_inventory
        if "gate_3_multi_sentence_indicator" in item["review_reasons"]
    )
    if sum(actual_gate_3_compounds.values()) != 123 or dict(actual_gate_3_compounds) != expected_compounds:
        raise IntegrityError(
            f"Gate 3 compound review queue drift: expected {expected_compounds}, got {dict(actual_gate_3_compounds)}"
        )
    structural_ids = {
        item["legacy_record_id"]
        for item in compound_inventory
        if "cross_block_structural_compound" in item["review_reasons"]
    }
    if structural_ids != set(compound_by_legacy):
        raise IntegrityError("compound review inventory does not include all 17 cross-block records")
    overlap = sum(
        set(item["review_reasons"])
        == {"gate_3_multi_sentence_indicator", "cross_block_structural_compound"}
        for item in compound_inventory
    )
    if len(compound_inventory) != 139 or overlap != 1:
        raise IntegrityError("unified compound review inventory must contain 139 records with one overlap")

    candidate_bytes = canonical_jsonl_bytes(migration_records)
    compound_bytes = canonical_jsonl_bytes(compound_inventory)
    body = {
        "migration_version": MIGRATION_VERSION,
        "repair_closure": {
            "path": str(repair_closure_path.resolve().relative_to(repo_root)),
            "sha256": sha256_file(repair_closure_path),
            "role": "passed_legacy_mechanical_repair_closure",
        },
        "migration_candidates": _artifact_binding(
            candidate_relative_path, candidate_bytes, "mechanically_valid_unaccepted_layer_e_candidates"
        ),
        "compound_review_inventory": _artifact_binding(
            compound_relative_path, compound_bytes, "complete_gate_3_compound_review_queue"
        ),
        "source_summaries": source_summaries,
        "legacy_record_count": 913,
        "migration_candidate_count": 913,
        "distinct_legacy_record_ids": 913,
        "compound_review_count": 139,
        "compound_review_source_counts": dict(
            sorted(Counter(item["source_id"] for item in compound_inventory).items())
        ),
        "gate_3_multi_sentence_review_count": 123,
        "gate_3_multi_sentence_source_counts": dict(sorted(actual_gate_3_compounds.items())),
        "cross_block_structural_compound_count": 17,
        "compound_queue_overlap_count": overlap,
        "retrospective_block_ledgers": 4,
        "all_source_blocks_accounted": True,
        "legacy_semantic_fields_imported": 0,
        "accepted_evidence_records": 0,
        "semantic_reviews_performed": 0,
        "mapping_records_created": 0,
        "reconciliation_records_created": 0,
        "provider_calls": 0,
        "accounted_cost_cents": 0,
        "google_sheets_interactions": 0,
        "passed": True,
    }
    report = {
        "schema_version": "M050-LAYER-E-LEGACY-MIGRATION-REPORT-0.1",
        "migration_report_id": content_id("lemr", body),
        **body,
    }
    validate_artifact("layer_e_legacy_migration_report", report)
    return candidate_bytes, compound_bytes, block_ledgers, report
