import json
from pathlib import Path

from median_gate5.review_planning import build_legacy_semantic_review_plan
from median_gate5.schema import validate_artifact


REPO_ROOT = Path(__file__).resolve().parents[4]
MIGRATION_RECEIPT = REPO_ROOT / "m050/extraction/audit/M050_Extraction_Gate_5_Layer_E_Legacy_Migration_Receipt_v0_1_MEDIANv0_5_0.json"
SEED = "M050-GATE5-LEGACY-TIER3-SAMPLE-2026-08-03"


def _build():
    return build_legacy_semantic_review_plan(
        repo_root=REPO_ROOT,
        migration_receipt_path=MIGRATION_RECEIPT,
        candidate_bundle_relative_path="m050/extraction/review/candidate-bundles.jsonl",
        coverage_bundle_relative_path="m050/extraction/review/coverage-bundles.jsonl",
        transition_relative_path="m050/extraction/review/transitions.jsonl",
        effective_date="2026-08-03",
        tier3_seed=SEED,
    )


def _jsonl(data: bytes):
    return [json.loads(line) for line in data.decode("utf-8").splitlines()]


def test_review_plan_accounts_for_candidates_compounds_and_uncovered_blocks():
    candidate_bytes, coverage_bytes, transition_bytes, report = _build()
    bundles = _jsonl(candidate_bytes)
    coverage = _jsonl(coverage_bytes)
    transitions = _jsonl(transition_bytes)
    assert sum(len(bundle["member_ids"]) for bundle in bundles) == 913
    assert len({member for bundle in bundles for member in bundle["member_ids"]}) == 913
    assert len({item for bundle in bundles for item in bundle["compound_review_ids"]}) == 139
    assert sum(len(bundle["member_ids"]) for bundle in coverage) == 518
    assert len(transitions) == 913
    assert all(item["prior_state"] == "mechanically_valid" for item in transitions)
    assert all(item["new_state"] == "semantic_review_pending" for item in transitions)
    assert report["risk_tier_candidate_counts"] == {"1": 18, "2": 858, "3": 37}
    validate_artifact("legacy_semantic_review_plan_report", report)


def test_review_plan_tier3_sample_is_pinned_and_risk_weighted():
    candidate_bytes, _, _, report = _build()
    bundles = _jsonl(candidate_bytes)
    selected = [
        bundle
        for bundle in bundles
        if bundle["sampling_state"] == "risk_weighted_sample_selected"
    ]
    assert len(selected) >= 3
    assert report["tier3_sampling"]["seed"] == SEED
    assert report["tier3_sampling"]["selected_bundle_ids"] == [
        bundle["review_bundle_id"] for bundle in selected
    ]
    assert all(bundle["risk_tier"] == 3 for bundle in selected)


def test_review_plan_is_byte_deterministic_and_performs_no_semantic_acceptance():
    first = _build()
    second = _build()
    assert first == second
    report = first[3]
    assert report["semantic_reviews_performed"] == 0
    assert report["author_decisions_recorded"] == 0
    assert report["accepted_evidence_records"] == 0
    assert report["mapping_records_created"] == 0
    assert report["reconciliation_records_created"] == 0
    assert report["compilation_records_created"] == 0
    assert report["provider_calls"] == 0
    assert report["google_sheets_interactions"] == 0
