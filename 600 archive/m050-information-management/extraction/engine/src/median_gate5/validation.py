from __future__ import annotations

from collections import Counter, defaultdict
from typing import Any

from .normalization import locate_quote


ALLOWED_DISPOSITIONS = {
    "atoms",
    "no_substantive_claim",
    "excluded",
    "review_required",
}


def validate_block_dispositions(
    blocks: list[dict[str, Any]], dispositions: list[dict[str, Any]]
) -> dict[str, Any]:
    eligible = {block["block_id"] for block in blocks if block.get("claim_bearing")}
    counts = Counter(disposition.get("block_id") for disposition in dispositions)
    unknown = sorted(block_id for block_id in counts if block_id not in eligible)
    missing = sorted(eligible - set(counts))
    duplicates = sorted(block_id for block_id, count in counts.items() if count > 1)
    invalid_kinds = sorted(
        {
            str(disposition.get("kind"))
            for disposition in dispositions
            if disposition.get("kind") not in ALLOWED_DISPOSITIONS
        }
    )
    empty_atoms = sorted(
        disposition["block_id"]
        for disposition in dispositions
        if disposition.get("kind") == "atoms" and not disposition.get("atoms")
    )
    errors = {
        "missing": missing,
        "duplicates": duplicates,
        "unknown": unknown,
        "invalid_kinds": invalid_kinds,
        "empty_atoms": empty_atoms,
    }
    return {"passed": not any(errors.values()), "errors": errors}


def validate_atoms(
    source_id: str,
    blocks: list[dict[str, Any]],
    dispositions: list[dict[str, Any]],
) -> dict[str, Any]:
    by_id = {block["block_id"]: block for block in blocks}
    results: list[dict[str, Any]] = []
    realized = defaultdict(int)
    for disposition in dispositions:
        if disposition.get("kind") != "atoms":
            continue
        block_id = disposition.get("block_id")
        block = by_id.get(block_id)
        for atom in disposition.get("atoms", []):
            errors: list[str] = []
            if atom.get("source_id") != source_id:
                errors.append("source_id mismatch")
            if atom.get("block_id") != block_id:
                errors.append("block_id mismatch")
            located = None
            if block is None:
                errors.append("unknown block")
            else:
                try:
                    located = locate_quote(block["text"], atom.get("exact_source_text", ""))
                except Exception as exc:
                    errors.append(str(exc))
            if located is not None:
                realized[block_id] += 1
            results.append(
                {
                    "proposal_id": atom.get("proposal_id"),
                    "passed": not errors,
                    "errors": errors,
                    "raw_text": located.raw_text if located else None,
                    "raw_start": located.start if located else None,
                    "raw_end": located.end if located else None,
                    "grounding_method": located.method if located else None,
                    "normalization_events": list(located.transformations) if located else [],
                }
            )

    low_yield = sorted(
        block["block_id"]
        for block in blocks
        if block.get("claim_bearing")
        and block.get("estimated_claims", 1) >= 2
        and realized[block["block_id"]] < block.get("estimated_claims", 1)
    )
    return {
        "passed": all(result["passed"] for result in results),
        "atom_results": results,
        "low_yield_review": low_yield,
    }
