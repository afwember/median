from __future__ import annotations

from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Iterable

from .bindings import repository_file
from .canonical import canonical_json_bytes, content_id, sha256_bytes, sha256_file
from .errors import ContractError, IntegrityError
from .legacy import canonical_jsonl_bytes
from .review import select_tier3_sample
from .schema import validate_artifact


PLANNER_VERSION = "M050-LEGACY-SEMANTIC-REVIEW-PLANNER-0.1"
MAX_BUNDLE_MEMBERS = 12
MAX_BUNDLE_TEXT_CHARACTERS = 12_000
TIER3_SAMPLE_RATE = 0.05

def _read_json(path: Path) -> dict[str, Any]:
    import json

    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ContractError(f"JSON root must be an object: {path}")
    return value


def _read_jsonl(path: Path) -> list[dict[str, Any]]:
    import json

    records: list[dict[str, Any]] = []
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not line.strip():
            raise ContractError(f"blank JSONL line at {path}:{line_number}")
        value = json.loads(line)
        if not isinstance(value, dict):
            raise ContractError(f"non-object JSONL record at {path}:{line_number}")
        records.append(value)
    return records


def _bound_file(repo_root: Path, binding: dict[str, Any]) -> Path:
    relative = binding.get("path", "")
    target = repository_file(repo_root, relative)
    if target is None:
        raise IntegrityError(f"review-plan binding is not a file: {relative}")
    if sha256_file(target) != binding.get("sha256"):
        raise IntegrityError(f"review-plan binding hash mismatch: {relative}")
    return target


def _artifact_binding(path: str, data: bytes, role: str) -> dict[str, str]:
    return {"path": path, "sha256": sha256_bytes(data), "role": role}


def _chunks(items: list[dict[str, Any]], text_key: str) -> Iterable[list[dict[str, Any]]]:
    current: list[dict[str, Any]] = []
    characters = 0
    for item in items:
        item_characters = len(item[text_key])
        if current and (
            len(current) >= MAX_BUNDLE_MEMBERS
            or characters + item_characters > MAX_BUNDLE_TEXT_CHARACTERS
        ):
            yield current
            current = []
            characters = 0
        current.append(item)
        characters += item_characters
    if current:
        yield current


def _section_key(candidate: dict[str, Any], blocks: dict[str, dict[str, Any]]) -> str:
    selected = [blocks[block_id] for block_id in candidate["effective_block_ids"]]
    selected.sort(key=lambda block: block["ordinal"])
    return selected[0].get("parent_heading") or "<ROOT>"


def _reviewer_fields(tier: int, selected_for_sample: bool) -> tuple[str, str, str]:
    if tier == 1:
        return (
            "Asa Wember — author decision pending",
            "Author is the sole substantive authority for Tier 1 decisions; legacy proposals are non-authoritative context.",
            "exhaustive_author_decision_required",
        )
    if tier == 2:
        return (
            "Independent semantic reviewer — unassigned",
            "Reviewer must independently compare exact source context with the quarantined legacy proposal and may not rely on extractor reasoning.",
            "exhaustive_independent_semantic_review_required",
        )
    if selected_for_sample:
        return (
            "Risk-weighted sampling reviewer — unassigned",
            "This bundle was selected by the pinned deterministic Tier 3 sampling rule.",
            "risk_weighted_sample_selected",
        )
    return (
        "Deterministic Tier 3 batch — review not yet assigned",
        "Human review is contingent on the fixed sample and anomaly queues passing; deterministic acceptance remains unperformed.",
        "eligible_not_selected_for_initial_sample",
    )


def _candidate_groups(
    candidates: list[dict[str, Any]],
    blocks_by_source: dict[str, dict[str, dict[str, Any]]],
) -> list[dict[str, Any]]:
    grouped: dict[tuple[str, int, str], list[dict[str, Any]]] = defaultdict(list)
    for candidate in candidates:
        source_id = candidate["source_id"]
        section = _section_key(candidate, blocks_by_source[source_id])
        grouped[(source_id, candidate["risk_tier"], section)].append(candidate)

    groups: list[dict[str, Any]] = []
    for (source_id, risk_tier, section), records in sorted(grouped.items()):
        block_map = blocks_by_source[source_id]
        records.sort(
            key=lambda item: (
                min(block_map[block_id]["ordinal"] for block_id in item["effective_block_ids"]),
                item["legacy_record_id"],
            )
        )
        for part in _chunks(records, "exact_source_text"):
            groups.append(
                {
                    "source_id": source_id,
                    "risk_tier": risk_tier,
                    "section": section,
                    "candidates": part,
                }
            )
    groups.sort(
        key=lambda group: (
            group["risk_tier"],
            group["source_id"],
            min(
                blocks_by_source[group["source_id"]][block_id]["ordinal"]
                for item in group["candidates"]
                for block_id in item["effective_block_ids"]
            ),
            group["section"],
        )
    )
    return groups


def _build_candidate_bundles(
    candidates: list[dict[str, Any]],
    blocks_by_source: dict[str, dict[str, dict[str, Any]]],
    compounds_by_candidate: dict[str, list[dict[str, Any]]],
    *,
    tier3_seed: str,
) -> list[dict[str, Any]]:
    groups = _candidate_groups(candidates, blocks_by_source)
    tier3_groups = [group for group in groups if group["risk_tier"] == 3]
    tier3_selection_input = []
    for ordinal, group in enumerate(tier3_groups, start=1):
        block_ids = {
            block_id
            for candidate in group["candidates"]
            for block_id in candidate["effective_block_ids"]
        }
        compound_count = sum(
            bool(compounds_by_candidate.get(candidate["migration_candidate_id"]))
            for candidate in group["candidates"]
        )
        tier3_selection_input.append(
            {
                "ordinal": ordinal,
                "claim_bearing_blocks": len(block_ids),
                "review_risk": compound_count * 10
                + sum(len(candidate["risk_signals"]) for candidate in group["candidates"]),
            }
        )
    selected_tier3_ordinals = set(
        select_tier3_sample(
            tier3_selection_input,
            seed=tier3_seed,
            rate=TIER3_SAMPLE_RATE,
        )
    )
    tier3_ordinal_by_group = {id(group): ordinal for ordinal, group in enumerate(tier3_groups, 1)}

    bundles: list[dict[str, Any]] = []
    for ordinal, group in enumerate(groups, start=1):
        source_id = group["source_id"]
        risk_tier = group["risk_tier"]
        candidates_in_group = group["candidates"]
        block_map = blocks_by_source[source_id]
        selected_for_sample = (
            risk_tier == 3
            and tier3_ordinal_by_group[id(group)] in selected_tier3_ordinals
        )
        reviewer, independence_basis, sampling_state = _reviewer_fields(
            risk_tier, selected_for_sample
        )
        member_ids = [item["migration_candidate_id"] for item in candidates_in_group]
        context_block_ids = sorted(
            {
                block_id
                for item in candidates_in_group
                for block_id in item["effective_block_ids"]
            },
            key=lambda block_id: block_map[block_id]["ordinal"],
        )
        members = []
        compound_ids: list[str] = []
        for candidate in candidates_in_group:
            compound_records = compounds_by_candidate.get(candidate["migration_candidate_id"], [])
            compound_ids.extend(record["compound_review_id"] for record in compound_records)
            members.append(
                {
                    "migration_candidate_id": candidate["migration_candidate_id"],
                    "evidence_id": candidate["evidence_id"],
                    "legacy_record_id": candidate["legacy_record_id"],
                    "source_location": candidate["source_location"],
                    "quote_sha256": candidate["quote_sha256"],
                    "exact_source_text": candidate["exact_source_text"],
                    "effective_block_ids": candidate["effective_block_ids"],
                    "risk_signals": candidate["risk_signals"],
                    "repair_disposition_ids": candidate["repair_disposition_ids"],
                    "legacy_proposals": candidate["legacy_proposals"],
                    "compound_review_ids": [
                        record["compound_review_id"] for record in compound_records
                    ],
                    "compound_review_reasons": sorted(
                        {
                            reason
                            for record in compound_records
                            for reason in record["review_reasons"]
                        }
                    ),
                }
            )
        body = {
            "ordinal": ordinal,
            "risk_tier": risk_tier,
            "source_id": source_id,
            "source_identity_card_id": candidates_in_group[0]["source_identity_card_id"],
            "section": group["section"],
            "member_ids": member_ids,
            "membership_sha256": sha256_bytes(canonical_json_bytes(member_ids)),
            "members": members,
            "context_blocks": [
                {
                    "block_id": block_id,
                    "block_sha256": block_map[block_id]["raw_sha256"],
                    "ordinal": block_map[block_id]["ordinal"],
                    "block_type": block_map[block_id]["block_type"],
                    "parent_heading": block_map[block_id].get("parent_heading"),
                    "text": block_map[block_id]["text"],
                }
                for block_id in context_block_ids
            ],
            "compound_review_ids": sorted(set(compound_ids)),
            "reviewer": reviewer,
            "independence_basis": independence_basis,
            "sampling_state": sampling_state,
            "disposition": "pending",
            "semantic_review_performed": False,
            "accepted_evidence_records": 0,
            "mapping_authorized": False,
            "reconciliation_authorized": False,
            "compilation_authorized": False,
        }
        bundle = {
            "schema_version": "M050-LAYER-E-LEGACY-SEMANTIC-REVIEW-BUNDLE-0.1",
            "review_bundle_id": content_id("lesrb", body),
            **body,
        }
        validate_artifact("legacy_semantic_review_bundle", bundle)
        bundles.append(bundle)
    return bundles


def _build_coverage_bundles(
    ledger_records: list[dict[str, Any]],
    blocks_by_source: dict[str, dict[str, dict[str, Any]]],
) -> list[dict[str, Any]]:
    uncovered = [
        record
        for record in ledger_records
        if record["terminal_disposition"] == "review_required_no_legacy_candidate"
    ]
    grouped: dict[tuple[str, str], list[dict[str, Any]]] = defaultdict(list)
    for record in uncovered:
        block = blocks_by_source[record["source_id"]][record["block_id"]]
        grouped[(record["source_id"], block.get("parent_heading") or "<ROOT>")].append(
            {**record, "text": block["text"], "estimated_claims": block["estimated_claims"]}
        )
    groups: list[tuple[str, str, list[dict[str, Any]]]] = []
    for (source_id, section), records in sorted(grouped.items()):
        records.sort(key=lambda item: item["block_ordinal"])
        for part in _chunks(records, "text"):
            groups.append((source_id, section, part))
    groups.sort(key=lambda item: (item[0], item[2][0]["block_ordinal"], item[1]))

    bundles: list[dict[str, Any]] = []
    for ordinal, (source_id, section, records) in enumerate(groups, start=1):
        member_ids = [record["block_id"] for record in records]
        body = {
            "ordinal": ordinal,
            "source_id": source_id,
            "section": section,
            "member_ids": member_ids,
            "membership_sha256": sha256_bytes(canonical_json_bytes(member_ids)),
            "members": [
                {
                    "block_disposition_id": record["block_disposition_id"],
                    "block_id": record["block_id"],
                    "block_sha256": record["block_sha256"],
                    "block_ordinal": record["block_ordinal"],
                    "block_type": record["block_type"],
                    "estimated_claims": record["estimated_claims"],
                    "text": record["text"],
                    "reason_code": record["reason_code"],
                }
                for record in records
            ],
            "review_requirement": "determine_fresh_extraction_or_nonclaim_disposition",
            "reviewer": "Coverage reviewer — unassigned",
            "disposition": "pending",
            "fresh_extraction_required": None,
            "semantic_review_performed": False,
            "provider_calls": 0,
        }
        bundle = {
            "schema_version": "M050-UNCOVERED-BLOCK-REVIEW-BUNDLE-0.1",
            "coverage_bundle_id": content_id("ubrb", body),
            **body,
        }
        validate_artifact("legacy_uncovered_block_review_bundle", bundle)
        bundles.append(bundle)
    return bundles


def _build_transitions(
    candidates: list[dict[str, Any]],
    bundles: list[dict[str, Any]],
    *,
    migration_receipt_sha256: str,
    effective_date: str,
) -> list[dict[str, Any]]:
    bundle_by_candidate = {
        candidate_id: bundle
        for bundle in bundles
        for candidate_id in bundle["member_ids"]
    }
    transitions: list[dict[str, Any]] = []
    for candidate in candidates:
        candidate_id = candidate["migration_candidate_id"]
        bundle = bundle_by_candidate.get(candidate_id)
        if bundle is None:
            raise IntegrityError(f"candidate lacks a review bundle: {candidate_id}")
        body = {
            "artifact_id": candidate_id,
            "artifact_sha256": sha256_bytes(canonical_json_bytes(candidate)),
            "prior_state": "mechanically_valid",
            "new_state": "semantic_review_pending",
            "reason": "assigned_to_hash_bound_risk_tier_review_bundle",
            "authority": "M050 Layer E Legacy Migration Transition Control",
            "tool_version": PLANNER_VERSION,
            "effective_date": effective_date,
            "predecessor_receipt_sha256": migration_receipt_sha256,
            "review_bundle_id": bundle["review_bundle_id"],
            "risk_tier": candidate["risk_tier"],
            "review_requirement": candidate["review_requirement"],
            "semantic_review_performed": False,
            "acceptance_state": "not_accepted",
        }
        transition = {
            "schema_version": "M050-LEGACY-EVIDENCE-REVIEW-TRANSITION-0.1",
            "transition_receipt_id": content_id("lert", body),
            **body,
        }
        validate_artifact("legacy_evidence_review_transition", transition)
        transitions.append(transition)
    transitions.sort(key=lambda record: record["artifact_id"])
    return transitions


EFFORT_POLICY = {
    "lower": {
        "tier_1_member": 5,
        "tier_1_bundle": 3,
        "tier_2_member": 2,
        "tier_2_bundle": 3,
        "compound_member_premium": 1,
        "tier_3_sampled_member": 2,
        "tier_3_sampled_bundle": 3,
        "uncovered_block": 1,
        "coverage_bundle": 3,
    },
    "expected": {
        "tier_1_member": 8,
        "tier_1_bundle": 5,
        "tier_2_member": 3,
        "tier_2_bundle": 5,
        "compound_member_premium": 2,
        "tier_3_sampled_member": 3,
        "tier_3_sampled_bundle": 5,
        "uncovered_block": 2,
        "coverage_bundle": 5,
    },
    "upper": {
        "tier_1_member": 12,
        "tier_1_bundle": 8,
        "tier_2_member": 5,
        "tier_2_bundle": 8,
        "compound_member_premium": 4,
        "tier_3_sampled_member": 5,
        "tier_3_sampled_bundle": 8,
        "uncovered_block": 4,
        "coverage_bundle": 8,
    },
}


def _effort_projection(
    bundles: list[dict[str, Any]], coverage_bundles: list[dict[str, Any]]
) -> dict[str, Any]:
    tier_bundle_counts = Counter(bundle["risk_tier"] for bundle in bundles)
    tier_member_counts = Counter(
        bundle["risk_tier"] for bundle in bundles for _ in bundle["member_ids"]
    )
    sampled = [
        bundle
        for bundle in bundles
        if bundle["sampling_state"] == "risk_weighted_sample_selected"
    ]
    compound_members = len(
        {
            member["migration_candidate_id"]
            for bundle in bundles
            for member in bundle["members"]
            if member["compound_review_ids"]
        }
    )
    uncovered_blocks = sum(len(bundle["member_ids"]) for bundle in coverage_bundles)
    scenarios: dict[str, Any] = {}
    for label, rates in EFFORT_POLICY.items():
        components = {
            "tier_1": tier_member_counts[1] * rates["tier_1_member"]
            + tier_bundle_counts[1] * rates["tier_1_bundle"],
            "tier_2": tier_member_counts[2] * rates["tier_2_member"]
            + tier_bundle_counts[2] * rates["tier_2_bundle"],
            "compound_complexity_premium": compound_members
            * rates["compound_member_premium"],
            "tier_3_initial_sample": sum(len(bundle["member_ids"]) for bundle in sampled)
            * rates["tier_3_sampled_member"]
            + len(sampled) * rates["tier_3_sampled_bundle"],
            "uncovered_block_review": uncovered_blocks * rates["uncovered_block"]
            + len(coverage_bundles) * rates["coverage_bundle"],
        }
        scenarios[label] = {"components_minutes": components, "total_minutes": sum(components.values())}
    return {
        "policy": EFFORT_POLICY,
        "counts": {
            "tier_1_members": tier_member_counts[1],
            "tier_1_bundles": tier_bundle_counts[1],
            "tier_2_members": tier_member_counts[2],
            "tier_2_bundles": tier_bundle_counts[2],
            "tier_3_members": tier_member_counts[3],
            "tier_3_bundles": tier_bundle_counts[3],
            "tier_3_sampled_members": sum(len(bundle["member_ids"]) for bundle in sampled),
            "tier_3_sampled_bundles": len(sampled),
            "compound_members": compound_members,
            "uncovered_blocks": uncovered_blocks,
            "coverage_bundles": len(coverage_bundles),
        },
        "scenarios": scenarios,
        "interpretation": "Planning estimate only. Semantic review, author decisions, and acceptance remain unperformed.",
    }


def build_legacy_semantic_review_plan(
    *,
    repo_root: Path,
    migration_receipt_path: Path,
    candidate_bundle_relative_path: str,
    coverage_bundle_relative_path: str,
    transition_relative_path: str,
    effective_date: str,
    tier3_seed: str,
) -> tuple[bytes, bytes, bytes, dict[str, Any]]:
    migration_receipt = _read_json(migration_receipt_path)
    if migration_receipt.get("status") != "LAYER_E_LEGACY_MIGRATION_CANDIDATES_COMPLETE":
        raise IntegrityError("review planning requires the completed Layer E legacy migration receipt")
    migration_receipt_sha256 = sha256_file(migration_receipt_path)
    artifacts = migration_receipt["artifacts"]
    candidates = _read_jsonl(_bound_file(repo_root, artifacts["migration_candidates"]))
    compounds = _read_jsonl(_bound_file(repo_root, artifacts["compound_review_inventory"]))
    if len(candidates) != 913 or Counter(item["risk_tier"] for item in candidates) != {
        1: 18,
        2: 858,
        3: 37,
    }:
        raise IntegrityError("legacy review-plan candidate coverage or risk tiers drifted")
    if len(compounds) != 139:
        raise IntegrityError("legacy review-plan compound inventory must contain 139 records")

    expected_cards: dict[str, str] = {}
    for candidate in candidates:
        source_id = candidate["source_id"]
        card_id = candidate["source_identity_card_id"]
        if source_id in expected_cards and expected_cards[source_id] != card_id:
            raise IntegrityError(f"migration candidates bind multiple source cards: {source_id}")
        expected_cards[source_id] = card_id
    card_directory = repo_root / "m050/extraction/control/source-identities/cards"
    approved_card_paths: dict[str, Path] = {}
    for card_path in sorted(card_directory.glob("*.json")):
        card = _read_json(card_path)
        card_id = card.get("card_id")
        if card.get("status") == "approved" and card_id in expected_cards.values():
            if card_id in approved_card_paths:
                raise IntegrityError(f"duplicate approved source card ID: {card_id}")
            approved_card_paths[card_id] = card_path

    blocks_by_source: dict[str, dict[str, dict[str, Any]]] = {}
    source_bindings: list[dict[str, Any]] = []
    for source_id, card_id in sorted(expected_cards.items()):
        card_path = approved_card_paths.get(card_id)
        if card_path is None:
            raise IntegrityError(f"missing approved source card: {source_id} {card_id}")
        card_relative = card_path.relative_to(repo_root).as_posix()
        card = _read_json(card_path)
        if (
            card.get("source_id") != source_id
            or card.get("card_id") != card_id
            or card.get("status") != "approved"
        ):
            raise IntegrityError(f"review planning requires approved source card: {source_id}")
        manifest_path = _bound_file(repo_root, card["block_manifest_binding"])
        manifest = _read_json(manifest_path)
        blocks_by_source[source_id] = {block["block_id"]: block for block in manifest["blocks"]}
        source_bindings.append(
            {
                "source_id": source_id,
                "source_identity_card": {
                    "path": card_relative,
                    "sha256": sha256_file(card_path),
                    "role": "approved_source_identity_card",
                },
                "block_manifest": card["block_manifest_binding"],
            }
        )

    compounds_by_candidate: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for record in compounds:
        compounds_by_candidate[record["migration_candidate_id"]].append(record)
    bundles = _build_candidate_bundles(
        candidates,
        blocks_by_source,
        compounds_by_candidate,
        tier3_seed=tier3_seed,
    )

    ledger_records: list[dict[str, Any]] = []
    for key, binding in sorted(artifacts.items()):
        if key.endswith("_block_ledger"):
            ledger_records.extend(_read_jsonl(_bound_file(repo_root, binding)))
    coverage_bundles = _build_coverage_bundles(ledger_records, blocks_by_source)
    transitions = _build_transitions(
        candidates,
        bundles,
        migration_receipt_sha256=migration_receipt_sha256,
        effective_date=effective_date,
    )
    if len(bundles) == 0 or sum(len(bundle["member_ids"]) for bundle in bundles) != 913:
        raise IntegrityError("semantic review bundles do not account for all 913 candidates")
    if len({candidate_id for bundle in bundles for candidate_id in bundle["member_ids"]}) != 913:
        raise IntegrityError("semantic review bundle membership is duplicated")
    if len({compound_id for bundle in bundles for compound_id in bundle["compound_review_ids"]}) != 139:
        raise IntegrityError("semantic review bundles do not preserve all 139 compound records")
    if sum(len(bundle["member_ids"]) for bundle in coverage_bundles) != 518:
        raise IntegrityError("coverage review bundles do not account for all 518 uncovered blocks")
    if len(transitions) != 913:
        raise IntegrityError("review transition ledger must contain exactly 913 receipts")

    candidate_bytes = canonical_jsonl_bytes(bundles)
    coverage_bytes = canonical_jsonl_bytes(coverage_bundles)
    transition_bytes = canonical_jsonl_bytes(transitions)
    effort = _effort_projection(bundles, coverage_bundles)
    body = {
        "planner_version": PLANNER_VERSION,
        "effective_date": effective_date,
        "migration_receipt": {
            "path": str(migration_receipt_path.resolve().relative_to(repo_root)),
            "sha256": migration_receipt_sha256,
            "role": "completed_layer_e_legacy_migration_receipt",
        },
        "source_bindings": source_bindings,
        "candidate_review_bundles": _artifact_binding(
            candidate_bundle_relative_path,
            candidate_bytes,
            "hash_bound_semantic_review_bundle_inventory",
        ),
        "uncovered_block_review_bundles": _artifact_binding(
            coverage_bundle_relative_path,
            coverage_bytes,
            "hash_bound_uncovered_block_review_bundle_inventory",
        ),
        "review_transition_ledger": _artifact_binding(
            transition_relative_path,
            transition_bytes,
            "mechanically_valid_to_semantic_review_pending_transition_receipts",
        ),
        "candidate_records": 913,
        "candidate_review_bundle_count": len(bundles),
        "risk_tier_candidate_counts": {
            str(tier): count for tier, count in sorted(Counter(item["risk_tier"] for item in candidates).items())
        },
        "risk_tier_bundle_counts": {
            str(tier): count for tier, count in sorted(Counter(item["risk_tier"] for item in bundles).items())
        },
        "compound_review_records_preserved": 139,
        "uncovered_blocks": 518,
        "uncovered_block_review_bundle_count": len(coverage_bundles),
        "review_transition_receipts": 913,
        "initial_state": "mechanically_valid",
        "new_state": "semantic_review_pending",
        "tier3_sampling": {
            "seed": tier3_seed,
            "rate_numerator": 5,
            "rate_denominator": 100,
            "selected_bundle_ids": [
                bundle["review_bundle_id"]
                for bundle in bundles
                if bundle["sampling_state"] == "risk_weighted_sample_selected"
            ],
        },
        "human_effort_projection": effort,
        "semantic_reviews_performed": 0,
        "author_decisions_recorded": 0,
        "accepted_evidence_records": 0,
        "mapping_records_created": 0,
        "reconciliation_records_created": 0,
        "compilation_records_created": 0,
        "provider_calls": 0,
        "accounted_cost_cents": 0,
        "google_sheets_interactions": 0,
        "passed": True,
    }
    report = {
        "schema_version": "M050-LEGACY-SEMANTIC-REVIEW-PLAN-REPORT-0.1",
        "review_plan_id": content_id("lesrp", body),
        **body,
    }
    validate_artifact("legacy_semantic_review_plan_report", report)
    return candidate_bytes, coverage_bytes, transition_bytes, report
