from median_gate5.bundles import build_reconciliation_bundles, orphaned_mapped_evidence
from median_gate5.dependencies import DependencyEdge, stale_descendants
from median_gate5.review import select_tier3_sample
from median_gate5.schema import validate_artifact


def test_staleness_walks_all_descendants_and_survives_cycle():
    edges = [
        DependencyEdge("source", "block", "contains"),
        DependencyEdge("block", "evidence", "grounds"),
        DependencyEdge("evidence", "mapping", "mapped_by"),
        DependencyEdge("mapping", "evidence", "cycle_fixture"),
        DependencyEdge("mapping", "compile", "feeds"),
    ]
    assert stale_descendants({"block"}, edges) == ["compile", "evidence", "mapping"]


def test_bundle_builder_accounts_for_exceptional_mapping_states():
    mappings = [
        {"evidence_id": "e1", "status": "mapped", "subjects": ["DWELL"]},
        {"evidence_id": "e2", "status": "ambiguous", "subjects": []},
        {"evidence_id": "e3", "status": "mapped", "subjects": []},
    ]
    bundles, exceptional = build_reconciliation_bundles(mappings, {"DWELL": ["HOME"]})
    assert {bundle["subject"] for bundle in bundles} == {"DWELL", "HOME"}
    assert exceptional == {"ambiguous": ["e2"], "mapped_without_subject": ["e3"]}
    assert orphaned_mapped_evidence(mappings, bundles) == ["e3"]
    for bundle in bundles:
        validate_artifact("reconciliation_bundle", bundle)


def test_tier3_sampling_is_deterministic_and_risk_weighted():
    chunks = [
        {"ordinal": index, "claim_bearing_blocks": index, "review_risk": 0}
        for index in range(1, 21)
    ]
    chunks[4]["review_risk"] = 99
    first = select_tier3_sample(chunks, seed="frozen-seed")
    second = select_tier3_sample(chunks, seed="frozen-seed")
    assert first == second
    assert 5 in first
    assert 20 in first
    assert len(first) == 3
