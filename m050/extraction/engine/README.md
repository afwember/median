# MEDIAN extraction engine

This is the offline-first, source-agnostic engine used by the MEDIAN v0.5.0
compile. Source differences belong in the bound identity card, block manifest,
disposition ledger, chunk plan, prompt, schema, and configuration—not in
source-specific worker code.

Identity approval is recorded on the card itself and in Git history. The active
configuration binds the approved card by hash; no parallel identity-transition
receipt is required.

## Runtime

- macOS arm64
- CPython 3.12
- repository-local `.venv`

Install and verify from the repository root:

```sh
m050/tools/m050_bootstrap_gate5.sh
```

The focused suite covers corpus order, source isolation, parsing, semantic-group
chunking, exact target coverage, table and pure-label handling, caching, spend
budgets, provider capture, validation, sequential review, and a zero-call
parse-and-plan compatibility sweep across all 22 compile-scope sources.

## Extraction machine

The active controller is `m050/tools/m050_extraction_machine_v0_1.py`. Its
normal commands are:

- `scaffold`: zero-call preparation for an approved new source;
- `replan`: complete-source re-apportionment at a calibrated target density;
- `prepare`: build one hash-bound call packet;
- `preflight`: derive provider readiness from canonical source work, offline
  gates, cumulative budget, cache, and prior review;
- `send`: make one ready call and preserve raw response, compact outcome, exact
  cost, and ledger evidence; and
- `review`: record the required substantive result before another call.

Only the current pilot packet is stored ahead of use. Later packets are
generated just in time from the active configuration and chunk plan.
Canonical state holds cumulative spend in place. The machine does not create
lifecycle receipts, per-call authorization records, or successor spend files.

The engine does not contain legacy migration, repair, replay, semantic-review
planning, mapping, or reconciliation commands. Those retired implementations
are preserved in the external CoS cleanup archive and may not be restored into
the active compile without a separate process-design decision.
