# MEDIAN v0.5.0 Current-State Checkpoint v0.4

Date: 2026-08-03

State: `AUTHORIAL_GRAMMAR_PILOT_R6_ACCEPTED_EXTRACTION_MACHINE_OFFLINE_READY`

## Corpus and source

- Corpus vector: **24 / 22 / 4 / 18 = 14 + 4**.
- Next outstanding source: Authorial Grammar.
- Pilot 001-R6 is accepted as perfect-for-release for its representative regimes.
- Pilot acceptance does not release the remaining five-chunk source plan.
- Further provider calls: zero authorized.

## Reusable extraction machine

One source-agnostic controller now handles zero-call source scaffolding, packet
preparation, exact lifecycle/spend preflight, provider capture, generic
validation, and sequential review. Source behavior is declarative. Stable
Claude system/schema content uses explicit one-hour caching. Routine calls use
one packet, one raw response, one compact outcome, and one chained-ledger
append. A malformed or defective response consumes the call and halts safely.

The accepted Authorial R6 response replays through the generic validator with
zero errors. The same engine scaffolds and fake-validates a second Spec Doc
without source-specific worker code. The complete offline suite passes 115
tests. No provider call was used to build or verify the machine.

## Clean operating contract

Root `AGENTS.md` is the sole active contract. The temporary
`AGENTS.override.md` mechanism has been removed. Active index v0.13,
checkpoint v0.4, bootstrap v0.3, and guard v0.8 form the clean successor-thread
entrypoint. Earlier versions remain historical evidence, not current controls.

## Authority boundary

A successor thread begins read-only. Full-source Authorial Grammar execution
requires a separate source-run lifecycle receipt. A cumulative $2.00 spend
envelope, if separately authorized, grants money authority only. Google Sheets,
Layer E semantic acceptance, mapping, reconciliation, and compiled prose remain
prohibited.
