# MEDIAN v0.5.0 Gate 5 Layer E Legacy Migration Report

Date: 2026-08-03

Result: **PASS — 913 mechanically valid migration candidates; zero accepted evidence**

## 1. Scope and boundary

This slice migrated the reusable mechanical assets of all four immutable legacy
candidate sets into a new Layer E candidate surface. It did not accept their
semantics. Every candidate preserves its legacy ID, exact quotation, quotation
hash, source location, approved identity card, replay result, effective block
coordinates, repair lineage, risk tier, and pending-review state.

Legacy classifications, MSID assignments, status labels, authority claims,
relations, and notes remain quarantined as explicitly labeled legacy proposals.
The three Gate 3 `do_not_import` fields are represented only by field name and
payload hash. No legacy semantic field became an accepted Layer E field.

## 2. Candidate coverage

| Source | Legacy records | Migration candidates | Tier 1 | Tier 2 | Tier 3 |
|---|---:|---:|---:|---:|---:|
| Crossing | 121 | 121 | 9 | 75 | 37 |
| Governing Philosophy and Architecture | 346 | 346 | 0 | 346 | 0 |
| Human Rulings | 173 | 173 | 2 | 171 | 0 |
| MSID Grammar | 273 | 273 | 7 | 266 | 0 |
| **Total** | **913** | **913** | **18** | **858** | **37** |

All 913 legacy IDs are unique and accounted once. All 913 candidates are in
`mechanically_valid`, `not_accepted`, and `pending` state. Claim normalization,
controlled claim kind, stream assignment, acceptance receipt, mapping, and
reconciliation remain unset. The 24 repaired replay records retain their exact
repair-disposition lineage; the six Human Rulings records grounded only in the
pre-reference-rewrite source retain that source hash plus active rewrite-block
coordinates.

## 3. Compound-review accounting

Gate 3's historical indicator was reproduced exactly as a period followed by
whitespace and an uppercase sentence start. It yields the recorded 123-source
queue without inference:

| Source | Gate 3 multi-sentence flags | Cross-block structural compounds | Unified unique records |
|---|---:|---:|---:|
| Crossing | 2 | 2 | 4 |
| Governing Philosophy and Architecture | 69 | 4 | 73 |
| Human Rulings | 21 | 2 | 22 |
| MSID Grammar | 31 | 9 | 40 |
| **Total** | **123** | **17** | **139** |

One Human Rulings record belongs to both queues, so the unified review inventory
contains 139 unique records. This preserves both the earlier 123-record
multi-sentence queue and every later cross-block structural compound without
pretending that one historical count included the other. No record was split.

## 4. Retrospective block and exclusion coverage

Four append-only ledgers give exactly one terminal migration disposition to all
2,464 source blocks:

| Terminal disposition | Blocks |
|---|---:|
| Legacy migration candidate support | 719 |
| Review required: legacy candidate in locally flagged block | 61 |
| Review required: legacy candidate in non-normative identity region | 4 |
| Review required: eligible block has no legacy candidate | 518 |
| Context only | 200 |
| Structurally excluded | 830 |
| Excluded by explicit silent/process/change-record identity region | 132 |
| **Total** | **2,464** |

The 518 uncovered eligible blocks remain visible review work. Their presence
does not invalidate the 913-record migration, but it prevents the legacy
extractions from being called complete block coverage and must inform later
review bundles or fresh extraction planning.

## 5. Transition control

The permitted next evidence transition is only:

`mechanically_valid -> semantic_review_pending`

There is no direct deterministic path to `reviewed` or `accepted`. Tier 1 needs
an author decision before normative use; Tier 2 needs exhaustive independent
semantic review and coherent bundle approval; Tier 3 needs deterministic checks
plus risk-weighted sampling. Every acceptance requires a review receipt.

Mapping, reconciliation, and compilation remain unauthorized and unstarted.
The transition control is machine-readable and hash-binds the candidate set,
migration report, and unified compound-review inventory.

## 6. Verification and cost

- 913 of 913 legacy records migrated once;
- 24 of 24 repair-lineage records preserved;
- 2,464 of 2,464 source blocks terminally dispositioned;
- 123 Gate 3 multi-sentence flags reproduced exactly;
- 17 of 17 cross-block structural compounds included;
- 139 unique compound-review records;
- zero accepted evidence records;
- zero semantic reviews, mappings, reconciliations, or compilations;
- zero provider calls and $0.00 accounted cost;
- zero Google Sheets interactions.

## 7. Next boundary

The next authorized slice is deterministic review-bundle design and
human-effort projection for the 18 Tier 1, 858 Tier 2, and 37 Tier 3
candidates, incorporating the 139-record compound queue and the 518 uncovered
eligible blocks. It may prepare review work; it may not perform semantic
acceptance, mapping, reconciliation, compilation, provider calls, or Google
Sheets interaction.
