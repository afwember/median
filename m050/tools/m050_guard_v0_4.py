#!/usr/bin/env python3
"""Verify the MEDIAN Gate 5 review-queued offline foundation."""

from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import importlib.util
import json
import pathlib
import sys


REPO_ROOT = pathlib.Path(__file__).resolve().parents[2]
PRIOR_GUARD_PATH = REPO_ROOT / "m050/tools/m050_guard_v0_3.py"
ACTIVE_INDEX = REPO_ROOT / "m050/extraction/control/M050_Active_Control_Index_v0_9_MEDIANv0_5_0.json"
PLANNING_RECEIPT = REPO_ROOT / "m050/extraction/audit/M050_Extraction_Gate_5_Semantic_Review_Planning_Receipt_v0_1_MEDIANv0_5_0.json"
PLANNING_REPORT = REPO_ROOT / "m050/extraction/review/M050_Layer_E_Legacy_Semantic_Review_Plan_Report_v0_1_MEDIANv0_5_0.json"
CANDIDATE_BUNDLES = REPO_ROOT / "m050/extraction/review/M050_Layer_E_Legacy_Semantic_Review_Bundle_Inventory_v0_1_MEDIANv0_5_0.jsonl"
COVERAGE_BUNDLES = REPO_ROOT / "m050/extraction/review/M050_Legacy_Uncovered_Block_Review_Bundle_Inventory_v0_1_MEDIANv0_5_0.jsonl"
TRANSITIONS = REPO_ROOT / "m050/extraction/review/M050_Layer_E_Legacy_Semantic_Review_Transition_Ledger_v0_1_MEDIANv0_5_0.jsonl"
MIGRATION_CANDIDATES = REPO_ROOT / "m050/extraction/migration/M050_Layer_E_Legacy_Migration_Candidates_v0_1_MEDIANv0_5_0.jsonl"
RELOCATION_MANIFEST = REPO_ROOT / "m050/extraction/evidence/legacy/M050_Legacy_Evidence_Relocation_Manifest_v0_1_MEDIANv0_5_0.json"
ARCHIVE_RECEIPT = REPO_ROOT / "m050/extraction/audit/M050_Extraction_Gate_5_Archive_Retirement_Receipt_v0_1_MEDIANv0_5_0.json"


def _load_prior_guard():
    spec = importlib.util.spec_from_file_location("m050_guard_v0_3", PRIOR_GUARD_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load predecessor Gate 5 guard")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


PRIOR = _load_prior_guard()


def canonical_bytes(value: object) -> bytes:
    return json.dumps(
        value, ensure_ascii=False, allow_nan=False, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: pathlib.Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def content_id(prefix: str, value: object) -> str:
    return f"{prefix}_{sha256_bytes(canonical_bytes(value))[:24]}"


def read_json(path: pathlib.Path, errors: list[str]) -> dict:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"cannot read JSON {path.relative_to(REPO_ROOT)}: {exc}")
        return {}
    if not isinstance(value, dict):
        errors.append(f"JSON root is not an object: {path.relative_to(REPO_ROOT)}")
        return {}
    return value


def read_jsonl(path: pathlib.Path, errors: list[str]) -> list[dict]:
    records: list[dict] = []
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except OSError as exc:
        errors.append(f"cannot read JSONL {path.relative_to(REPO_ROOT)}: {exc}")
        return records
    for number, line in enumerate(lines, 1):
        try:
            value = json.loads(line)
        except json.JSONDecodeError as exc:
            errors.append(f"invalid JSONL at {path.relative_to(REPO_ROOT)}:{number}: {exc}")
            continue
        if not isinstance(value, dict):
            errors.append(f"non-object JSONL at {path.relative_to(REPO_ROOT)}:{number}")
            continue
        records.append(value)
    return records


def validate_active_index(errors: list[str]) -> None:
    index = read_json(ACTIVE_INDEX, errors)
    if index.get("execution_state") != "GATE_5_LAYER_E_SEMANTIC_REVIEW_QUEUED":
        errors.append("active control index has unexpected execution state")
    if index.get("provider_call_authorized") is not False:
        errors.append("active control index does not prohibit provider calls")
    if index.get("google_sheets_interaction_authorized") is not False:
        errors.append("active control index does not preserve the Google Sheets pause")
    review = index.get("review_state", {})
    expected = {
        "candidate_review_bundles": 181,
        "tier_1_candidates": 18,
        "tier_1_bundles": 5,
        "tier_2_candidates": 858,
        "tier_2_bundles": 164,
        "tier_3_candidates": 37,
        "tier_3_bundles": 12,
        "tier_3_sampled_bundles": 3,
        "tier_3_sampled_candidates": 16,
        "compound_records_preserved": 139,
        "uncovered_block_review_bundles": 132,
        "uncovered_blocks": 518,
        "review_transition_receipts": 913,
        "semantic_reviews_performed": 0,
        "author_decisions_recorded": 0,
        "layer_e_acceptances": 0,
    }
    if any(review.get(key) != value for key, value in expected.items()):
        errors.append("active control index review state drifted")
    if any(review.get(key) is not False for key in ("mapping_started", "reconciliation_started", "compilation_started")):
        errors.append("active control index starts an unauthorized downstream layer")
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


def validate_retired_archive(errors: list[str]) -> int:
    if (REPO_ROOT / "m050/archive").exists():
        errors.append("retired m050/archive directory has reappeared")
    manifest = read_json(RELOCATION_MANIFEST, errors)
    receipt = read_json(ARCHIVE_RECEIPT, errors)
    items = manifest.get("relocations", manifest.get("items", []))
    if not isinstance(items, list) or len(items) != 12:
        errors.append("legacy evidence relocation manifest must contain 12 records")
        return 0
    seen: set[str] = set()
    for item in items:
        relative = item.get("relocated_path") or item.get("current_path") or item.get("path")
        if not isinstance(relative, str) or relative in seen:
            errors.append(f"invalid or duplicate relocated evidence path: {relative}")
            continue
        seen.add(relative)
        target = REPO_ROOT / relative
        if not target.is_file() or sha256_file(target) != item.get("sha256"):
            errors.append(f"relocated legacy evidence is missing or changed: {relative}")
    if receipt.get("status") != "ARCHIVE_RETIRED_EVIDENCE_RELOCATED":
        errors.append("archive retirement receipt has unexpected status")
    return len(seen)


def validate_review_plan(errors: list[str]) -> tuple[int, int, int, int]:
    report = read_json(PLANNING_REPORT, errors)
    receipt = read_json(PLANNING_RECEIPT, errors)
    bundles = read_jsonl(CANDIDATE_BUNDLES, errors)
    coverage = read_jsonl(COVERAGE_BUNDLES, errors)
    transitions = read_jsonl(TRANSITIONS, errors)
    candidates = read_jsonl(MIGRATION_CANDIDATES, errors)
    candidate_by_id = {record.get("migration_candidate_id"): record for record in candidates}

    membership: dict[str, str] = {}
    compound_ids: set[str] = set()
    tier_members: Counter[int] = Counter()
    tier_bundles: Counter[int] = Counter()
    sampled_members = 0
    sampled_bundles = 0
    for bundle in bundles:
        body = {key: value for key, value in bundle.items() if key not in {"schema_version", "review_bundle_id"}}
        if bundle.get("review_bundle_id") != content_id("lesrb", body):
            errors.append(f"review bundle content ID mismatch: {bundle.get('review_bundle_id')}")
        member_ids = bundle.get("member_ids", [])
        if bundle.get("membership_sha256") != sha256_bytes(canonical_bytes(member_ids)):
            errors.append(f"review bundle membership hash mismatch: {bundle.get('review_bundle_id')}")
        tier = bundle.get("risk_tier")
        tier_bundles[tier] += 1
        tier_members[tier] += len(member_ids)
        for candidate_id in member_ids:
            if candidate_id in membership:
                errors.append(f"candidate appears in multiple review bundles: {candidate_id}")
            membership[candidate_id] = bundle.get("review_bundle_id")
        compound_ids.update(bundle.get("compound_review_ids", []))
        if bundle.get("sampling_state") == "risk_weighted_sample_selected":
            sampled_bundles += 1
            sampled_members += len(member_ids)
    if len(bundles) != 181 or tier_bundles != {1: 5, 2: 164, 3: 12}:
        errors.append("semantic review bundle counts drifted")
    if len(membership) != 913 or tier_members != {1: 18, 2: 858, 3: 37}:
        errors.append("semantic review candidate coverage drifted")
    if set(candidate_by_id) != set(membership):
        errors.append("review bundle candidates differ from migration candidates")
    if len(compound_ids) != 139:
        errors.append("review bundles do not preserve all 139 compound records")
    if (sampled_bundles, sampled_members) != (3, 16):
        errors.append("Tier 3 pinned sample drifted")

    coverage_ids: set[str] = set()
    for bundle in coverage:
        body = {key: value for key, value in bundle.items() if key not in {"schema_version", "coverage_bundle_id"}}
        if bundle.get("coverage_bundle_id") != content_id("ubrb", body):
            errors.append(f"coverage bundle content ID mismatch: {bundle.get('coverage_bundle_id')}")
        member_ids = bundle.get("member_ids", [])
        if bundle.get("membership_sha256") != sha256_bytes(canonical_bytes(member_ids)):
            errors.append(f"coverage bundle membership hash mismatch: {bundle.get('coverage_bundle_id')}")
        for block_id in member_ids:
            if block_id in coverage_ids:
                errors.append(f"uncovered block appears in multiple bundles: {block_id}")
            coverage_ids.add(block_id)
    if len(coverage) != 132 or len(coverage_ids) != 518:
        errors.append("uncovered block review coverage drifted")

    transition_ids: set[str] = set()
    for transition in transitions:
        body = {key: value for key, value in transition.items() if key not in {"schema_version", "transition_receipt_id"}}
        if transition.get("transition_receipt_id") != content_id("lert", body):
            errors.append(f"review transition content ID mismatch: {transition.get('artifact_id')}")
        candidate_id = transition.get("artifact_id")
        candidate = candidate_by_id.get(candidate_id)
        if candidate is None:
            errors.append(f"review transition references unknown candidate: {candidate_id}")
            continue
        if transition.get("artifact_sha256") != sha256_bytes(canonical_bytes(candidate)):
            errors.append(f"review transition candidate hash mismatch: {candidate_id}")
        if transition.get("review_bundle_id") != membership.get(candidate_id):
            errors.append(f"review transition bundle mismatch: {candidate_id}")
        if transition.get("prior_state") != "mechanically_valid" or transition.get("new_state") != "semantic_review_pending":
            errors.append(f"invalid review transition state: {candidate_id}")
        transition_ids.add(candidate_id)
    if len(transitions) != 913 or transition_ids != set(candidate_by_id):
        errors.append("review transition ledger coverage drifted")

    report_body = {key: value for key, value in report.items() if key not in {"schema_version", "review_plan_id"}}
    if report.get("review_plan_id") != content_id("lesrp", report_body):
        errors.append("semantic review plan report content ID mismatch")
    artifact_paths = {
        "candidate_review_bundles": CANDIDATE_BUNDLES,
        "uncovered_block_review_bundles": COVERAGE_BUNDLES,
        "review_transition_ledger": TRANSITIONS,
    }
    for key, path in artifact_paths.items():
        binding = report.get(key, {})
        if binding.get("sha256") != sha256_file(path):
            errors.append(f"semantic review report binding mismatch: {key}")
    expected_minutes = {"lower": 3407, "expected": 5600, "upper": 9646}
    scenarios = report.get("human_effort_projection", {}).get("scenarios", {})
    if any(scenarios.get(label, {}).get("total_minutes") != minutes for label, minutes in expected_minutes.items()):
        errors.append("human-effort projection drifted")
    if any(report.get(key) != 0 for key in (
        "semantic_reviews_performed",
        "author_decisions_recorded",
        "accepted_evidence_records",
        "mapping_records_created",
        "reconciliation_records_created",
        "compilation_records_created",
        "provider_calls",
        "accounted_cost_cents",
        "google_sheets_interactions",
    )):
        errors.append("review planning crossed an unauthorized semantic or downstream boundary")

    if receipt:
        for key, path in {
            "candidate_review_bundles": CANDIDATE_BUNDLES,
            "uncovered_block_review_bundles": COVERAGE_BUNDLES,
            "review_transition_ledger": TRANSITIONS,
            "planning_report": PLANNING_REPORT,
        }.items():
            if receipt.get("artifacts", {}).get(key, {}).get("sha256") != sha256_file(path):
                errors.append(f"semantic review planning receipt binding mismatch: {key}")
        if receipt.get("active_control_index", {}).get("sha256") != sha256_file(ACTIVE_INDEX):
            errors.append("semantic review planning receipt active-index binding mismatch")
        verification = receipt.get("verification", {})
        engine_files, engine_digest = PRIOR.engine_snapshot()
        if verification.get("engine_files") != engine_files or verification.get("engine_digest") != engine_digest:
            errors.append("semantic review planning receipt engine snapshot mismatch")
        if verification.get("gate_5_guard_sha256") != sha256_file(pathlib.Path(__file__)):
            errors.append("semantic review planning receipt guard hash mismatch")
    return len(bundles), len(coverage_ids), len(transitions), len(compound_ids)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--work-order", type=pathlib.Path)
    parser.add_argument("--skip-archive", action="store_true")
    parser.add_argument("--with-tests", action="store_true")
    args = parser.parse_args()

    if PRIOR.run_legacy_guard(True, args.work_order):
        print("M050 GATE 5 REVIEW GUARD: FAIL — Gate 4 guard failed")
        return 1
    errors: list[str] = []
    PRIOR.validate_active_index(errors)
    approved_identity_cards = PRIOR.validate_identity_approval(errors)
    replay_records, replay_queue = PRIOR.validate_legacy_replay(errors)
    ruling_sections, ruling_fields, ruling_coordinates = PRIOR.validate_human_rulings_reconstruction(errors)
    mechanically_dispositioned = PRIOR.validate_repair_closure(errors)
    migration_errors: list[str] = []
    migration_candidates, compound_review_records, retrospective_blocks = PRIOR.validate_layer_e_migration(migration_errors)
    errors.extend(
        error
        for error in migration_errors
        if error != "historical Layer E migration verification snapshot mismatch"
    )
    relocated_evidence = validate_retired_archive(errors)
    validate_active_index(errors)
    review_bundles, uncovered_blocks, transitions, preserved_compounds = validate_review_plan(errors)
    PRIOR.validate_lock(errors)
    json_controls = PRIOR.validate_json_controls(errors)
    PRIOR.validate_offline_imports(errors)
    engine_files, engine_digest = PRIOR.engine_snapshot()
    if args.with_tests and PRIOR.run_tests():
        errors.append("Gate 5 offline regression suite failed")

    if errors:
        print("M050 GATE 5 REVIEW GUARD: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1
    print("M050 GATE 5 REVIEW GUARD: PASS")
    print(f"- engine files: {engine_files}")
    print(f"- engine digest: {engine_digest}")
    print(f"- parsed JSON controls: {json_controls}")
    print(f"- approved identity cards: {approved_identity_cards}")
    print(f"- replayed legacy records: {replay_records}")
    print(f"- replay repair queue: {replay_queue}")
    print(f"- reconstructed Human Rulings sections: {ruling_sections}")
    print(f"- reconstructed Human Rulings fields: {ruling_fields}")
    print(f"- Human Rulings legacy coordinates: {ruling_coordinates}")
    print(f"- mechanically dispositioned replay queue: {mechanically_dispositioned}/24")
    print(f"- mechanically valid Layer E migration candidates: {migration_candidates}/913")
    print(f"- migration compound review records: {compound_review_records}/139")
    print(f"- retrospectively dispositioned source blocks: {retrospective_blocks}/2464")
    print(f"- relocated legacy evidence files: {relocated_evidence}/12")
    print(f"- semantic review bundles: {review_bundles}/181")
    print(f"- semantic-review-pending transitions: {transitions}/913")
    print(f"- preserved compound review records: {preserved_compounds}/139")
    print(f"- uncovered eligible blocks queued: {uncovered_blocks}/518")
    print("- semantic reviews: 0")
    print("- accepted evidence: 0")
    print("- provider calls: prohibited")
    print("- Google Sheets: paused")
    if args.with_tests:
        print("- offline regression suite: pass")
    return 0


if __name__ == "__main__":
    sys.exit(main())
