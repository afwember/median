"""Phase 0 — corpus manifest.

Reads the human-authored source registry, hashes every file, validates the
corpus, and writes manifest.csv. No model calls. Deterministic.
"""

from __future__ import annotations

import csv
import hashlib
from dataclasses import dataclass, field
from pathlib import Path

import yaml

from .config import Build
from .models import MANIFEST_COLUMNS, Disposition, ManifestRow, SourceEntry


def sha256(path: Path, chunk: int = 1 << 20) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        while block := fh.read(chunk):
            h.update(block)
    return h.hexdigest()


@dataclass
class Validation:
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)

    @property
    def ok(self) -> bool:
        return not self.errors


def load_entries(build: Build) -> list[SourceEntry]:
    if not build.sources_yaml.exists():
        raise FileNotFoundError(f"no source registry at {build.sources_yaml}")
    doc = yaml.safe_load(build.sources_yaml.read_text(encoding="utf-8")) or {}
    return [SourceEntry.model_validate(row) for row in doc.get("sources", [])]


def validate(entries: list[SourceEntry], build: Build) -> Validation:
    """Corpus-level checks. Per-row shape is already enforced by Pydantic."""
    v = Validation()
    ids = {e.id for e in entries}

    # Primary key is (id, version); at most one compiled row per id.
    seen_keys: set[tuple[str, str]] = set()
    compiled: dict[str, int] = {}
    for e in entries:
        key = (e.id, e.version)
        if key in seen_keys:
            v.errors.append(f"duplicate (id, version) key: {e.id} {e.version}")
        seen_keys.add(key)
        if e.disposition is Disposition.compile:
            compiled[e.id] = compiled.get(e.id, 0) + 1

    for sid, n in compiled.items():
        if n > 1:
            v.errors.append(
                f"{sid}: {n} rows carry disposition 'compile'; record IDs would be "
                "ambiguous (naming scheme rule 4)"
            )

    for e in entries:
        resolved = build.resolve(e.path)
        if not resolved.exists():
            v.errors.append(f"{e.id} {e.version}: missing file {e.path}")
        elif resolved.is_dir():
            v.errors.append(f"{e.id} {e.version}: path is a directory {e.path}")

        for dep in e.dependencies:
            if dep not in ids:
                v.errors.append(f"{e.id}: unknown dependency {dep!r}")
            if dep == e.id:
                v.errors.append(f"{e.id}: declares itself as a dependency")

        if e.supersedes and e.supersedes not in ids:
            v.errors.append(f"{e.id}: supersedes unknown source {e.supersedes!r}")

    # A source that claims supersession must have something to supersede.
    for e in entries:
        if e.supersedes:
            targets = [
                o for o in entries
                if o.id == e.supersedes and o.version != e.version
            ]
            if not targets:
                v.errors.append(
                    f"{e.id} {e.version}: supersedes {e.supersedes} but no other "
                    "version of it is registered"
                )
            elif not any(o.disposition is Disposition.superseded for o in targets):
                v.warnings.append(
                    f"{e.id} {e.version}: supersedes {e.supersedes}, but no matching "
                    "row is marked disposition 'superseded'"
                )

    # Duplicate content is a corpus smell worth surfacing, not an error.
    by_hash: dict[str, list[str]] = {}
    for e in entries:
        resolved = build.resolve(e.path)
        if resolved.exists() and resolved.is_file():
            by_hash.setdefault(sha256(resolved), []).append(f"{e.id} {e.version}")
    for digest, who in by_hash.items():
        if len(who) > 1:
            v.warnings.append(f"identical content ({digest[:12]}) in: {', '.join(who)}")

    return v


def build_rows(entries: list[SourceEntry], build: Build) -> list[ManifestRow]:
    rows = []
    for e in sorted(entries, key=lambda x: (x.processing_order, x.id, x.version)):
        resolved = build.resolve(e.path)
        rows.append(ManifestRow.from_entry(e, resolved, sha256(resolved)))
    return rows


def write(rows: list[ManifestRow], build: Build) -> Path:
    build.manifest.parent.mkdir(parents=True, exist_ok=True)
    with build.manifest.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=MANIFEST_COLUMNS)
        w.writeheader()
        for r in rows:
            w.writerow(r.model_dump())
    return build.manifest


def read(build: Build) -> list[ManifestRow]:
    with build.manifest.open(newline="", encoding="utf-8") as fh:
        return [ManifestRow.model_validate(r) for r in csv.DictReader(fh)]


def compiled_rows(build: Build) -> list[ManifestRow]:
    return [r for r in read(build) if r.disposition == Disposition.compile.value]
