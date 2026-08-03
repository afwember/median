#!/usr/bin/env python3
"""Verify MEDIAN v0.5.0 frozen-corpus and immutable-evidence integrity."""

from __future__ import annotations

import argparse
import hashlib
import json
import pathlib
import sys
from typing import Iterable


REPO_ROOT = pathlib.Path(__file__).resolve().parents[2]
MANIFEST_PATH = REPO_ROOT / "m050/extraction/control/M050_Frozen_Corpus_Manifest_v0_1_MEDIANv0_5_0.json"
SOURCE_DISPOSITION_PATH = REPO_ROOT / "m050/extraction/audit/M050_Extraction_Gate_2_Source_Disposition_v0_1_MEDIANv0_5_0.yaml"
IGNORED_NAMES = {".DS_Store"}


def sha256_file(path: pathlib.Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def relative_files(roots: Iterable[str]) -> set[str]:
    found: set[str] = set()
    for root_text in roots:
        root = REPO_ROOT / root_text
        if not root.is_dir():
            continue
        for path in root.rglob("*"):
            if path.is_file() and path.name not in IGNORED_NAMES:
                found.add(path.relative_to(REPO_ROOT).as_posix())
    return found


def archive_snapshot(root_text: str) -> tuple[int, int, str]:
    root = REPO_ROOT / root_text
    digest = hashlib.sha256()
    count = 0
    total_bytes = 0
    for path in sorted(p for p in root.rglob("*") if p.is_file() and p.name not in IGNORED_NAMES):
        relative = path.relative_to(REPO_ROOT).as_posix()
        file_hash = sha256_file(path)
        digest.update(relative.encode("utf-8") + b"\0" + file_hash.encode("ascii") + b"\n")
        count += 1
        total_bytes += path.stat().st_size
    return count, total_bytes, digest.hexdigest()


def gate2_registered_sources() -> dict[str, tuple[str, str]]:
    """Read only the simple source_id/path/sha256 triplets from the Gate 2 YAML."""
    records: dict[str, tuple[str, str]] = {}
    current: dict[str, str] = {}
    in_sources = False
    for raw_line in SOURCE_DISPOSITION_PATH.read_text(encoding="utf-8").splitlines():
        if raw_line == "sources:":
            in_sources = True
            continue
        if in_sources and raw_line and not raw_line.startswith(" "):
            break
        if not in_sources:
            continue
        stripped = raw_line.strip()
        if stripped.startswith("- source_id: "):
            if {"source_id", "path", "sha256"} <= current.keys():
                records[current["source_id"]] = (current["path"], current["sha256"])
            current = {"source_id": stripped.split(": ", 1)[1]}
        elif stripped.startswith("path: "):
            current["path"] = stripped.split(": ", 1)[1]
        elif stripped.startswith("sha256: "):
            current["sha256"] = stripped.split(": ", 1)[1]
    if {"source_id", "path", "sha256"} <= current.keys():
        records[current["source_id"]] = (current["path"], current["sha256"])
    return records


def verify_work_order(path: pathlib.Path, errors: list[str]) -> None:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"work order cannot be read as JSON: {exc}")
        return
    candidates: list[str] = []
    for key in ("source_path", "path", "input_path"):
        value = data.get(key)
        if isinstance(value, str):
            candidates.append(value)
    values = data.get("input_paths")
    if isinstance(values, list):
        candidates.extend(value for value in values if isinstance(value, str))
    contaminated = sorted(value for value in candidates if value == "m051" or value.startswith("m051/"))
    if contaminated:
        errors.append("work order contains prohibited m051 input(s): " + ", ".join(contaminated))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--work-order", type=pathlib.Path, help="optional JSON work order to check for m051 contamination")
    parser.add_argument("--skip-archive", action="store_true", help="skip the slower archive-tree digest check")
    args = parser.parse_args()

    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    errors: list[str] = []

    expected_sources = {item["path"]: item["sha256"] for item in manifest["frozen_files"]}
    registered_manifest = {
        item["source_id"]: (item["path"], item["sha256"])
        for item in manifest["frozen_files"]
        if item["kind"] == "registered_source"
    }
    gate2_sources = gate2_registered_sources()
    if gate2_sources != registered_manifest:
        missing_ids = sorted(set(registered_manifest) - set(gate2_sources))
        extra_ids = sorted(set(gate2_sources) - set(registered_manifest))
        changed_ids = sorted(
            source_id
            for source_id in set(gate2_sources) & set(registered_manifest)
            if gate2_sources[source_id] != registered_manifest[source_id]
        )
        errors.append(
            "Gate 2 source disposition disagrees with freeze manifest: "
            f"missing={missing_ids} extra={extra_ids} changed={changed_ids}"
        )
    actual_sources = relative_files(manifest["source_roots"])
    missing = sorted(set(expected_sources) - actual_sources)
    extra = sorted(actual_sources - set(expected_sources))
    errors.extend(f"missing frozen source: {path}" for path in missing)
    errors.extend(f"unregistered file in frozen source root: {path}" for path in extra)
    for relative, expected in expected_sources.items():
        path = REPO_ROOT / relative
        if path.is_file():
            actual = sha256_file(path)
            if actual != expected:
                errors.append(f"frozen source hash mismatch: {relative} expected={expected} actual={actual}")

    for item in manifest["immutable_accepted_files"]:
        path = REPO_ROOT / item["path"]
        if not path.is_file():
            errors.append(f"missing immutable accepted artifact: {item['path']}")
            continue
        actual = sha256_file(path)
        if actual != item["sha256"]:
            errors.append(
                f"immutable accepted artifact hash mismatch: {item['path']} "
                f"expected={item['sha256']} actual={actual}"
            )

    if not args.skip_archive:
        expected_archive = manifest["archive_snapshot"]
        count, total_bytes, digest = archive_snapshot(expected_archive["root"])
        if count != expected_archive["file_count_excluding_ds_store"]:
            errors.append(
                f"archive file-count mismatch: expected={expected_archive['file_count_excluding_ds_store']} actual={count}"
            )
        if total_bytes != expected_archive["total_bytes"]:
            errors.append(f"archive byte-count mismatch: expected={expected_archive['total_bytes']} actual={total_bytes}")
        if digest != expected_archive["ordered_path_and_sha256_digest"]:
            errors.append(
                "archive tree digest mismatch: "
                f"expected={expected_archive['ordered_path_and_sha256_digest']} actual={digest}"
            )

    if args.work_order:
        verify_work_order(args.work_order, errors)

    if errors:
        print("M050 GUARD: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    print("M050 GUARD: PASS")
    print(f"- frozen source files: {len(expected_sources)}")
    print(f"- immutable accepted artifacts: {len(manifest['immutable_accepted_files'])}")
    if args.skip_archive:
        print("- archive snapshot: skipped")
    else:
        print(f"- archive files: {manifest['archive_snapshot']['file_count_excluding_ds_store']}")
        print(f"- archive digest: {manifest['archive_snapshot']['ordered_path_and_sha256_digest']}")
    print("- m051 input: prohibited for m050 processing")
    return 0


if __name__ == "__main__":
    sys.exit(main())
