# MEDIAN v0.5.0 Current-State Checkpoint v0.5

Date: 2026-08-03

State: `AUTHORIAL_GRAMMAR_SOURCE_RUN_HALTED_REQUANTIZED_PILOT_FROZEN`

## Corpus and source

- Corpus vector: **24 / 22 / 4 / 18 = 14 + 4**.
- Next outstanding source: Authorial Grammar.
- Pilot 001-R6 remains accepted for its representative regimes.
- The first full-source C0001 attempt is rejected for output truncation and the five-call source release is revoked.

## Defect and spend

Anthropic returned HTTP 200 with `stop_reason: max_tokens` after 6,000 output
tokens. The response completed 23 dispositions before truncation. The attempt
cost exactly $0.081618 (display $0.09). Cache creation telemetry was present.
The successor spend envelope is inactive with $1.918382 remaining from the
original cumulative $2.00 authority.

## Complete-source requantization

Accepted R6 completed 27 dispositions at 5,665 output tokens. The failed C0001
completed 23 before exhausting 6,000. The calibrated source quantization is
therefore 20 provider-eligible target blocks per chunk. The generic `replan`
workflow re-apportioned all 590 source blocks and 228 target blocks, preserving
source order, tables, and heading context. Chunk count was not supplied or
preserved; the generated result is 12 chunks with target counts
`20 × 10, 17, 11`.

All 12 chunks prepare and fake-validate offline. Their conservative cache-miss
ceilings sum to $1.377152, below the reconciled remaining balance. The engine
suite passes 116 tests.

## Authority boundary

The quantized C0001 pilot is frozen offline but not authorized. No provider
call, spend-envelope reactivation, full-source release, Google Sheets work,
semantic acceptance, mapping, reconciliation, or compiled prose is authorized.
The next possible transition is an exact one-call C0001 pilot authorization
under an $0.11 cap plus explicit reactivation of the reconciled remaining
$1.918382 envelope.
