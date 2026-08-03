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

## Source-agnostic extraction machine

The provider-eligible controller is `m050/tools/m050_extraction_machine_v0_1.py`. Source behavior is supplied by a hash-bound JSON configuration; the controller contains no Authorial Grammar, Home, or other source-specific extraction policy.

Its normal sequence is:

```sh
.venv/bin/python m050/tools/m050_extraction_machine_v0_1.py scaffold \
  --repo-root . --source-id SOURCE_ID --source-path SOURCE.md \
  --identity-card APPROVED_CARD --identity-approval-receipt APPROVAL.json \
  --allowed-stream STREAM --output-block-manifest NEW_MANIFEST.json \
  --output-disposition-ledger NEW_DISPOSITIONS.jsonl \
  --output-chunk-plan NEW_PLAN.json --output-prompt NEW_PROMPT.md \
  --output-response-schema NEW_SCHEMA.json --output-config NEW_CONFIG.json

.venv/bin/python m050/tools/m050_extraction_machine_v0_1.py prepare \
  --repo-root . --config SOURCE_CONFIG.json --chunk C0001 --output CALL_PACKET.json

.venv/bin/python m050/tools/m050_extraction_machine_v0_1.py preflight \
  --packet CALL_PACKET.json --spend-envelope SPEND.json \
  --lifecycle-receipt RELEASE.json --run-ledger RUN.jsonl

.venv/bin/python m050/tools/m050_extraction_machine_v0_1.py send \
  --packet CALL_PACKET.json --expected-packet-sha256 FILE_SHA256 \
  --spend-envelope SPEND.json --successor-spend-envelope SPEND_NEXT.json \
  --lifecycle-receipt RELEASE.json --run-ledger RUN.jsonl \
  --api-key-file KEY_FILE --raw-response RAW.json --outcome OUTCOME.json

.venv/bin/python m050/tools/m050_extraction_machine_v0_1.py review \
  --run-ledger RUN.jsonl --outcome OUTCOME.json --result passed \
  --reviewer REVIEWER --reason REVIEW_FINDING
```

`scaffold` is a zero-provider-call onboarding step. It requires an exactly
approved content/provenance identity card and produces conservative draft
dispositions, a heading- and table-aware chunk plan, a source-bound prompt and
schema, and a provider-disabled configuration. Those drafts still require
source review and bounded pilot calibration; scaffolding never authorizes a
pilot or full-source run.

`send` is fail-closed: exact lifecycle bindings and a cumulative money-only envelope are both required; the cache-write ceiling must fit; the raw response and compact outcome are preserved; and another call is blocked until the outcome receives a passing substantive review. Explicit one-hour Claude caching must produce cache creation or cache-read telemetry on the first live call.

The two independent authorization inputs have deliberately small shapes. They
must be created only from Asa Wember's explicit authorization; these examples
describe the machine contract but grant nothing:

```json
{
  "state": "source_run_authorized",
  "authority": "Asa Wember",
  "provider_call_limit": 5,
  "authorized_chunk_ids": ["C0001", "C0002", "C0003", "C0004", "C0005"],
  "execution_cadence": "sequential_one_call_review",
  "revoked": false,
  "binding": {
    "source_id": "SOURCE_ID",
    "configuration_sha256": "CONFIG_SHA256",
    "model": "claude-sonnet-5",
    "reasoning_effort": "low",
    "cache_ttl": "1h"
  }
}
```

```json
{
  "authority": "Asa Wember",
  "scope": "provider_spend_only",
  "active": true,
  "authorized_usd": "2.00",
  "spent_usd": "0.00"
}
```

The spend envelope contains no day, shift, or timer. The machine debits exact
usage into an append-only successor envelope and stops only when the next
conservative call ceiling will not fit, or when an independent decision/defect
gate stops it. A successful but malformed provider response consumes the call,
halts the run, and deactivates the successor envelope so it cannot be retried
without reconciliation.

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
