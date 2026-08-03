import copy

import pytest

from median_gate5.calibration import (
    require_full_source_release,
    require_pilot_acceptance,
    require_source_readiness,
    require_staged_chunk_execution,
    require_transition,
)
from median_gate5.errors import ContractError


def _pilot():
    return {
        "state": "pilot_accepted",
        "binding": {
            "source_id": "M050-SRC-TEST-001",
            "source_sha256": "1" * 64,
            "gate_2_disposition": "source_bounded_atomic_extraction",
            "output_streams_sha256": "6" * 64,
            "identity_card_sha256": "7" * 64,
            "source_profile_sha256": "8" * 64,
            "pilot_chunk_id": "C0002",
            "pilot_chunk_sha256": "2" * 64,
            "prompt_sha256": "3" * 64,
            "schema_sha256": "4" * 64,
            "chunker_sha256": "5" * 64,
            "engine_digest": "9" * 64,
            "validator_sha256": "a" * 64,
            "normalization_spec_sha256": "b" * 64,
            "exclusion_policy_sha256": "c" * 64,
            "model": "provider-model",
            "reasoning_effort": "low",
        },
        "mechanical_gate": {
            "schema_errors": 0,
            "grounding_errors": 0,
            "coverage_errors": 0,
            "atomicity_errors": 0,
            "truncation_errors": 0,
            "table_structure_errors": 0,
        },
        "semantic_gate": {
            "source_comparison_complete": True,
            "ownership_correct": True,
            "status_correct": True,
            "authority_scope_correct": True,
            "qualifiers_preserved": True,
            "no_unsupported_identifiers": True,
            "no_unresolved_defects": True,
        },
        "reference_comparison": {
            "required": True,
            "complete": True,
            "expected_items": 10,
            "matched_items": 10,
        },
    }


def _release(pilot):
    return {
        "state": "source_run_authorized",
        "authority": "Asa Wember",
        "provider_call_limit": 12,
        "cost_cap_cents": 100,
        "execution_cadence": "sequential_one_call_review",
        "revoked": False,
        "binding": copy.deepcopy(pilot["binding"]),
    }


def test_calibration_sequence_forbids_skipping_pilot_or_whole_document_review():
    require_transition("source_selected", "identity_card_draft")
    require_transition("identity_card_reviewed", "identity_card_approved")
    require_transition("identity_card_approved", "offline_dry_run")
    require_transition("pilot_response_captured", "pilot_rejected")
    require_transition("pilot_rejected", "offline_dry_run")
    require_transition("source_candidate_complete", "source_extraction_candidate_accepted")
    with pytest.raises(ContractError, match="prohibited"):
        require_transition("offline_dry_run", "source_run_authorized")
    with pytest.raises(ContractError, match="prohibited"):
        require_transition("source_run_in_progress", "source_accepted")


def test_imperfect_pilot_cannot_release_a_source():
    pilot = _pilot()
    pilot["mechanical_gate"]["grounding_errors"] = 1
    with pytest.raises(ContractError, match="mechanical"):
        require_pilot_acceptance(pilot)
    pilot = _pilot()
    pilot["semantic_gate"]["qualifiers_preserved"] = False
    with pytest.raises(ContractError, match="semantic"):
        require_pilot_acceptance(pilot)


def test_full_source_release_requires_author_cost_cap_and_exact_configuration():
    pilot = _pilot()
    release = _release(pilot)
    require_full_source_release(pilot, release)
    release["authority"] = "Codex"
    with pytest.raises(ContractError, match="Asa Wember"):
        require_full_source_release(pilot, release)
    release = _release(pilot)
    release["cost_cap_cents"] = 0
    with pytest.raises(ContractError, match="cost cap"):
        require_full_source_release(pilot, release)
    release = _release(pilot)
    release["execution_cadence"] = "batch"
    with pytest.raises(ContractError, match="sequential"):
        require_full_source_release(pilot, release)


def test_any_source_or_execution_configuration_drift_invalidates_pilot_acceptance():
    pilot = _pilot()
    for field in (
        "source_sha256",
        "identity_card_sha256",
        "source_profile_sha256",
        "prompt_sha256",
        "chunker_sha256",
        "engine_digest",
        "validator_sha256",
        "normalization_spec_sha256",
        "exclusion_policy_sha256",
        "model",
    ):
        release = _release(pilot)
        release["binding"][field] = "drifted"
        with pytest.raises(ContractError, match="drift"):
            require_full_source_release(pilot, release)


def test_defect_revokes_run_and_authorization_never_transfers_to_next_source():
    pilot = _pilot()
    release = _release(pilot)
    require_staged_chunk_execution(
        release, 0, "M050-SRC-TEST-001", prior_chunk_review_passed=True
    )
    release["revoked"] = True
    with pytest.raises(ContractError, match="revoked"):
        require_staged_chunk_execution(
            release, 1, "M050-SRC-TEST-001", prior_chunk_review_passed=True
        )
    release["revoked"] = False
    with pytest.raises(ContractError, match="another source"):
        require_staged_chunk_execution(
            release, 1, "M050-SRC-NEXT-001", prior_chunk_review_passed=True
        )
    with pytest.raises(ContractError, match="prior chunk"):
        require_staged_chunk_execution(
            release, 1, "M050-SRC-TEST-001", prior_chunk_review_passed=False
        )


def _readiness():
    return {
        "source_id": "M050-SRC-TEST-001",
        "source_selection_authority": "Asa Wember",
        "identity_card": {"state": "approved", "sha256": "1" * 64},
        "gate_2_disposition": "source_bounded_atomic_extraction",
        "output_streams": ["evidence_game_semantic"],
        "stream_routing_complete": True,
        "model_extraction_prohibited": False,
        "execution_mode": "provider_calibrated",
        "provider_call_limit": 0,
        "prompt_extractable_source_ids": ["M050-SRC-TEST-001"],
        "foreign_evidence_record_count": 0,
        "structural_accounting": {
            "total_blocks": 10,
            "eligible_blocks": 7,
            "excluded_blocks": 2,
            "context_only_blocks": 1,
            "embedded_media_count": 1,
        },
        "media_dispositions": [
            {"media_id": "media-1", "state": "caption_text_eligible"}
        ],
    }


def test_source_readiness_requires_author_selected_approved_identity_card():
    readiness = _readiness()
    require_source_readiness(readiness)
    readiness["identity_card"]["state"] = "draft"
    with pytest.raises(ContractError, match="approved"):
        require_source_readiness(readiness)


def test_source_readiness_preserves_stream_routing_and_source_only_prompt():
    readiness = _readiness()
    readiness["stream_routing_complete"] = False
    with pytest.raises(ContractError, match="routing"):
        require_source_readiness(readiness)
    readiness = _readiness()
    readiness["prompt_extractable_source_ids"].append("M050-SRC-FOREIGN-001")
    with pytest.raises(ContractError, match="firewall"):
        require_source_readiness(readiness)


def test_deterministic_only_disposition_never_enters_provider_calibration():
    readiness = _readiness()
    readiness["model_extraction_prohibited"] = True
    readiness["execution_mode"] = "deterministic_only"
    require_source_readiness(readiness)
    readiness["execution_mode"] = "provider_calibrated"
    readiness["provider_call_limit"] = 1
    with pytest.raises(ContractError, match="deterministic-only"):
        require_source_readiness(readiness)


def test_non_atomic_companion_cannot_enter_atomization():
    readiness = _readiness()
    readiness["gate_2_disposition"] = "retain_companion_no_atomic_compile_extraction"
    with pytest.raises(ContractError, match="non-atomic"):
        require_source_readiness(readiness)


def test_every_embedded_media_reference_requires_explicit_disposition():
    readiness = _readiness()
    readiness["structural_accounting"]["embedded_media_count"] = 2
    with pytest.raises(ContractError, match="media accounting"):
        require_source_readiness(readiness)
    readiness = _readiness()
    readiness["media_dispositions"][0]["state"] = "silently_ignored"
    with pytest.raises(ContractError, match="terminal"):
        require_source_readiness(readiness)
