# MEDIAN v0.5.0 Extraction — Gate 3 Completed-Extraction Reuse Audit

**Status:** Gate 3 passed with mandatory migration repairs; paid extraction remains frozen  
**Date:** 2026-08-02  
**Machine-readable disposition:** `M050_Extraction_Gate_3_Reuse_Disposition_v0_1_MEDIANv0_5_0.yaml`  
**Scope:** Crossing, Human Rulings Ledger, MSID Grammar, and Governing Philosophy and Architecture  
**Execution authority:** None. This audit authorizes no external model call and no direct reconciliation of the legacy rows.

## 1. Decision

The four completed extraction sets are **usable and worth preserving**, but they are not valid as finished records in the Gate 2 architecture.

They contain a strong source-evidence core:

- 913 valid JSONL records;
- 913 unique atom IDs;
- 913 distinct exact-source quotations;
- every quotation occurs verbatim in the frozen source used by its run, now retained under the Gate 4 archive where a live source identity changed;
- every quotation occurs inside its cited source location;
- all four accepted-candidate hashes and all four source hashes match their acceptance records;
- no duplicate exact-source quotation occurs within a source set.

They also contain a legacy semantic shell that must not be mistaken for accepted evidence:

- extraction-time MSID assignments;
- inferred authority scope and authority effect;
- inferred status, class, relation, Register, operator, and Mode fields;
- premature supersession judgments;
- a Human Rulings partition that excludes rules needed by the corrected process.

**Gate 3 conclusion:** retain and migrate the grounded quotations, locations, source identities, and receipts into Layer E. Treat every other semantic field as an unaccepted legacy proposal unless it is re-established from the quotation or source structure by a later controlled stage. No wholesale paid re-extraction of these four documents is justified.

## 2. What was tested

The audit independently checked:

1. JSONL parseability, schema labels, record counts, source IDs, and atom-ID uniqueness;
2. accepted-candidate SHA-256 values against the acceptance reports;
3. current source SHA-256 values against the acceptance reports;
4. exact quotation occurrence in the source;
5. quotation containment within every cited line range or paragraph coordinate;
6. duplicate quotations and repeated source locations;
7. field population and uncontrolled vocabulary growth;
8. likely compound-atom indicators, including long and multi-sentence quotations;
9. the Human Rulings source structure against the accepted atoms and the later 100/73 partition;
10. silent/provenance-boundary handling in Governing Philosophy and Architecture.

The acceptance reports' claims of semantic completeness were considered evidence about the old process, not accepted as proof under the new block-disposition contract. The old runs did not emit the Gate 2 block ledger, so Gate 3 cannot retroactively prove the stronger form of coverage required for future sources.

## 3. Aggregate findings

| Source | Records | Unique cited locations | Median words | 90th percentile | Maximum words | Multi-sentence review flags | Reuse decision |
|---|---:|---:|---:|---:|---:|---:|---|
| Crossing | 121 | 88 | 11 | 20 | 37 | 2 | Reuse as Layer E evidence after local migration |
| Human Rulings | 173 | 61 | 13 | 27 | 97 | 21 | Reuse, but reconstruct ruling records and replace the legacy partition |
| MSID Grammar | 273 | 202 | 11 | 22 | 108 | 31 | Reuse as ontology evidence; ignore extraction-time mappings |
| Philosophy and Architecture | 346 | 204 | 15 | 27 | 57 | 69 | Reuse as constitutional evidence after compound review |
| **Total** | **913** | **555** | — | — | — | **123 review flags** | **No wholesale re-extraction** |

The multi-sentence count is a review queue, not an error count. Some valid atomic units require several sentences; lists and table rows may also be one indivisible evidentiary unit. Migration must review these records rather than split them mechanically.

## 4. Field-level disposition

| Legacy field | Gate 3 disposition | Reason |
|---|---|---|
| `schema_version` | Replace | The legacy overloaded schema is superseded by Layers E, M, R, and C. |
| `atom_id` | Preserve as `legacy_record_id` | It is useful for traceability, but a local deterministic process assigns the new evidence ID. |
| `source_id` | Preserve after Gate 4 alias resolution | It ties the record to a frozen source. |
| `source_location` | Preserve and normalize | All 913 locations ground correctly. Future records use deterministic block IDs as well. |
| `exact_source_text` | Preserve | This is the strongest reusable asset; all 913 quotations passed exact grounding. |
| `source_declared_class` | Do not import as truth | In these runs it often came from the registry profile rather than the quoted block. Literal source status is re-parsed from source structure. |
| `adjudicated_class` | Legacy proposal only | The four sets contain 22, 16, 54, and 38 distinct free-form values respectively. The vocabulary is uncontrolled and mixes layers. |
| `primary_msid_candidate` | Move to unaccepted mapping proposal | Final MSID mapping belongs to Layer M, after ontology evidence is accepted. |
| `related_msid_candidates` | Move to unaccepted mapping proposal | Same separation as the primary candidate. |
| `semantic_relation` | Legacy proposal only | It is inferred and inconsistently expressed. |
| `register`, `operator`, `mode` | Re-derive later | Preserve only literals explicitly present in the quotation; inferred assignments belong to mapping/reconciliation. |
| `record_status`, `msid_status` | Re-derive from source or later decision | The old model mixed source-declared status with adjudicated status. |
| `authority_scope`, `authority_effect` | Do not import into Layer E | All 913 `authority_effect` values are model-written paraphrases and none occurs verbatim in its source. Authority is decided in Layer R. |
| `conformance_basis` | Do not import | Each row merely cites its own source; it is not a cross-source conformance decision. |
| `cross_source_support` | Discard empty shell | It is empty in all 913 records, as expected from source-bounded extraction. |
| `supersedes` | Legacy proposal only | Eighteen Human records and two MSID records contain premature relationships; none is accepted before reconciliation. |
| `conflicts_with` | Discard empty shell | It is empty in all 913 records. Conflicts belong to Layer R. |
| `notes` | Preserve as legacy review notes only | Notes may assist review but do not constitute source evidence. |

## 5. Source dispositions

### 5.1 Crossing — reusable with a small review queue

Crossing is the cleanest of the four game-semantic sets. Its 121 quotations all ground, and its table retests repaired the known species and capacity-row defects. The source's tables and species rows often form legitimate indivisible evidence, so row-shaped atoms are not automatically compound.

Required migration work:

1. import quotation, coordinate, source identity, and legacy ID into Layer E;
2. derive status only from explicit source markers;
3. place the two multi-sentence flags and any table-row normalization questions in local review;
4. discard the calibration prompt's old Register/world-situation assumptions and every extraction-time MSID or authority assignment;
5. generate a retrospective block-disposition ledger locally before declaring Layer E complete.

**Verdict:** usable without another paid extraction.

### 5.2 Human Rulings Ledger — source preserved, legacy partition rejected

The full 173-record candidate is grounded and useful, but it does not preserve the ledger as a ruling-pair structure. The source contains 41 `HR-*` ruling records with fields such as exact human statement, adopted proposition, normalized ruling, authority effect, affected sources, and semantic scope. The candidate primarily atomizes normalized and adopted propositions. None of the 39 single-line `Exact statement` payloads is represented as its own accepted quotation, even though the source itself remains intact.

This matters because Gate 2 requires the direct human decision **as issued** to remain separately traceable from its normalized operational interpretation.

The subsequent deterministic partition is also unsafe under Gate 2. It designated 100 records as canonical-rule streams and 73 as `excluded_control_or_provenance`. That excluded set contains lineage, source-scope, authority, admissibility, correction, and process rules needed by grand reconciliation. Those records may not become game mechanics, but neither may they be removed from the applicable reconciliation and provenance streams.

Required repair is local and deterministic:

1. parse all 41 `HR-*` sections by ruling ID and labeled field;
2. preserve the exact human statement or statements and normalized proposition as distinct linked evidence;
3. attach every legacy atom to its ruling ID and field of origin;
4. emit one ruling-level disposition across the Gate 2 streams;
5. rebuild the partition so lineage and authority rules enter `reconciliation_rule` or `provenance_evidence` as appropriate;
6. record obsolete extraction instructions as superseded process evidence rather than executable controls.

The original 173-record file remains a useful normalized-claim inventory in the Gate 4 archive. The v0.2 100/73 partition must not feed reconciliation unchanged. Gate 4's approved identity migration changed live cross-references in the Human Rulings source; its pre-migration hash and accepted candidate therefore remain linked in archive, while deterministic reconstruction uses the newly hashed live ledger.

**Verdict:** usable after deterministic reconstruction; no paid re-extraction warranted.

### 5.3 MSID Grammar — reusable as grammar evidence, not as pre-mapped canon

The 273 quotations are fully grounded and capture a broad ontology inventory. The high count of free-form classes and the 108-word classification checklist show why the old atom schema is a poor final representation, but they do not invalidate the quotations.

Required migration work:

1. import source-grounded ontology claims into `evidence_ontology_grammar`;
2. preserve literal MSID examples from source text as literals, not accepted mappings for other atoms;
3. exclude or supersede the document's embedded description of the former extraction lifecycle where it conflicts with Gate 2;
4. review the 31 multi-sentence flags, especially checklists and precedence lists, as structured rule sets rather than mechanically splitting them;
5. build the controlled vocabulary and validator only after the grammar evidence is accepted.

**Verdict:** usable without another paid extraction.

### 5.4 Governing Philosophy and Architecture — reusable with compound review

All 346 quotations ground correctly. The previous process also correctly enforced the explicit `STATE: SILENT` provenance boundary: the final silent endnote produced no accepted game atoms. The larger multi-sentence queue reflects the document's constitutional prose; many passages express one protected principle through explanation and consequence.

Required migration work:

1. import grounded constitutional claims into Layer E;
2. retain the silent-endnote exclusion as an explicit block disposition;
3. review 69 multi-sentence flags for genuinely separable obligations, without fragmenting coherent principles;
4. remove all extraction-time MSID and authority conclusions;
5. construct a retrospective block ledger from the frozen source and accepted locations.

**Verdict:** usable without another paid extraction.

## 6. Mandatory migration controls

Gate 4 and Gate 5 must enforce all of the following:

1. The accepted JSONL files remain immutable legacy evidence and are never edited in place.
2. A migration receipt records every new Layer E record's legacy ID, source hash, quotation, and disposition.
3. No legacy semantic field becomes accepted merely because it was populated or previously labeled `canonical`.
4. Human Rulings are rebuilt from ruling structure before any grand reconciliation.
5. The Human v0.2 partition is marked legacy and cannot be an active reconciliation input.
6. Likely compound atoms receive a review disposition; they are not split by punctuation alone.
7. Retrospective block ledgers must account for all source blocks, including silent, furniture, example, historical, and change-record regions.
8. Any quotation or coordinate failure during migration stops that source. It is not silently repaired.
9. Gate 4 source-ID aliases and the mandatory misleading-name migration are resolved before new evidence IDs are minted.
10. No external model call is needed for these repairs.

## 7. Gate result

Gate 3 is **passed with mandatory migration repairs**.

This means:

- the four paid extractions were not wasted;
- their grounded evidence can seed the corrected corpus;
- none may enter reconciliation in its old overloaded form;
- Human Rulings requires the most important repair, but the repair is deterministic and source-preserving;
- the freeze remains active through Gate 4 and Gate 5.
