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
