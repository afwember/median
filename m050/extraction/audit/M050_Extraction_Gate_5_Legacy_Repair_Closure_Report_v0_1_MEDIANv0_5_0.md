# MEDIAN v0.5.0 Gate 5 Legacy Repair Closure Report

Date: 2026-08-03

Status: **PASS — mechanical replay repair overlay complete; semantic review and Layer E migration have not begun**

## Result

Every record in the original 24-record replay repair queue now has an explicit,
source-preserving mechanical disposition:

- six Human Rulings records use the deterministic Gate 4 reference-rewrite map;
- 17 cross-block records are preserved as single indivisible legacy compounds;
- one repeated MSID quotation is pinned to its unique exact whole-line match;
- zero records remain without a grounding or coordinate disposition; and
- zero legacy, replay, or frozen-source records were modified or split.

The raw replay ledgers and reports intentionally remain unchanged. Rebuilding
all four replays from the approved cards, frozen sources, block manifests, and
legacy candidates produced four byte-identical ledgers and four byte-identical
reports covering all 913 records.

## Cross-block compound disposition

All 17 quotations are exact contiguous source spans over consecutive,
homogeneous, locally eligible blocks under one heading and status context.
Their distribution is:

| Source | Records |
| --- | ---: |
| Crossing | 2 |
| Governing Philosophy and Architecture | 4 |
| Human Rulings | 2 |
| MSID Grammar | 9 |

The boundary repair preserves each legacy record as one compound. It does not
approve the compound's semantics or split it into new claims. All 17 remain
Tier 2 and require exhaustive independent semantic review in coherent bundles.

## MSID occurrence resolution

`ATOM-MSID-DIRECT-0062` quotes `Away.Crossing`. The active MSID Grammar contains
38 exact substring occurrences. Its pinned location, lines 287–290, contains
two: one whole-line `Away.Crossing` at line 288 and one prefix inside
`Away.Crossing.Phase.Planning` at line 289. The exact-whole-line rule selects
line 288 uniquely and binds it to block
`M050-SRC-MSID-GRAMMAR-001__B00188_917d0db52d06`.

The general replay matcher was not weakened or changed. The record remains
Tier 2 ontology evidence pending independent semantic review.

## Immutable outputs

| Artifact | SHA-256 |
| --- | --- |
| Compound disposition ledger | `3d7202cac57dcbbbeb8b07168a8da6697a787f6adf124c3704bc9b056365adea` |
| Compound disposition report | `14a83732aeb5ee5b5212711f53f62492edb178bf39e5dad8cf0c0f51618bd035` |
| Ambiguous occurrence resolution | `5ca389ae46f057a7e61e9460995bb660ef059984b1773eccc6e24749a14ff6f2` |
| Repair closure report | `1075c71dd2c309e5a51a52f6cdc02119386e8d34a8992fb9e90d1bc6a4ce8078` |

## Boundary and cost

- Provider calls: **0**
- Accounted cost: **$0.00**
- Google Sheets interactions: **0**
- Semantic acceptances: **0**
- Layer E migration: **not started**
- Production mapping, reconciliation, and compilation: **not started**

## Next authorized transition

Design and build the deterministic Layer E migration candidate format and
transition rules. A candidate must retain its legacy ID, exact quotation and
coordinates, approved identity boundary, repair disposition, risk tier, and
review state. Mechanical migration must never convert a legacy semantic label
into accepted evidence or bypass Tier 1/Tier 2 review. Retrospective block and
exclusion ledgers and the full 123-record compound-review inventory remain
required before Gate 5 can close.
