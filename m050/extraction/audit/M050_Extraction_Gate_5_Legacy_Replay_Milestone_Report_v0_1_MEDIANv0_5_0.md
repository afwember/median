# MEDIAN v0.5.0 Gate 5 Legacy Replay Milestone Report

Date: 2026-08-03

Status: deterministic replay passed; bounded repair queue required before
Layer E migration

## Outcome

All 913 immutable legacy candidate records were replayed against the four
approved source identity cards and their exact bound sources and block
manifests. Every quotation remained grounded in either the active frozen source
or, for six known Human Rulings reference-rewrite cases, the exact legacy
extraction source. There were zero hidden quotation failures.

The engine built every ledger and report twice from the same pinned inputs. All
four repeated ledgers and all four repeated reports were byte-identical. No
provider SDK was imported, no provider call occurred, and accounted cost was
$0.00.

Replay passing does not mean that every record is ready for migration. The
engine deliberately exposed 24 records that require explicit repair or review:

- 17 exact quotations span more than one structural block and therefore cannot
  be silently assigned to one block or mechanically split;
- six Human Rulings quotations exist exactly in the pre-reference-rewrite
  extraction source but not verbatim in the active frozen ledger;
- one short MSID quotation remains ambiguous after its recorded line location
  is applied.

The remaining 889 records have one deterministic active-source block binding.
They have not yet been promoted or rewritten as Layer E candidates.

## Source results

| Source | Records | Single-block eligible | Repair queue | Grounding failures |
| --- | ---: | ---: | ---: | ---: |
| Crossing | 121 | 119 | 2 | 0 |
| Governing Philosophy and Architecture | 346 | 342 | 4 | 0 |
| Human Rulings | 173 | 165 | 8 | 0 |
| MSID Grammar | 273 | 263 | 10 | 0 |
| **Total** | **913** | **889** | **24** | **0** |

## Control behavior proved

The replay command fails closed on changed input hashes, unapproved identity
cards, substituted block manifests, duplicate or malformed legacy record IDs,
source-ID drift, record-count drift, source-location-count drift, and quotations
that cannot be grounded. It records repeated-quotation disambiguation,
cross-block membership, legacy-source-only grounding, safe normalization events,
and every non-eligible migration disposition.

The source candidates, acceptance reports, source files, identity cards, and
block manifests were read only. The replay outputs are append-only JSONL ledgers
and content-addressed JSON reports.

## Next boundary

Layer E migration remains unstarted. The next safe slice is to resolve the
24-record replay repair queue, beginning with the already-required Human Rulings
section and labeled-field reconstruction. Cross-block records must be reviewed
as compounds, and the ambiguous MSID occurrence must receive an explicit
location disposition. Replay should then be repeated before any record is
promoted.

No provider request, positive-cost work order, production mapping,
reconciliation, or compilation is authorized by this milestone.
