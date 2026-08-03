#!/usr/bin/env python3
from __future__ import annotations

import argparse
import importlib.util
import json
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--validator", required=True)
    parser.add_argument("--payload", required=True)
    parser.add_argument("--response", required=True)
    parser.add_argument("--schema", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    output = Path(args.output)
    if output.exists():
        raise SystemExit(f"refusing to overwrite: {output}")
    spec = importlib.util.spec_from_file_location("bound_pilot_validator", args.validator)
    module = importlib.util.module_from_spec(spec)
    if spec.loader is None:
        raise SystemExit("validator loader unavailable")
    spec.loader.exec_module(module)
    result = module.validate_pilot_response(
        json.loads(Path(args.payload).read_text(encoding="utf-8")),
        json.loads(Path(args.response).read_text(encoding="utf-8")),
        json.loads(Path(args.schema).read_text(encoding="utf-8")),
    )
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"passed": result["passed"], "error_count": len(result["errors"])}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
