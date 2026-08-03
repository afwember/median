import copy
import json
from pathlib import Path

import pytest

from median_gate5.errors import IntegrityError
from median_gate5.repairs import (
    build_compound_dispositions,
    build_occurrence_resolution,
    build_repair_closure,
)


REPO_ROOT = Path(__file__).resolve().parents[4]
MILESTONE_PATH = REPO_ROOT / "m050/extraction/audit/M050_Extraction_Gate_5_Legacy_Replay_Milestone_Receipt_v0_1_MEDIANv0_5_0.json"
HUMAN_REPORT_PATH = REPO_ROOT / "m050/extraction/reconstruction/human-rulings/M050_Human_Rulings_Reconstruction_Report_v0_1_MEDIANv0_5_0.json"
COMPOUND_REPORT_PATH = REPO_ROOT / "m050/extraction/repairs/M050_Legacy_Cross_Block_Compound_Disposition_Report_v0_1_MEDIANv0_5_0.json"
OCCURRENCE_PATH = REPO_ROOT / "m050/extraction/repairs/M050_Legacy_Ambiguous_Occurrence_Resolution_v0_1_MEDIANv0_5_0.json"


def _build(milestone=None):
    value = milestone or json.loads(MILESTONE_PATH.read_text(encoding="utf-8"))
    return build_compound_dispositions(
        repo_root=REPO_ROOT,
        replay_milestone=value,
        replay_milestone_path=MILESTONE_PATH,
        ledger_relative_path="m050/extraction/repairs/compound-dispositions.jsonl",
    )


def test_all_17_cross_block_records_are_preserved_as_indivisible_compounds():
    ledger_bytes, report = _build()
    records = [json.loads(line) for line in ledger_bytes.splitlines()]
    assert report["passed"] is True
    assert report["record_count"] == 17
    assert len(records) == len({record["legacy_record_id"] for record in records}) == 17
    assert {summary["source_id"]: summary["cross_block_records"] for summary in report["source_summaries"]} == {
        "M050-SRC-CROSSING-001": 2,
        "M050-SRC-PA-001": 4,
        "M050-SRC-HUMAN-RULINGS-001": 2,
        "M050-SRC-MSID-GRAMMAR-001": 9,
    }
    assert all(all(record["structural_checks"].values()) for record in records)
    assert all(record["split_performed"] is False for record in records)
    assert all(record["legacy_record_modified"] is False for record in records)
    assert all(record["risk_tier"] == 2 for record in records)
    assert all(record["semantic_review_performed"] is False for record in records)


def test_compound_disposition_is_byte_deterministic():
    assert _build() == _build()


def test_compound_disposition_fails_closed_on_replay_aggregate_drift():
    milestone = json.loads(MILESTONE_PATH.read_text(encoding="utf-8"))
    changed = copy.deepcopy(milestone)
    changed["aggregate"]["cross_block_records"] = 16
    with pytest.raises(IntegrityError, match="unexpected aggregate counts"):
        _build(changed)


def test_ambiguous_msid_occurrence_resolves_to_unique_whole_line_in_pinned_range():
    milestone = json.loads(MILESTONE_PATH.read_text(encoding="utf-8"))
    resolution = build_occurrence_resolution(
        repo_root=REPO_ROOT,
        replay_milestone=milestone,
        replay_milestone_path=MILESTONE_PATH,
    )
    assert resolution["legacy_record_id"] == "ATOM-MSID-DIRECT-0062"
    assert resolution["original_occurrence_count"] == 38
    assert resolution["pinned_range_occurrence_count"] == 2
    assert resolution["pinned_range_whole_line_occurrence_count"] == 1
    assert resolution["selected_span"]["start_line"] == 288
    assert resolution["selected_span"]["end_line"] == 288
    assert resolution["selected_block_type"] == "code_fence"
    assert resolution["legacy_record_modified"] is False
    assert resolution["replay_record_modified"] is False


def test_ambiguous_occurrence_resolution_is_deterministic():
    milestone = json.loads(MILESTONE_PATH.read_text(encoding="utf-8"))
    first = build_occurrence_resolution(
        repo_root=REPO_ROOT,
        replay_milestone=milestone,
        replay_milestone_path=MILESTONE_PATH,
    )
    second = build_occurrence_resolution(
        repo_root=REPO_ROOT,
        replay_milestone=milestone,
        replay_milestone_path=MILESTONE_PATH,
    )
    assert first == second


def test_repair_closure_exactly_covers_queue_and_replays_byte_identically():
    milestone = json.loads(MILESTONE_PATH.read_text(encoding="utf-8"))
    closure = build_repair_closure(
        repo_root=REPO_ROOT,
        replay_milestone=milestone,
        replay_milestone_path=MILESTONE_PATH,
        human_reconstruction_report_path=HUMAN_REPORT_PATH,
        compound_report_path=COMPOUND_REPORT_PATH,
        occurrence_resolution_path=OCCURRENCE_PATH,
    )
    assert closure["passed"] is True
    assert closure["legacy_record_count"] == 913
    assert closure["raw_replay_queue_count"] == 24
    assert closure["mechanically_dispositioned_queue_count"] == 24
    assert closure["unresolved_grounding_or_coordinate_repairs"] == 0
    assert closure["replay_ledgers_byte_identical"] == 4
    assert closure["replay_reports_byte_identical"] == 4
    assert closure["semantic_acceptance_performed"] is False
    assert closure["layer_e_migration_started"] is False


def test_repair_closure_is_deterministic():
    milestone = json.loads(MILESTONE_PATH.read_text(encoding="utf-8"))
    arguments = {
        "repo_root": REPO_ROOT,
        "replay_milestone": milestone,
        "replay_milestone_path": MILESTONE_PATH,
        "human_reconstruction_report_path": HUMAN_REPORT_PATH,
        "compound_report_path": COMPOUND_REPORT_PATH,
        "occurrence_resolution_path": OCCURRENCE_PATH,
    }
    assert build_repair_closure(**arguments) == build_repair_closure(**arguments)
