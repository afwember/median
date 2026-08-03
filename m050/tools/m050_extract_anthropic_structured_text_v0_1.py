#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--raw-response", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    output = Path(args.output)
    if output.exists():
        raise SystemExit(f"refusing to overwrite: {output}")
    response = json.loads(Path(args.raw_response).read_text(encoding="utf-8"))
    texts = [item.get("text", "") for item in response.get("content", []) if item.get("type") == "text"]
    if len(texts) != 1:
        raise SystemExit(f"expected exactly one text content block, found {len(texts)}")
    json.loads(texts[0])
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(texts[0], encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
