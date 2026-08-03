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
MARKDOWN_OUTPUT = REPO_ROOT / "m050/extraction/control/M050_Compile_Source_State_Matrix_v0_1_MEDIANv0_5_0.md"


def build() -> dict:
    gate_2 = yaml.safe_load(GATE_2.read_text(encoding="utf-8"))
    return derive_compile_source_state(
        gate_2,
        manifest_path=GATE_2.relative_to(REPO_ROOT).as_posix(),
        manifest_sha256=sha256_file(GATE_2),
    )


def render_markdown(state: dict) -> bytes:
    summary = state["summary"]
    lines = [
        "# MEDIAN v0.5.0 Compile Source State Matrix",
        "",
        "This is a generated, human-readable view of the authoritative Gate 2 source disposition. "
        "The JSON companion and the active guard are the machine-enforced controls.",
        "",
        "## Corpus vector",
        "",
        f"- Registered sources: **{summary['registered_sources']}**",
        f"- Atomic compile scope: **{summary['compile_scope_sources']}**",
        f"- Existing atomized legacy seed: **{summary['atomized_legacy_seed_sources']}**",
        f"- Outstanding compile-scope sources: **{summary['outstanding_compile_scope_sources']}**",
        f"- Outstanding before reconciliation: **{summary['outstanding_pre_reconciliation_sources']}**",
        f"- Later or conditional compile stages: **{summary['outstanding_later_or_conditional_sources']}**",
        f"- Non-atomic companions excluded from atomic compile: **{summary['atomic_compile_exclusions']}**",
        "",
        "> The four-source legacy migration is preserved as a useful seed. It is not whole-corpus "
        "atomization and does not authorize semantic review, acceptance, mapping, reconciliation, or compiled prose.",
        "",
        "## Source-by-source state",
        "",
        "| # | Source ID | Disposition | Compile | Current state | Phase |",
        "|---:|---|---|:---:|---|---|",
    ]
    for row in state["sources"]:
        lines.append(
            f"| {row['position']} | `{row['source_id']}` | `{row['disposition']}` | "
            f"{'yes' if row['in_compile_scope'] else 'no'} | `{row['current_state']}` | "
            f"`{row['processing_phase']}` |"
        )
    lines.extend(
        [
            "",
            "## Transition boundary",
            "",
            "Until the outstanding source work is completed and a new guarded transition explicitly authorizes it:",
            "",
            "- the legacy semantic-review queues remain preserved but dormant;",
            "- semantic acceptance, mapping, reconciliation, and compiled prose remain prohibited;",
            "- provider calls remain prohibited; and",
            "- Google Sheets interaction remains paused.",
            "",
            f"Machine state ID: `{state['corpus_state_id']}`",
            "",
        ]
    )
    return "\n".join(lines).encode("utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    state = build()
    json_bytes = canonical_json_bytes(state) + b"\n"
    markdown_bytes = render_markdown(state)
    if args.check:
        errors = []
        for path, expected in ((JSON_OUTPUT, json_bytes), (MARKDOWN_OUTPUT, markdown_bytes)):
            if not path.is_file() or path.read_bytes() != expected:
                errors.append(path.relative_to(REPO_ROOT).as_posix())
        if errors:
            print("compile source state drift: " + ", ".join(errors), file=sys.stderr)
            return 1
        print(json.dumps(state["summary"], sort_keys=True))
        return 0
    write_new_bytes(JSON_OUTPUT, json_bytes)
    write_new_bytes(MARKDOWN_OUTPUT, markdown_bytes)
    print(json.dumps(state["summary"], sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
