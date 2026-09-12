#!/usr/bin/env python3
"""Sole repository guard for creation-first MEDIAN v0.5.0 compilation."""

from __future__ import annotations

import argparse
from collections import Counter
from datetime import datetime
import hashlib
import json
from pathlib import Path
import subprocess
import sys
from typing import Iterable
from zoneinfo import ZoneInfo


ROOT = Path(__file__).resolve().parents[2]
AGENTS = ROOT / "AGENTS.md"
OVERRIDE = ROOT / "AGENTS.override.md"
STATUS = ROOT / "STATUS.md"
STATE = ROOT / "m050/control/M050_Compile_State_MEDIANv0_5_0.json"
MANIFEST = ROOT / "m050/corpus/M050_Authorial_Atom_Corpus_Manifest_MEDIANv0_5_0.json"
CORPUS = ROOT / "m050/corpus/M050_Authorial_Atom_Corpus_MEDIANv0_5_0.jsonl"
ARCHIVE = ROOT / "600 archive/m050-information-management"

ATOM_SCHEMA = "M050-AUTHORIAL-CORPUS-ATOM-0.1"
MANIFEST_SCHEMA = "M050-AUTHORIAL-CORPUS-MANIFEST-0.1"
STATE_SCHEMA = "M050-COMPILE-STATE-2.0"
EXPECTED_ATOMS = 5382
EXPECTED_SOURCES = 18
EXPECTED_FROZEN_FILES = 33
IGNORED_NAMES = {".DS_Store"}
RETIRED_ACTIVE_PATHS = (
    "m050/extraction",
    "m050/mapping",
    "m050/reconciliation",
)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def sha256_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def read_json(path: Path, errors: list[str]) -> dict:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"cannot read JSON {path.relative_to(ROOT)}: {exc}")
        return {}
    if not isinstance(value, dict):
        errors.append(f"JSON root is not an object: {path.relative_to(ROOT)}")
        return {}
    return value


def read_jsonl(path: Path, errors: list[str]) -> list[dict]:
    records: list[dict] = []
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except OSError as exc:
        errors.append(f"cannot read JSONL {path.relative_to(ROOT)}: {exc}")
        return records
    for line_number, line in enumerate(lines, start=1):
        if not line.strip():
            continue
        try:
            record = json.loads(line)
        except json.JSONDecodeError as exc:
            errors.append(f"invalid JSONL {path.relative_to(ROOT)}:{line_number}: {exc}")
            continue
        if not isinstance(record, dict):
            errors.append(f"JSONL record is not an object: {path.relative_to(ROOT)}:{line_number}")
            continue
        records.append(record)
    return records


def expected_status(state: dict) -> str:
    dashboard = state.get("dashboard", {})
    return (
        "# MEDIAN COMPILE — v0.5.0\n\n"
        f"{dashboard.get('updated_human', '')}<br>\n\n"
        "<!-- Derived dashboard only; m050/control/M050_Compile_State_MEDIANv0_5_0.json is authoritative. -->\n\n"
        f"**STATUS:** {dashboard.get('status', '')}<br>\n"
        f"**PHASE:** {dashboard.get('phase', '')}<br>\n"
        f"**SOURCE:** {dashboard.get('source', '')}<br>\n"
        f"**PROGRESS:** {dashboard.get('progress', '')}<br>\n"
        f"**NOW:** {dashboard.get('now', '')}<br>\n"
        f"**NEXT:** {dashboard.get('next', '')}\n"
    )


def validate_timestamp(state: dict, errors: list[str]) -> None:
    try:
        exact = datetime.fromisoformat(state.get("updated", ""))
    except (TypeError, ValueError):
        errors.append("canonical timestamp is not valid ISO-8601")
        return
    if exact.tzinfo is None or exact.microsecond:
        errors.append("canonical timestamp must be timezone-aware and rounded to the second")
        return
    eastern = exact.astimezone(ZoneInfo("America/New_York"))
    expected = (
        f"{eastern.strftime('%B')} {eastern.day}, {eastern.year} at "
        f"{eastern.strftime('%I').lstrip('0')}:{eastern.strftime('%M:%S %p %Z')}"
    )
    if state.get("dashboard", {}).get("updated_human") != expected:
        errors.append("dashboard timestamp disagrees with canonical timestamp")


def validate_operating_contract(errors: list[str]) -> None:
    if OVERRIDE.exists() or OVERRIDE.is_symlink():
        errors.append("AGENTS.override.md exists")
    try:
        text = AGENTS.read_text(encoding="utf-8")
    except OSError as exc:
        errors.append(f"cannot read AGENTS.md: {exc}")
        return
    for heading in (
        "## Conservation of System",
        "## Roles and authority",
        "## Canonical controls",
        "## Historical archive",
        "## Required cold start",
        "## Active phase profile — authorial GDD preparation",
        "## Gates and halt conditions",
        "## STATUS contract",
    ):
        if heading not in text:
            errors.append(f"AGENTS omits required section: {heading}")
    if len(text.encode("utf-8")) > 32 * 1024:
        errors.append("AGENTS exceeds the 32 KiB discovery limit")
    for required in (STATE, MANIFEST, CORPUS, ARCHIVE / "README.md"):
        relative = required.relative_to(ROOT).as_posix()
        if relative not in text:
            errors.append(f"AGENTS omits active or archival boundary: {relative}")


def validate_topology(errors: list[str]) -> None:
    for relative in RETIRED_ACTIVE_PATHS:
        if (ROOT / relative).exists():
            errors.append(f"retired information-management path remains active: {relative}")
    if not ARCHIVE.is_dir():
        errors.append("information-management archive is missing")
    active_python = {
        path.relative_to(ROOT).as_posix()
        for path in (ROOT / "m050/tools").glob("*.py")
    }
    expected_python = {
        "m050/tools/m050_guard.py",
        "m050/tools/m050_render_status.py",
    }
    if active_python != expected_python:
        errors.append(
            "active tool surface drifted: "
            f"expected {sorted(expected_python)}, found {sorted(active_python)}"
        )


def validate_manifest_and_corpus(state: dict, errors: list[str]) -> tuple[int, int]:
    manifest = read_json(MANIFEST, errors)
    if not manifest:
        return 0, 0
    if manifest.get("schema_version") != MANIFEST_SCHEMA:
        errors.append("authorial corpus manifest schema is invalid")
    if manifest.get("status") != "FROZEN_AUTHORIAL_SOURCE_LIBRARY":
        errors.append("authorial corpus manifest is not frozen")
    if manifest.get("corpus_record") != CORPUS.relative_to(ROOT).as_posix():
        errors.append("manifest points to the wrong authorial corpus")
    if not CORPUS.is_file() or manifest.get("corpus_record_sha256") != sha256_file(CORPUS):
        errors.append("authorial corpus hash drifted")
    if manifest.get("atom_count") != EXPECTED_ATOMS or manifest.get("source_count") != EXPECTED_SOURCES:
        errors.append("authorial corpus manifest count drifted")

    library = state.get("source_library", {})
    if library.get("manifest") != MANIFEST.relative_to(ROOT).as_posix():
        errors.append("canonical state points to the wrong corpus manifest")
    if library.get("manifest_sha256") != sha256_file(MANIFEST):
        errors.append("canonical corpus-manifest binding drifted")
    if library.get("record") != CORPUS.relative_to(ROOT).as_posix():
        errors.append("canonical state points to the wrong corpus record")
    if library.get("record_sha256") != sha256_file(CORPUS):
        errors.append("canonical corpus-record binding drifted")
    if library.get("atom_count") != EXPECTED_ATOMS or library.get("source_count") != EXPECTED_SOURCES:
        errors.append("canonical source-library count drifted")

    frozen_files = manifest.get("frozen_source_files", [])
    expected_paths = {
        item.get("path"): item.get("sha256")
        for item in frozen_files
        if isinstance(item, dict)
    }
    if len(frozen_files) != EXPECTED_FROZEN_FILES or len(expected_paths) != EXPECTED_FROZEN_FILES:
        errors.append("frozen source-file manifest count drifted")
    actual_paths: set[str] = set()
    for root in (ROOT / "m050/docs/baseline", ROOT / "m050/docs/v0.5"):
        if root.is_dir():
            actual_paths.update(
                item.relative_to(ROOT).as_posix()
                for item in root.rglob("*")
                if item.is_file() and item.name not in IGNORED_NAMES
            )
    if actual_paths != set(expected_paths):
        errors.append("frozen source-file topology drifted")
    for relative, expected_hash in expected_paths.items():
        target = ROOT / str(relative)
        if not target.is_file() or sha256_file(target) != expected_hash:
            errors.append(f"frozen source file drifted: {relative}")

    records = read_jsonl(CORPUS, errors)
    required_keys = {
        "schema_version", "corpus_position", "atom_key", "atom_id", "source_id",
        "source_label", "source_document", "source_position", "source_atom_position",
        "section", "block_key", "block_id", "block_type", "claim_kind",
        "exact_source_text", "normalized_claim", "effective_claim",
        "effective_claim_origin", "effective_claim_sha256", "accepted_candidate_sha256",
        "authorial_decision",
    }
    source_documents = {
        item.get("source_id"): item
        for item in manifest.get("source_documents", [])
        if isinstance(item, dict)
    }
    keys: set[str] = set()
    source_counts: Counter[str] = Counter()
    for position, record in enumerate(records, start=1):
        if set(record) != required_keys:
            errors.append(f"authorial corpus record shape drifted at row {position}")
            continue
        if record.get("schema_version") != ATOM_SCHEMA or record.get("corpus_position") != position:
            errors.append(f"authorial corpus order or schema drifted at row {position}")
        atom_key = record.get("atom_key")
        if not isinstance(atom_key, str) or atom_key in keys:
            errors.append(f"duplicate or invalid atom key at row {position}")
        else:
            keys.add(atom_key)
        claim = record.get("effective_claim")
        if not isinstance(claim, str) or not claim.strip() or record.get("effective_claim_sha256") != sha256_text(claim):
            errors.append(f"effective claim binding drifted: {atom_key}")
        source_id = record.get("source_id")
        source = source_documents.get(source_id)
        if source is None or record.get("source_document") != source.get("path"):
            errors.append(f"source binding drifted: {atom_key}")
        source_counts[str(source_id)] += 1
        decision = record.get("authorial_decision")
        if not isinstance(decision, dict) or set(decision) != {
            "triage", "triage_event_id", "rewrite_resolution", "rewrite_event_id",
        }:
            errors.append(f"authorial decision shape drifted: {atom_key}")
    if len(records) != EXPECTED_ATOMS or len(keys) != EXPECTED_ATOMS:
        errors.append("authorial corpus does not contain 5,382 unique atoms")
    if len(source_counts) != EXPECTED_SOURCES:
        errors.append("authorial corpus source coverage drifted")
    for source_id, source in source_documents.items():
        if source_counts[source_id] != source.get("atom_count"):
            errors.append(f"authorial corpus source count drifted: {source_id}")
    return len(records), len(source_counts)


def validate_state(state: dict, errors: list[str]) -> None:
    required = {
        "schema_version", "status", "updated", "execution_state", "scope",
        "source_library", "information_management_archive", "authorial_gdd",
        "authority", "dashboard", "next_possible_transition",
    }
    if set(state) != required:
        errors.append("canonical state shape drifted")
    if state.get("schema_version") != STATE_SCHEMA:
        errors.append("canonical state schema is invalid")
    if state.get("status") != "AUTHORIAL_GDD_PREPARATION_READY" or state.get("execution_state") != state.get("status"):
        errors.append("canonical authorial-preparation lifecycle is invalid")
    scope = state.get("scope", {})
    if scope != {
        "version": "MEDIAN v0.5.0",
        "registered_sources": 24,
        "compile_scope_sources": 22,
        "atomized_authorial_sources": 18,
        "later_or_conditional_sources": 4,
        "non_atomic_companions": 2,
        "m051_allowed": False,
    }:
        errors.append("canonical m050 scope boundary drifted")
    authority = state.get("authority", {})
    if set(authority) != {
        "repository_writes_authorized", "corpus_modification_authorized",
        "gdd_structure_authorized", "compiled_prose_authorized",
    } or any(value is not False for value in authority.values()):
        errors.append("authorial-preparation authority is not fully inactive")
    if state.get("information_management_archive", {}).get("status") != "RETIRED":
        errors.append("information-management system is not retired")
    gdd = state.get("authorial_gdd", {})
    if gdd != {
        "status": "NOT_STARTED",
        "output_root": "m050/gdd",
        "structure_status": "NOT_PROPOSED",
        "composition_status": "NOT_STARTED",
        "coverage_status": "NOT_STARTED",
    }:
        errors.append("authorial GDD preparation boundary drifted")
    if (ROOT / "m050/gdd").exists():
        errors.append("GDD material exists before structure authorization")
    dashboard = state.get("dashboard", {})
    if dashboard.get("status") != "READY — authorial GDD preparation":
        errors.append("dashboard does not name the preparation boundary")
    validate_timestamp(state, errors)
    try:
        rendered = STATUS.read_text(encoding="utf-8")
    except OSError as exc:
        errors.append(f"cannot read STATUS.md: {exc}")
    else:
        if rendered != expected_status(state):
            errors.append("STATUS.md does not exactly mirror canonical state")


def validate_work_order(path: Path | None, errors: list[str]) -> None:
    if path is None:
        return
    value = read_json(path.resolve(), errors)
    serialized = json.dumps(value, ensure_ascii=False)
    if '"m051' in serialized or 'm051/' in serialized:
        errors.append("work order contains prohibited m051 input")


def run_tests() -> int:
    return subprocess.run(
        [
            str(ROOT / ".venv/bin/python"), "-m", "pytest",
            "m050/tools/tests/test_m050_authorial_guard.py",
            "m050/tools/tests/test_m050_render_status.py", "-q",
        ],
        cwd=ROOT,
        check=False,
    ).returncode


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--work-order", type=Path)
    parser.add_argument("--with-tests", action="store_true")
    args = parser.parse_args()

    errors: list[str] = []
    state = read_json(STATE, errors)
    validate_operating_contract(errors)
    validate_topology(errors)
    validate_state(state, errors)
    atom_count, source_count = validate_manifest_and_corpus(state, errors)
    validate_work_order(args.work_order, errors)
    if args.with_tests and run_tests():
        errors.append("focused regression suite failed")

    if errors:
        print("M050 AUTHORIAL PREPARATION GUARD: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    print("M050 AUTHORIAL PREPARATION GUARD: PASS")
    print(f"- frozen authorial source library: {atom_count:,} atoms across {source_count} sources")
    print(f"- frozen source files: {EXPECTED_FROZEN_FILES}")
    print("- retired information-management engine: archived and inactive")
    print("- provider, spend, tranche, reconciliation, and prose authority: absent")
    print("- m051 input: prohibited")
    if args.with_tests:
        print("- focused regression suite: pass")
    return 0


if __name__ == "__main__":
    sys.exit(main())
