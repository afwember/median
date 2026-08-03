# MEDIAN Next Action

Action date: 2026-08-03

Transition: mechanically closed replay repair overlay to Layer E migration candidates

## Preconditions

1. confirm the legacy repair closure checkpoint is committed and pushed;
2. confirm local `HEAD` and `origin/main` are identical and the worktree is clean;
3. read the repair closure report and receipt and active control index v0.6;
4. verify exact coverage of all 24 raw replay-queue records and byte-identical
   regeneration of all four replay ledgers and reports;
5. preserve all 913 legacy inputs, replay artifacts, reconstruction artifacts,
   and repair dispositions byte-for-byte;
6. keep all follow-on work offline and source-preserving;
7. keep all Google Sheets interactions paused.

## Authorized transition

Design and build deterministic Layer E migration candidates without accepting
their semantics:

1. specify the Layer E candidate schema and lifecycle transition from immutable
   legacy record to mechanically validated migration candidate;
2. retain each legacy ID, source hash, exact quotation hash and coordinates,
   approved identity boundary, replay result, repair disposition, risk tier,
   and review state;
3. remove extraction-time authority, canonicality, status, mapping, and MSID
   conclusions from the accepted-evidence surface while retaining them only as
   clearly labeled legacy claims when provenance requires;
4. keep all Tier 1 and Tier 2 material pending its required review and prevent
   deterministic code from moving any candidate to accepted;
5. build retrospective block and exclusion ledgers for all four legacy sources;
6. construct the full 123-record likely-compound review inventory, including
   the 17 cross-block compounds already mechanically dispositioned;
7. generate migration coverage and risk reports proving that every legacy
   record has one explicit state and no evidence is orphaned;
8. only after those controls pass, prepare coherent review bundles and the
   fresh-source zero-call calibration plan.

## Stop conditions

Stop if migration would invent or rewrite source text, split a legacy compound,
promote a legacy semantic label into accepted evidence, choose a substantive
interpretation, bypass Tier 1/Tier 2 review, weaken an approved identity
boundary, or leave a legacy record unaccounted for. Also stop before any
provider request, positive-cost work order, production mapping, reconciliation,
compilation, or semantic acceptance. Those require later evidence review and,
where specified, explicit author authorization.
