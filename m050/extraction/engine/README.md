# MEDIAN extraction engine

This is the offline-first, source-agnostic engine used by the MEDIAN v0.5.0
compile. Source differences belong in the bound identity card, block manifest,
disposition ledger, chunk plan, prompt, schema, and configuration—not in
source-specific worker code.

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
envelopes, provider capture, validation, and sequential review.

## Extraction machine

The active controller is `m050/tools/m050_extraction_machine_v0_1.py`. Its
normal commands are:

- `scaffold`: zero-call preparation for an approved new source;
- `replan`: complete-source re-apportionment at a calibrated target density;
- `prepare`: build one hash-bound call packet;
- `preflight`: enforce source, lifecycle, spend, cache, and prior-review gates;
- `send`: make one authorized call and preserve raw response, outcome, spend,
  and ledger evidence; and
- `review`: record the required substantive result before another call.

Only the current pilot packet is stored ahead of use. Later packets are
generated just in time from the active configuration and chunk plan.

The engine does not contain legacy migration, repair, replay, semantic-review
planning, mapping, or reconciliation commands. Those retired implementations
are preserved in the external CoS cleanup archive and may not be restored into
the active compile without a separate process-design decision.
