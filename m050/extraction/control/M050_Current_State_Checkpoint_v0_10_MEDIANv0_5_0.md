# MEDIAN v0.5.0 Current-State Checkpoint v0.10

Date: 2026-08-03

State: `AUTHORIAL_GRAMMAR_STRUCTURAL_SOURCE_RUN_HALTED_C0003_LAYOUT_ATOM`

## Corpus and accepted evidence

- Corpus vector: **24 / 22 / 4 / 18 = 14 + 4**.
- Next outstanding source: Authorial Grammar.
- New-plan C0001 passed mechanical and substantive review during the run.
- New-plan C0002 remains the accepted structural pilot.
- C0003 is rejected; no whole-source candidate exists.

## Halt defect

The authorized remaining-source run completed C0001 successfully for an exact
$0.042259. C0003 then returned cleanly and passed mechanical validation, but
failed substantive review. For B00071, the structural table header
`Construction | Meaning | Example`, the provider emitted an atom claiming that
a table has those columns. That is layout metadata, not an Authorial Grammar
rule. It conflicts with the lean evidence policy and the correct
`no_substantive_claim` treatment of equivalent table headers.

The defect immediately halted and revoked the remaining release. C0004-C0013
were not called. No workaround, silent atom deletion, retry, or prompt/schema/
exclusion-policy modification is authorized.

Both source-run calls used the required cache. C0003 cost $0.055599. Total
source-run spend was $0.097858.

## Spend and authority

- Cumulative spend: $0.352455.
- Active money-only balance: $1.647545.
- The money envelope grants no lifecycle authority.

No provider call, retry, remaining-source execution, Google Sheets work,
semantic acceptance, mapping, reconciliation, or compiled prose is authorized.
The next possible activity is author review and explicit selection of a new
offline calibration path for the nonsemantic layout-metadata atom defect.
