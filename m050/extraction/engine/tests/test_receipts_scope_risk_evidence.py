from pathlib import Path

import pytest

from median_gate5.errors import ContractError, IntegrityError
from median_gate5.evidence import accept_evidence_candidate, make_evidence_candidate
from median_gate5.receipts import append_receipt, artifact_hash, require_receipt_chain
from median_gate5.risk import classify_review_risk, exclusion_audit
from median_gate5.schema import validate_artifact
from median_gate5.scope import (
    require_input_paths,
    require_new_output_path,
    require_zero_cost_for_offline,
)
from median_gate5.states import transition_receipt


def make_receipt(predecessor=None, state="offline_verified"):
    return transition_receipt(
        machine="work_order",
        artifact_id="wo-1",
        prior_state="draft",
        new_state=state,
        authority="Codex",
        reason="offline verification",
        tool_version="0.1.0",
        predecessor_receipt_hash=predecessor,
        timestamp="2026-08-02T00:00:00Z",
    )


def test_receipt_chain_and_append_only_paths(tmp_path):
    first = make_receipt()
    second = transition_receipt(
        machine="work_order",
        artifact_id="wo-1",
        prior_state="offline_verified",
        new_state="awaiting_authorization",
        authority="Codex",
        reason="ready for author",
        tool_version="0.1.0",
        predecessor_receipt_hash=artifact_hash(first),
        timestamp="2026-08-02T00:01:00Z",
    )
    require_receipt_chain([first, second])
    target = append_receipt(tmp_path, 1, first)
    assert target.is_file()
    with pytest.raises(FileExistsError):
        append_receipt(tmp_path, 1, first)
    broken = dict(second, predecessor_receipt_hash="0" * 64)
    with pytest.raises(IntegrityError, match="predecessor mismatch"):
        require_receipt_chain([first, broken])


def test_path_allowlist_and_m051_exclusion(tmp_path):
    allowed = tmp_path / "m050" / "docs"
    allowed.mkdir(parents=True)
    source = allowed / "source.md"
    source.write_text("source", encoding="utf-8")
    require_input_paths(tmp_path, [source], [Path("m050/docs")])
    forbidden = tmp_path / "m051"
    forbidden.mkdir()
    future = forbidden / "future.md"
    future.write_text("future", encoding="utf-8")
    with pytest.raises(IntegrityError, match="forbidden"):
        require_input_paths(tmp_path, [future], [Path("m050/docs")])


def test_output_path_cannot_escape_or_overwrite(tmp_path):
    extraction = tmp_path / "m050" / "extraction"
    extraction.mkdir(parents=True)
    allowed = require_new_output_path(tmp_path, Path("m050/extraction/new/report.json"))
    assert allowed == extraction / "new" / "report.json"
    existing = extraction / "existing.json"
    existing.write_text("preserved", encoding="utf-8")
    with pytest.raises(IntegrityError, match="exists"):
        require_new_output_path(tmp_path, existing)
    with pytest.raises(IntegrityError, match="escapes"):
        require_new_output_path(tmp_path, tmp_path / "outside.json")


def test_offline_work_order_must_be_zero_cost():
    require_zero_cost_for_offline(0, "offline")
    with pytest.raises(ContractError, match="zero cost"):
        require_zero_cost_for_offline(1, "offline")


def test_risk_tiers_and_exclusion_audit():
    high = classify_review_risk(
        {"text": "This human ruling supersedes the old rule.", "block_type": "paragraph"}
    )
    elevated = classify_review_risk(
        {"text": "Capacity is 4.", "block_type": "table_row", "estimated_claims": 1}
    )
    routine = classify_review_risk(
        {"text": "The colony rests nearby.", "block_type": "paragraph", "estimated_claims": 1}
    )
    assert (high["risk_tier"], elevated["risk_tier"], routine["risk_tier"]) == (1, 2, 3)
    audit = exclusion_audit(
        4,
        [
            {"block_id": "b1", "stage": "structural", "review_state": "pending"},
            {"block_id": "b2", "stage": "extraction", "review_state": "accepted"},
        ],
    )
    assert audit["anomalous_rate"]
    assert audit["heuristic_review"] == ["b1"]
    assert audit["pending_review"] == ["b1"]


def test_evidence_ids_are_local_and_content_derived():
    values = dict(
        source_id="SRC",
        source_sha256="a" * 64,
        block_id="SRC__B00001_deadbeef0000",
        exact_source_text="Colonists rest.",
        normalized_claim="Colonists rest.",
        claim_kind="mechanic",
        stream="evidence_game_semantic",
        request_id="req-1",
        response_id="resp-1",
    )
    first = make_evidence_candidate(**values)
    second = make_evidence_candidate(**values)
    assert first["evidence_id"] == second["evidence_id"]
    validate_artifact("layer_e_candidate", first)
    accepted = accept_evidence_candidate(first, "accept-1")
    assert accepted["evidence_id"] == first["evidence_id"]
    validate_artifact("layer_e", accepted)
