#!/usr/bin/env python3
"""Zero-call Stage 4 MSID mapping inventory, lifecycle, and record store."""

from __future__ import annotations

import argparse
import copy
from dataclasses import dataclass
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import stat
import subprocess
import tempfile
import uuid

try:
    from m050.tools.m050_atom_triage import (
        DEFAULT_DECISIONS,
        DecisionStore,
        TriageError,
        _read_json,
        _read_jsonl,
        _sha256,
        load_corpus,
    )
    from m050.tools.m050_atom_rewrite import DEFAULT_REWRITES, RewriteCorpus, RewriteStore
except ModuleNotFoundError:
    from m050_atom_triage import (
        DEFAULT_DECISIONS,
        DecisionStore,
        TriageError,
        _read_json,
        _read_jsonl,
        _sha256,
        load_corpus,
    )
    from m050_atom_rewrite import DEFAULT_REWRITES, RewriteCorpus, RewriteStore


STATE = Path("m050/extraction/control/M050_Compile_State_MEDIANv0_5_0.json")
DEFAULT_VOCABULARY = Path("m050/mapping/M050_MSID_Vocabulary_MEDIANv0_5_0.json")
DEFAULT_MAPPINGS = Path("m050/mapping/M050_Atom_MSID_Mappings_MEDIANv0_5_0.jsonl")
SCHEMA_VERSION = "M050-ATOM-MSID-MAPPING-0.1"
VOCABULARY_SCHEMA_VERSION = "M050-MSID-VOCABULARY-0.1"
MAPPING_STATUSES = {"mapped", "unmapped", "ambiguous", "invalid", "human_required"}
REVIEW_STATES = {"worker_validated", "human_required"}
MSID_LITERAL = re.compile(r"\b(?:[A-Z][A-Za-z0-9]*\.)+[A-Z][A-Za-z0-9]*\b")
MSID_MAPPING_LIFECYCLE = {
    "MSID_MAPPING_READY": ("READY", "READY — Stage 4 MSID mapping", False),
    "MSID_MAPPING_AUTHORIZED_AWAITING_PROCEED": (
        "AUTHORIZED_AWAITING_PROCEED",
        "AUTHORIZED — Stage 4 MSID mapping; awaiting Proceed",
        True,
    ),
    "MSID_MAPPING_ACTIVE": ("ACTIVE", "ACTIVE — Stage 4 MSID mapping", True),
}
TRANSITIONS = {"prepare-spark-up", "activate-on-proceed", "prepare-stopdown"}


def _text_sha256(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def _atomic_write_json(path: Path, value: dict) -> None:
    """Replace one existing canonical JSON object without creating a sidecar."""
    mode = stat.S_IMODE(path.stat().st_mode) if path.exists() else 0o644
    descriptor, name = tempfile.mkstemp(dir=path.parent, prefix=f".{path.name}.")
    temporary = Path(name)
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8") as handle:
            json.dump(value, handle, indent=2, ensure_ascii=False)
            handle.write("\n")
            handle.flush()
            os.fsync(handle.fileno())
        os.chmod(temporary, mode)
        os.replace(temporary, path)
    except BaseException:
        temporary.unlink(missing_ok=True)
        raise


@dataclass(frozen=True)
class MappingAtom:
    atom: object
    effective_claim: str
    effective_claim_sha256: str
    effective_claim_origin: str

    @property
    def key(self) -> str:
        return self.atom.key


class MappingCorpus:
    """The exact triage-and-rewrite-filtered Stage 4 input corpus."""

    def __init__(self, repo_root: Path):
        self.full_corpus = load_corpus(repo_root)
        self.triage_path = repo_root / DEFAULT_DECISIONS
        self.rewrite_path = repo_root / DEFAULT_REWRITES
        triage = DecisionStore(self.triage_path, self.full_corpus)
        if len(triage.decisions) != len(self.full_corpus.atoms):
            raise TriageError("authorial triage is not canonically complete")
        rewrite_corpus = RewriteCorpus(repo_root)
        rewrites = RewriteStore(self.rewrite_path, rewrite_corpus)
        if len(rewrites.rewrites) != len(rewrite_corpus.atoms):
            raise TriageError("authorial rewrite is not canonically complete")
        self.triage_sha256 = _sha256(self.triage_path)
        self.rewrite_sha256 = _sha256(self.rewrite_path)
        selected: list[MappingAtom] = []
        for atom in self.full_corpus.atoms:
            decision = triage.decisions[atom.key]
            if decision["decision"] == "retain":
                claim = atom.normalized_claim
                origin = "triage_retained_normalized_claim"
            elif decision["decision"] == "uncertain":
                record = rewrites.rewrites.get(atom.key)
                if record is None:
                    raise TriageError(f"rewrite-list atom lacks canonical disposition: {atom.key}")
                resolution = record.get("resolution", "rewrite")
                if resolution == "exclude":
                    continue
                claim = record["replacement_claim"]
                origin = "authorial_rewrite" if resolution == "rewrite" else "authorial_accept"
            else:
                continue
            selected.append(MappingAtom(atom, claim, _text_sha256(claim), origin))
        self.atoms = tuple(selected)
        self.by_key = {item.key: item for item in self.atoms}
        self.source_labels = {
            item.atom.source_id: item.atom.source_label for item in self.atoms
        }
        self.source_ids = tuple(self.source_labels)
        self.source_totals = {
            source_id: sum(item.atom.source_id == source_id for item in self.atoms)
            for source_id in self.source_ids
        }
        if len(self.atoms) != 5382:
            raise TriageError(f"Stage 4 input coverage is {len(self.atoms)}, expected 5382")


class MSIDVocabulary:
    """Hash-bound Stage 4 vocabulary and mechanical path validator."""

    def __init__(self, repo_root: Path, path: Path | None = None):
        self.repo_root = repo_root
        self.path = path or repo_root / DEFAULT_VOCABULARY
        self.data = _read_json(self.path)
        if self.data.get("schema_version") != VOCABULARY_SCHEMA_VERSION:
            raise TriageError("MSID vocabulary schema version is invalid")
        if self.data.get("status") != "HASH_BOUND_STAGE_4_VALIDATION_PROJECTION":
            raise TriageError("MSID vocabulary is not the Stage 4 validation projection")
        authority = self.data.get("authority")
        if not isinstance(authority, dict):
            raise TriageError("MSID vocabulary authority binding is missing")
        for key, value in authority.items():
            if key.endswith("_sha256"):
                continue
            expected = authority.get(f"{key}_sha256")
            if not isinstance(value, str) or not isinstance(expected, str):
                raise TriageError(f"MSID vocabulary authority binding is malformed: {key}")
            target = repo_root / value
            if _sha256(target) != expected:
                raise TriageError(f"MSID vocabulary authority hash drifted: {key}")
        rules = self.data.get("rules", {})
        self.minimum_segments = rules.get("minimum_segments")
        try:
            self.segment_pattern = re.compile(rules.get("segment_pattern", ""))
        except re.error as exc:
            raise TriageError(f"MSID segment pattern is invalid: {exc}") from exc
        self.settled_tlds = frozenset(self.data.get("settled_tlds", []))
        self.provisional_tlds = frozenset(self.data.get("provisional_tlds", []))
        self.settled_paths = frozenset(self.data.get("settled_paths", []))
        self.provisional_paths = frozenset(self.data.get("provisional_paths", []))
        self.aliases = dict(self.data.get("aliases", {}))
        self.rejected_paths = frozenset(self.data.get("rejected_paths", []))
        self.semantic_relations = frozenset(self.data.get("semantic_relations", []))
        self.operator_segments = frozenset(rules.get("operators_are_not_path_segments", []))
        if self.minimum_segments != 2 or not self.settled_tlds:
            raise TriageError("MSID vocabulary rules are incomplete")
        for path_value in self.settled_paths | self.provisional_paths:
            if self.classify(path_value) in {"invalid", "alias", "rejected"}:
                raise TriageError(f"MSID vocabulary contains an invalid path: {path_value}")

    def classify(self, value: str) -> str:
        if not isinstance(value, str) or not value:
            return "invalid"
        if value in self.aliases:
            return "alias"
        if value in self.rejected_paths:
            return "rejected"
        segments = value.split(".")
        if len(segments) < self.minimum_segments:
            return "invalid"
        if any(not self.segment_pattern.fullmatch(segment) for segment in segments):
            return "invalid"
        if any(segment in self.operator_segments for segment in segments):
            return "invalid"
        tld = segments[0]
        if tld in self.provisional_tlds or value in self.provisional_paths:
            return "provisional"
        if tld not in self.settled_tlds:
            return "invalid"
        if segments[1] == tld and len(segments) != 2:
            return "invalid"
        if any(left == right for left, right in zip(segments[1:], segments[2:])):
            return "invalid"
        if len(segments) >= 3 and segments[1] == "Register" and segments[2].upper() in self.operator_segments:
            return "invalid"
        return "settled" if value in self.settled_paths else "candidate"


class MappingStore:
    """One current, input-bound Stage 4 mapping per eligible atom."""

    def __init__(self, path: Path, corpus: MappingCorpus, vocabulary: MSIDVocabulary):
        self.path = path
        self.corpus = corpus
        self.vocabulary = vocabulary
        self.mappings: dict[str, dict] = {}
        self._order = {item.key: index for index, item in enumerate(corpus.atoms)}
        ontology_sources = {"M050-SRC-MSID-GRAMMAR-001", "M050-SRC-HUMAN-RULINGS-001"}
        self.ontology_basis_keys = {
            item.key for item in corpus.atoms if item.atom.source_id in ontology_sources
        }
        if path.exists():
            self._load()

    def _validate(self, record: dict) -> None:
        required = {
            "schema_version", "mapping_id", "atom_key", "atom_id", "source_id",
            "block_key", "candidate_sha256", "triage_decision_sha256",
            "rewrite_record_sha256", "effective_claim_sha256", "effective_claim_origin",
            "mapping_status", "primary_msid", "related_msids",
            "alternate_primary_msids", "semantic_relation", "rationale",
            "ontology_basis_atom_keys", "mapper", "review_state", "mapped_at",
        }
        if set(record) != required:
            raise TriageError("Stage 4 mapping shape is invalid")
        item = self.corpus.by_key.get(record.get("atom_key"))
        if item is None:
            raise TriageError(f"mapping references an ineligible atom: {record.get('atom_key')}")
        atom = item.atom
        if (
            record.get("schema_version") != SCHEMA_VERSION
            or record.get("atom_id") != atom.atom_id
            or record.get("source_id") != atom.source_id
            or record.get("block_key") != atom.block_key
            or record.get("candidate_sha256") != atom.candidate_sha256
            or record.get("triage_decision_sha256") != self.corpus.triage_sha256
            or record.get("rewrite_record_sha256") != self.corpus.rewrite_sha256
            or record.get("effective_claim_sha256") != item.effective_claim_sha256
            or record.get("effective_claim_origin") != item.effective_claim_origin
        ):
            raise TriageError(f"Stage 4 mapping binding drifted: {item.key}")
        status = record.get("mapping_status")
        primary = record.get("primary_msid")
        related = record.get("related_msids")
        alternates = record.get("alternate_primary_msids")
        if status not in MAPPING_STATUSES or not isinstance(related, list) or not isinstance(alternates, list):
            raise TriageError("Stage 4 mapping status or candidates are invalid")
        if len(related) != len(set(related)) or len(alternates) != len(set(alternates)):
            raise TriageError("Stage 4 mapping candidates contain duplicates")
        paths = ([primary] if primary else []) + related + alternates
        if not all(isinstance(path, str) for path in paths):
            raise TriageError("Stage 4 mapping contains a non-string MSID")
        if len(paths) != len(set(paths)):
            raise TriageError("Stage 4 mapping repeats an MSID across roles")
        classes = {path: self.vocabulary.classify(path) for path in paths}
        if status == "mapped":
            if not isinstance(primary, str) or alternates:
                raise TriageError("mapped status requires one primary and no alternates")
            if any(value not in {"settled", "candidate"} for value in classes.values()):
                raise TriageError("mapped status contains a non-current MSID")
        elif status == "ambiguous":
            if primary is not None or len(alternates) < 2 or related:
                raise TriageError("ambiguous status requires two alternate primaries only")
            if any(value not in {"settled", "candidate", "provisional"} for value in classes.values()):
                raise TriageError("ambiguous status contains an invalid alternative")
        elif status == "human_required":
            if primary is not None or related:
                raise TriageError("human-required status cannot assert a primary mapping")
        elif primary is not None or related or alternates:
            raise TriageError(f"{status} status must not assert an MSID")
        relation = record.get("semantic_relation")
        if status == "mapped" and relation not in self.vocabulary.semantic_relations:
            raise TriageError("mapped status requires a controlled semantic relation")
        if status != "mapped" and relation is not None:
            raise TriageError("only mapped status may assert a semantic relation")
        rationale = record.get("rationale")
        basis = record.get("ontology_basis_atom_keys")
        if not isinstance(rationale, str) or not rationale.strip() or rationale != rationale.strip():
            raise TriageError("Stage 4 mapping rationale must be nonempty and trimmed")
        if (
            not isinstance(basis, list)
            or not basis
            or len(basis) != len(set(basis))
            or not set(basis) <= self.ontology_basis_keys
        ):
            raise TriageError("Stage 4 mapping ontology basis is missing or ineligible")
        if record.get("review_state") not in REVIEW_STATES:
            raise TriageError("Stage 4 mapping review state is invalid")
        if status == "human_required" and record.get("review_state") != "human_required":
            raise TriageError("human-required mapping must retain human-required review state")
        if status != "human_required" and record.get("review_state") != "worker_validated":
            raise TriageError("non-human-required mapping must be worker validated")
        if status == "human_required" and any(
            value not in {"settled", "candidate", "provisional"}
            for value in classes.values()
        ):
            raise TriageError("human-required mapping contains an invalid alternative")
        if not isinstance(record.get("mapper"), str) or not record["mapper"].strip():
            raise TriageError("Stage 4 mapping mapper is missing")
        if not isinstance(record.get("mapping_id"), str) or not record["mapping_id"].startswith("mapping_"):
            raise TriageError("Stage 4 mapping identifier is invalid")
        try:
            mapped_at = datetime.fromisoformat(record.get("mapped_at", ""))
        except (TypeError, ValueError) as exc:
            raise TriageError("Stage 4 mapping timestamp is invalid") from exc
        if mapped_at.tzinfo is None:
            raise TriageError("Stage 4 mapping timestamp lacks a timezone")

    def _load(self) -> None:
        mapping_ids: set[str] = set()
        for record in _read_jsonl(self.path):
            self._validate(record)
            key = record["atom_key"]
            if key in self.mappings:
                raise TriageError(f"duplicate current Stage 4 mapping: {key}")
            if record["mapping_id"] in mapping_ids:
                raise TriageError(f"duplicate Stage 4 mapping identifier: {record['mapping_id']}")
            mapping_ids.add(record["mapping_id"])
            self.mappings[key] = record

    def replace(self, records: list[dict]) -> None:
        replacement: dict[str, dict] = {}
        for record in records:
            self._validate(record)
            if record["atom_key"] in replacement:
                raise TriageError(f"duplicate replacement mapping: {record['atom_key']}")
            replacement[record["atom_key"]] = record
        self.mappings = replacement
        self._write()

    def _write(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        descriptor, name = tempfile.mkstemp(dir=self.path.parent, prefix=f".{self.path.name}.")
        temporary = Path(name)
        try:
            with os.fdopen(descriptor, "w", encoding="utf-8") as handle:
                for key in sorted(self.mappings, key=self._order.__getitem__):
                    handle.write(json.dumps(self.mappings[key], ensure_ascii=False, sort_keys=True) + "\n")
                handle.flush()
                os.fsync(handle.fileno())
            os.replace(temporary, self.path)
        except BaseException:
            temporary.unlink(missing_ok=True)
            raise

    def make_record(
        self, atom_key: str, *, mapping_status: str, primary_msid: str | None = None,
        related_msids: list[str] | None = None, alternate_primary_msids: list[str] | None = None,
        semantic_relation: str | None = None, rationale: str,
        ontology_basis_atom_keys: list[str], mapper: str = "Compile Worker",
        review_state: str = "worker_validated",
    ) -> dict:
        item = self.corpus.by_key.get(atom_key)
        if item is None:
            raise TriageError(f"cannot map ineligible atom: {atom_key}")
        atom = item.atom
        record = {
            "schema_version": SCHEMA_VERSION,
            "mapping_id": f"mapping_{uuid.uuid4().hex}",
            "atom_key": atom.key,
            "atom_id": atom.atom_id,
            "source_id": atom.source_id,
            "block_key": atom.block_key,
            "candidate_sha256": atom.candidate_sha256,
            "triage_decision_sha256": self.corpus.triage_sha256,
            "rewrite_record_sha256": self.corpus.rewrite_sha256,
            "effective_claim_sha256": item.effective_claim_sha256,
            "effective_claim_origin": item.effective_claim_origin,
            "mapping_status": mapping_status,
            "primary_msid": primary_msid,
            "related_msids": related_msids or [],
            "alternate_primary_msids": alternate_primary_msids or [],
            "semantic_relation": semantic_relation,
            "rationale": rationale,
            "ontology_basis_atom_keys": ontology_basis_atom_keys,
            "mapper": mapper,
            "review_state": review_state,
            "mapped_at": datetime.now(timezone.utc).isoformat(timespec="microseconds"),
        }
        self._validate(record)
        return record

    def counts(self) -> dict[str, int]:
        result = {status: 0 for status in sorted(MAPPING_STATUSES)}
        for record in self.mappings.values():
            result[record["mapping_status"]] += 1
        result.update({
            "mapped_records": len(self.mappings),
            "remaining": len(self.corpus.atoms) - len(self.mappings),
            "total": len(self.corpus.atoms),
        })
        return result


def active_source(corpus: MappingCorpus, store: MappingStore) -> str | None:
    return next(
        (
            source_id for source_id in corpus.source_ids
            if any(item.key not in store.mappings for item in corpus.atoms if item.atom.source_id == source_id)
        ),
        None,
    )


def inventory(corpus: MappingCorpus, vocabulary: MSIDVocabulary, store: MappingStore) -> dict:
    literal_atoms = 0
    literal_classes: dict[str, int] = {}
    legacy_shell_atoms = 0
    origins: dict[str, int] = {}
    for item in corpus.atoms:
        origins[item.effective_claim_origin] = origins.get(item.effective_claim_origin, 0) + 1
        literals = set(MSID_LITERAL.findall(item.effective_claim))
        if literals:
            literal_atoms += 1
        for literal in literals:
            classification = vocabulary.classify(literal)
            literal_classes[classification] = literal_classes.get(classification, 0) + 1
        if "primary_msid_candidate" in item.atom.raw:
            legacy_shell_atoms += 1
    return {
        "schema_version": "M050-MSID-MAPPING-INVENTORY-0.1",
        "external_calls": 0,
        "input_atoms": len(corpus.atoms),
        "input_sources": len(corpus.source_ids),
        "effective_claim_origins": origins,
        "literal_msid_atoms": literal_atoms,
        "literal_msid_classifications": literal_classes,
        "legacy_semantic_shell_atoms_ignored": legacy_shell_atoms,
        "mapping_counts": store.counts(),
        "active_source_id": active_source(corpus, store),
        "source_counts": [
            {"source_id": source_id, "label": corpus.source_labels[source_id], "atoms": corpus.source_totals[source_id]}
            for source_id in corpus.source_ids
        ],
    }


def _source_progress(corpus: MappingCorpus, store: MappingStore) -> dict[str, dict[str, int]]:
    mapped = {source_id: 0 for source_id in corpus.source_ids}
    for item in corpus.atoms:
        if item.key in store.mappings:
            mapped[item.atom.source_id] += 1
    return {
        source_id: {
            "mapped": mapped[source_id],
            "total": corpus.source_totals[source_id],
            "remaining": corpus.source_totals[source_id] - mapped[source_id],
        }
        for source_id in corpus.source_ids
    }


def _validate_order_boundary(
    corpus: MappingCorpus,
    store: MappingStore,
    errors: list[str],
) -> str | None:
    """Require a complete prefix, at most one partial source, and an empty suffix."""
    progress = _source_progress(corpus, store)
    current = active_source(corpus, store)
    if current is None:
        return None
    current_index = corpus.source_ids.index(current)
    for source_id in corpus.source_ids[:current_index]:
        if progress[source_id]["remaining"]:
            errors.append(f"earlier mapping source is incomplete: {source_id}")
    for source_id in corpus.source_ids[current_index + 1:]:
        if progress[source_id]["mapped"]:
            errors.append(f"later mapping source was entered early: {source_id}")
    return current


def _dashboard_source_id(state: dict, corpus: MappingCorpus) -> str | None:
    text = state.get("dashboard", {}).get("source")
    if not isinstance(text, str):
        return None
    matches = [source_id for source_id in corpus.source_ids if f"({source_id})" in text]
    return matches[0] if len(matches) == 1 else None


def _dashboard_matches(state: dict, expected: dict[str, str]) -> bool:
    dashboard = state.get("dashboard", {})
    return (
        isinstance(dashboard, dict)
        and set(dashboard) <= set(expected) | {"updated_human"}
        and all(dashboard.get(key) == value for key, value in expected.items())
    )


def _replace_dashboard_fields(state: dict, fields: dict[str, str]) -> None:
    updated_human = state.get("dashboard", {}).get("updated_human")
    state["dashboard"] = dict(fields)
    if isinstance(updated_human, str):
        state["dashboard"]["updated_human"] = updated_human


def _expected_prepared_dashboard(
    corpus: MappingCorpus,
    store: MappingStore,
    source_id: str,
) -> dict[str, str]:
    progress = _source_progress(corpus, store)[source_id]
    label = corpus.source_labels[source_id]
    return {
        "status": "AUTHORIZED — Stage 4 MSID mapping; awaiting Proceed",
        "phase": "MSID mapping — semantic address assignment",
        "source": (
            f"{label} ({source_id}) — {progress['total']:,} eligible claims; "
            f"{progress['mapped']:,} mapped"
        ),
        "progress": f"{len(store.mappings):,} / {len(corpus.atoms):,} Stage 4 mappings recorded",
        "now": f"{label} authority is prepared; no substantive mapping has begun",
        "next": f"Await Asa's Proceed to release the already-authorized {label} source work",
    }


def _expected_active_dashboard(
    corpus: MappingCorpus,
    store: MappingStore,
    source_id: str,
) -> dict[str, str]:
    dashboard = _expected_prepared_dashboard(corpus, store, source_id)
    label = corpus.source_labels[source_id]
    dashboard.update({
        "status": "ACTIVE — Stage 4 MSID mapping",
        "now": f"{label} Stage 4 mapping is active within the released source boundary",
        "next": f"Complete only {label}, then formally Stop Down; do not enter another source",
    })
    return dashboard


def _expected_ready_dashboard(
    corpus: MappingCorpus,
    store: MappingStore,
    source_id: str,
    *,
    cancelled: bool,
) -> tuple[dict[str, str], str]:
    progress = _source_progress(corpus, store)[source_id]
    label = corpus.source_labels[source_id]
    next_source = active_source(corpus, store)
    if next_source is None:
        next_text = "Stage 4 mapping is complete; halt for separately authorized Stage 5 reconciliation"
        transition = (
            "Stage 4 mapping is complete; Stopdown must remain in force until Asa separately "
            "authorizes Stage 5 reconciliation."
        )
    else:
        next_label = corpus.source_labels[next_source]
        next_text = (
            f"Await Asa's Spark Up; it may prepare {next_label} authority but must halt before execution"
        )
        transition = (
            f"Spark Up may grant bounded Stage 4 mapping work on {next_label} and prepare the "
            "execution fermata; Proceed cannot grant authority, and Stage 5 remains prohibited."
        )
    now = (
        f"{label} prepared authority was cancelled before execution and the Compile Worker has Stopped Down"
        if cancelled
        else f"{label} Stage 4 mapping is complete and the Compile Worker has Stopped Down"
    )
    return ({
        "status": "READY — Stage 4 MSID mapping",
        "phase": "MSID mapping — semantic address assignment",
        "source": f"{label} ({source_id}) — {progress['mapped']:,} / {progress['total']:,} mappings complete",
        "progress": f"{len(store.mappings):,} / {len(corpus.atoms):,} Stage 4 mappings recorded",
        "now": now,
        "next": next_text,
    }, transition)


def _validate_lifecycle_baseline(
    state: dict,
    corpus: MappingCorpus,
    store: MappingStore,
) -> None:
    errors: list[str] = []
    status = state.get("status")
    lifecycle = MSID_MAPPING_LIFECYCLE.get(status)
    if lifecycle is None or state.get("execution_state") != status:
        errors.append("canonical Stage 4 lifecycle is invalid")
        expected_mapping_status, expected_dashboard_status, authority_active = None, None, False
    else:
        expected_mapping_status, expected_dashboard_status, authority_active = lifecycle
    authority = state.get("authority", {})
    for key in (
        "triage_authorized", "rewrite_authorized", "google_sheets_interaction_authorized",
        "semantic_acceptance_authorized", "reconciliation_authorized", "compiled_prose_authorized",
    ):
        if authority.get(key) is not False:
            errors.append(f"prohibited authority is active: {key}")
    for key in ("mapping_authorized", "source_work_authorized", "repository_writes_authorized"):
        if authority.get(key) is not authority_active:
            errors.append(f"Stage 4 authority disagrees with lifecycle: {key}")
    if state.get("mapping", {}).get("status") != expected_mapping_status:
        errors.append("mapping status disagrees with lifecycle")
    if state.get("dashboard", {}).get("status") != expected_dashboard_status:
        errors.append("dashboard status disagrees with lifecycle")
    if state.get("dashboard", {}).get("phase") != "MSID mapping — semantic address assignment":
        errors.append("dashboard phase is not Stage 4 MSID mapping")
    if state.get("spend", {}).get("active") is not False:
        errors.append("provider spend is active during provider-free Stage 4")
    expected_progress = f"{len(store.mappings):,} / {len(corpus.atoms):,} Stage 4 mappings recorded"
    if status != "MSID_MAPPING_ACTIVE" and state.get("dashboard", {}).get("progress") != expected_progress:
        errors.append("Stage 4 dashboard progress is stale outside active execution")
    _validate_order_boundary(corpus, store, errors)
    if errors:
        raise TriageError("; ".join(errors))


def plan_lifecycle_transition(
    state: dict,
    corpus: MappingCorpus,
    store: MappingStore,
    transition: str,
) -> tuple[dict, dict]:
    """Return a validated canonical-state replacement and an ephemeral report."""
    if transition not in TRANSITIONS:
        raise TriageError(f"unknown Stage 4 lifecycle transition: {transition}")
    _validate_lifecycle_baseline(state, corpus, store)
    before = state.get("status")
    current = active_source(corpus, store)
    result = copy.deepcopy(state)
    changed = True
    cancelled = False

    if transition == "prepare-spark-up":
        if before == "MSID_MAPPING_AUTHORIZED_AWAITING_PROCEED":
            source_id = _dashboard_source_id(state, corpus)
            if source_id is None or source_id != current or not _dashboard_matches(
                state, _expected_prepared_dashboard(corpus, store, source_id)
            ):
                raise TriageError("prepared-authority boundary drifted")
            changed = False
        elif before != "MSID_MAPPING_READY":
            raise TriageError("Spark Up preparation requires READY or the existing fermata")
        else:
            source_id = current
            if source_id is None:
                raise TriageError("Stage 4 has complete coverage; Spark Up cannot select a source")
            result["status"] = result["execution_state"] = "MSID_MAPPING_AUTHORIZED_AWAITING_PROCEED"
            result["mapping"]["status"] = "AUTHORIZED_AWAITING_PROCEED"
            for key in ("mapping_authorized", "source_work_authorized", "repository_writes_authorized"):
                result["authority"][key] = True
            _replace_dashboard_fields(
                result, _expected_prepared_dashboard(corpus, store, source_id)
            )
            label = corpus.source_labels[source_id]
            result["next_possible_transition"] = (
                f"Proceed may release the already-authorized {label} Stage 4 work; without Proceed no "
                "substantive source work may begin, and Stage 5 remains prohibited."
            )
    elif transition == "activate-on-proceed":
        if before != "MSID_MAPPING_AUTHORIZED_AWAITING_PROCEED":
            raise TriageError("Proceed release requires the prepared-authority fermata")
        source_id = _dashboard_source_id(state, corpus)
        if source_id is None or source_id != current:
            raise TriageError("prepared source no longer matches the canonical mapping boundary")
        if not _dashboard_matches(state, _expected_prepared_dashboard(corpus, store, source_id)):
            raise TriageError("prepared-authority inventory drifted")
        result["status"] = result["execution_state"] = "MSID_MAPPING_ACTIVE"
        result["mapping"]["status"] = "ACTIVE"
        _replace_dashboard_fields(result, _expected_active_dashboard(corpus, store, source_id))
        label = corpus.source_labels[source_id]
        result["next_possible_transition"] = (
            f"Complete only {label}, then formally Stop Down; another source and Stage 5 remain prohibited."
        )
    else:
        if before == "MSID_MAPPING_READY":
            source_id = _dashboard_source_id(state, corpus)
            changed = False
        elif before == "MSID_MAPPING_AUTHORIZED_AWAITING_PROCEED":
            source_id = _dashboard_source_id(state, corpus)
            if source_id is None or source_id != current or not _dashboard_matches(
                state, _expected_prepared_dashboard(corpus, store, source_id)
            ):
                raise TriageError("prepared-authority boundary drifted before cancellation")
            cancelled = True
        elif before == "MSID_MAPPING_ACTIVE":
            source_id = _dashboard_source_id(state, corpus)
            if source_id is None:
                raise TriageError("active mapping source is absent from canonical state")
            progress = _source_progress(corpus, store)[source_id]
            if progress["remaining"]:
                raise TriageError(
                    f"formal Stopdown requires complete source coverage: {progress['remaining']} remain"
                )
            source_index = corpus.source_ids.index(source_id)
            expected_completed_index = (
                len(corpus.source_ids) - 1
                if current is None
                else corpus.source_ids.index(current) - 1
            )
            if expected_completed_index < 0 or source_index != expected_completed_index:
                raise TriageError("active grant does not match the just-completed source boundary")
            if any(
                _source_progress(corpus, store)[later]["mapped"]
                for later in corpus.source_ids[source_index + 1:]
            ):
                raise TriageError("formal Stopdown found mappings beyond the granted source")
        else:
            raise TriageError("formal Stopdown requires READY, ACTIVE, or the prepared fermata")
        if changed:
            result["status"] = result["execution_state"] = "MSID_MAPPING_READY"
            result["mapping"]["status"] = "READY"
            for key in ("mapping_authorized", "source_work_authorized", "repository_writes_authorized"):
                result["authority"][key] = False
            dashboard, result["next_possible_transition"] = _expected_ready_dashboard(
                corpus, store, source_id, cancelled=cancelled
            )
            _replace_dashboard_fields(result, dashboard)

    source_progress = _source_progress(corpus, store).get(source_id, {}) if source_id else {}
    if not changed:
        next_operations = (
            ["halt at the existing prepared-authority fermata"]
            if transition == "prepare-spark-up"
            else ["none; formal Stopdown is already in force"]
        )
    elif transition == "prepare-spark-up":
        next_operations = [
            "render STATUS.md", "run full guard", "commit", "push",
            "confirm clean synchronization", "halt at the prepared-authority fermata",
        ]
    elif transition == "activate-on-proceed":
        next_operations = ["begin only the released source work"]
    else:
        next_operations = [
            "render STATUS.md", "run full guard", "commit", "push",
            "confirm clean synchronization", "notify Compile Supervisor",
        ]
    report = {
        "transition": transition,
        "changed": changed,
        "from_lifecycle": before,
        "to_lifecycle": result.get("status"),
        "source_id": source_id,
        "source_label": corpus.source_labels.get(source_id) if source_id else None,
        "source_progress": source_progress,
        "mapping_records": len(store.mappings),
        "external_calls": 0,
        "next_required_operations": next_operations,
    }
    return result, report


def _require_clean_synchronized_checkpoint(repo_root: Path) -> None:
    status = subprocess.run(
        ["git", "status", "--porcelain"], cwd=repo_root, check=True,
        capture_output=True, text=True,
    ).stdout
    if status.strip():
        raise TriageError("prepared lifecycle transition requires a clean worktree")
    head = subprocess.run(
        ["git", "rev-parse", "HEAD"], cwd=repo_root, check=True,
        capture_output=True, text=True,
    ).stdout.strip()
    origin = subprocess.run(
        ["git", "rev-parse", "origin/main"], cwd=repo_root, check=True,
        capture_output=True, text=True,
    ).stdout.strip()
    if head != origin:
        raise TriageError("prepared lifecycle transition requires local HEAD equal to origin/main")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=Path.cwd())
    parser.add_argument("--inventory", action="store_true")
    parser.add_argument("--stats", action="store_true")
    parser.add_argument("--preview", action="store_true")
    parser.add_argument("--transition", choices=sorted(TRANSITIONS))
    parser.add_argument(
        "--apply",
        action="store_true",
        help="atomically apply a validated --transition to canonical compile state",
    )
    args = parser.parse_args(argv)
    try:
        selected = sum(bool(value) for value in (args.inventory, args.stats, args.preview, args.transition))
        if selected != 1:
            raise TriageError("select exactly one inventory, stats, preview, or lifecycle transition operation")
        if args.apply and not args.transition:
            raise TriageError("--apply is valid only with --transition")
        if args.transition == "activate-on-proceed" and not args.apply:
            raise TriageError(
                "Proceed activation requires one atomic --apply invocation; "
                "a separate lifecycle dry-run is prohibited"
            )
        root = args.repo_root.resolve()
        corpus = MappingCorpus(root)
        vocabulary = MSIDVocabulary(root)
        store = MappingStore(root / DEFAULT_MAPPINGS, corpus, vocabulary)
        if args.transition:
            if args.transition in {"prepare-spark-up", "activate-on-proceed"}:
                _require_clean_synchronized_checkpoint(root)
            state_path = root / STATE
            state = _read_json(state_path)
            replacement, report = plan_lifecycle_transition(
                state, corpus, store, args.transition
            )
            report["applied"] = bool(args.apply and report["changed"])
            if args.apply and report["changed"]:
                _atomic_write_json(state_path, replacement)
            print(json.dumps(report, indent=2, ensure_ascii=False))
        elif args.inventory:
            print(json.dumps(inventory(corpus, vocabulary, store), indent=2, ensure_ascii=False))
        elif args.stats:
            print(json.dumps(store.counts(), indent=2))
        elif args.preview:
            source_id = active_source(corpus, store)
            item = next((item for item in corpus.atoms if item.atom.source_id == source_id and item.key not in store.mappings), None)
            print(json.dumps({
                "active_source_id": source_id,
                "atom_key": item.key if item else None,
                "effective_claim": item.effective_claim if item else None,
                "effective_claim_origin": item.effective_claim_origin if item else None,
            }, indent=2, ensure_ascii=False))
        return 0
    except (TriageError, subprocess.CalledProcessError) as exc:
        print(f"MSID MAPPING ERROR: {exc}", file=os.sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
