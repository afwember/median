# MEDIAN v0.5.0 Extraction — Gate 1 Process Diagnosis

**Status:** Gate 1 passed; recovery freeze active  
**Date:** 2026-08-02  
**Scope:** Diagnosis only. This document does not approve any accepted candidate, resume paid extraction, or authorize deletion of prior evidence.

## Executive verdict

The extraction effort is **recoverable, but the current pipeline must not resume unchanged**.

The first rounds of calibration were legitimate process refinement. Crossing exposed real problems in source conversion, chunk boundaries, atomicity, grounding, ownership, and semantic classification. Those discoveries justified iteration.

The later growth is substantially process drift. Work moved between conversational threads without one small executable contract. Each new source inherited and modified source-specific code and controls. Extraction, ontology assignment, authority adjudication, conformance, and cross-document reconciliation became partially combined. More controls were added without retiring their predecessors. The result is not merely a sophisticated pipeline: it is a collection of useful evidence and experiments whose current authority is ambiguous.

This is not a corpus-loss event. Source documents, paid model responses, run receipts, accepted candidates, and cost records remain available. The correct recovery action is to preserve that evidence, define a simpler target process, audit the four accepted source results for reuse, and only then restart extraction.

## What was legitimate refinement

The following problems were real and deserved explicit safeguards:

- Markdown converted from PDF/DOCX contains tables, headings, endnotes, and editorial material that complicate semantic chunking.
- Token count alone does not bound atom density or output size.
- Model-produced source endpoints can be malformed even when the intended quotation is recoverable.
- Silent provenance and revision-history sections must not become game-canon atoms.
- Atomicity, exact-source grounding, and table-cell boundaries require deterministic validation.
- Source documents have different semantic roles: gameplay specifications, ontology grammar, authorial grammar, constitutional material, mixed ledgers, and non-corpus process records cannot all use an identical disposition policy.
- Calibration on a representative sample before a full paid run is warranted.

These discoveries should survive into the recovered process as tests and explicit stage boundaries.

## Where refinement became drift

### 1. No single operational authority

At diagnosis time, the repository presents multiple active-looking sources of process truth:

- the canonical source registry;
- the rule-document processing order;
- the extraction execution lanes;
- the runbook and handoff packet;
- the Claude operations provisioning guide;
- nine retained prompt versions;
- four retained proposal-schema versions;
- the final atom schema;
- source-specific worker scripts.

The registry and processing-order files do not express the same source order or processing-policy vocabulary. Eleven registry-enabled sources are absent from the newer canonical queue. Older controls remain adjacent to newer controls without consistent `current`, `superseded`, or `historical` status markers. A new task can therefore follow a plausible-looking but obsolete path.

### 2. Extraction and adjudication were combined

The stated extraction contract is source-bounded, but the proposal and atom formats request fields such as:

- adjudicated class;
- primary and related MSID paths;
- authority scope and effect;
- conflicts and supersession;
- conformance basis and cross-source support.

Some of those fields require other documents or an authority decision. Supplying them during source extraction encourages the model to interpret the source through an already chosen corpus structure. The many free-form `adjudicated_class` values in accepted candidates are evidence that this combined stage is not controlled by a stable vocabulary.

The recovered process must separate:

1. source-bounded evidence extraction;
2. deterministic grounding and structural validation;
3. corpus organization using the accepted MSID vocabulary;
4. authority adjudication and cross-source reconciliation;
5. compile/render output.

### 3. Cross-source context leaked into source extraction

Later source workers inherited code and assumptions from earlier workers. In the clearest failure, an Authorial Grammar calibration embedded the complete 20-atom Human Rulings authorial partition into a nominally small source call. The provider received 14,713 input tokens and returned the 6,000-token maximum; the result was rejected and cost $0.089426.

MSID Grammar is a legitimate foundational corpus source. It should be atomized itself, and its accepted identifier vocabulary may later constrain corpus organization. Its full atom set should not be passed into every other document's evidence-extraction prompt. A small frozen list of legal identifier syntax may be used for validation, but it must not silently perform cross-document interpretation.

### 4. Source-specific forks replaced one stable engine

The live extraction tool directory contains 14 worker or support scripts plus four tests. Authorial Grammar and Human Rulings workers import MSID-specific calibration or direct-run code; their behavior therefore depends on a lineage of prior source fixes. This made a local correction capable of changing another source's behavior and forced new task threads to reconstruct implicit history.

The repository now contains 85 extraction run directories. The largest retry families include 23 MSID direct runs and 23 Philosophy/Architecture direct runs. Retry evidence is valuable, but the number and source-specific version lineages show that the experiment record became the de facto specification.

### 5. Conversation threads carried state that the repository did not clearly encode

Successive tasks had to infer terms such as “source 4,” decide document eligibility from filenames, and reconstruct which calibration rules were current. This caused attempts to process governance material as game material, attempts to start the wrong document, and inconsistent interpretations of whether extraction should receive prior-document atoms.

The root problem is not that a new task lacks intelligence or sufficient context. The repository did not provide one short, current, machine-checkable job contract from which the right action followed unambiguously.

### 6. Acceptance labels exceed what has been demonstrated

There are accepted-candidate artifacts for four sources:

- Crossing — 121 records;
- MSID Grammar — 273 records;
- Governing Philosophy and Architecture — 346 records;
- Human Rulings Ledger — 173 original records, later partitioned into 54 game-semantic, 26 ontology-grammar, 20 authorial-rule, and 73 excluded/control-or-provenance records.

These files demonstrate completed extraction work. They do **not yet demonstrate that every field is suitable for the final corpus**. Exact quotation, source location, and atom boundary may be reusable even where MSID ownership, adjudicated class, authority effect, conformance, conflict, or supersession is not. Gate 3 will decide reuse field by field and source by source.

Home has only a zero-call dry-run snapshot: 58 chunks, 115 synthetic atoms, projected maximum output 5,859 tokens, and zero external model calls. Authorial Grammar has calibration artifacts but no accepted full extraction. Neither is counted among the four accepted sources.

## Operational footprint

At the Gate 1 snapshot, the repository contains:

| Measure | Observed state |
|---|---:|
| Extraction run directories | 85 |
| Top-level extraction worker/support scripts | 14 |
| Extraction test files | 4 |
| Active-looking operations files | 14 |
| Files under `extraction/accepted` | 16 |
| Accepted source sets | 4 |
| Cost-ledger entries | 154 |

The cost ledger records **$10.249100** total compile-process spend:

- $4.930000 user-reported legacy Claude extraction spend from the abandoned process;
- $5.319100 provider-confirmed subsequent API spend.

The subsequent spend includes useful accepted output, calibration, rejected responses, and replay/retry work. Cost is not the principal failure. The controlling failure is that repeatable process state became difficult to distinguish from experimental history.

## Root-cause assessment

The primary root cause is **stage-boundary failure combined with authority proliferation**.

Contributing causes are:

1. source eligibility and source role were not fixed in one authoritative manifest;
2. filenames and conversational shorthand were trusted more than content inventories;
3. extraction requested decisions belonging to organization and reconciliation;
4. source-specific worker forks accumulated instead of converging into one engine plus declarative profiles;
5. new prompt/schema versions were added without retiring old ones;
6. task handoffs relied on narrative context rather than a small executable work order;
7. “accepted candidate” was allowed to sound more final than its validation evidence warranted.

## Recoverability judgment

### Preserve as evidence

- all immutable source Markdown and source hashes;
- raw provider requests, responses, and usage receipts;
- deterministic replay artifacts;
- accepted candidates and acceptance reports;
- Human Rulings partitions and disposition ledger;
- cost entries;
- tests that encode a source-independent grounding or atomicity invariant.

### Treat as provisional pending later gates

- all four accepted candidate sets;
- every semantic classification and ownership field within them;
- source-role classifications in the competing registry/queue controls;
- the Home dry-run chunk profile;
- Authorial Grammar calibration work;
- source-specific repairs that have not been expressed as general tests.

### Do not use as current execution authority

Until Gate 5 explicitly replaces the freeze, none of the following independently authorizes a paid call or determines the next source:

- the existing runbook;
- the Claude thread provisioning guide or bootstrap prompt;
- the existing registry by itself;
- the processing-order file by itself;
- the execution-lanes file by itself;
- any numbered prompt or proposal schema;
- any source-specific direct or calibration worker;
- any prior conversational task prompt.

This designation does not mean these files are valueless or should be deleted. It means they are historical/provisional inputs to recovery, not a safe current pipeline.

## Recovery freeze

Effective with this Gate 1 decision:

- no paid extraction calls;
- no new source-specific worker forks;
- no modification of accepted candidates in place;
- no promotion of dry-run output to accepted status;
- no deletion or archival move of run evidence during Gates 2–3;
- no resumption based solely on a prior task's instructions;
- no cross-source reconciliation disguised as extraction.

Read-only audit, deterministic local validation, new recovery documentation, and additive audit artifacts remain permitted. Gate 4 may move drift artifacts into a dated archive only after Gate 3 identifies the evidence needed for reuse assessment. Every move must be recoverable and recorded in a disposition manifest; Gate 4 does not authorize deletion.

The freeze ends only when:

1. Gate 2 defines the exact desired corpus, stages, schemas, source roles, and success conditions;
2. Gate 3 reports which existing fields and records are reusable;
3. Gate 4 archives drift artifacts under a complete disposition manifest;
4. Gate 5 installs and verifies one guarded process and the user authorizes its first paid calibration.

## Gate 1 decision

**PASS — diagnosis complete, with mandatory recovery freeze.**

The repository contains enough source material and extraction evidence to continue. The current operational controls are too numerous and contradictory to continue safely. The next authorized activity is Gate 2: define the actual desired process and outcome without running extraction.
