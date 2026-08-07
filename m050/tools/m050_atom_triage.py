#!/usr/bin/env python3
"""Deterministic authorial triage prototype for accepted MEDIAN atoms.

Accepted extraction candidates are immutable evidence.  This tool reads them,
joins block-addressed atoms to their frozen source blocks, and records only the
author's current reconciliation-eligibility decisions in one JSONL file.
"""

from __future__ import annotations

import argparse
import base64
from dataclasses import dataclass
from datetime import datetime, timezone
import hashlib
import hmac
from http.server import BaseHTTPRequestHandler, HTTPServer
import ipaddress
import json
import os
from pathlib import Path
import re
import shutil
import sys
import tempfile
import textwrap
from typing import Iterable
from urllib.parse import parse_qs, urlparse
import uuid


STATE = Path("m050/extraction/control/M050_Compile_State_MEDIANv0_5_0.json")
MATRIX = Path("m050/extraction/control/M050_Compile_Source_State_Matrix_v0_1_MEDIANv0_5_0.json")
ORDER = Path("m050/extraction/control/M050_Compile_Source_Processing_Order_v0_1_MEDIANv0_5_0.json")
ACCEPTED = Path("m050/extraction/accepted")
EXTRACTION = Path("m050/extraction")
DEFAULT_DECISIONS = Path(
    "m050/reconciliation/triage/M050_Authorial_Triage_Decisions_MEDIANv0_5_0.jsonl"
)

SCHEMA_VERSION = "M050-AUTHORIAL-TRIAGE-DECISION-0.1"
DECISIONS = {"retain", "exclude", "uncertain"}
EXCLUSION_REASONS = {
    "obsolete_or_superseded",
    "administrative_or_provenance_only",
    "outside_v0_5_scope",
    "true_duplicate",
    "other_authorial_exclusion",
}
REASON_KEYS = {
    "o": "obsolete_or_superseded",
    "a": "administrative_or_provenance_only",
    "s": "outside_v0_5_scope",
    "d": "true_duplicate",
    "x": "other_authorial_exclusion",
}


class TriageError(RuntimeError):
    """Raised when canonical triage inputs or decisions are inconsistent."""


def _read_json(path: Path) -> dict:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise TriageError(f"cannot read JSON {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise TriageError(f"expected a JSON object: {path}")
    return value


def _read_jsonl(path: Path) -> list[dict]:
    records: list[dict] = []
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except OSError as exc:
        raise TriageError(f"cannot read JSONL {path}: {exc}") from exc
    for line_number, line in enumerate(lines, start=1):
        if not line.strip():
            continue
        try:
            value = json.loads(line)
        except json.JSONDecodeError as exc:
            raise TriageError(f"invalid JSONL {path}:{line_number}: {exc}") from exc
        if not isinstance(value, dict):
            raise TriageError(f"expected a JSON object at {path}:{line_number}")
        records.append(value)
    return records


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _atom_identifier(record: dict) -> str:
    for field in ("proposal_id", "atom_id", "record_id"):
        value = record.get(field)
        if isinstance(value, str) and value:
            return value
    raise TriageError("accepted atom lacks proposal_id, atom_id, or record_id")


def _short_block(block_key: str) -> str:
    match = re.search(r"__B(\d{5})_", block_key)
    if match:
        return f"B{match.group(1)}"
    if "__LOCATION__" in block_key:
        return block_key.rsplit("__LOCATION__", 1)[-1]
    return block_key


def _display_section(value: str) -> str:
    cleaned = re.sub(r"^#+\s*", "", value.strip())
    return cleaned.strip("*_` ").replace("\\.", ".")


def _display_source_text(value: str) -> str:
    """Hide extraction coordinates without changing canonical source text."""
    return re.sub(r"<!--@[^>]*-->\s*", "", value).strip()


@dataclass(frozen=True)
class Atom:
    key: str
    atom_id: str
    source_id: str
    source_label: str
    candidate_sha256: str
    source_position: int
    source_atom_position: int
    corpus_position: int
    block_key: str
    block_id: str | None
    section: str
    block_type: str
    source_text: str
    exact_source_text: str
    normalized_claim: str
    claim_kind: str
    chunk_id: str | None
    raw: dict


@dataclass(frozen=True)
class Corpus:
    atoms: tuple[Atom, ...]
    candidate_hashes: dict[str, str]
    source_labels: dict[str, str]

    def __post_init__(self) -> None:
        keys = [atom.key for atom in self.atoms]
        if len(keys) != len(set(keys)):
            raise TriageError("corpus atom keys are not unique")

    @property
    def by_key(self) -> dict[str, Atom]:
        return {atom.key: atom for atom in self.atoms}

    @property
    def source_totals(self) -> dict[str, int]:
        totals: dict[str, int] = {}
        for atom in self.atoms:
            totals[atom.source_id] = totals.get(atom.source_id, 0) + 1
        return totals

    @property
    def block_members(self) -> dict[str, tuple[Atom, ...]]:
        grouped: dict[str, list[Atom]] = {}
        for atom in self.atoms:
            grouped.setdefault(atom.block_key, []).append(atom)
        return {key: tuple(value) for key, value in grouped.items()}


def _accepted_candidates(repo_root: Path) -> tuple[dict[str, Path], dict[str, str]]:
    candidate_paths: dict[str, Path] = {}
    for path in sorted((repo_root / ACCEPTED).glob("**/*Accepted_Candidate*.jsonl")):
        records = _read_jsonl(path)
        if not records:
            raise TriageError(f"accepted candidate is empty: {path}")
        source_ids = {record.get("source_id") for record in records}
        if len(source_ids) != 1 or not all(isinstance(item, str) and item for item in source_ids):
            raise TriageError(f"accepted candidate has inconsistent source IDs: {path}")
        source_id = next(iter(source_ids))
        if source_id in candidate_paths:
            raise TriageError(f"multiple accepted candidates found for {source_id}")
        candidate_paths[source_id] = path

    report_hashes: dict[str, str] = {}
    for path in sorted((repo_root / ACCEPTED).glob("**/*Acceptance_Report*.json")):
        report = _read_json(path)
        source_id = report.get("source_id")
        expected = report.get("candidate_sha256") or report.get("candidate_atoms_sha256")
        if isinstance(source_id, str) and isinstance(expected, str):
            report_hashes[source_id] = expected

    actual_hashes: dict[str, str] = {}
    for source_id, path in candidate_paths.items():
        actual = _sha256(path)
        expected = report_hashes.get(source_id)
        if expected is None:
            raise TriageError(f"accepted candidate lacks acceptance-report hash: {source_id}")
        if actual != expected:
            raise TriageError(f"accepted candidate hash drifted: {source_id}")
        actual_hashes[source_id] = actual
    return candidate_paths, actual_hashes


def _block_manifests(repo_root: Path) -> dict[str, dict[str, dict]]:
    manifests: dict[str, dict[str, dict]] = {}
    for path in sorted((repo_root / EXTRACTION).glob("**/*Block_Manifest*.json")):
        manifest = _read_json(path)
        source_id = manifest.get("source_id")
        blocks = manifest.get("blocks")
        if not isinstance(source_id, str) or not isinstance(blocks, list):
            continue
        indexed = {
            block["block_id"]: block
            for block in blocks
            if isinstance(block, dict) and isinstance(block.get("block_id"), str)
        }
        if source_id in manifests and manifests[source_id] != indexed:
            raise TriageError(f"multiple differing block manifests found for {source_id}")
        manifests[source_id] = indexed
    return manifests


def load_corpus(repo_root: Path) -> Corpus:
    """Load and integrity-check all completed accepted candidates in source order."""
    state = _read_json(repo_root / STATE)
    matrix = _read_json(repo_root / MATRIX)
    order = _read_json(repo_root / ORDER)
    completed = state.get("progress", {}).get("completed_source_ids")
    if not isinstance(completed, list) or not all(isinstance(item, str) for item in completed):
        raise TriageError("canonical state lacks completed source IDs")
    completed_set = set(completed)

    matrix_by_id = {
        item["source_id"]: item
        for item in matrix.get("sources", [])
        if isinstance(item, dict) and isinstance(item.get("source_id"), str)
    }
    labels = {
        item["source_id"]: item.get("label", item["source_id"])
        for item in order.get("sequence", [])
        if isinstance(item, dict)
        and isinstance(item.get("source_id"), str)
        and item["source_id"] in completed_set
    }
    ordered_ids = [
        item["source_id"]
        for item in order.get("sequence", [])
        if isinstance(item, dict)
        and item.get("source_id") in completed_set
    ]
    if set(ordered_ids) != completed_set:
        raise TriageError("completed-source set disagrees with canonical processing order")
    if any(source_id not in matrix_by_id for source_id in ordered_ids):
        raise TriageError("completed source is absent from the source-state matrix")

    candidate_paths, candidate_hashes = _accepted_candidates(repo_root)
    if set(candidate_paths) != completed_set:
        missing = sorted(completed_set - set(candidate_paths))
        extra = sorted(set(candidate_paths) - completed_set)
        raise TriageError(f"accepted candidate coverage differs from progress: missing={missing}, extra={extra}")
    manifests = _block_manifests(repo_root)

    atoms: list[Atom] = []
    corpus_position = 0
    for source_position, source_id in enumerate(ordered_ids, start=1):
        records = _read_jsonl(candidate_paths[source_id])
        source_manifest = manifests.get(source_id, {})
        for source_atom_position, record in enumerate(records, start=1):
            atom_id = _atom_identifier(record)
            block_id = record.get("block_id")
            if not isinstance(block_id, str) or not block_id:
                block_id = None
            location = record.get("source_location")
            location_text = location if isinstance(location, str) and location else atom_id
            block_key = block_id or f"{source_id}__LOCATION__{location_text}"
            block = source_manifest.get(block_id, {}) if block_id else {}
            exact = record.get("exact_source_text")
            if not isinstance(exact, str) or not exact:
                raise TriageError(f"accepted atom lacks exact source text: {source_id} / {atom_id}")
            normalized = record.get("normalized_claim")
            if not isinstance(normalized, str) or not normalized:
                normalized = exact
            claim_kind = next(
                (
                    value
                    for value in (
                        record.get("claim_kind"),
                        record.get("adjudicated_class"),
                        record.get("source_declared_class"),
                        record.get("record_status"),
                    )
                    if isinstance(value, str) and value
                ),
                "unclassified",
            )
            section = block.get("parent_heading") if isinstance(block, dict) else None
            if not isinstance(section, str) or not section:
                section = location_text if block_id is None else "Unheaded source preface"
            section = _display_section(section)
            source_text = block.get("text") if isinstance(block, dict) else None
            if not isinstance(source_text, str) or not source_text:
                source_text = exact
            block_type = block.get("block_type") if isinstance(block, dict) else None
            if not isinstance(block_type, str) or not block_type:
                block_type = "legacy_record" if block_id is None else "unknown"
            chunk_id = record.get("accepted_chunk_id")
            if not isinstance(chunk_id, str) or not chunk_id:
                chunk_id = None
            corpus_position += 1
            atoms.append(
                Atom(
                    key=f"{source_id}::{atom_id}",
                    atom_id=atom_id,
                    source_id=source_id,
                    source_label=labels[source_id],
                    candidate_sha256=candidate_hashes[source_id],
                    source_position=source_position,
                    source_atom_position=source_atom_position,
                    corpus_position=corpus_position,
                    block_key=block_key,
                    block_id=block_id,
                    section=section,
                    block_type=block_type,
                    source_text=source_text,
                    exact_source_text=exact,
                    normalized_claim=normalized,
                    claim_kind=claim_kind,
                    chunk_id=chunk_id,
                    raw=record,
                )
            )
    return Corpus(tuple(atoms), candidate_hashes, labels)


class DecisionStore:
    """One current, candidate-bound authorial decision per atom."""

    def __init__(self, path: Path, corpus: Corpus):
        self.path = path
        self.corpus = corpus
        self.decisions: dict[str, dict] = {}
        self._order = {atom.key: index for index, atom in enumerate(corpus.atoms)}
        if path.exists():
            self._load()

    def _validate(self, decision: dict) -> None:
        required = {
            "schema_version",
            "event_id",
            "atom_key",
            "atom_id",
            "source_id",
            "candidate_sha256",
            "decision",
            "exclusion_reason",
            "decision_scope",
            "block_key",
            "decided_at",
        }
        if set(decision) != required:
            raise TriageError("triage decision shape is invalid")
        atom = self.corpus.by_key.get(decision.get("atom_key"))
        if atom is None:
            raise TriageError(f"triage decision references an unknown atom: {decision.get('atom_key')}")
        if (
            decision.get("schema_version") != SCHEMA_VERSION
            or decision.get("atom_id") != atom.atom_id
            or decision.get("source_id") != atom.source_id
            or decision.get("candidate_sha256") != atom.candidate_sha256
            or decision.get("block_key") != atom.block_key
        ):
            raise TriageError(f"triage decision binding drifted: {atom.key}")
        value = decision.get("decision")
        reason = decision.get("exclusion_reason")
        if value not in DECISIONS:
            raise TriageError(f"invalid triage decision: {value}")
        if value == "exclude":
            if reason not in EXCLUSION_REASONS:
                raise TriageError(f"invalid exclusion reason: {reason}")
        elif reason is not None:
            raise TriageError("non-exclusion decision has an exclusion reason")
        if decision.get("decision_scope") not in {"atom", "block"}:
            raise TriageError("invalid triage decision scope")

    def _load(self) -> None:
        for decision in _read_jsonl(self.path):
            self._validate(decision)
            key = decision["atom_key"]
            if key in self.decisions:
                raise TriageError(f"duplicate current decision for {key}")
            self.decisions[key] = decision

    def _write(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        descriptor, temporary_name = tempfile.mkstemp(
            dir=self.path.parent,
            prefix=f".{self.path.name}.",
        )
        temporary_path = Path(temporary_name)
        try:
            with os.fdopen(descriptor, "w", encoding="utf-8") as handle:
                for key in sorted(self.decisions, key=self._order.__getitem__):
                    handle.write(json.dumps(self.decisions[key], ensure_ascii=False, sort_keys=True))
                    handle.write("\n")
                handle.flush()
                os.fsync(handle.fileno())
            os.replace(temporary_path, self.path)
        except BaseException:
            temporary_path.unlink(missing_ok=True)
            raise

    def apply(
        self,
        atoms: Iterable[Atom],
        decision: str,
        *,
        scope: str = "atom",
        exclusion_reason: str | None = None,
    ) -> dict[str, dict | None]:
        if decision not in DECISIONS:
            raise TriageError(f"invalid triage decision: {decision}")
        if decision == "exclude" and exclusion_reason not in EXCLUSION_REASONS:
            raise TriageError("exclude requires a valid reason")
        if decision != "exclude" and exclusion_reason is not None:
            raise TriageError("only exclusions may carry a reason")
        if scope not in {"atom", "block"}:
            raise TriageError(f"invalid decision scope: {scope}")
        selected = tuple(atoms)
        if not selected:
            raise TriageError("cannot apply a decision to an empty selection")
        now = datetime.now(timezone.utc).isoformat(timespec="microseconds")
        event_id = f"triage_{uuid.uuid4().hex}"
        previous: dict[str, dict | None] = {}
        for atom in selected:
            previous[atom.key] = self.decisions.get(atom.key)
            record = {
                "schema_version": SCHEMA_VERSION,
                "event_id": event_id,
                "atom_key": atom.key,
                "atom_id": atom.atom_id,
                "source_id": atom.source_id,
                "candidate_sha256": atom.candidate_sha256,
                "decision": decision,
                "exclusion_reason": exclusion_reason,
                "decision_scope": scope,
                "block_key": atom.block_key,
                "decided_at": now,
            }
            self._validate(record)
            self.decisions[atom.key] = record
        self._write()
        return previous

    def restore(self, previous: dict[str, dict | None]) -> None:
        for key, value in previous.items():
            if value is None:
                self.decisions.pop(key, None)
            else:
                self._validate(value)
                self.decisions[key] = value
        self._write()

    def undo_latest(self, *, source_id: str | None = None) -> tuple[str, ...]:
        """Remove and return the atom keys from the most recent decision event."""
        eligible = [
            record
            for record in self.decisions.values()
            if source_id is None or record["source_id"] == source_id
        ]
        if not eligible:
            return ()
        latest = max(eligible, key=lambda item: item["decided_at"])
        event_id = latest["event_id"]
        keys = [
            key for key, record in self.decisions.items() if record["event_id"] == event_id
        ]
        for key in keys:
            self.decisions.pop(key)
        self._write()
        return tuple(keys)

    def next_undecided(self, *, source_id: str | None = None, after: int = -1) -> int | None:
        for index in range(after + 1, len(self.corpus.atoms)):
            atom = self.corpus.atoms[index]
            if source_id is not None and atom.source_id != source_id:
                continue
            if atom.key not in self.decisions:
                return index
        return None

    def counts(self) -> dict[str, int]:
        counts = {value: 0 for value in sorted(DECISIONS)}
        for record in self.decisions.values():
            counts[record["decision"]] += 1
        counts["decided"] = len(self.decisions)
        counts["undecided"] = len(self.corpus.atoms) - len(self.decisions)
        counts["total"] = len(self.corpus.atoms)
        return counts


def _wrap(value: str, width: int, *, indent: str = "") -> str:
    lines = []
    for paragraph in value.strip().splitlines() or [""]:
        lines.append(
            textwrap.fill(
                paragraph,
                width=width,
                initial_indent=indent,
                subsequent_indent=indent,
                replace_whitespace=False,
            )
        )
    return "\n".join(lines)


def render_atom(corpus: Corpus, index: int, decisions: dict[str, dict], *, width: int = 72) -> str:
    atom = corpus.atoms[index]
    source_total = corpus.source_totals[atom.source_id]
    siblings = corpus.block_members[atom.block_key]
    rule = "═" * min(width, 60)
    fine = "─" * min(width, 48)
    chunks = [
        "MEDIAN — AUTHORIAL ATOM TRIAGE",
        "",
        f"SOURCE: {atom.source_label}",
        f"SOURCE ID: {atom.source_id}",
        f"SECTION: {atom.section}",
        "",
        "CURRENT ATOM",
        "",
        _wrap(f"“{_display_source_text(atom.exact_source_text)}”", width),
        "",
        "NORMALIZED CLAIM",
        "",
        _wrap(atom.normalized_claim, width),
        "",
        rule,
        "",
        "SOURCE TEXT",
        "",
        _wrap(_display_source_text(atom.source_text), width),
        "",
        rule,
        "",
        "OTHER ATOMS FROM THIS SOURCE BLOCK",
        "",
    ]
    for sibling in siblings:
        marker = "CURRENT" if sibling.key == atom.key else sibling.claim_kind.upper().replace("_", " ")
        chunks.append(f"  {marker}:")
        chunks.append(_wrap(sibling.normalized_claim, width, indent="  "))
        chunks.append("")
    chunks.extend(
        [
            f"BLOCK TYPE: {atom.block_type}",
            f"BLOCK: {_short_block(atom.block_key)}",
            f"CHUNK: {atom.chunk_id or 'not recorded in accepted atom'}",
            "",
            fine,
            fine,
            "",
            f"SOURCE PROGRESS: {atom.source_atom_position} / {source_total} atoms",
            f"CORPUS PROGRESS: {atom.corpus_position} / {len(corpus.atoms)} atoms",
            "",
            fine,
            "",
            "[Y] Retain for reconciliation",
            "[N] Exclude from active v0.5.0 reconciliation",
            "[?] Uncertain — route specifically to GPT-5.6",
            "",
            "[B] Review or decide the entire source block",
            "[→] Skip without deciding",
            "[U] Undo previous decision",
            "[Q] Save and quit",
            "",
        ]
    )
    existing = decisions.get(atom.key)
    if existing:
        chunks.append(f"CURRENT DECISION: {existing['decision'].upper()}")
    else:
        chunks.append("DECISION: _")
    return "\n".join(chunks)


WEB_PAGE = r"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
  <meta name="color-scheme" content="dark">
  <title>MEDIAN — Authorial Atom Triage</title>
  <style>
    :root {
      --bg: #11110f;
      --surface: #1b1b18;
      --surface-2: #24231f;
      --line: #393832;
      --text: #f3efe4;
      --muted: #aaa79d;
      --accent: #d9bd78;
      --retain: #4b9b73;
      --exclude: #a8564f;
      --uncertain: #b78a3d;
      --radius: 18px;
    }
    * { box-sizing: border-box; }
    html { background: var(--bg); }
    body {
      margin: 0;
      background: var(--bg);
      color: var(--text);
      font-family: ui-rounded, -apple-system, BlinkMacSystemFont, "SF Pro Text", system-ui, sans-serif;
      line-height: 1.45;
      -webkit-font-smoothing: antialiased;
    }
    button, select { font: inherit; }
    button { -webkit-tap-highlight-color: transparent; }
    .shell { max-width: 760px; margin: 0 auto; padding: 10px 12px 190px; }
    header { display: grid; gap: 7px; margin-bottom: 7px; }
    header > div:first-child { display: flex; align-items: baseline; gap: 8px; min-width: 0; }
    .eyebrow { color: var(--accent); font-size: .72rem; font-weight: 800; letter-spacing: .13em; text-transform: uppercase; }
    h1 { font-size: clamp(1.12rem, 4.5vw, 2rem); margin: 0; line-height: 1.08; }
    .toolbar { display: flex; gap: 8px; align-items: center; }
    select {
      width: 100%; min-height: 38px; padding: 0 10px;
      color: var(--text); background: var(--surface); border: 1px solid var(--line); border-radius: 12px;
    }
    .status-dot { width: 10px; height: 10px; border-radius: 50%; background: var(--retain); flex: 0 0 auto; }
    .progress { display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 5px; }
    .pill { min-width: 0; background: var(--surface); border: 1px solid var(--line); border-radius: 10px; padding: 5px 4px; text-align: center; }
    .pill strong { display: block; overflow: hidden; font-size: .76rem; white-space: nowrap; text-overflow: ellipsis; }
    .pill span { display: block; overflow: hidden; color: var(--muted); font-size: .55rem; text-transform: uppercase; letter-spacing: .04em; white-space: nowrap; text-overflow: ellipsis; }
    .card { background: var(--surface); border: 1px solid var(--line); border-radius: var(--radius); padding: 14px; margin: 8px 0; }
    .identity { color: var(--muted); font-size: .78rem; }
    .identity > span { display: block; overflow: hidden; white-space: nowrap; text-overflow: ellipsis; }
    .identity strong { color: var(--text); display: block; font-size: .92rem; line-height: 1.2; margin-top: 1px; }
    .section { color: var(--accent); margin-top: 4px; font-size: .8rem; line-height: 1.25; font-weight: 700; }
    .label { color: var(--muted); font-size: .68rem; font-weight: 800; letter-spacing: .11em; text-transform: uppercase; margin-bottom: 7px; }
    blockquote { margin: 0; font-family: ui-serif, Georgia, serif; font-size: clamp(1.22rem, 5vw, 1.72rem); line-height: 1.38; }
    .normalized { margin-top: 16px; padding-top: 15px; border-top: 1px solid var(--line); color: #d8d3c7; }
    pre { white-space: pre-wrap; overflow-wrap: anywhere; margin: 0; font: .94rem/1.55 ui-monospace, "SFMono-Regular", Menlo, monospace; color: #ded9cc; }
    .siblings { display: grid; gap: 12px; }
    .sibling { padding-left: 12px; border-left: 3px solid var(--line); }
    .sibling.current { border-left-color: var(--accent); }
    .kind { color: var(--accent); font-size: .7rem; font-weight: 800; letter-spacing: .08em; text-transform: uppercase; }
    .claim { margin-top: 3px; }
    details summary { cursor: pointer; color: var(--muted); font-weight: 700; }
    .metadata { margin-top: 12px; display: grid; grid-template-columns: auto 1fr; gap: 6px 12px; font-size: .82rem; }
    .metadata dt { color: var(--muted); }
    .metadata dd { margin: 0; overflow-wrap: anywhere; }
    .decision-banner { display: none; border-color: var(--accent); color: var(--accent); font-weight: 750; }
    .complete { text-align: center; padding: 46px 24px; }
    .complete h2 { font-size: 1.65rem; margin: 0 0 8px; }
    .controls {
      position: fixed; z-index: 10; left: 0; right: 0; bottom: 0;
      padding: 10px max(12px, env(safe-area-inset-right)) calc(10px + env(safe-area-inset-bottom)) max(12px, env(safe-area-inset-left));
      background: color-mix(in srgb, var(--bg) 92%, transparent); backdrop-filter: blur(16px); border-top: 1px solid var(--line);
    }
    .controls-inner { max-width: 732px; margin: 0 auto; display: grid; gap: 8px; }
    .primary { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 8px; }
    .secondary { display: grid; grid-template-columns: 1.2fr 1fr 1fr; gap: 8px; }
    .action { min-height: 54px; border: 0; border-radius: 14px; color: white; font-weight: 800; cursor: pointer; }
    .action:active { transform: scale(.98); }
    .retain { background: var(--retain); }
    .exclude { background: var(--exclude); }
    .uncertain { background: var(--uncertain); }
    .quiet { min-height: 46px; background: var(--surface-2); border: 1px solid var(--line); color: var(--text); }
    .action:disabled { opacity: .38; cursor: default; }
    dialog { width: min(92vw, 520px); border: 1px solid var(--line); border-radius: 22px; padding: 0; color: var(--text); background: var(--surface); }
    dialog::backdrop { background: rgba(0,0,0,.72); backdrop-filter: blur(3px); }
    .dialog-body { padding: 20px; }
    .dialog-body h2 { margin: 0 0 6px; font-size: 1.25rem; }
    .dialog-body p { color: var(--muted); margin: 0 0 16px; }
    .reason-grid { display: grid; gap: 8px; }
    .reason-grid button { min-height: 50px; text-align: left; padding: 0 14px; }
    .cancel { width: 100%; margin-top: 10px; }
    .toast { position: fixed; z-index: 20; top: calc(12px + env(safe-area-inset-top)); left: 50%; transform: translateX(-50%); background: #302f29; border: 1px solid var(--line); border-radius: 999px; padding: 9px 14px; opacity: 0; pointer-events: none; transition: opacity .18s; }
    .toast.show { opacity: 1; }
    [hidden] { display: none !important; }
    @media (min-width: 680px) {
      .shell { padding-top: 28px; }
      .card { padding: 22px; }
      header { gap: 12px; margin-bottom: 16px; }
      h1 { font-size: clamp(1.35rem, 5vw, 2rem); }
      select { min-height: 46px; padding: 0 12px; }
      .pill { padding: 9px 11px; text-align: left; }
      .pill strong { font-size: .9rem; }
      .pill span { font-size: .72rem; letter-spacing: .06em; }
      .identity strong { font-size: 1rem; margin-top: 2px; }
      .section { margin-top: 8px; font-size: .92rem; }
      .label { margin-bottom: 10px; }
    }
  </style>
</head>
<body>
  <main class="shell">
    <header>
      <div><div class="eyebrow">MEDIAN v0.5.0</div><h1>Authorial Atom Triage</h1></div>
      <div class="toolbar"><span class="status-dot" id="statusDot"></span><select id="sourceFilter" aria-label="Filter by source"><option value="">All completed sources</option></select></div>
      <div class="progress">
        <div class="pill"><strong id="sourceProgress">—</strong><span>Source</span></div>
        <div class="pill"><strong id="corpusProgress">—</strong><span>Corpus</span></div>
        <div class="pill"><strong id="decidedProgress">—</strong><span>Decided</span></div>
        <div class="pill"><strong id="uncertainProgress">—</strong><span>Uncertain</span></div>
      </div>
    </header>

    <section id="workspace">
      <div class="card identity"><span id="sourceId"></span><strong id="sourceLabel"></strong><div class="section" id="section"></div></div>
      <div class="card decision-banner" id="decisionBanner"></div>
      <article class="card"><div class="label">Current atom</div><blockquote id="currentAtom"></blockquote><div class="normalized"><div class="label">Normalized claim</div><div id="normalizedClaim"></div></div></article>
      <article class="card"><div class="label">Source text</div><pre id="sourceText"></pre></article>
      <article class="card"><div class="label">Other atoms from this source block</div><div class="siblings" id="siblings"></div></article>
      <details class="card"><summary>Provenance and metadata</summary><dl class="metadata"><dt>Block type</dt><dd id="blockType"></dd><dt>Block</dt><dd id="blockId"></dd><dt>Chunk</dt><dd id="chunkId"></dd><dt>Atom ID</dt><dd id="atomId"></dd></dl></details>
    </section>
    <section class="card complete" id="complete" hidden><h2>Review scope complete</h2><p>No undecided atoms remain in this source selection.</p></section>
  </main>

  <nav class="controls" aria-label="Triage decisions"><div class="controls-inner">
    <div class="primary"><button class="action retain" data-decision="retain">Retain</button><button class="action exclude" id="excludeButton">Exclude</button><button class="action uncertain" data-decision="uncertain">Uncertain</button></div>
    <div class="secondary"><button class="action quiet" id="blockButton">Whole block</button><button class="action quiet" id="skipButton">Skip</button><button class="action quiet" id="undoButton">Undo</button></div>
  </div></nav>

  <dialog id="reasonDialog"><div class="dialog-body"><h2>Why exclude?</h2><p id="reasonScope">This reason is authorial routing, not deletion of evidence.</p><div class="reason-grid">
    <button class="action quiet" data-reason="obsolete_or_superseded">Obsolete or superseded</button>
    <button class="action quiet" data-reason="administrative_or_provenance_only">Administrative or provenance-only</button>
    <button class="action quiet" data-reason="outside_v0_5_scope">Outside v0.5 scope</button>
    <button class="action quiet" data-reason="true_duplicate">True duplicate</button>
    <button class="action quiet" data-reason="other_authorial_exclusion">Other authorial exclusion</button>
  </div><button class="action quiet cancel" data-close="reasonDialog">Cancel</button></div></dialog>

  <dialog id="blockDialog"><div class="dialog-body"><h2>Decide the entire block?</h2><p id="blockSummary"></p><div class="reason-grid"><button class="action retain" data-block-decision="retain">Retain entire block</button><button class="action exclude" data-block-decision="exclude">Exclude entire block</button><button class="action uncertain" data-block-decision="uncertain">Mark entire block uncertain</button></div><button class="action quiet cancel" data-close="blockDialog">Cancel</button></div></dialog>
  <div class="toast" id="toast" role="status"></div>

  <script>
    const ui = { atom: null, sourceId: "", pendingScope: "atom", busy: false };
    const $ = (id) => document.getElementById(id);
    const buttons = [...document.querySelectorAll(".controls button")];

    async function api(path, options = {}) {
      const response = await fetch(path, { headers: { "Content-Type": "application/json", ...(options.headers || {}) }, ...options });
      if (!response.ok) { const body = await response.json().catch(() => ({})); throw new Error(body.error || `Request failed (${response.status})`); }
      return response.json();
    }
    function setBusy(value) { ui.busy = value; buttons.forEach((button) => button.disabled = value); $("statusDot").style.background = value ? "var(--uncertain)" : "var(--retain)"; }
    function toast(message) { $("toast").textContent = message; $("toast").classList.add("show"); setTimeout(() => $("toast").classList.remove("show"), 1300); }
    function querySource() { return ui.sourceId ? `?source_id=${encodeURIComponent(ui.sourceId)}` : ""; }

    function render(payload) {
      ui.atom = payload.atom;
      const complete = !payload.atom;
      $("workspace").hidden = complete; $("complete").hidden = !complete;
      const stats = payload.stats;
      $("decidedProgress").textContent = `${stats.decided} / ${stats.total}`;
      $("uncertainProgress").textContent = stats.uncertain;
      if (complete) { $("sourceProgress").textContent = "Complete"; $("corpusProgress").textContent = `${stats.total} atoms`; return; }
      const atom = payload.atom;
      $("sourceId").textContent = atom.source_id; $("sourceId").title = atom.source_id; $("sourceLabel").textContent = atom.source_label; $("section").textContent = atom.section;
      $("currentAtom").textContent = `“${atom.exact_source_text}”`; $("normalizedClaim").textContent = atom.normalized_claim; $("sourceText").textContent = atom.source_text;
      $("sourceProgress").textContent = `${atom.source_atom_position} / ${atom.source_total}`; $("corpusProgress").textContent = `${atom.corpus_position} / ${stats.total}`;
      $("blockType").textContent = atom.block_type; $("blockId").textContent = atom.block_display; $("chunkId").textContent = atom.chunk_id || "Not recorded"; $("atomId").textContent = atom.atom_id;
      const siblings = $("siblings"); siblings.replaceChildren();
      atom.siblings.forEach((item) => { const row = document.createElement("div"); row.className = `sibling${item.current ? " current" : ""}`; const kind = document.createElement("div"); kind.className = "kind"; kind.textContent = item.current ? "Current" : item.claim_kind.replaceAll("_", " "); const claim = document.createElement("div"); claim.className = "claim"; claim.textContent = item.normalized_claim; row.append(kind, claim); siblings.append(row); });
      const banner = $("decisionBanner"); if (atom.decision) { banner.style.display = "block"; banner.textContent = `Current decision: ${atom.decision.decision.toUpperCase()}`; } else { banner.style.display = "none"; }
      $("blockButton").textContent = `Whole block (${atom.siblings.length})`;
    }

    async function loadState() { setBusy(true); try { render(await api(`/api/state${querySource()}`)); } catch (error) { toast(error.message); } finally { setBusy(false); } }
    async function decide(decision, reason = null, scope = "atom") {
      if (!ui.atom || ui.busy) return; setBusy(true);
      try { render(await api("/api/decision", { method: "POST", body: JSON.stringify({ atom_key: ui.atom.atom_key, decision, exclusion_reason: reason, scope, source_id: ui.sourceId || null }) })); toast(scope === "block" ? "Block saved" : "Decision saved"); }
      catch (error) { toast(error.message); } finally { setBusy(false); }
    }
    async function skip() { if (!ui.atom || ui.busy) return; setBusy(true); try { render(await api("/api/skip", { method: "POST", body: JSON.stringify({ atom_key: ui.atom.atom_key, source_id: ui.sourceId || null }) })); } catch (error) { toast(error.message); } finally { setBusy(false); } }
    async function undo() { if (!ui.atom || ui.busy) return; const visibleAtomKey = ui.atom.atom_key; setBusy(true); try { const payload = await api("/api/undo", { method: "POST", body: JSON.stringify({ source_id: ui.sourceId || null, visible_atom_key: visibleAtomKey }) }); render(payload); toast(payload.duplicate ? "Duplicate Undo ignored" : payload.undone ? `Undid ${payload.undone} decision${payload.undone === 1 ? "" : "s"}` : "Nothing to undo"); } catch (error) { toast(error.message); } finally { setBusy(false); } }

    document.querySelectorAll("[data-decision]").forEach((button) => button.addEventListener("click", () => decide(button.dataset.decision)));
    $("excludeButton").addEventListener("click", () => { ui.pendingScope = "atom"; $("reasonScope").textContent = "Exclude this atom from active reconciliation; preserve its evidence."; $("reasonDialog").showModal(); });
    $("blockButton").addEventListener("click", () => { if (!ui.atom) return; $("blockSummary").textContent = `This will apply one reversible decision to all ${ui.atom.siblings.length} atoms in ${ui.atom.block_display}.`; $("blockDialog").showModal(); });
    $("skipButton").addEventListener("click", skip); $("undoButton").addEventListener("click", undo);
    document.querySelectorAll("[data-block-decision]").forEach((button) => button.addEventListener("click", () => { const value = button.dataset.blockDecision; $("blockDialog").close(); if (value === "exclude") { ui.pendingScope = "block"; $("reasonScope").textContent = `Exclude all ${ui.atom.siblings.length} atoms in this block; preserve their evidence.`; $("reasonDialog").showModal(); } else decide(value, null, "block"); }));
    document.querySelectorAll("[data-reason]").forEach((button) => button.addEventListener("click", () => { $("reasonDialog").close(); decide("exclude", button.dataset.reason, ui.pendingScope); }));
    document.querySelectorAll("[data-close]").forEach((button) => button.addEventListener("click", () => $(button.dataset.close).close()));
    $("sourceFilter").addEventListener("change", (event) => { ui.sourceId = event.target.value; loadState(); });
    document.addEventListener("keydown", (event) => { if (["INPUT","SELECT","BUTTON"].includes(document.activeElement.tagName) || document.querySelector("dialog[open]")) return; if (event.key.toLowerCase() === "y") decide("retain"); else if (event.key === "?") decide("uncertain"); else if (event.key.toLowerCase() === "n") $("excludeButton").click(); else if (event.key.toLowerCase() === "b") $("blockButton").click(); else if (event.key === "ArrowRight") skip(); else if (event.key.toLowerCase() === "u") undo(); });

    (async () => { try { const data = await api("/api/sources"); data.sources.forEach((source) => { const option = document.createElement("option"); option.value = source.source_id; option.textContent = `${source.position}. ${source.label} (${source.atoms})`; $("sourceFilter").append(option); }); await loadState(); } catch (error) { toast(error.message); } })();
  </script>
</body>
</html>
"""


def _atom_payload(corpus: Corpus, store: DecisionStore, index: int | None) -> dict:
    payload: dict = {"stats": store.counts(), "atom": None}
    if index is None:
        return payload
    atom = corpus.atoms[index]
    siblings = corpus.block_members[atom.block_key]
    payload["atom"] = {
        "atom_key": atom.key,
        "atom_id": atom.atom_id,
        "source_id": atom.source_id,
        "source_label": atom.source_label,
        "section": atom.section,
        "source_atom_position": atom.source_atom_position,
        "source_total": corpus.source_totals[atom.source_id],
        "corpus_position": atom.corpus_position,
        "exact_source_text": _display_source_text(atom.exact_source_text),
        "normalized_claim": atom.normalized_claim,
        "source_text": _display_source_text(atom.source_text),
        "block_type": atom.block_type,
        "block_display": _short_block(atom.block_key),
        "chunk_id": atom.chunk_id,
        "decision": store.decisions.get(atom.key),
        "siblings": [
            {
                "atom_key": sibling.key,
                "claim_kind": sibling.claim_kind,
                "normalized_claim": sibling.normalized_claim,
                "current": sibling.key == atom.key,
            }
            for sibling in siblings
        ],
    }
    return payload


def create_web_server(
    corpus: Corpus,
    store: DecisionStore,
    *,
    host: str = "127.0.0.1",
    port: int = 8765,
    pin: str | None = None,
) -> HTTPServer:
    """Create the local triage web server without starting its event loop."""
    if host in {"0.0.0.0", "::"}:
        raise TriageError("wildcard web binding is prohibited; use the exact private-network address")
    if not _web_host_allowed(host):
        raise TriageError("web access requires loopback or an exact Tailscale address")
    by_key = corpus.by_key
    index_by_key = {atom.key: index for index, atom in enumerate(corpus.atoms)}
    last_undo = {"signature": None}

    class Handler(BaseHTTPRequestHandler):
        server_version = "MEDIANTriage/0.1"

        def log_message(self, format: str, *args: object) -> None:
            sys.stderr.write(f"TRIAGE WEB: {format % args}\n")

        def _authorized(self) -> bool:
            if pin is None:
                return True
            header = self.headers.get("Authorization", "")
            if not header.startswith("Basic "):
                return False
            try:
                decoded = base64.b64decode(header[6:], validate=True).decode("utf-8")
                _username, supplied = decoded.split(":", 1)
            except (ValueError, UnicodeDecodeError):
                return False
            return hmac.compare_digest(supplied, pin)

        def _require_authorized(self) -> bool:
            if self._authorized():
                return True
            self.send_response(401)
            self.send_header("WWW-Authenticate", 'Basic realm="MEDIAN Triage", charset="UTF-8"')
            self.send_header("Content-Length", "0")
            self.end_headers()
            return False

        def _same_origin(self) -> bool:
            origin = self.headers.get("Origin")
            if not origin:
                return True
            return urlparse(origin).netloc == self.headers.get("Host")

        def _json(self, value: dict, *, status: int = 200) -> None:
            body = json.dumps(value, ensure_ascii=False).encode("utf-8")
            self.send_response(status)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Cache-Control", "no-store")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        def _error(self, status: int, message: str) -> None:
            self._json({"error": message}, status=status)

        def _body(self) -> dict:
            try:
                length = int(self.headers.get("Content-Length", "0"))
            except ValueError as exc:
                raise TriageError("invalid request length") from exc
            if length <= 0 or length > 64 * 1024:
                raise TriageError("request body is empty or too large")
            try:
                value = json.loads(self.rfile.read(length))
            except json.JSONDecodeError as exc:
                raise TriageError("request body is not valid JSON") from exc
            if not isinstance(value, dict):
                raise TriageError("request body must be a JSON object")
            return value

        def _source(self, value: object) -> str | None:
            if value in (None, ""):
                return None
            if not isinstance(value, str) or value not in corpus.source_labels:
                raise TriageError("unknown source filter")
            return value

        def _next(self, source_id: str | None, *, after: int = -1) -> int | None:
            index = store.next_undecided(source_id=source_id, after=after)
            if index is None and after >= 0:
                index = store.next_undecided(source_id=source_id)
            return index

        def do_GET(self) -> None:
            if not self._require_authorized():
                return
            parsed = urlparse(self.path)
            if parsed.path == "/":
                body = WEB_PAGE.encode("utf-8")
                self.send_response(200)
                self.send_header("Content-Type", "text/html; charset=utf-8")
                self.send_header("Cache-Control", "no-store")
                self.send_header("Content-Security-Policy", "default-src 'self'; style-src 'unsafe-inline'; script-src 'unsafe-inline'; connect-src 'self'; base-uri 'none'; frame-ancestors 'none'")
                self.send_header("X-Content-Type-Options", "nosniff")
                self.send_header("Content-Length", str(len(body)))
                self.end_headers()
                self.wfile.write(body)
                return
            try:
                query = parse_qs(parsed.query)
                source_id = self._source((query.get("source_id") or [None])[0])
                if parsed.path == "/api/state":
                    self._json(_atom_payload(corpus, store, self._next(source_id)))
                elif parsed.path == "/api/sources":
                    totals = corpus.source_totals
                    sources = [
                        {
                            "source_id": source_id,
                            "label": corpus.source_labels[source_id],
                            "position": next(atom.source_position for atom in corpus.atoms if atom.source_id == source_id),
                            "atoms": totals[source_id],
                        }
                        for source_id in corpus.source_labels
                    ]
                    self._json({"sources": sources})
                else:
                    self._error(404, "not found")
            except TriageError as exc:
                self._error(400, str(exc))

        def do_POST(self) -> None:
            if not self._require_authorized():
                return
            if not self._same_origin():
                self._error(403, "cross-origin write rejected")
                return
            parsed = urlparse(self.path)
            try:
                body = self._body()
                source_id = self._source(body.get("source_id"))
                if parsed.path == "/api/decision":
                    atom_key = body.get("atom_key")
                    atom = by_key.get(atom_key)
                    if atom is None:
                        raise TriageError("decision references an unknown atom")
                    if source_id is not None and atom.source_id != source_id:
                        raise TriageError("decision atom is outside the selected source")
                    scope = body.get("scope", "atom")
                    selected = corpus.block_members[atom.block_key] if scope == "block" else (atom,)
                    store.apply(
                        selected,
                        body.get("decision"),
                        scope=scope,
                        exclusion_reason=body.get("exclusion_reason"),
                    )
                    last_undo["signature"] = None
                    index = self._next(source_id, after=index_by_key[atom.key])
                    self._json(_atom_payload(corpus, store, index))
                elif parsed.path == "/api/skip":
                    atom_key = body.get("atom_key")
                    atom = by_key.get(atom_key)
                    if atom is None:
                        raise TriageError("skip references an unknown atom")
                    if source_id is not None and atom.source_id != source_id:
                        raise TriageError("skip atom is outside the selected source")
                    last_undo["signature"] = None
                    index = self._next(source_id, after=index_by_key[atom.key])
                    self._json(_atom_payload(corpus, store, index))
                elif parsed.path == "/api/undo":
                    visible_atom_key = body.get("visible_atom_key")
                    visible_atom = by_key.get(visible_atom_key)
                    if visible_atom is None:
                        raise TriageError("undo must identify the currently visible atom")
                    if source_id is not None and visible_atom.source_id != source_id:
                        raise TriageError("undo atom is outside the selected source")
                    signature = (source_id, visible_atom_key)
                    if last_undo["signature"] == signature:
                        payload = _atom_payload(corpus, store, self._next(source_id))
                        payload["undone"] = 0
                        payload["duplicate"] = True
                        self._json(payload)
                        return
                    undone_keys = store.undo_latest(source_id=source_id)
                    return_index = max((index_by_key[key] for key in undone_keys), default=None)
                    last_undo["signature"] = signature
                    payload = _atom_payload(
                        corpus,
                        store,
                        return_index if return_index is not None else self._next(source_id),
                    )
                    payload["undone"] = len(undone_keys)
                    payload["duplicate"] = False
                    self._json(payload)
                else:
                    self._error(404, "not found")
            except TriageError as exc:
                self._error(400, str(exc))

    return HTTPServer((host, port), Handler)


def _web_host_allowed(host: str) -> bool:
    """Allow web access only on loopback or Tailscale IPv4."""
    if host in {"localhost", "::1"}:
        return True
    try:
        address = ipaddress.ip_address(host)
    except ValueError:
        return False
    return address.is_loopback or address in ipaddress.ip_network("100.64.0.0/10")


def _require_canonical_write_authority(
    repo_root: Path,
    decision_path: Path,
    corpus: Corpus,
) -> None:
    canonical = (repo_root / DEFAULT_DECISIONS).resolve()
    if decision_path.resolve() != canonical:
        return
    state = _read_json(repo_root / STATE)
    triage = state.get("triage", {})
    authority = state.get("authority", {})
    if (
        state.get("status") != "AUTHORIAL_TRIAGE_ACTIVE"
        or state.get("execution_state") != "AUTHORIAL_TRIAGE_ACTIVE"
        or triage.get("status") != "ACTIVE"
        or triage.get("decision_record") != DEFAULT_DECISIONS.as_posix()
        or triage.get("decision_schema_version") != SCHEMA_VERSION
        or triage.get("input_atom_count") != len(corpus.atoms)
        or authority.get("repository_writes_authorized") is not True
        or authority.get("triage_authorized") is not True
        or authority.get("source_work_authorized") is not False
    ):
        raise TriageError("canonical triage write authority is inactive or inconsistent")


def serve_web(
    corpus: Corpus,
    store: DecisionStore,
    *,
    host: str,
    port: int,
    pin: str | None,
) -> None:
    server = create_web_server(corpus, store, host=host, port=port, pin=pin)
    actual_host, actual_port = server.server_address[:2]
    print(f"MEDIAN triage available at http://{actual_host}:{actual_port}/")
    if pin:
        print("Use any username and the configured PIN when the browser asks for credentials.")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


def _read_key() -> str:
    if not sys.stdin.isatty():
        return input().strip().lower()[:1]
    import termios
    import tty
    import select

    descriptor = sys.stdin.fileno()
    original = termios.tcgetattr(descriptor)
    try:
        tty.setraw(descriptor)
        value = sys.stdin.read(1)
        if value == "\x1b":
            readable, _writable, _exceptional = select.select([sys.stdin], [], [], 0.05)
            if readable:
                suffix = sys.stdin.read(2)
                if suffix == "[C":
                    return ">"
        return value.lower()
    finally:
        termios.tcsetattr(descriptor, termios.TCSADRAIN, original)


def _choose_exclusion_reason() -> str | None:
    print("\nEXCLUSION REASON: [O] Obsolete  [A] Administrative  [S] Scope  [D] Duplicate  [X] Other  [Esc] Cancel")
    while True:
        key = _read_key()
        if key in REASON_KEYS:
            return REASON_KEYS[key]
        if key == "\x1b":
            return None


def _choose_block_decision(count: int) -> tuple[str, str | None] | None:
    print(f"\nApply one decision to all {count} atoms in this displayed block?")
    print("[Y] Retain  [N] Exclude  [?] Uncertain  [Esc] Cancel")
    while True:
        key = _read_key()
        if key == "y":
            return "retain", None
        if key == "?":
            return "uncertain", None
        if key == "n":
            reason = _choose_exclusion_reason()
            return ("exclude", reason) if reason else None
        if key == "\x1b":
            return None


def interactive_review(corpus: Corpus, store: DecisionStore, *, source_id: str | None = None) -> None:
    index = store.next_undecided(source_id=source_id)
    if index is None:
        print("No undecided atoms remain in this review scope.")
        return
    history: list[dict[str, dict | None]] = []
    width = max(56, min(88, shutil.get_terminal_size((72, 24)).columns))
    while index is not None:
        print("\033[2J\033[H", end="")
        print(render_atom(corpus, index, store.decisions, width=width))
        key = _read_key()
        atom = corpus.atoms[index]
        if key == "q":
            break
        if key == "u":
            if history:
                store.restore(history.pop())
            else:
                store.undo_latest(source_id=source_id)
            index = store.next_undecided(source_id=source_id)
            continue
        if key in {">", "s"}:
            index = store.next_undecided(source_id=source_id, after=index)
            if index is None:
                index = store.next_undecided(source_id=source_id)
            continue
        if key == "b":
            members = corpus.block_members[atom.block_key]
            selected = _choose_block_decision(len(members))
            if selected:
                decision, reason = selected
                history.append(
                    store.apply(members, decision, scope="block", exclusion_reason=reason)
                )
        elif key == "y":
            history.append(store.apply((atom,), "retain"))
        elif key == "?":
            history.append(store.apply((atom,), "uncertain"))
        elif key == "n":
            reason = _choose_exclusion_reason()
            if reason:
                history.append(store.apply((atom,), "exclude", exclusion_reason=reason))
        else:
            continue
        index = store.next_undecided(source_id=source_id, after=index)
        if index is None:
            index = store.next_undecided(source_id=source_id)
    print("\nSaved triage decisions.")
    print(json.dumps(store.counts(), indent=2))


def _repo_root(value: str) -> Path:
    path = Path(value).resolve()
    if not (path / STATE).is_file():
        raise argparse.ArgumentTypeError(f"not a MEDIAN repository root: {path}")
    return path


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=_repo_root, default=Path.cwd())
    parser.add_argument("--decisions", type=Path, default=DEFAULT_DECISIONS)
    parser.add_argument("--source-id")
    parser.add_argument("--preview", action="store_true", help="render the next atom without writing")
    parser.add_argument("--stats", action="store_true", help="report decision coverage without writing")
    parser.add_argument("--serve", action="store_true", help="serve the local mobile web interface")
    parser.add_argument("--host", default="127.0.0.1", help="web bind address; non-loopback requires --pin")
    parser.add_argument("--port", type=int, default=8765, help="web port (default: 8765)")
    parser.add_argument("--pin", help="password/PIN required for private-network web access")
    args = parser.parse_args(argv)

    repo_root = Path(args.repo_root).resolve()
    decision_path = args.decisions
    if not decision_path.is_absolute():
        decision_path = repo_root / decision_path
    try:
        corpus = load_corpus(repo_root)
        if args.source_id and args.source_id not in corpus.source_labels:
            raise TriageError(f"unknown or incomplete source ID: {args.source_id}")
        if not args.stats and not args.preview:
            _require_canonical_write_authority(repo_root, decision_path, corpus)
        store = DecisionStore(decision_path, corpus)
        if args.serve:
            serve_web(corpus, store, host=args.host, port=args.port, pin=args.pin)
            return 0
        if args.stats:
            print(json.dumps(store.counts(), indent=2))
            return 0
        if args.preview:
            index = store.next_undecided(source_id=args.source_id)
            if index is None:
                print("No undecided atoms remain in this review scope.")
            else:
                print(render_atom(corpus, index, store.decisions))
            return 0
        interactive_review(corpus, store, source_id=args.source_id)
        return 0
    except TriageError as exc:
        print(f"TRIAGE ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
