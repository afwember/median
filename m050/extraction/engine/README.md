# MEDIAN Gate 5 engine

This directory contains the offline-first, source-independent processing foundation for MEDIAN v0.5.0.

The frozen corpus and existing accepted artifacts are outside this directory and remain immutable. Archived runners are historical evidence only; this package does not import them.

## Runtime

- macOS arm64
- CPython 3.12
- repository-local `.venv`

From the repository root, the intended setup is:

```sh
/opt/anaconda3/bin/python3.12 -m venv .venv
.venv/bin/python -m pip install --require-hashes -r m050/extraction/engine/requirements.lock
.venv/bin/python -m pip install --no-build-isolation --no-deps -e m050/extraction/engine
.venv/bin/python -m pytest m050/extraction/engine/tests
```

The lock file is authoritative for the local environment. Provider SDKs are deliberately absent from the offline-core lock and require separate, author-approved installation before a provider adapter can be used.

## Safety boundary

Running the package without a provider extra must never import a provider SDK, read API credentials, or access the network. A provider response can be captured and replayed, but a positive-cost work order and explicit author authorization are required before any future send operation.

## Deterministic legacy replay

`replay-legacy` reads one approved identity card and its bound immutable legacy
candidate, acceptance report, sources, and block manifest. It writes an
append-only record ledger and content-addressed report. Replay classifies
single-block grounding, line-location disambiguation, cross-block compounds,
legacy-source-only Human Rulings quotations, ambiguity, and grounding failures.
It never edits or promotes a legacy record.

```sh
.venv/bin/python -m median_gate5.cli replay-legacy \
  --repo-root . \
  --card APPROVED_CARD.json \
  --block-manifest BOUND_BLOCK_MANIFEST.json \
  --output-ledger NEW_REPLAY_LEDGER.jsonl \
  --output-report NEW_REPLAY_REPORT.json
```

## Deterministic Layer E legacy migration

`migrate-legacy-layer-e` consumes the passed mechanical-repair closure and
produces 913 content-addressed Layer E migration candidates, four retrospective
block/exclusion ledgers, and one unified compound-review inventory. Candidates
stop at `mechanically_valid`: legacy semantic fields remain labeled legacy
proposals, while claim normalization, stream assignment, mapping,
reconciliation, semantic review, and acceptance remain unset.

The review inventory preserves both the 123 Gate 3 multi-sentence flags and
all 17 later cross-block structural compounds. One record overlaps, yielding
139 unique review records without changing either source queue.

## Deterministic legacy semantic-review planning

`plan-legacy-semantic-review` consumes the completed Layer E migration receipt
and creates section-coherent review bundles, uncovered-block coverage bundles,
and one append-only state-transition receipt per candidate. It moves queue
state only from `mechanically_valid` to `semantic_review_pending`; it performs
no semantic review or acceptance.

The planner preserves all 913 candidates and 139 compound-review records,
queues all 518 eligible blocks lacking a legacy candidate, pins the Tier 3
sample seed and membership, and produces lower, expected, and upper
human-effort projections. Bundle limits are deterministic: at most 12 members
and 12,000 source-text characters.

```sh
.venv/bin/python -m median_gate5.cli plan-legacy-semantic-review \
  --repo-root . \
  --migration-receipt MIGRATION_RECEIPT.json \
  --effective-date YYYY-MM-DD \
  --tier3-seed PINNED_SEED \
  --output-candidate-bundles NEW_CANDIDATE_BUNDLES.jsonl \
  --output-coverage-bundles NEW_COVERAGE_BUNDLES.jsonl \
  --output-transitions NEW_TRANSITIONS.jsonl \
  --output-report NEW_REPORT.json
```
