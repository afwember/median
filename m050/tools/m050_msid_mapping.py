#!/usr/bin/env python3
"""Zero-call Stage 4 MSID mapping inventory, validation, and record store."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
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


def _text_sha256(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


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


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=Path.cwd())
    parser.add_argument("--inventory", action="store_true")
    parser.add_argument("--stats", action="store_true")
    parser.add_argument("--preview", action="store_true")
    args = parser.parse_args(argv)
    try:
        root = args.repo_root.resolve()
        corpus = MappingCorpus(root)
        vocabulary = MSIDVocabulary(root)
        store = MappingStore(root / DEFAULT_MAPPINGS, corpus, vocabulary)
        if args.inventory:
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
        else:
            raise TriageError("use --inventory, --stats, or --preview")
        return 0
    except TriageError as exc:
        print(f"MSID MAPPING ERROR: {exc}", file=os.sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
