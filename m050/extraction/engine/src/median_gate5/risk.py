from __future__ import annotations

import re
from typing import Any


HIGH_RISK_TERMS = re.compile(
    r"\b(?:ruling|authority|supersed(?:e|es|ed|ing)|conflict|constitutional|"
    r"human[_ -]?required|rejected|historical|provisional)\b",
    re.IGNORECASE,
)
ELEVATED_TERMS = re.compile(
    r"\b(?:must|shall|cannot|never|except|unless|only|maximum|minimum|capacity|"
    r"tier|percent|percentage|cost|duration)\b|\d",
    re.IGNORECASE,
)


def classify_review_risk(block: dict[str, Any], atom: dict[str, Any] | None = None) -> dict[str, Any]:
    text = block.get("text", "") + " " + (atom or {}).get("normalized_claim", "")
    signals: list[str] = []
    if HIGH_RISK_TERMS.search(text):
        signals.append("authority_status_or_provisional_language")
    if block.get("block_type") == "table_row":
        signals.append("table_derived")
    if ELEVATED_TERMS.search(text):
        signals.append("numeric_negation_exception_or_obligation")
    if block.get("estimated_claims", 1) > 1:
        signals.append("likely_compound_or_dense")
    if block.get("status_markers"):
        signals.append("explicit_status_boundary")
    if "authority_status_or_provisional_language" in signals:
        tier = 1
    elif signals:
        tier = 2
    else:
        tier = 3
    return {"risk_tier": tier, "signals": sorted(set(signals))}


def exclusion_audit(
    total_claim_bearing_blocks: int,
    exclusions: list[dict[str, Any]],
    anomalous_rate: float = 0.25,
) -> dict[str, Any]:
    if total_claim_bearing_blocks < 0:
        raise ValueError("block count cannot be negative")
    count = len(exclusions)
    rate = count / total_claim_bearing_blocks if total_claim_bearing_blocks else 0.0
    heuristic = sorted(
        exclusion.get("block_id", "")
        for exclusion in exclusions
        if exclusion.get("stage") in {"identity", "structural"}
    )
    pending = sorted(
        exclusion.get("block_id", "")
        for exclusion in exclusions
        if exclusion.get("review_state") not in {"reviewed", "accepted"}
    )
    return {
        "exclusion_count": count,
        "exclusion_rate": rate,
        "anomalous_rate": rate > anomalous_rate,
        "heuristic_review": heuristic,
        "pending_review": pending,
    }
