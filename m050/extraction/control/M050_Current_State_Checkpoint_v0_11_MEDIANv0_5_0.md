# MEDIAN v0.5.0 Current-State Checkpoint v0.11

Date: 2026-08-03

State: `AUTHORIAL_GRAMMAR_LEAN_TABLE_C0003_PILOT_FROZEN`

The corpus vector remains **24 / 22 / 4 / 18 = 14 + 4**. Authorial
Grammar remains the next source. New-plan C0001 and C0002 remain accepted;
C0003 remains rejected and no whole-source candidate exists.

The approved offline recalibration is complete. The generic prompt now requires
every Markdown table header and delimiter row to return
`no_substantive_claim`, while substantive body rows remain eligible. The
mechanical validator independently enforces the same rule and fails closed.
This is not a B00071-only patch.

The 13-chunk structural plan and 20-target quantization are unchanged. All 13
chunks prepare and fake-validate. Offline replay preserves accepted C0001 and
C0002 under the new validator and rejects captured C0003 with exactly one table
structure error. The engine suite passes 121 tests.

C0003 is frozen as the representative lean-table pilot. It contains header
B00071, delimiter B00072, and substantive body row B00073. Its conservative
cache-miss ceiling is $0.122044, requiring a $0.13 one-call cap.

Cumulative spend remains $0.352455; the active money-only balance remains
$1.647545. No provider call, retry, remaining-source execution, Google Sheets
work, semantic acceptance, mapping, reconciliation, or compiled prose is
authorized. The next possible transition is an exact one-call C0003 pilot
authorization bound to the new configuration.
