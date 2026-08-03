# MEDIAN v0.5.0 Source Atomization Pilot-Calibration Protocol

Date: 2026-08-03

Status: mandatory before every new source atomization run; no current provider-call authority

## Purpose

Each MEDIAN source has its own structure, authority pattern, exclusions, tables, media, terminology, status language, and ownership hazards. A prompt that succeeded elsewhere is evidence, not authorization. Every provider-eligible atomization source must prove its extraction configuration on a bounded representative pilot before the rest of that source can run.

This protocol restores the technique used to build the four preserved legacy source candidates. It converts that technique from task memory into a repository-enforced lifecycle.

## Historical evidence

The four preserved legacy sources required 152 controlled paid calls:

| Source | Paid calls | What the run proved |
|---|---:|---|
| Crossing | 22 | Seven calibration/comparison calls preceded release; full review still required targeted table repairs |
| Philosophy/Architecture | 53 | Calibration continued throughout 42 chunks through repeated stops, replays, targeted retries, and control revisions |
| MSID Grammar | 31 | One accepted pilot did not prevent later ownership, truncation, marker, and provisional-status defects |
| Human Rulings | 46 | One accepted pilot preceded source-specific exclusions, replay, split, completeness, and marker corrections |
| **Total** | **152** | Continuous source-by-source calibration, not bulk execution |

Crossing alone used seven calibration/provider-comparison calls, twelve full-run calls including one retry, and three table retests. Philosophy/Architecture was substantially heavier: 53 paid calls and many zero-cost replays, with control revisions and semantic inspection continuing throughout the source.

These totals exclude multiple offline prompt/chunker iterations, zero-cost deterministic replays, and the earlier abandoned compiler work. The evidence is retained in:

- `m050/extraction/progress/M050_Compile_Cost_Ledger_v0_1_MEDIANv0_5_0.md`;
- `m050/docs/operations/costs/M050_Compile_Cost_Entries_v0_1_MEDIANv0_5_0.csv`; and
- `m050/extraction/accepted/crossing/M050_Crossing_Full_Extraction_Acceptance_Report_v0_1_MEDIANv0_5_0.json`.

Crossing proves that pilot acceptance is necessary but insufficient: its full-document review found omitted and malformed table evidence, halted promotion, and required targeted recalibration. Philosophy/Architecture proves the stronger rule: calibration is continuous. A defect in any later chunk can reveal a categorical prompt, context, ownership, span, table, or validator weakness and must stop or narrow the run even after an earlier pilot passed.

## Lifecycle

### 1. Select and identify one source

Follow `M050_Compile_Source_Processing_Order_v0_1_MEDIANv0_5_0.json`; do not infer order from filenames or task recency. Record the exact source ID, path, SHA-256, Gate 2 disposition, output streams, exclusions, and authority limitations. Authorization never transfers between source IDs or source hashes.

Before extraction preparation, create the Gate 2 content/provenance identity card, have it reviewed, and obtain author approval. The card must account for actual section-level contents, genealogy, reason for existence, internal authority claims, mixed/provisional regions, output streams, exclusions, predecessor warnings, and section-level candidate owners. A filename or document self-description cannot substitute for this gate.

### 2. Develop entirely offline

Before any provider call:

1. parse the complete source and prove byte/structure preservation;
2. classify structural blocks, tables, captions, embedded figures/media references, and deterministic exclusions;
3. produce a bounded chunk plan with context and output-size forecasts;
4. choose representative pilot material covering the source’s highest-risk structures;
5. exercise fake responses, malformed responses, and known regression fixtures;
6. give every media reference a terminal disposition: caption text eligible, visual evidence requiring a separate multimodal pilot, nonsemantic illustration, publication-only, or review required;
7. prove that extractable prompt content comes from exactly one source and that cross-source rulings/evidence remain outside the provider payload;
8. validate schema, grounding, span reconstruction, atomicity, coverage, tables, status, ownership, qualifiers, authority scope, and unsupported identifiers; and
9. iterate the prompt, deterministic controls, and chunk boundaries until all offline tests pass.

If materially different structural regimes exist, select more than one pilot. Every identified regime must clear calibration before its corresponding remainder can be released.

### 3. Freeze the pilot contract

The pilot contract binds:

- source ID and source hash;
- Gate 2 disposition and output-stream routing;
- approved identity-card and source-profile hashes;
- pilot chunk ID and chunk hash;
- prompt hash;
- output schema hash;
- chunker, engine, validator, normalization, and exclusion-policy hashes;
- model and reasoning effort;
- provider-call limit of exactly one;
- maximum output allowance; and
- author-approved cost cap rounded up to the cent.

Changing any binding invalidates the pilot result for release purposes unless an explicit compatibility receipt proves that the affected saved responses can be replayed without changing their extraction-quality disposition.

### 4. Make one explicitly authorized pilot call

Provider execution remains physically and procedurally separate from offline preparation. One authorization permits only the bound pilot request. It does not permit a retry, second pilot, full source, subsequent source, or corpus batch.

### 5. Evaluate; reject by default

Preserve the raw response and usage receipt before evaluation. A pilot is perfect-for-release only when:

- schema, grounding, coverage, atomicity, truncation, and table-structure errors are zero;
- exact evidence spans and all required reference items are recovered;
- ownership, status, authority scope, qualifiers, and identifiers are substantively correct;
- no extractable source material, atoms, or contextual authority has leaked from another source;
- no unresolved defect remains; and
- the evaluation is recorded against the frozen bindings.

“Perfect-for-release” means no known defect remains under the defined gates. It does not mean the model is presumed infallible.

Any failure produces an immutable rejection. Correct the method offline and request fresh authority for another bounded pilot. Never silently repair provider output or promote a partially correct pilot.

### 6. Obtain a separate full-source release

Pilot acceptance alone does not release the source. Asa Wember must explicitly approve:

- the exact accepted pilot binding;
- the source-run provider-call limit;
- the rounded-up cost cap; and
- the proposed execution cadence.

The default cadence is synchronous, sequential, one-call-then-review. Any batch, parallel wave, or review-skipping cadence requires separate explicit author approval after evidence of source-specific stability; it is never implied by a full-source release.

### 7. Execute in stoppable chunks

Run sequentially one call at a time by default, preserving each request, response, validation result, extraction-quality review result, and cost receipt. Validate and inspect each chunk before the next call. An accepted initial pilot is not permission to stop learning from later chunks.

The first mechanical or semantic defect:

1. stops new calls;
2. revokes the current release;
3. preserves all accepted and rejected attempts without mutation;
4. returns the affected configuration or structural regime to offline calibration; and
5. requires a new pilot/release receipt for any materially changed binding.

Unaffected validated chunks may be replayed or composed later only when their exact bindings remain valid.

### 8. Perform the whole-document gate

A mechanically complete chunk set is only a candidate. Before source acceptance, audit:

- every substantive source block and intentional exclusion;
- cross-chunk omissions, duplication, overlap, and dependent fragments;
- tables, lists, labels, antecedents, and structural context;
- ownership/status/authority distributions;
- unresolved and review-required material; and
- source-boundary leakage.

Only the whole-document gate can move a source candidate to `source_extraction_candidate_accepted`. This means the source-bounded extraction is complete enough to enter the later controlled evidence lifecycle. It is not Layer E semantic acceptance, canonization, mapping, reconciliation, or permission to write compiled prose. Acceptance of one source does not start the next.

### Authorial Grammar source-specific conformance gate

The recovered historical processing order adds one source-specific obligation for Authorial Grammar. After source-bounded extraction and local validation, but before `source_extraction_candidate_accepted`, compare its candidate against the applicable Human Rulings authorial evidence. Use the active frozen Human Rulings source, its approved identity and coordinate controls, and mechanically valid reconstruction evidence. The retired v0.2 partition is historical rejection evidence, not active authority.

Human Rulings prose, atoms, and candidate records remain prohibited from the Authorial Grammar provider prompt. This is a post-extraction conformance review: record conflicts, omissions, and status mismatches and return defects to calibration. It does not perform Layer E semantic acceptance or cross-source reconciliation.

## Machine state sequence

`source_selected → identity_card_draft → identity_card_reviewed → identity_card_approved → offline_dry_run → pilot_frozen → pilot_call_authorized → pilot_response_captured → pilot_rejected ↺ offline_dry_run`

or, after a perfect-for-release pilot:

`pilot_response_captured → pilot_accepted → source_run_authorized → source_run_in_progress → source_run_halted ↺ offline_dry_run`

or, after clean staged execution:

`source_run_in_progress → source_candidate_complete → source_extraction_candidate_accepted`

Direct transitions that skip identity approval, calibration, author release, stoppable execution, or whole-document review are prohibited.

## Disposition-specific paths

- `retain_companion_no_atomic_compile_extraction`: never enters atomization.
- `deterministic_publication_control_parse` with `model_extraction: prohibited`: uses deterministic fixtures, validation, and whole-artifact review only; every provider state is prohibited.
- deferred, optional, manifestation, and post-reconciliation dispositions remain blocked until their Gate 2 timing or author-selection condition is satisfied.
- multi-stream or partitioning dispositions preserve record-level stream routing; they are never flattened into one game-semantic stream.

## Current boundary

This protocol provisions future work but does not itself authorize source selection, identity-card writes, offline atomization writes, provider calls, or spending. Compile B remains read-only until the author accepts its amended cold-start report and explicitly transfers repository write authority. After transfer, the next controlled source is Authorial Grammar, beginning with its identity card—not a provider call.
