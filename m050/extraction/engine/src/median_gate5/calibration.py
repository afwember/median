from __future__ import annotations

from typing import Any

from .errors import ContractError


SOURCE_CALIBRATION_STATES = (
    "source_selected",
    "identity_card_draft",
    "identity_card_reviewed",
    "identity_card_approved",
    "offline_dry_run",
    "pilot_frozen",
    "pilot_call_authorized",
    "pilot_response_captured",
    "pilot_rejected",
    "pilot_accepted",
    "source_run_authorized",
    "source_run_in_progress",
    "source_run_halted",
    "source_candidate_complete",
    "source_extraction_candidate_accepted",
)

ALLOWED_TRANSITIONS = {
    "source_selected": {"identity_card_draft"},
    "identity_card_draft": {"identity_card_reviewed"},
    "identity_card_reviewed": {"identity_card_draft", "identity_card_approved"},
    "identity_card_approved": {"offline_dry_run"},
    "offline_dry_run": {"pilot_frozen"},
    "pilot_frozen": {"offline_dry_run", "pilot_call_authorized"},
    "pilot_call_authorized": {"pilot_response_captured"},
    "pilot_response_captured": {"pilot_rejected", "pilot_accepted"},
    "pilot_rejected": {"offline_dry_run"},
    "pilot_accepted": {"source_run_authorized"},
    "source_run_authorized": {"source_run_in_progress"},
    "source_run_in_progress": {"source_run_halted", "source_candidate_complete"},
    "source_run_halted": {"offline_dry_run"},
    "source_candidate_complete": {
        "source_extraction_candidate_accepted",
        "source_run_halted",
    },
    "source_extraction_candidate_accepted": set(),
}

BINDING_FIELDS = (
    "source_id",
    "source_sha256",
    "gate_2_disposition",
    "output_streams_sha256",
    "identity_card_sha256",
    "source_profile_sha256",
    "pilot_chunk_id",
    "pilot_chunk_sha256",
    "prompt_sha256",
    "schema_sha256",
    "chunker_sha256",
    "engine_digest",
    "validator_sha256",
    "normalization_spec_sha256",
    "exclusion_policy_sha256",
    "model",
    "reasoning_effort",
)

TERMINAL_MEDIA_DISPOSITIONS = {
    "caption_text_eligible",
    "visual_evidence_requires_multimodal_pilot",
    "illustration_nonsemantic",
    "publication_only",
    "review_required",
}


def require_transition(prior_state: str, new_state: str) -> None:
    if prior_state not in ALLOWED_TRANSITIONS:
        raise ContractError(f"unknown calibration state: {prior_state}")
    if new_state not in ALLOWED_TRANSITIONS[prior_state]:
        raise ContractError(
            f"prohibited calibration transition: {prior_state} -> {new_state}"
        )


def require_exact_bindings(binding: dict[str, Any]) -> None:
    missing = [field for field in BINDING_FIELDS if not binding.get(field)]
    if missing:
        raise ContractError(f"calibration binding is incomplete: {', '.join(missing)}")


def require_source_readiness(readiness: dict[str, Any]) -> None:
    source_id = readiness.get("source_id")
    if readiness.get("source_selection_authority") != "Asa Wember":
        raise ContractError("source selection requires explicit Asa Wember authority")
    identity = readiness.get("identity_card", {})
    if identity.get("state") != "approved" or not identity.get("sha256"):
        raise ContractError("source requires an approved content/provenance identity card")
    disposition = readiness.get("gate_2_disposition")
    if disposition == "retain_companion_no_atomic_compile_extraction":
        raise ContractError("non-atomic companion cannot enter source atomization")
    streams = readiness.get("output_streams")
    if not isinstance(streams, list) or not streams:
        raise ContractError("source readiness must preserve explicit output-stream routing")
    if readiness.get("stream_routing_complete") is not True:
        raise ContractError("mixed source streams require explicit record-level routing")

    execution_mode = readiness.get("execution_mode")
    if readiness.get("model_extraction_prohibited") is True:
        if execution_mode != "deterministic_only" or readiness.get("provider_call_limit") != 0:
            raise ContractError("deterministic-only source cannot enter provider calibration")
    elif execution_mode != "provider_calibrated":
        raise ContractError("model-eligible source requires provider-calibrated execution mode")

    prompt_sources = readiness.get("prompt_extractable_source_ids")
    if prompt_sources != [source_id] or readiness.get("foreign_evidence_record_count") != 0:
        raise ContractError("provider prompt violates the one-source extractable-content firewall")

    structure = readiness.get("structural_accounting", {})
    total = structure.get("total_blocks")
    accounted = sum(
        structure.get(field, -10**9)
        for field in ("eligible_blocks", "excluded_blocks", "context_only_blocks")
    )
    if not isinstance(total, int) or total < 1 or accounted != total:
        raise ContractError("structural block accounting is incomplete")
    media_count = structure.get("embedded_media_count")
    media = readiness.get("media_dispositions")
    if not isinstance(media, list) or media_count != len(media):
        raise ContractError("embedded media accounting is incomplete")
    if any(item.get("state") not in TERMINAL_MEDIA_DISPOSITIONS for item in media):
        raise ContractError("embedded media lacks a terminal explicit disposition")


def require_pilot_acceptance(pilot_receipt: dict[str, Any]) -> None:
    if pilot_receipt.get("state") != "pilot_accepted":
        raise ContractError("full-source release requires an accepted pilot")
    require_exact_bindings(pilot_receipt.get("binding", {}))
    mechanical = pilot_receipt.get("mechanical_gate", {})
    required_mechanical = {
        "schema_errors": 0,
        "grounding_errors": 0,
        "coverage_errors": 0,
        "atomicity_errors": 0,
        "truncation_errors": 0,
        "table_structure_errors": 0,
    }
    if any(mechanical.get(key) != expected for key, expected in required_mechanical.items()):
        raise ContractError("pilot mechanical gate is not perfect-for-release")
    semantic = pilot_receipt.get("semantic_gate", {})
    required_semantic = (
        "source_comparison_complete",
        "ownership_correct",
        "status_correct",
        "authority_scope_correct",
        "qualifiers_preserved",
        "no_unsupported_identifiers",
        "no_unresolved_defects",
    )
    if any(semantic.get(field) is not True for field in required_semantic):
        raise ContractError("pilot semantic gate is not perfect-for-release")
    reference = pilot_receipt.get("reference_comparison", {})
    if reference.get("required") is True and (
        reference.get("complete") is not True
        or reference.get("expected_items") != reference.get("matched_items")
    ):
        raise ContractError("pilot does not completely match its reference set")


def require_full_source_release(
    pilot_receipt: dict[str, Any], release_receipt: dict[str, Any]
) -> None:
    require_pilot_acceptance(pilot_receipt)
    if release_receipt.get("state") != "source_run_authorized":
        raise ContractError("source run lacks an explicit release receipt")
    if release_receipt.get("authority") != "Asa Wember":
        raise ContractError("only Asa Wember may authorize a full-source run")
    if release_receipt.get("provider_call_limit", 0) < 1:
        raise ContractError("source release must carry a positive provider-call limit")
    if release_receipt.get("cost_cap_cents", 0) < 1:
        raise ContractError("source release must carry an explicit positive cost cap")
    if release_receipt.get("execution_cadence") != "sequential_one_call_review":
        raise ContractError("default source release requires sequential one-call review")
    pilot_binding = pilot_receipt.get("binding", {})
    release_binding = release_receipt.get("binding", {})
    require_exact_bindings(release_binding)
    drift = [field for field in BINDING_FIELDS if pilot_binding.get(field) != release_binding.get(field)]
    if drift:
        raise ContractError(
            "pilot acceptance is invalid after source or configuration drift: "
            + ", ".join(drift)
        )


def require_staged_chunk_execution(
    release_receipt: dict[str, Any],
    completed_calls: int,
    next_chunk_source_id: str,
    *,
    prior_chunk_review_passed: bool,
) -> None:
    if release_receipt.get("state") != "source_run_authorized":
        raise ContractError("chunk execution requires a source-run authorization")
    limit = release_receipt.get("provider_call_limit")
    if not isinstance(limit, int) or completed_calls >= limit:
        raise ContractError("provider-call limit exhausted")
    if next_chunk_source_id != release_receipt.get("binding", {}).get("source_id"):
        raise ContractError("a source authorization cannot carry into another source")
    if release_receipt.get("revoked") is True:
        raise ContractError("source-run authorization was revoked by a defect")
    if completed_calls and not prior_chunk_review_passed:
        raise ContractError("next call is blocked until the prior chunk passes review")
