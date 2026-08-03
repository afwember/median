#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

from median_gate5.canonical import content_id
from median_gate5.schema import validate_artifact


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--block-manifest", required=True)
    parser.add_argument("--section-level", type=int, default=1)
    parser.add_argument("--max-tokens", type=int, required=True)
    parser.add_argument("--max-claim-blocks", type=int, required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    if not 1 <= args.section_level <= 6:
        raise SystemExit("section level must be between 1 and 6")

    manifest = json.loads(Path(args.block_manifest).read_text(encoding="utf-8"))
    marker = "#" * args.section_level + " "
    groups: list[list[dict]] = []
    current_group: list[dict] = []
    for block in manifest["blocks"]:
        boundary = block["block_type"] == "heading" and block["text"].startswith(marker)
        if boundary and current_group:
            groups.append(current_group)
            current_group = []
        current_group.append(block)
    if current_group:
        groups.append(current_group)

    chunks: list[dict] = []
    current: list[dict] = []
    tokens = 0
    claims = 0

    def measures(items: list[dict]) -> tuple[int, int]:
        return (
            sum(max(1, (len(item["text"]) + 3) // 4) for item in items),
            sum(int(item["claim_bearing"]) for item in items),
        )

    def flush() -> None:
        nonlocal current, tokens, claims
        if not current:
            return
        chunks.append(
            {
                "ordinal": len(chunks) + 1,
                "block_ids": [item["block_id"] for item in current],
                "estimated_tokens": tokens,
                "claim_bearing_blocks": claims,
            }
        )
        current, tokens, claims = [], 0, 0

    for group in groups:
        group_tokens, group_claims = measures(group)
        if group_tokens > args.max_tokens or group_claims > args.max_claim_blocks:
            raise SystemExit(f"section exceeds limits: {group[0]['block_id']}")
        if current and (
            tokens + group_tokens > args.max_tokens
            or claims + group_claims > args.max_claim_blocks
        ):
            flush()
        current.extend(group)
        tokens += group_tokens
        claims += group_claims
    flush()

    body = {
        "source_id": manifest["source_id"],
        "block_manifest_id": manifest["manifest_id"],
        "max_tokens": args.max_tokens,
        "max_claim_blocks": args.max_claim_blocks,
        "chunks": chunks,
    }
    artifact = {
        "schema_version": "M050-CHUNK-PLAN-0.1",
        "plan_id": content_id("cp", body),
        **body,
    }
    validate_artifact("chunk_plan", artifact)
    output = Path(args.output)
    if output.exists():
        raise SystemExit(f"refusing to overwrite: {output}")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        json.dumps(artifact, sort_keys=True, separators=(",", ":")) + "\n",
        encoding="utf-8",
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
