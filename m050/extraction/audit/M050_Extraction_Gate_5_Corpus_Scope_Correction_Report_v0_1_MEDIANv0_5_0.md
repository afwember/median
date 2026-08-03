# MEDIAN v0.5.0 Gate 5 Corpus-Scope Correction Report

Date: 2026-08-03
Status: corrective control installed; compile execution remains paused

## Finding

The Gate 2 source disposition registers 24 documents. Two are deliberately retained as non-atomic companions, leaving 22 documents in the complete compile scope. Reusable legacy candidates exist for four of those 22 sources. Eighteen compile-scope sources therefore remain outstanding: 14 require work before grand reconciliation and four belong to later or conditional compile stages.

The v0.8 and v0.9 controls accurately preserved and planned review for the four-source legacy subset, but their wording allowed “Layer E migration complete” and “semantic review queued” to be read as global corpus status. That interpretation was incorrect. The 913 candidates, 181 review bundles, 139 compound records, and 518 uncovered-block records apply only to the four legacy-seed sources.

## Process-control failure

Three safeguards were missing:

1. no machine-derived 24-source progress vector was present in the active control;
2. the guard proved internal consistency of the legacy subset without proving whole-corpus coverage; and
3. the next authorized activity was selected from the latest partial milestone rather than reconciled against the terminal compile definition.

Task-context compaction can amplify recency bias, but it is not the controlling cause and is not an excuse. Durable repository controls must make the incorrect transition impossible even in a fresh task with no transcript history.

## Correction

- A generated matrix now derives every source state from Gate 2.
- The active control is superseded by v0.10 with the explicit vector `24 / 22 / 4 / 18 = 14 + 4`.
- The v0.9 review queues remain immutable and useful, but are reclassified as dormant partial-legacy planning.
- Guard v0.5 validates the whole-corpus boundary and prohibits review, acceptance, mapping, reconciliation, and compiled prose while the boundary is incomplete.
- Root `AGENTS.md`, a current-state checkpoint, and a new-task bootstrap provide a compact, testable cold start independent of transcript context.

No atomization, semantic review, provider call, Google Sheets interaction, acceptance, mapping, reconciliation, or prose compilation was performed by this corrective operation.
