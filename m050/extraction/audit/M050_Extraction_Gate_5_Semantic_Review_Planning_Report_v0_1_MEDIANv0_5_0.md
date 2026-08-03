# MEDIAN v0.5.0 Gate 5 Semantic Review Planning Report

Date: 2026-08-03

Result: **PASS — the complete migrated Layer E candidate surface is queued for controlled review**

## 1. Compile meaning and boundary

For MEDIAN operations, **the compile** means the entire controlled process from
source preparation through evidence review, mapping, reconciliation, and final
document production. This increment advances that process without skipping its
internal state boundaries.

The increment performs deterministic review planning only. It does not make a
semantic decision, accept evidence, map an MSID, reconcile a subject, or create
compiled prose.

## 2. Candidate review bundles

All 913 mechanically valid legacy migration candidates now have exactly one
hash-bound review bundle and one append-only transition receipt from
`mechanically_valid` to `semantic_review_pending`.

| Tier | Candidates | Bundles | Required treatment |
|---|---:|---:|---|
| Tier 1 | 18 | 5 | Author decision before normative use |
| Tier 2 | 858 | 164 | Exhaustive independent semantic review |
| Tier 3 | 37 | 12 | Deterministic checks plus pinned risk-weighted sampling |
| **Total** | **913** | **181** | |

Each candidate bundle is section-coherent, limited to at most 12 candidate
records and 12,000 quotation characters, and contains the exact quotation,
effective block context, legacy proposal fields as non-authoritative review
context, risk signals, repair lineage, and compound-review lineage.

The 139-record unified compound inventory is preserved in full. No compound
record was split or modified.

## 3. Tier 3 sampling

The Tier 3 sample uses the frozen seed
`M050-GATE5-LEGACY-TIER3-SAMPLE-2026-08-03` and the approved five-percent rule
with a minimum of three bundles. Three of the 12 Tier 3 bundles were selected,
covering 16 of the 37 Tier 3 candidates. The selection includes the highest
context-density bundle, the highest review-risk bundle, and deterministic
seed-ranked membership.

No sampled bundle has yet been reviewed or accepted.

## 4. Uncovered-block review

The four retrospective block ledgers contain 518 eligible source blocks with no
legacy migration candidate. All 518 are preserved in 132 section-coherent,
hash-bound coverage bundles. Each bundle retains exact block text and hashes and
requires an explicit later decision between fresh extraction and a justified
non-claim disposition.

This queue prevents the legacy candidate surface from being mistaken for
complete source coverage.

## 5. Human-effort projection

The projection is a manual-review baseline, not elapsed machine time and not a
commitment to a paid service.

| Scenario | Minutes | Human time |
|---|---:|---:|
| Lower | 3,407 | 56 h 47 m |
| Expected | 5,600 | 93 h 20 m |
| Upper | 9,646 | 160 h 46 m |

The expected estimate consists of:

- 169 minutes for the five Tier 1 author bundles;
- 3,394 minutes for exhaustive Tier 2 review;
- 278 minutes of additional compound-record complexity;
- 63 minutes for the initial Tier 3 sample;
- 1,696 minutes for the 518 uncovered blocks.

These figures expose the workload rather than silently converting it into
unreviewed automation. Codex can prepare and perform much of the independent
review work, but author decisions remain author decisions and every acceptance
still requires its proper receipt.

## 6. Verification and cost

- 913 of 913 candidates assigned once;
- 913 state-transition receipts;
- 139 of 139 compound-review records preserved;
- 518 of 518 uncovered eligible blocks bundled;
- zero semantic reviews performed;
- zero author decisions inferred;
- zero accepted evidence records;
- zero mapping, reconciliation, or compilation records;
- zero provider calls and $0.00 accounted cost;
- zero Google Sheets interactions.

## 7. Next boundary

The next compile increment may execute the review queues: prepare the five Tier
1 bundles for author decision, begin independent Tier 2 semantic review, and run
the pinned Tier 3 sample. It may also disposition uncovered blocks through
review. It may not accept evidence without the required review receipt or begin
mapping, reconciliation, or compiled prose while Layer E acceptance remains
incomplete.
