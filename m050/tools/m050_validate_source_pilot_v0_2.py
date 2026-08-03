#!/usr/bin/env python3
from __future__ import annotations

import argparse
from collections import Counter
import json
from pathlib import Path
from typing import Any

import jsonschema

from median_gate5.validation import validate_atoms, validate_block_dispositions


SOURCE_ID = "M050-SRC-AUTHORIAL-GRAMMAR-001"
ALLOWED_STREAM = "evidence_authorial_rule"


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def validate_pilot_response(
    payload: dict[str, Any],
    response: dict[str, Any],
    schema: dict[str, Any],
) -> dict[str, Any]:
    errors: list[str] = []
    schema_errors = sorted(
        jsonschema.Draft202012Validator(schema).iter_errors(response),
        key=lambda error: list(error.absolute_path),
    )
    errors.extend(f"schema: {error.message}" for error in schema_errors)

    if payload.get("source_id") != SOURCE_ID:
        errors.append("payload source_id violates the bound source")
    if response.get("source_id") != SOURCE_ID:
        errors.append("response source_id violates the bound source")

    blocks = payload.get("blocks", [])
    eligible = [
        {**block, "claim_bearing": True}
        for block in blocks
        if block.get("structural_disposition") == "eligible"
    ]
    context_ids = {
        block.get("block_id")
        for block in blocks
        if block.get("structural_disposition") == "context_only"
    }
    dispositions = response.get("dispositions", [])
    coverage = validate_block_dispositions(eligible, dispositions)
    if not coverage["passed"]:
        errors.append(f"coverage: {json.dumps(coverage['errors'], sort_keys=True)}")

    conditional_errors = 0
    for disposition in dispositions:
        block_id = disposition.get("block_id")
        kind = disposition.get("kind")
        if block_id in context_ids:
            errors.append(f"context-only block was dispositioned: {block_id}")
        if kind == "excluded":
            errors.append(f"pre-filtered eligible block was provider-excluded: {block_id}")
        if kind == "atoms" and not disposition.get("atoms"):
            conditional_errors += 1
            errors.append(f"atoms disposition lacks atoms: {block_id}")
        if kind != "atoms" and "atoms" in disposition:
            conditional_errors += 1
            errors.append(f"non-atoms disposition carries atoms: {block_id}")

    grounding = validate_atoms(SOURCE_ID, eligible, dispositions)
    if not grounding["passed"]:
        errors.append("one or more atoms failed exact contiguous grounding")

    proposal_ids: list[str] = []
    by_id = {block.get("block_id"): block for block in blocks}
    for disposition in dispositions:
        block = by_id.get(disposition.get("block_id"), {})
        statuses = {
            marker.split(":", 1)[-1].strip().upper()
            for marker in block.get("status_markers", [])
        }
        for atom in disposition.get("atoms", []):
            proposal_ids.append(str(atom.get("proposal_id")))
            if atom.get("source_id") != SOURCE_ID:
                errors.append("atom source_id violates the bound source")
            if atom.get("block_id") != disposition.get("block_id"):
                errors.append("atom block_id differs from its disposition block")
            if atom.get("stream") != ALLOWED_STREAM:
                errors.append("atom stream violates the bound output stream")
            normalized = str(atom.get("normalized_claim", "")).upper()
            for status in statuses:
                if status and status not in normalized:
                    errors.append(
                        f"status qualifier {status} missing from atom {atom.get('proposal_id')}"
                    )

    duplicates = sorted(
        proposal_id
        for proposal_id, count in Counter(proposal_ids).items()
        if count > 1
    )
    if duplicates:
        errors.append(f"duplicate proposal IDs: {', '.join(duplicates)}")

    checks = {
        "schema_errors": len(schema_errors),
        "coverage_errors": 0 if coverage["passed"] else 1,
        "conditional_atoms_errors": conditional_errors,
        "grounding_errors": sum(
            not result["passed"] for result in grounding["atom_results"]
        ),
        "low_yield_review_blocks": grounding["low_yield_review"],
    }
    return {"passed": not errors, "checks": checks, "errors": errors}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--payload", required=True)
    parser.add_argument("--response", required=True)
    parser.add_argument("--schema", required=True)
    args = parser.parse_args()
    result = validate_pilot_response(
        read_json(Path(args.payload)),
        read_json(Path(args.response)),
        read_json(Path(args.schema)),
    )
    print(json.dumps(result, sort_keys=True))
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
