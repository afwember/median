#!/usr/bin/env python3
"""Derive the complete MEDIAN compile-source state from Gate 2."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

import yaml


REPO_ROOT = Path(__file__).resolve().parents[2]
ENGINE_SRC = REPO_ROOT / "m050/extraction/engine/src"
sys.path.insert(0, str(ENGINE_SRC))

from median_gate5.canonical import canonical_json_bytes, sha256_file, write_new_bytes  # noqa: E402
from median_gate5.corpus import derive_compile_source_state  # noqa: E402


GATE_2 = REPO_ROOT / "m050/extraction/audit/M050_Extraction_Gate_2_Source_Disposition_v0_1_MEDIANv0_5_0.yaml"
JSON_OUTPUT = REPO_ROOT / "m050/extraction/control/M050_Compile_Source_State_Matrix_v0_1_MEDIANv0_5_0.json"


def build() -> dict:
    gate_2 = yaml.safe_load(GATE_2.read_text(encoding="utf-8"))
    return derive_compile_source_state(
        gate_2,
        manifest_path=GATE_2.relative_to(REPO_ROOT).as_posix(),
        manifest_sha256=sha256_file(GATE_2),
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    state = build()
    json_bytes = canonical_json_bytes(state) + b"\n"
    if args.check:
        if not JSON_OUTPUT.is_file() or JSON_OUTPUT.read_bytes() != json_bytes:
            print(
                "compile source state drift: " + JSON_OUTPUT.relative_to(REPO_ROOT).as_posix(),
                file=sys.stderr,
            )
            return 1
        print(json.dumps(state["summary"], sort_keys=True))
        return 0
    write_new_bytes(JSON_OUTPUT, json_bytes)
    print(json.dumps(state["summary"], sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
