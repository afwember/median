# MEDIAN Continuity Control

This directory is the canonical, compact entry point for resuming MEDIAN work
after context compaction, a machine restart, or a task handoff. It records
operational truth and directs the reader to authoritative evidence; it is not a
replacement for Git history, Gate receipts, or the archived conversation.

## Read order

1. [`HANDOFF.md`](HANDOFF.md) — safe bootstrap and authority rules.
2. [`CURRENT_STATE.md`](CURRENT_STATE.md) — evidence-backed state at the latest
   checkpoint.
3. [`NEXT_ACTION.md`](NEXT_ACTION.md) — exact immediate transition and stop
   conditions.
4. [`DECISIONS.md`](DECISIONS.md) — durable author choices and working
   preferences.
5. [`OPERATIONS.md`](OPERATIONS.md) — checkpoint, reboot, recovery, and handoff
   procedures.

Then run the read-only host check:

```sh
./m050/tools/m050_verify_mac_mini.sh
```

Use `--deep` to add the Python dependency check and Gate 5 regression suite.

## Authority hierarchy

When records differ, apply this order:

1. the author's latest explicit instruction;
2. immutable source material and accepted evidence;
3. current Git artifacts, receipts, schemas, and executable tests;
4. these continuity records;
5. the Google Sheet remote presentation;
6. task summaries and historical transcripts.

Do not infer that a newer timestamp makes a lower-authority source controlling.
Resolve material disagreement before changing project state.

## Freshness rule

Update `CURRENT_STATE.md` and `NEXT_ACTION.md` before every planned shutdown,
risky environment change, or task handoff. Update `DECISIONS.md` only for a
durable author choice. Keep these files compact; link to evidence rather than
copying large reports.

The laptop transcript is retained outside Git at
`/Users/ambulatoryworld/Documents/Codex/median-support/MEDIAN_Codex_Thread_Export_2026-08-02.md`.
It is archive-only: search it for a specific ambiguity, never load it wholesale
as the normal bootstrap context, and promote any recovered durable fact into
the appropriate canonical record after verification.
