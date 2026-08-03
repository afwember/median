# MEDIAN Next Action

Action date: 2026-08-03

Transition: mechanically valid Layer E legacy candidates to review-bundle design

## Preconditions

1. confirm the Layer E migration checkpoint is committed and pushed;
2. confirm local `HEAD` and `origin/main` are identical and the worktree is clean;
3. read Active Control Index v0.7, the migration report and receipt, and the
   machine-readable transition control;
4. verify exact coverage of 913 migration candidates, 24 repair-lineage
   records, 2,464 retrospectively dispositioned source blocks, and the unified
   139-record compound-review inventory;
5. preserve every legacy, replay, reconstruction, repair, and migration
   artifact byte-for-byte;
6. keep all follow-on work offline and source-preserving;
7. keep all Google Sheets interactions paused.

## Authorized transition

Design and build deterministic, hash-bound review preparation without accepting
candidate semantics:

1. create coherent review-bundle rules for 18 Tier 1, 858 Tier 2, and 37 Tier 3
   candidates, with candidate membership and hashes fixed before review;
2. preserve the complete 139-record compound queue, distinguishing the 123
   Gate 3 multi-sentence flags, 17 cross-block structural compounds, and their
   one-record overlap;
3. route Tier 1 candidates to author-decision preparation, Tier 2 candidates to
   exhaustive independent semantic review, and Tier 3 candidates to the fixed
   risk-weighted sampling design;
4. incorporate the 518 eligible source blocks with no legacy candidate as an
   explicit coverage-gap queue rather than declaring block completeness;
5. estimate human-review effort and define bundle stop conditions without
   sending any provider request;
6. keep every candidate at `mechanically_valid` until a separate transition
   receipt moves a fixed bundle to `semantic_review_pending`;
7. only after review-bundle controls pass, present the proposed review sequence
   and any fresh-source zero-call calibration plan for discussion.

## Stop conditions

Stop if review preparation would choose a substantive interpretation, accept a
candidate, hide an uncovered block, split a legacy compound, weaken an identity
boundary, promote a legacy semantic label, or change a pinned bundle after
review begins. Also stop before provider calls, positive-cost work orders,
production mapping, reconciliation, compilation, or Google Sheets interaction.
