import json
from pathlib import Path

from median_gate5.migration import (
    build_layer_e_legacy_migration,
    is_compound_review_quote,
)
from median_gate5.canonical import content_id
from median_gate5.schema import validate_artifact


REPO_ROOT = Path(__file__).resolve().parents[4]
CLOSURE_PATH = REPO_ROOT / "m050/extraction/repairs/M050_Legacy_Repair_Closure_Report_v0_1_MEDIANv0_5_0.json"
TRANSITION_CONTROL_PATH = REPO_ROOT / "m050/extraction/migration/M050_Layer_E_Legacy_Migration_Transition_Control_v0_1_MEDIANv0_5_0.json"
BLOCK_PATHS = {
    "M050-SRC-CROSSING-001": "m050/extraction/migration/block-dispositions/crossing.jsonl",
    "M050-SRC-HUMAN-RULINGS-001": "m050/extraction/migration/block-dispositions/human-rulings.jsonl",
    "M050-SRC-MSID-GRAMMAR-001": "m050/extraction/migration/block-dispositions/msid.jsonl",
    "M050-SRC-PA-001": "m050/extraction/migration/block-dispositions/pa.jsonl",
}


def _build():
    closure = json.loads(CLOSURE_PATH.read_text(encoding="utf-8"))
    return build_layer_e_legacy_migration(
        repo_root=REPO_ROOT,
        repair_closure=closure,
        repair_closure_path=CLOSURE_PATH,
        candidate_relative_path="m050/extraction/migration/candidates.jsonl",
        compound_relative_path="m050/extraction/migration/compound-review.jsonl",
        block_ledger_relative_paths=BLOCK_PATHS,
    )


def test_gate_3_compound_indicator_is_narrow_and_reproducible():
    assert is_compound_review_quote("First sentence. Second sentence.") is True
    assert is_compound_review_quote("First row.\n| second row.") is False
    assert is_compound_review_quote("No special subsystem. this remains one indicator-free unit.") is False


def test_layer_e_migration_accounts_for_all_records_blocks_and_compounds_without_acceptance():
    candidates, compounds, block_ledgers, report = _build()
    candidate_records = [json.loads(line) for line in candidates.splitlines()]
    compound_records = [json.loads(line) for line in compounds.splitlines()]
    assert report["passed"] is True
    assert len(candidate_records) == 913
    assert len({record["legacy_record_id"] for record in candidate_records}) == 913
    assert all(record["state"] == "mechanically_valid" for record in candidate_records)
    assert all(record["acceptance_state"] == "not_accepted" for record in candidate_records)
    assert all(record["legacy_semantic_fields_imported"] is False for record in candidate_records)
    assert all(record["normalized_claim"] is None for record in candidate_records)
    assert all(record["assigned_stream"] is None for record in candidate_records)
    assert len(compound_records) == 139
    assert report["gate_3_multi_sentence_source_counts"] == {
        "M050-SRC-CROSSING-001": 2,
        "M050-SRC-HUMAN-RULINGS-001": 21,
        "M050-SRC-MSID-GRAMMAR-001": 31,
        "M050-SRC-PA-001": 69,
    }
    assert report["cross_block_structural_compound_count"] == 17
    assert report["compound_queue_overlap_count"] == 1
    assert set(block_ledgers) == set(BLOCK_PATHS)
    assert sum(len(data.splitlines()) for data in block_ledgers.values()) == 2464
    assert report["accepted_evidence_records"] == 0
    assert report["semantic_reviews_performed"] == 0
    assert report["provider_calls"] == 0
    assert report["google_sheets_interactions"] == 0


def test_layer_e_migration_is_byte_deterministic():
    assert _build() == _build()


def test_migration_transition_control_prohibits_direct_acceptance_and_downstream_work():
    control = json.loads(TRANSITION_CONTROL_PATH.read_text(encoding="utf-8"))
    validate_artifact("layer_e_legacy_migration_transition_control", control)
    body = {
        key: value
        for key, value in control.items()
        if key not in {"schema_version", "transition_control_id"}
    }
    assert control["transition_control_id"] == content_id("lemtc", body)
    assert control["permitted_next_state"] == "semantic_review_pending"
    assert control["direct_acceptance_from_mechanically_valid_prohibited"] is True
    assert control["mapping_authorized"] is False
    assert control["reconciliation_authorized"] is False
    assert control["compilation_authorized"] is False
