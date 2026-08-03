from __future__ import annotations

from collections import defaultdict
from typing import Any

from .canonical import content_id, sha256_bytes, canonical_json_bytes
from .errors import ContractError


TERMINAL_MAPPING_STATES = {
    "mapped",
    "unmapped",
    "ambiguous",
    "invalid",
    "human_required",
}


def build_reconciliation_bundles(
    mappings: list[dict[str, Any]], aliases: dict[str, list[str]] | None = None
) -> tuple[list[dict[str, Any]], dict[str, list[str]]]:
    aliases = aliases or {}
    members: dict[str, dict[str, set[str]]] = defaultdict(lambda: defaultdict(set))
    exceptional: dict[str, list[str]] = defaultdict(list)

    for mapping in mappings:
        evidence_id = mapping.get("evidence_id")
        status = mapping.get("status")
        subjects = mapping.get("subjects", [])
        if not evidence_id or status not in TERMINAL_MAPPING_STATES:
            raise ContractError("mapping lacks evidence_id or valid terminal status")
        if status != "mapped":
            exceptional[status].append(evidence_id)
            continue
        if not subjects:
            exceptional["mapped_without_subject"].append(evidence_id)
            continue
        for subject in subjects:
            members[subject][evidence_id].add("direct_mapping")
            for alias in aliases.get(subject, []):
                members[alias][evidence_id].add(f"alias_of:{subject}")

    bundles: list[dict[str, Any]] = []
    for subject in sorted(members):
        membership = [
            {"evidence_id": evidence_id, "inclusion_reasons": sorted(reasons)}
            for evidence_id, reasons in sorted(members[subject].items())
        ]
        body = {"subject": subject, "membership": membership}
        bundles.append(
            {
                "schema_version": "M050-RECONCILIATION-BUNDLE-0.1",
                "bundle_id": content_id("rb", body),
                "state": "constructed",
                "subject": subject,
                "membership": membership,
                "membership_sha256": sha256_bytes(canonical_json_bytes(membership)),
            }
        )
    return bundles, {key: sorted(set(value)) for key, value in sorted(exceptional.items())}


def orphaned_mapped_evidence(
    mappings: list[dict[str, Any]], bundles: list[dict[str, Any]]
) -> list[str]:
    expected = {
        mapping["evidence_id"]
        for mapping in mappings
        if mapping.get("status") == "mapped"
    }
    present = {
        member["evidence_id"]
        for bundle in bundles
        for member in bundle.get("membership", [])
    }
    return sorted(expected - present)
