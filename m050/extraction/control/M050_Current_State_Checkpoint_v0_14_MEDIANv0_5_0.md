# MEDIAN v0.5.0 Current-State Checkpoint v0.14

State: `AUTHORIAL_GRAMMAR_TARGET_COVERAGE_C0003_PILOT_FROZEN` (2026-08-03)

Corpus vector remains **24 / 22 / 4 / 18 = 14 + 4**; Authorial Grammar is
next. C0001/C0002 remain accepted. The latest C0003 pilot is rejected, and no
whole-source candidate exists.

The pure-label pilot correctly returned Markdown table structure and all three
pure labels as `no_substantive_claim`, but omitted substantive example-list
targets B00085 and B00121. It stopped normally at 3,629 output tokens, created
2,523 one-hour cache tokens, and cost $0.056146. The one-call authorization is
consumed; no retry or later chunk is authorized.

Offline recalibration now requires the returned disposition IDs to match every
target ID exactly. Example bodies, code fences, lists, quotations, and table
rows remain independently disposition-required even when governed by a pure
label. This is generic and does not name the failed blocks in the prompt.

The 20-target quantization and 13-chunk plan remain unchanged because C0003 had
only 19 targets and did not approach the output limit. C0001/C0002 pass replay;
captured C0003 fails exactly the two missing-target coverage checks. All 13
chunks fake-validate; 122 tests pass.

C0003 is frozen as the representative target-coverage pilot with a $0.12354
cache-miss ceiling. A new exact one-call authorization under $0.13 is required.
Spend is $0.475963 cumulative with $1.524037 money-only remaining. No provider
call or later-stage authority is active.
