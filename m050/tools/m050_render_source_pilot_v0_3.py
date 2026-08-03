#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def read_jsonl(path: Path):
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines()]


def write_new(path: Path, value) -> None:
    if path.exists():
        raise SystemExit(f"refusing to overwrite: {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n", encoding="utf-8")


def block_record(block):
    return {
        "block_id": block["block_id"],
        "block_type": block["block_type"],
        "status_markers": block["status_markers"],
        "text": block["text"],
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", required=True)
    parser.add_argument("--ledger", required=True)
    parser.add_argument("--prompt", required=True)
    parser.add_argument("--schema", required=True)
    parser.add_argument("--pilot-id", required=True)
    parser.add_argument("--start-ordinal", type=int, required=True)
    parser.add_argument("--end-ordinal", type=int, required=True)
    parser.add_argument("--max-output-tokens", type=int, required=True)
    parser.add_argument("--output-payload", required=True)
    parser.add_argument("--output-request", required=True)
    args = parser.parse_args()

    manifest = read_json(Path(args.manifest))
    ledger = {item["block_id"]: item for item in read_jsonl(Path(args.ledger))}
    prompt = Path(args.prompt).read_text(encoding="utf-8")
    schema = read_json(Path(args.schema))
    selected = [
        block for block in manifest["blocks"]
        if args.start_ordinal <= block["ordinal"] <= args.end_ordinal
        and ledger[block["block_id"]]["disposition"] != "excluded"
    ]
    context_blocks = [
        block_record(block) for block in selected
        if ledger[block["block_id"]]["disposition"] == "context_only"
    ]
    target_blocks = [
        block_record(block) for block in selected
        if ledger[block["block_id"]]["disposition"] == "eligible"
    ]
    if not target_blocks:
        raise SystemExit("pilot target selection is empty")
    disposition_schema = schema["properties"]["dispositions"]
    if disposition_schema.get("minItems") not in (None, 0, 1):
        raise SystemExit("provider schema uses unsupported array minItems")
    if "maxItems" in disposition_schema:
        raise SystemExit("provider schema uses unsupported array maxItems")
    payload = {
        "schema_version": "M050-PILOT-PAYLOAD-0.2",
        "pilot_id": args.pilot_id,
        "source_id": manifest["source_id"],
        "source_sha256": manifest["source_sha256"],
        "ordinal_range": [args.start_ordinal, args.end_ordinal],
        "required_target_disposition_count": len(target_blocks),
        "context_blocks": context_blocks,
        "target_blocks": target_blocks,
    }
    write_new(Path(args.output_payload), payload)
    payload_bytes = Path(args.output_payload).read_bytes()
    user_text = "SOURCE_BLOCKS\n" + json.dumps(payload, sort_keys=True, separators=(",", ":")) + "\nEND_SOURCE_BLOCKS"
    response_schema = {key: value for key, value in schema.items() if key not in {"$schema", "$id"}}
    request = {
        "model": "claude-sonnet-5",
        "max_tokens": args.max_output_tokens,
        "thinking": {"type": "adaptive"},
        "output_config": {
            "effort": "low",
            "format": {"type": "json_schema", "schema": response_schema},
        },
        "system": prompt,
        "messages": [{"role": "user", "content": user_text}],
    }
    write_new(Path(args.output_request), request)
    request_bytes = Path(args.output_request).read_bytes()
    print(json.dumps({
        "pilot_id": args.pilot_id,
        "payload_sha256": hashlib.sha256(payload_bytes).hexdigest(),
        "request_sha256": hashlib.sha256(request_bytes).hexdigest(),
        "target_blocks": len(target_blocks),
        "context_blocks": len(context_blocks),
        "request_bytes": len(request_bytes),
        "conservative_input_token_forecast": (len(request_bytes) + 2) // 3,
        "maximum_output_tokens": args.max_output_tokens,
    }, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
