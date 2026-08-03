from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

from .canonical import content_id
from .errors import ContractError


WORK_ORDER_TRANSITIONS: dict[str, frozenset[str]] = {
    "draft": frozenset({"offline_verified", "rejected", "cancelled"}),
    "offline_verified": frozenset({"awaiting_authorization", "rejected", "cancelled"}),
    "awaiting_authorization": frozenset({"authorized", "rejected", "cancelled"}),
    "authorized": frozenset({"active", "failed_cost", "failed_integrity", "cancelled"}),
    "active": frozenset({"closed", "failed_cost", "failed_integrity", "cancelled"}),
    "closed": frozenset(),
    "rejected": frozenset(),
    "failed_transport": frozenset(),
    "failed_cost": frozenset(),
    "failed_integrity": frozenset(),
    "cancelled": frozenset(),
}

REQUEST_TRANSITIONS: dict[str, frozenset[str]] = {
    "rendered": frozenset({"verified", "not_sent", "invalid_response"}),
    "verified": frozenset({"authorized_for_send", "not_sent", "cost_blocked"}),
    "authorized_for_send": frozenset({"sent", "not_sent", "cost_blocked"}),
    "sent": frozenset({"response_captured", "transport_failed", "truncated"}),
    "response_captured": frozenset({"locally_processed", "invalid_response", "truncated"}),
    "locally_processed": frozenset({"dispositioned", "invalid_response", "retry_authorized"}),
    "retry_authorized": frozenset({"dispositioned"}),
    "dispositioned": frozenset(),
    "not_sent": frozenset(),
    "transport_failed": frozenset({"retry_authorized"}),
    "cost_blocked": frozenset(),
    "truncated": frozenset({"retry_authorized"}),
    "invalid_response": frozenset({"retry_authorized"}),
}

EVIDENCE_TRANSITIONS: dict[str, frozenset[str]] = {
    "proposed": frozenset({"mechanically_valid", "mechanically_rejected"}),
    "mechanically_valid": frozenset({"semantic_review_pending"}),
    "mechanically_rejected": frozenset(),
    "semantic_review_pending": frozenset({"reviewed", "human_required"}),
    "reviewed": frozenset({"accepted", "rejected", "human_required"}),
    "accepted": frozenset({"superseded", "stale"}),
    "rejected": frozenset(),
    "human_required": frozenset({"reviewed", "rejected"}),
    "superseded": frozenset(),
    "stale": frozenset({"superseded"}),
}

IDENTITY_CARD_TRANSITIONS = {
    "draft": frozenset({"reviewed"}),
    "reviewed": frozenset({"approved", "draft"}),
    "approved": frozenset({"challenged", "superseded"}),
    "challenged": frozenset({"superseded"}),
    "superseded": frozenset(),
}

MAPPING_TRANSITIONS = {
    "proposed": frozenset({"validated", "rejected"}),
    "validated": frozenset({"reviewed", "rejected"}),
    "reviewed": frozenset({"accepted", "human_required", "rejected"}),
    "human_required": frozenset({"reviewed", "rejected"}),
    "accepted": frozenset({"stale", "superseded"}),
    "stale": frozenset({"superseded"}),
    "rejected": frozenset(),
    "superseded": frozenset(),
}

BUNDLE_TRANSITIONS = {
    "constructed": frozenset({"completeness_verified", "rejected"}),
    "completeness_verified": frozenset({"sealed", "rejected"}),
    "sealed": frozenset({"reviewed", "stale"}),
    "reviewed": frozenset({"accepted", "human_required", "stale"}),
    "human_required": frozenset({"reviewed", "rejected"}),
    "accepted": frozenset({"stale", "superseded"}),
    "stale": frozenset({"superseded"}),
    "rejected": frozenset(),
    "superseded": frozenset(),
}

QUESTION_TRANSITIONS = {
    "open": frozenset({"prepared", "deferred"}),
    "prepared": frozenset({"presented", "deferred"}),
    "presented": frozenset({"answered", "deferred"}),
    "answered": frozenset({"encoded"}),
    "encoded": frozenset({"closed"}),
    "deferred": frozenset({"prepared"}),
    "closed": frozenset(),
}

RULING_TRANSITIONS = {
    "drafted_by_codex": frozenset({"author_confirmed", "rejected"}),
    "author_confirmed": frozenset({"recorded"}),
    "recorded": frozenset({"effective"}),
    "effective": frozenset({"superseded"}),
    "rejected": frozenset(),
    "superseded": frozenset(),
}

COMPILE_TRANSITIONS = {
    "drafted": frozenset({"mechanically_validated", "rejected"}),
    "mechanically_validated": frozenset({"editorially_reviewed", "rejected"}),
    "editorially_reviewed": frozenset({"accepted", "human_required", "rejected"}),
    "human_required": frozenset({"editorially_reviewed", "rejected"}),
    "accepted": frozenset({"published", "stale", "superseded"}),
    "published": frozenset({"stale", "superseded"}),
    "stale": frozenset({"superseded"}),
    "rejected": frozenset(),
    "superseded": frozenset(),
}

STATE_MACHINES = {
    "identity_card": IDENTITY_CARD_TRANSITIONS,
    "work_order": WORK_ORDER_TRANSITIONS,
    "request": REQUEST_TRANSITIONS,
    "evidence": EVIDENCE_TRANSITIONS,
    "mapping": MAPPING_TRANSITIONS,
    "bundle": BUNDLE_TRANSITIONS,
    "question": QUESTION_TRANSITIONS,
    "ruling": RULING_TRANSITIONS,
    "compile": COMPILE_TRANSITIONS,
}

AUTHOR_ONLY_TRANSITIONS = {
    ("work_order", "awaiting_authorization", "authorized"),
    ("ruling", "drafted_by_codex", "author_confirmed"),
}


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def transition_receipt(
    *,
    machine: str,
    artifact_id: str,
    prior_state: str,
    new_state: str,
    authority: str,
    reason: str,
    tool_version: str,
    predecessor_receipt_hash: str | None,
    timestamp: str | None = None,
) -> dict[str, Any]:
    transitions = STATE_MACHINES.get(machine)
    if transitions is None:
        raise ContractError(f"unknown state machine: {machine}")
    if new_state not in transitions.get(prior_state, frozenset()):
        raise ContractError(f"prohibited {machine} transition: {prior_state} -> {new_state}")
    if (machine, prior_state, new_state) in AUTHOR_ONLY_TRANSITIONS and authority != "Asa Wember":
        raise ContractError(f"transition requires author authority: {prior_state} -> {new_state}")
    if not all((artifact_id, authority, reason, tool_version)):
        raise ContractError("transition fields must be non-empty")
    body: dict[str, Any] = {
        "schema_version": "M050-TRANSITION-RECEIPT-0.1",
        "machine": machine,
        "artifact_id": artifact_id,
        "prior_state": prior_state,
        "new_state": new_state,
        "authority": authority,
        "reason": reason,
        "tool_version": tool_version,
        "timestamp": timestamp or _utc_now(),
        "predecessor_receipt_hash": predecessor_receipt_hash,
    }
    body["receipt_id"] = content_id("tr", body)
    return body
