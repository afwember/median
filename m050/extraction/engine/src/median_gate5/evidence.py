from __future__ import annotations

from typing import Any

from .canonical import content_id
from .errors import ContractError


def make_evidence_candidate(
    *,
    source_id: str,
    source_sha256: str,
    block_id: str,
    exact_source_text: str,
    normalized_claim: str,
    claim_kind: str,
    stream: str,
    request_id: str,
    response_id: str,
    legacy_record_id: str | None = None,
) -> dict[str, Any]:
    required = {
        "source_id": source_id,
        "source_sha256": source_sha256,
        "block_id": block_id,
        "exact_source_text": exact_source_text,
        "normalized_claim": normalized_claim,
        "claim_kind": claim_kind,
        "stream": stream,
        "request_id": request_id,
        "response_id": response_id,
    }
    if not all(required.values()):
        raise ContractError("Layer E candidate fields must be non-empty")
    identity = {
        key: required[key]
        for key in (
            "source_sha256",
            "block_id",
            "exact_source_text",
            "normalized_claim",
            "claim_kind",
            "stream",
        )
    }
    result: dict[str, Any] = {
        "schema_version": "M050-LAYER-E-CANDIDATE-0.1",
        "evidence_id": content_id("e", identity),
        "state": "reviewed",
        **required,
        "legacy_record_id": legacy_record_id,
    }
    return result


def accept_evidence_candidate(
    candidate: dict[str, Any], acceptance_receipt_id: str
) -> dict[str, Any]:
    if candidate.get("schema_version") != "M050-LAYER-E-CANDIDATE-0.1":
        raise ContractError("only a Layer E candidate can be accepted")
    if candidate.get("state") != "reviewed":
        raise ContractError("Layer E candidate must be reviewed before acceptance")
    if not acceptance_receipt_id:
        raise ContractError("acceptance receipt ID is required")
    accepted = dict(candidate)
    accepted.update(
        schema_version="M050-LAYER-E-0.1",
        state="accepted",
        acceptance_receipt_id=acceptance_receipt_id,
        supersedes_evidence_id=None,
    )
    return accepted
