# MEDIAN v0.5.0 Extraction — Gate 2 Target Process and Error Correction

**Status:** Gate 2 passed; implementation and paid work remain frozen  
**Date:** 2026-08-02  
**Companion source disposition:** `M050_Extraction_Gate_2_Source_Disposition_v0_1_MEDIANv0_5_0.yaml`  
**Execution authority:** None. Paid calls remain frozen.

## 1. Desired outcome

The immediate product is not a rewritten GDD and not a flat pile of model summaries. It is a **source-preserving, typed atomic evidence corpus** from which MEDIAN v0.5.0 can be mapped, reconciled, checked against its historical baseline, and compiled.

The finished system must provide:

1. immutable source files with hashes;
2. grounded atomic evidence that preserves exact wording and normalized meaning;
3. a disposition for every claim-bearing source block, including justified exclusions;
4. separate game-semantic, ontology, authorial, human-ruling, reconciliation, manifestation, publication, and provenance streams;
5. MSID mappings that are traceable proposals or decisions rather than extraction-time guesses;
6. reconciliation decisions tied to their evidence and authority basis;
7. a completeness audit against the prior corpus;
8. deterministic compiler inputs capable of producing a human-readable MEDIAN v0.5.0 specification set and Sourcebook structure;
9. append-only receipts for every correction, retry, promotion, exclusion, and transformation.

The target is successful when a reader can move in both directions:

```text
source wording → evidence atom → MSID mapping → reconciliation decision → compiled passage
compiled passage → reconciliation decision → evidence atom → exact source location
```

## 2. Non-goals

Atomic extraction does not:

- decide which conflicting source wins;
- infer authority from a title or internal rhetoric;
- assign final MSIDs;
- normalize terminology by rewriting source quotations;
- apply the conformance directive to source evidence;
- merge different documents;
- produce polished prose;
- import v0.5.1 material;
- mine historical sources for canon before current-source reconciliation;
- treat a provider response as accepted merely because it parses.

## 3. Identity doctrine

### 3.1 Filename is not identity

Every source receives a content-and-provenance identity card before any paid work. The card records actual section-level contents, origin, predecessor material, purpose, internal authority claims, human-adjudicated role, mixed-status regions, candidate owners, streams, and exclusions. Its predecessor coverage is an early warning map only; it is not a source-versus-baseline semantic diff and does not influence extraction.

A filename or title may be retained as a stable filesystem label without controlling semantic treatment. “Canonical,” “adopted,” “development-lock,” “dedicated,” “global,” and similar self-labels are source evidence only.

The human-supplied development genealogy controls the identity of the four former `CATCHALL` documents:

1. The v0.4.6 GDD was followed by two v0.4.7 decision-development documents.
2. A major Home reconception within that work became the first v0.5 specification.
3. Additional v0.5 system specifications followed.
4. After v0.5 had substantially crystallized, the BSA process returned to the v0.4.7 decision material to determine what still fit the new conception.
5. BSA-11 grew into the dedicated Away Mode specification.
6. Later continuation of the v0.4.7 adaptation became v0.4.7 Cross-System Carryforward.
7. A final review of subjects insufficiently covered from the actual v0.4.6 GDD produced the document named *v0.4.6 GDD Coverage-Gap Development*.

Therefore:

- BSA, BDL, and v0.4.7 Cross-System Carryforward are v0.4.7-to-v0.5 developmental-bridge sources containing substantive rules that must participate in grand reconciliation.
- Away is a dedicated descendant of the BSA process and leads within its actual scope, but it does not erase unrelated bridge material by silence.
- The v0.4.6 GDD Coverage-Gap Development is late coverage-gap development, not a coherent global owner and not merely residual v0.4.7 material.
- The v0.4.6 GDD alone is the baseline being revised.

Every substantive claim from the two v0.4.7 bridge ledgers, the v0.4.7 Cross-System Carryforward, and the v0.4.6 GDD Coverage-Gap Development will be extracted and mapped. Source role affects reconciliation and authority; it does not authorize silent exclusion.

### 3.2 Identity card is a hard gate

A work order cannot be issued when:

- the source role was derived from filename alone;
- its origin or predecessor is unresolved;
- a mixed source lacks section dispositions;
- internal authority claims have not been separated from human-adjudicated authority;
- the exact source hash differs from the Gate 2 manifest;
- the requested output stream does not match its content inventory.

## 4. Atomic streams

The corpus is typed. Records do not gain authority by sharing a directory.

| Stream | Contains | Does not contain |
|---|---|---|
| `evidence_game_semantic` | Game identity, systems, mechanics, state, content contracts, and presentation behavior | MSID assignments or cross-source authority decisions |
| `evidence_ontology_grammar` | MSID syntax, identifier semantics, aliases, and ontology rules | Gameplay merely mentioned as an example |
| `evidence_authorial_rule` | Canonical language, typography, orthography, voice, and lint | Publication scheduling or extraction operations |
| `evidence_human_ruling` | Each direct human ruling as issued | Automatic flattening into game canon |
| `reconciliation_rule` | Authority scopes, explicit corrections, conformance, and precedence | Independent game mechanics |
| `manifestation_rule` | Cross-medium invariants and medium-specific translations | Core game rules presented as though newly owned by a manifestation |
| `publication_rule` | Appendix, Sourcebook, index, and production architecture | Game canon |
| `provenance_evidence` | Historical claims, survivorship, lineage, exclusions, and gap evidence | Default current canon |

## 5. Stage architecture

### Stage 0 — Source freeze and content identity

Inputs are immutable Markdown sources and a single source-disposition manifest. The system verifies path, hash, v0.5.0 identity, identity card, source role, allowed streams, and exclusions.

No model is called. Failure stops the work order.

### Stage 1 — Structural preparation

A single source-independent parser assigns stable block IDs to:

- headings;
- paragraphs;
- list items;
- table headings, rows, and cells;
- callouts;
- explicit examples;
- status declarations;
- endnotes and change records.

Chunks group those blocks without breaking a table row, crossing an explicit status boundary, or crossing a silent/provenance boundary. Chunking has two independent limits:

- input-token ceiling;
- maximum claim-bearing block count.

The dry run produces the block inventory, chunk plan, prompt-size estimate, output-density projection, excluded regions, and calibration sample. It makes no external call.

### Stage 2 — Source-bounded evidence extraction

The model receives:

- one source identity card;
- one set of owned blocks from that same source;
- the evidence proposal schema;
- the extraction instructions.

It does not receive prior atoms, other sources, the full authority map, conformance corrections, or final MSID assignments.

For every input block, it must return exactly one of:

1. one or more proposed atoms grounded in that block;
2. `no_substantive_claim`;
3. an allowed exclusion code;
4. `review_required` with a reason.

This **block-disposition ledger** makes omission visible. A response with an undispositioned or multiply dispositioned block is incomplete and rejected.

### Stage 3 — Deterministic validation and evidence acceptance

The runner, not the model:

- assigns record IDs;
- verifies source and block hashes;
- resolves exact source locations;
- checks every quotation against the immutable source;
- rejects cross-block quotations unless the work order explicitly permits them;
- validates schema and enums;
- detects duplicates;
- verifies block disposition completeness;
- flags likely compound atoms;
- preserves the raw request, response, and usage receipt.

Accepted Stage 3 evidence is still source testimony. It has no final MSID or cross-source authority effect.

### Stage 4 — MSID vocabulary construction and mapping

Accepted MSID Grammar evidence is used to build a controlled vocabulary and validator. Each game, authorial, manifestation, or ruling atom is then mapped separately.

Mapping output records:

- zero, one, or more MSID candidates;
- mapping status: `mapped`, `unmapped`, `ambiguous`, `invalid`, or `human_required`;
- rationale tied to ontology rules;
- mapper version;
- any literal MSID the source itself stated.

The exact source quotation never changes. A mapping correction creates a new mapping record rather than changing the evidence atom.

### Stage 5 — Authority and conformance reconciliation

Only here are sources compared. Reconciliation receives validated evidence, MSID mappings, human rulings, source identity cards, the authority manifest, and conformance rules.

The grand reconciliation includes all substantive evidence from the two v0.4.7 bridge ledgers, the v0.4.7 Cross-System Carryforward, and the v0.4.6 GDD Coverage-Gap Development even though some currently reside in a provenance folder. Each atom must receive one explicit disposition:

- represented or corroborated by a current owner;
- uniquely surviving and accepted into v0.5;
- superseded by identified later evidence;
- conflicting and unresolved;
- provisional or deferred;
- diagnostic/process material excluded with reason.

No valid rule loses merely because it appears only in a developmental-bridge or coverage-gap source. No dedicated descendant erases an unaddressed claim by silence.

It determines:

- agreement and corroboration;
- owner and authority scope;
- active, working, provisional, tuning, example, historical, retired, or unresolved status;
- conflict and ambiguity;
- supersession or aliasing;
- terminology correction without rewriting the source quotation;
- need for an explicit human ruling.

No inference may promote a remainder, companion, historical source, or document self-label over an actual owner.

### Stage 6 — Baseline survivorship and gap audit

The reconciled current corpus is the proposed v0.5.0 target. Only after that target exists is it checked against the v0.4.6 GDD, which is the actual baseline being revised. Relevant v0.4.6 material is grounded as `provenance_evidence` and compared at compatible semantic or MSID scope.

The documents currently named *v0.4.7 Development Survivorship Review* and *v0.4.7 Development Rulings Ledger* are not audits of the v0.4.6 GDD and are not Stage 6 baseline indexes. Their word “Baseline” referred to earlier v0.4.7 development material within the originating conversation. Their substantive contents have already entered Stage 5 as developmental-bridge evidence.

Each baseline subject is classified as:

- covered by reconciled current evidence;
- deliberately changed or retired by explicit current authority;
- moved or reorganized without substantive loss;
- historical only;
- deferred;
- unresolved and requiring a ruling;
- genuinely absent from the v0.5.0 source set.

Absence from a current specification never means retirement by inference. If the audit exposes an actual omission or unexplained loss, it opens a ruling/reconciliation issue and returns to Stage 5 before compilation. Historical material is never silently restored.

A directional change guide may later be derived if a chosen compiler or editorial workflow needs one. It is not a required semantic stage and does not organize the corpus.

### Stage 7 — Manifestation and publication processing

Manifestations are extracted into their own stream and reconciled against the already reconciled core. Appendix and Sourcebook architecture are compiled as publication controls. Market and production companions remain reference material unless explicitly selected.

### Stage 8 — Compilation and bidirectional audit

The compiler consumes only reconciled records and publication controls. It emits readable documents plus a map from every compiled claim to its reconciliation and evidence IDs. A bidirectional audit checks that no compiled claim lacks evidence and no accepted required record disappears silently.

## 6. Layered record model

One overloaded atom schema is replaced by linked layers.

### Layer E — Evidence atom

Required concepts:

- evidence schema version;
- evidence ID assigned locally;
- source ID and source hash;
- block ID and exact source location;
- exact source text;
- normalized claim text;
- controlled claim kind;
- explicitly declared source status, if present;
- literal terms or identifiers stated by the source;
- raw response and chunk receipt IDs.

It contains no inferred MSID, authority effect, conformance basis, cross-source support, conflict, or supersession.

### Layer M — Mapping record

Required concepts:

- mapping ID and version;
- evidence ID;
- MSID candidates;
- mapping status and rationale;
- ontology evidence IDs;
- mapper identity;
- review state.

### Layer R — Reconciliation record

Required concepts:

- reconciliation ID and version;
- subject/MSID;
- supporting and opposing evidence IDs;
- applicable authority and conformance rule IDs;
- adjudicated meaning and status;
- conflict, alias, or supersession links;
- decision type: deterministic, model-proposed, or explicit human ruling;
- review and acceptance receipt.

### Layer C — Compile record

Required concepts:

- compile ID;
- reconciliation IDs used;
- target document and location;
- rendered text;
- compiler version and input hashes.

All layers are append-only. Superseded records remain addressable.

## 7. Procedural error correction

### 7.1 Correction hierarchy

Use the least interpretive correction that fully resolves the error:

1. deterministic local validation or lossless normalization;
2. deterministic replay of the already-paid raw response;
3. targeted retry of only the failed block or chunk under the unchanged prompt;
4. prompt/schema/engine revision followed by the complete regression suite and replay of preserved responses;
5. explicit human ruling.

Never repurchase a valid response merely because downstream code changed. Never broaden a correction rule to make one example pass without adversarial regression cases.

### 7.2 Error classes and permitted response

| Error | Required response | Forbidden shortcut |
|---|---|---|
| Source path/hash mismatch | Stop; resolve identity and regenerate the work order | Using the similarly named file |
| Wrong source role or mixed-content boundary | Stop; revise the identity card under human review | Inferring from title or folder |
| Chunk crosses status, table, or silent boundary | Rechunk locally before any call | Asking the model to infer the boundary |
| Prompt exceeds budget | Reduce owned blocks; rerun dry run | Raising output limit without density analysis |
| Transport interruption | Preserve receipt; retry the identical request if no complete response exists | Treating a partial response as complete |
| Output ceiling/truncation | Reject the whole response; reduce block count; targeted retry | Accepting complete-looking leading records |
| JSON/schema failure | Lossless parser repair only when semantics are unchanged; otherwise retry | Inventing missing values locally |
| Quotation not found | Reject the atom; targeted replay/retry | Silently substituting similar source prose |
| Extra or duplicated quote prefix | Repair only when deterministic exact matching proves a duplicated token; retain repair receipt | General fuzzy truncation |
| Compound atom | Split deterministically only if source spans and normalized claims remain unambiguous; otherwise targeted retry | Arbitrary clause chopping |
| Missing block disposition | Reject response as incomplete; targeted retry | Assuming no claim |
| Suspected semantic omission | Independent coverage review of the affected block; append recovered evidence | Editing the accepted atom set in place |
| Wrong claim kind | Correct in a new validation/adjudication record | Altering exact evidence |
| Invalid or disputed MSID | Correct Layer M only | Re-extracting the source claim |
| Cross-source conflict | Create unresolved Layer R record or human question | Rewriting or deleting one source atom |
| Incorrect authority | Correct Layer R with cited authority evidence | Changing the source's self-description |
| Human correction | Append explicit ruling and superseding decision | Retroactively hiding the prior decision |

### 7.3 Retry and mutation limits

- A paid work order pins source hash, engine, prompt, schema, provider, model, parameters, and cost cap.
- The prompt and schema cannot change inside that work order.
- A targeted retry may contain only the original failed source blocks.
- One unchanged-prompt retry is permitted for transport or truncation after local rechunking.
- A repeated semantic failure stops the document and opens a process issue; it does not start a chain of source-specific prompt versions.
- Any engine or prompt change creates a new global version and must pass the fixed regression corpus before another paid call.
- Source-specific behavior is declarative in the identity card; no source-specific worker fork is permitted.

### 7.4 Calibration and coverage controls

Each source's calibration sample must include, when present:

- ordinary prose;
- the densest claim-bearing section;
- a table;
- a mixed-status or provisional region;
- an example/non-normative boundary;
- an endnote, change record, or excluded region.

Calibration acceptance requires 100% block disposition, exact grounding, schema validity, no context leakage, and semantic review of every calibration atom. A full run remains prohibited until the calibration report is accepted.

Full-document review includes:

- deterministic checks on every atom and block;
- human review of every error, ambiguity, provisional/tuning record, table-derived atom, and exclusion;
- section-edge sampling;
- an independent coverage pass that can propose omissions but cannot modify evidence directly.

## 8. Work-order contract

Every run begins from one small machine-readable work order containing:

- one source ID, exact path, and hash;
- identity-card version;
- allowed input blocks and output streams;
- prompt, schema, engine, provider, and model versions;
- dry-run receipt;
- calibration selection;
- request-token, output-token, and claim-block limits;
- maximum authorized spend, defaulting to `$0.00`;
- retry allowance;
- stop conditions;
- expected output paths.

The worker cannot select the next source, edit controls, increase cost, or accept output. A task may operate the worker, but the repository contract determines what the worker can do.

## 9. Cost and evidence accounting

- Every external request is logged immediately, including rejected and interrupted calls.
- Anthropic, OpenAI, and other providers use the same ledger fields.
- Cached tokens, uncached tokens, output tokens, confirmed cost, request ID, and result disposition are recorded separately.
- Prompt caching is an optional cost optimization, never a correctness dependency.
- Batch execution is disabled for calibration and remains opt-in for later repetitive work.
- No work order with a positive cost cap runs without explicit user authorization.

## 10. Acceptance gates

### Evidence-source acceptance

- source identity card approved;
- source hash verified;
- dry run approved;
- calibration approved;
- every block dispositioned;
- every accepted quote grounded exactly;
- schema and enum validation passed;
- all anomalies resolved or explicitly marked;
- raw response and cost receipts present;
- semantic acceptance report signed;
- accepted output written as a new immutable candidate.

### Mapping acceptance

- controlled MSID vocabulary version pinned;
- no invalid identifier accepted;
- ambiguous and unmapped records remain explicit;
- mapping corrections do not alter evidence atoms.

### Reconciliation acceptance

- all supporting and conflicting evidence linked;
- authority comes from explicit rules, not filenames or rhetoric;
- unresolved conflicts remain unresolved;
- every human decision has a ruling receipt;
- no source quotation is rewritten.

### Compile acceptance

- every substantive compiled claim traces to accepted reconciliation records;
- every required reconciled record has a disposition in the compiled output;
- historical survivorship audit completed;
- no baseline omission has been interpreted as retirement without authority;
- v0.5.1 contamination count is zero;
- build is reproducible from pinned inputs.

## 11. Gate 2 completion criteria

Gate 2 passes when:

1. this target process is accepted as the only recovery design;
2. the companion source-disposition manifest covers every current v0.5 document;
3. the v0.4.6 GDD Coverage-Gap Development misidentification and the filename-is-not-identity rule are recorded;
4. the atomic streams and layered schemas are fixed conceptually;
5. the error-correction hierarchy and stop rules are fixed;
6. no paid call has occurred;
7. Gate 3 can evaluate existing candidates against Layer E without relying on their premature Layer M/R fields.

Gate 2 does not approve implementation. Schemas, engine, work-order format, identity cards, regression fixtures, and archival moves are created or finalized in Gates 4–5 after the reuse audit.

## 12. Gate 2 decision

**PASS — target process and corpus roles defined.**

Gate 3 may audit existing accepted candidates against the evidence-only Layer E standard. Gate 4 must complete the coordinated source-identity migration and prove that the misleading *v0.4.6 GDD Coverage-Gap Development* identity has zero non-archive filenames, paths, identifiers, or textual references before Gate 5 may begin.
