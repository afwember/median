#!/usr/bin/env python3
"""Build the immutable authorial atom corpus from the completed compile evidence."""

from __future__ import annotations

from collections import Counter
import hashlib
import json
import os
from pathlib import Path
import stat
import tempfile

from m050_atom_rewrite import DEFAULT_REWRITES, RewriteCorpus, RewriteStore
from m050_atom_triage import DEFAULT_DECISIONS, DecisionStore, load_corpus
from m050_msid_mapping import DEFAULT_MAPPINGS, MSIDVocabulary, MappingCorpus, MappingStore


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "m050/corpus/M050_Authorial_Atom_Corpus_MEDIANv0_5_0.jsonl"
MANIFEST = ROOT / "m050/corpus/M050_Authorial_Atom_Corpus_Manifest_MEDIANv0_5_0.json"
MATRIX = ROOT / "m050/extraction/control/M050_Compile_Source_State_Matrix_v0_1_MEDIANv0_5_0.json"
FROZEN = ROOT / "m050/extraction/control/M050_Frozen_Corpus_Manifest_v0_1_MEDIANv0_5_0.json"
RECONCILIATIONS = ROOT / "m050/reconciliation/M050_Reconciled_Semantic_Units_MEDIANv0_5_0.jsonl"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def read_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def atomic_write(path: Path, content: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    mode = stat.S_IMODE(path.stat().st_mode) if path.exists() else 0o644
    descriptor, name = tempfile.mkstemp(dir=path.parent, prefix=f".{path.name}.")
    temporary = Path(name)
    try:
        with os.fdopen(descriptor, "wb") as handle:
            handle.write(content)
            handle.flush()
            os.fsync(handle.fileno())
        os.chmod(temporary, mode)
        os.replace(temporary, path)
    except BaseException:
        temporary.unlink(missing_ok=True)
        raise


def main() -> int:
    full_corpus = load_corpus(ROOT)
    decisions = DecisionStore(ROOT / DEFAULT_DECISIONS, full_corpus)
    rewrite_corpus = RewriteCorpus(ROOT)
    rewrites = RewriteStore(ROOT / DEFAULT_REWRITES, rewrite_corpus)
    corpus = MappingCorpus(ROOT)
    vocabulary = MSIDVocabulary(ROOT)
    mappings = MappingStore(ROOT / DEFAULT_MAPPINGS, corpus, vocabulary)
    matrix = json.loads(MATRIX.read_text(encoding="utf-8"))
    frozen = json.loads(FROZEN.read_text(encoding="utf-8"))

    source_paths = {
        item["source_id"]: item["path"]
        for item in matrix["sources"]
        if item["source_id"] in corpus.source_ids
    }
    historical_units = read_jsonl(RECONCILIATIONS)
    prior_unit_by_atom = {
        member["atom_key"]: unit["unit_id"]
        for unit in historical_units
        for member in unit["members"]
    }

    records: list[dict] = []
    for item in corpus.atoms:
        atom = item.atom
        decision = decisions.decisions[item.key]
        resolution = None
        rewrite_event_id = None
        if decision["decision"] == "uncertain":
            rewrite = rewrites.rewrites[item.key]
            resolution = rewrite.get("resolution", "rewrite")
            rewrite_event_id = rewrite["event_id"]
        mapping = mappings.mappings[item.key]
        records.append({
            "schema_version": "M050-AUTHORIAL-CORPUS-ATOM-0.1",
            "corpus_position": len(records) + 1,
            "atom_key": item.key,
            "atom_id": atom.atom_id,
            "source_id": atom.source_id,
            "source_label": atom.source_label,
            "source_document": source_paths[atom.source_id],
            "source_position": atom.source_position,
            "source_atom_position": atom.source_atom_position,
            "section": atom.section,
            "block_key": atom.block_key,
            "block_id": atom.block_id,
            "block_type": atom.block_type,
            "claim_kind": atom.claim_kind,
            "exact_source_text": atom.exact_source_text,
            "normalized_claim": atom.normalized_claim,
            "effective_claim": item.effective_claim,
            "effective_claim_origin": item.effective_claim_origin,
            "effective_claim_sha256": item.effective_claim_sha256,
            "accepted_candidate_sha256": atom.candidate_sha256,
            "authorial_decision": {
                "triage": decision["decision"],
                "triage_event_id": decision["event_id"],
                "rewrite_resolution": resolution,
                "rewrite_event_id": rewrite_event_id,
            },
            "prior_classification": {
                "status": mapping["mapping_status"],
                "primary_msid": mapping["primary_msid"],
                "alternate_primary_msids": mapping["alternate_primary_msids"],
                "related_msids": mapping["related_msids"],
                "semantic_relation": mapping["semantic_relation"],
                "rationale": mapping["rationale"],
            },
            "prior_reconciliation_unit_id": prior_unit_by_atom.get(item.key),
        })

    corpus_bytes = b"".join(
        json.dumps(record, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8") + b"\n"
        for record in records
    )
    atomic_write(OUTPUT, corpus_bytes)

    mapping_counts = Counter(record["prior_classification"]["status"] for record in records)
    source_documents = []
    frozen_by_path = {item["path"]: item for item in frozen["frozen_files"]}
    for source_id in corpus.source_ids:
        path = source_paths[source_id]
        source_documents.append({
            "source_id": source_id,
            "label": corpus.source_labels[source_id],
            "path": path,
            "sha256": frozen_by_path[path]["sha256"],
            "atom_count": corpus.source_totals[source_id],
        })
    manifest = {
        "schema_version": "M050-AUTHORIAL-CORPUS-MANIFEST-0.1",
        "status": "FROZEN_AUTHORIAL_SOURCE_LIBRARY",
        "created": "2026-09-12",
        "scope": "MEDIAN v0.5.0 pre-composition evidence after completed atomization, authorial triage and rewrite",
        "corpus_record": OUTPUT.relative_to(ROOT).as_posix(),
        "corpus_record_sha256": sha256(OUTPUT),
        "corpus_atom_schema_version": "M050-AUTHORIAL-CORPUS-ATOM-0.1",
        "atom_count": len(records),
        "source_count": len(corpus.source_ids),
        "source_documents": source_documents,
        "frozen_source_files": frozen["frozen_files"],
        "prior_classification_counts": dict(sorted(mapping_counts.items())),
        "historical_reconciliation": {
            "unit_count": len(historical_units),
            "accounted_atom_count": len(prior_unit_by_atom),
            "status": "ARCHIVED_ADVISORY_EVIDENCE",
        },
        "rules": {
            "authorial_judgment_controls_final_gdd": True,
            "prior_classification_is_advisory": True,
            "prior_reconciliation_is_advisory": True,
            "exhaustive_semantic_reconciliation_required": False,
            "m051_input_allowed": False,
        },
    }
    atomic_write(
        MANIFEST,
        (json.dumps(manifest, indent=2, ensure_ascii=False) + "\n").encode("utf-8"),
    )
    print(f"Wrote {len(records):,} authorial atoms from {len(corpus.source_ids)} sources.")
    print(f"Corpus SHA-256: {manifest['corpus_record_sha256']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
