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
