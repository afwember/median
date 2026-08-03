# MEDIAN v0.5.0 Current-State Checkpoint v0.13

State: `AUTHORIAL_GRAMMAR_PURE_LABEL_C0003_PILOT_FROZEN` (2026-08-03)

Corpus vector remains **24 / 22 / 4 / 18 = 14 + 4**; Authorial Grammar is
next. C0001/C0002 remain accepted, C0003 rejected, and no whole-source
candidate exists.

Offline recalibration identified 14 pure structural labels matching
`Example(s):`, `Prefer:`, `Preferred:`, `Avoid:`, `Not:`, `Correct:`, or
`Incorrect:`. Bound payloads now mark them as requiring
`no_substantive_claim`; the validator fails closed. Substantive sentences that
end in a colon remain eligible. The 13-chunk plan is unchanged.

C0001/C0002 pass replay under newly built packets. Captured C0003 fails exactly
two required-disposition checks at B00101/B00105. All 13 chunks fake-validate;
122 tests pass.

C0003 is frozen as the representative pilot with three marked labels and a
$0.120852 cache-miss ceiling. A $0.13 exact one-call authorization is required.
Spend remains $0.419817 cumulative with $1.580183 money-only remaining. No
provider call or later-stage authority is active.
