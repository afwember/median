# MEDIAN v0.5.0 Extraction Gate 4 Completion Report

Date: 2026-08-02

Status: **PASSED**

External model calls during Gate 4: **0**

## Purpose

Gate 4 finishes the repository-gardening phase before extraction-system development resumes. Its purpose is to leave one frozen v0.5.0 corpus, one understandable set of active controls, a recoverable archive for superseded material, and deterministic checks that prevent accidental corpus or version drift.

This report records repository state. It does not approve an extraction implementation or a provider call.

## Frozen corpus

The v0.5.0 corpus is frozen in `M050_Frozen_Corpus_Manifest_v0_1_MEDIANv0_5_0.json` at the repository snapshot identified by commit `b171b179e1bf2540880e9fc562400836e3f2be79`.

- 24 registered Markdown sources are frozen by exact path and SHA-256.
- 9 source-linked media assets are frozen by exact path and SHA-256.
- The resulting frozen source inventory is 33 files.
- All 24 registered-source path, source-ID, and hash triplets agree with the accepted Gate 2 source disposition.
- Source addition, modification, deletion, or replacement is prohibited for v0.5.0.
- New design material belongs under `m051/`; it is not input to v0.5.0 processing.

## Preserved extraction evidence

The three reusable accepted extraction sets remain immutable evidence:

- Crossing: acceptance report and accepted candidate
- MSID Grammar: acceptance report and accepted candidate
- Governing Philosophy and Architecture: acceptance report and accepted candidate

All six files match the exact hashes in the frozen manifest. The fourth completed legacy run remains archived pending the deterministic reconstruction required by the Gate 3 reuse disposition. Gate 4 neither promotes nor discards it.

## Repository cleanup

The cleanup was archival and recoverable.

- Noncurrent operations controls, prompts, schemas, migration scripts, and runbooks were moved out of the active operations tree under the dated Gate 4 archive.
- Only the provider-neutral cost CSV remains live under `m050/docs/operations/`; the human-readable cost ledger and two trackers remain under `m050/extraction/progress/`.
- Thirteen spreadsheet-generation intermediates and redundant previews were retired from the repository-root output area into the Gate 4 archive.
- Fourteen misleadingly named historical originals outside the v0.5.0 source tree were moved, with their origin structure preserved, into the source-identity-migration archive.
- Fifty-one generated Python and test-cache files were excluded from the sealed archive because Git intentionally ignores them and they are neither evidence nor reproducible repository content.
- A repository-wide filename scan of all non-archive paths found zero filenames matching the retired identity-pattern set. Historical wording inside frozen sources and immutable quotations was preserved rather than falsified.
- The archive was not rewritten or discarded. Its complete snapshot is bound by file count, byte count, and ordered path-and-hash digest.

## Active controls

The active control surface is intentionally small:

1. frozen corpus manifest;
2. repository write-authority and freeze policy;
3. Gate 2 content-derived source disposition;
4. Gate 2 target process and error-correction design;
5. Gate 3 legacy-extraction reuse disposition;
6. this Gate 4 completion report and its machine-readable receipt;
7. the deterministic `m050_guard.py` integrity guard;
8. the two progress workbooks and the provider-neutral cost records.

Everything under `m050/archive/`, and every prior prompt, worker, registry, runbook, or conversational bootstrap packet found there, is historical evidence only. None is executable authority.

## Authority and change discipline

Asa Wember remains the root of design authority. Codex is the repository operator under explicit author direction. Only one explicitly authorized Codex task may write the repository at a time. Any handoff must begin from repository state and active controls, not conversational memory.

The v0.5.0 design corpus is frozen. A request to alter that corpus requires an explicit freeze exception recorded before the change; ordinary extraction work does not carry that authority.

## Verification results

The deterministic guard passed all current checks:

- frozen source inventory and hashes;
- Gate 2 registered-source agreement;
- accepted-evidence hashes;
- complete, Git-reproducible archive snapshot;
- prohibition on m051 input to m050 processing.

The progress workbook was updated and visually verified. It now reports four completed gates, zero gates in progress, and Gate 5 not begun.

## Gate decision

**Gate 4 passes.** Repository gardening is complete for the recovered process.

The next permitted activity is deliberation and specification of Gate 5: the simpler source-bounded extraction implementation and its offline verification. No runner implementation, corpus extraction, paid calibration, batch submission, or provider call is authorized by this report.
