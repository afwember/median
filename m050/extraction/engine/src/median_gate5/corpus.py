from __future__ import annotations

from collections import Counter
from copy import deepcopy
from typing import Any

from .canonical import content_id
from .errors import ContractError


EXCLUDED_DISPOSITIONS = {"retain_companion_no_atomic_compile_extraction"}
PRE_RECONCILIATION_DISPOSITIONS = {
    "source_bounded_atomic_extraction",
    "source_bounded_atomic_extraction_before_grand_reconciliation",
    "source_bounded_atomic_extraction_then_content_partition_before_grand_reconciliation",
}
LATER_OR_CONDITIONAL_DISPOSITIONS = {
    "deferred_source_bounded_atomic_extraction",
    "deterministic_publication_control_parse",
    "deferred_optional_extraction",
    "post_reconciliation_grounded_v0_4_6_coverage_audit",
}
LEGACY_ATOMIZED_DISPOSITIONS = PRE_RECONCILIATION_DISPOSITIONS | {
    "ruling_id_bounded_extraction_then_deterministic_partition"
}


def classify_source(source: dict[str, Any]) -> tuple[bool, str, str]:
    """Return compile inclusion, current state, and processing phase.

    Gate 2's disposition and explicit Gate 3 reuse flag are authoritative. A
    source without a recognized disposition fails closed rather than silently
    disappearing from the corpus boundary.
    """

    disposition = source.get("disposition")
    existing = source.get("gate_3_existing_candidate") is True
    if disposition in EXCLUDED_DISPOSITIONS:
        if existing:
            raise ContractError("an excluded companion cannot be a Gate 3 candidate")
        return False, "excluded_non_atomic_companion", "outside_atomic_compile"
    if existing:
        if disposition not in LEGACY_ATOMIZED_DISPOSITIONS:
            raise ContractError(
                f"Gate 3 candidate has incompatible disposition: {disposition}"
            )
        return True, "atomized_legacy_seed", "preserved_pre_reconciliation_seed"
    if disposition in PRE_RECONCILIATION_DISPOSITIONS:
        return True, "outstanding", "pre_reconciliation_atomization"
    if disposition in LATER_OR_CONDITIONAL_DISPOSITIONS:
        return True, "outstanding", "later_or_conditional_compile_stage"
    raise ContractError(f"unrecognized Gate 2 source disposition: {disposition}")


def derive_compile_source_state(
    gate_2: dict[str, Any], *, manifest_path: str, manifest_sha256: str
) -> dict[str, Any]:
    sources = gate_2.get("sources")
    if not isinstance(sources, list):
        raise ContractError("Gate 2 source disposition must contain a sources list")

    rows: list[dict[str, Any]] = []
    source_ids: set[str] = set()
    for position, source in enumerate(sources, 1):
        if not isinstance(source, dict):
            raise ContractError(f"Gate 2 source {position} is not an object")
        source_id = source.get("source_id")
        if not isinstance(source_id, str) or not source_id:
            raise ContractError(f"Gate 2 source {position} lacks source_id")
        if source_id in source_ids:
            raise ContractError(f"duplicate Gate 2 source_id: {source_id}")
        source_ids.add(source_id)
        in_compile_scope, current_state, phase = classify_source(source)
        row = {
            "position": position,
            "source_id": source_id,
            "path": source.get("path"),
            "sha256": source.get("sha256"),
            "content_role": source.get("content_role"),
            "disposition": source.get("disposition"),
            "output_streams": deepcopy(source.get("output_streams", [])),
            "gate_3_existing_candidate": source.get("gate_3_existing_candidate") is True,
            "in_compile_scope": in_compile_scope,
            "current_state": current_state,
            "processing_phase": phase,
        }
        for optional in ("timing", "reason", "note", "model_extraction"):
            if optional in source:
                row[optional] = deepcopy(source[optional])
        rows.append(row)

    states = Counter(row["current_state"] for row in rows)
    phases = Counter(row["processing_phase"] for row in rows)
    summary = {
        "registered_sources": len(rows),
        "atomic_compile_exclusions": states["excluded_non_atomic_companion"],
        "compile_scope_sources": sum(row["in_compile_scope"] for row in rows),
        "atomized_legacy_seed_sources": states["atomized_legacy_seed"],
        "outstanding_compile_scope_sources": states["outstanding"],
        "outstanding_pre_reconciliation_sources": phases[
            "pre_reconciliation_atomization"
        ],
        "outstanding_later_or_conditional_sources": phases[
            "later_or_conditional_compile_stage"
        ],
    }
    if summary != {
        "registered_sources": 24,
        "atomic_compile_exclusions": 2,
        "compile_scope_sources": 22,
        "atomized_legacy_seed_sources": 4,
        "outstanding_compile_scope_sources": 18,
        "outstanding_pre_reconciliation_sources": 14,
        "outstanding_later_or_conditional_sources": 4,
    }:
        raise ContractError(f"unexpected Gate 2 corpus vector: {summary}")

    body = {
        "title": "MEDIAN v0.5.0 Compile Source State Matrix",
        "created": "2026-08-03",
        "status": "CORPUS_ATOMIZATION_INCOMPLETE",
        "authority": {
            "source_manifest_path": manifest_path,
            "source_manifest_sha256": manifest_sha256,
            "derivation_rule": "Gate 2 disposition plus explicit Gate 3 existing-candidate flag; no filename inference",
        },
        "summary": summary,
        "transition_constraints": {
            "partial_legacy_seed_may_be_called_corpus_complete": False,
            "legacy_review_queue_execution_authorized": False,
            "semantic_acceptance_authorized": False,
            "mapping_authorized": False,
            "reconciliation_authorized": False,
            "compiled_prose_authorized": False,
            "google_sheets_interactions_authorized": False,
        },
        "sources": rows,
    }
    return {
        "schema_version": "M050-COMPILE-SOURCE-STATE-MATRIX-0.1",
        "corpus_state_id": content_id("cssm", body),
        **body,
    }
