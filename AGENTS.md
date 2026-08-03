# MEDIAN repository operating contract

This is the sole active root operating contract. If an `AGENTS.override.md` file
also exists, stop: the repository contract is ambiguous and must be repaired
before work continues. The repository, not a task transcript, is the durable
source of operational truth.

## Compile scope

- “The compile” means the complete controlled pipeline: evidence preparation and atomization, semantic review, mapping, reconciliation, and final document production.
- Gate 2 registers 24 sources. Two are non-atomic companions. The compile scope is 22 sources.
- Current state is 4 atomized legacy-seed sources and 18 outstanding compile-scope sources: 14 pre-reconciliation and 4 later or conditional.
- Never describe the four-source legacy migration or its review queues as whole-corpus completion.

## Required cold start

1. Confirm that root `AGENTS.override.md` is absent.
2. Read `m050/extraction/control/M050_Active_Control_Index_v0_23_MEDIANv0_5_0.json` completely.
3. Read `m050/extraction/control/M050_Current_State_Checkpoint_v0_13_MEDIANv0_5_0.md` completely.
4. Read `m050/extraction/control/M050_Compile_Source_Processing_Order_v0_1_MEDIANv0_5_0.json` completely.
5. Read `m050/extraction/control/M050_Source_Atomization_Pilot_Calibration_Protocol_v0_1_MEDIANv0_5_0.md` completely.
6. Read `m050/extraction/control/M050_Compile_Execution_Standard_v0_3_MEDIANv0_5_0.md` completely.
7. Read root `STATUS.md` completely and verify it is a derived mirror of the active index and checkpoint, not execution authority.
8. Run `.venv/bin/python m050/tools/m050_guard_v0_18.py --with-tests` before control/code checkpoints, provider-enabled configuration release, whole-source acceptance, and commit/push. Routine append-only provider capture uses the execution standard's focused preflight and validation.
9. Report the exact `24 / 22 / 4 / 18 = 14 + 4` corpus vector; the next source; the accepted-pilot boundary; the source-run and spend-envelope boundary; the required cadence and halt conditions; all prohibited later stages; the next authorized transition; whether `STATUS.md` is current; and whether local `HEAD` equals `origin/main`.

The paste-ready successor-thread audit is
`m050/extraction/control/M050_New_Task_Bootstrap_v0_13_MEDIANv0_5_0.md`.

## Mandatory source-by-source calibration

- Follow the approved processing order. The next outstanding source is Authorial Grammar; do not choose by filename, convenience, or task memory.
- Every new source is a new calibration problem. Prior-source success grants no authority for the next source.
- Draft, review, and obtain author approval of the source's content/provenance identity card before offline extraction preparation.
- Begin with offline parsing, chunk planning, fake-response testing, validation, and prompt iteration.
- Freeze one or more representative pilot chunks and the complete execution configuration: source, disposition, streams, identity card, profile, chunk, prompt, schema, chunker, engine, validator, normalization, exclusion policy, model, and reasoning effort.
- A provider authorization covers only the explicitly bound pilot call and cost cap.
- Mechanically validate and substantively compare every pilot. Preserve rejected output; revise offline; repeat only a bounded pilot until it is perfect-for-release.
- Pilot acceptance does not authorize the remainder. Asa Wember must separately authorize the full-source call limit and cost cap.
- Run sequentially one call and extraction-quality review at a time unless Asa separately authorizes a different cadence. Any defect halts and revokes the run, returning the affected method/material to calibration.
- After a full-source release, an independently authorized cumulative spend envelope may cover routine calls without a new cost approval for each transaction. The envelope grants money authority only; source, lifecycle, call-limit, cadence, prior-review, and defect controls remain independent.
- Provider prompts may expose extractable content from exactly one source. Other-source atoms or prose never enter the extraction payload.
- Every embedded figure, caption, and media reference receives an explicit disposition.
- A complete candidate still requires whole-document coverage and extraction-quality review before source-bounded candidate acceptance. This is not Layer E semantic or canonical acceptance.
- Authorial Grammar has an additional post-extraction/pre-candidate conformance review against applicable Human Rulings authorial evidence. Human Rulings content remains outside its provider prompt, and this review is not Layer E acceptance or reconciliation.

## Hard controls

- One explicitly authorized repository-writing task at a time. Never infer that write authority transferred.
- A successor task begins read-only until Asa Wember explicitly transfers write authority.
- The v0.9 legacy semantic-review artifacts are preserved but dormant.
- Semantic acceptance, mapping, reconciliation, and compiled prose are prohibited while corpus atomization is incomplete.
- Provider/model calls are prohibited unless a later exact, source-bound author receipt permits one. Google Sheets interaction is paused.
- A Gate 2 deterministic-only source never enters provider calibration; a non-atomic companion never enters atomization.
- Preserve historical receipts and control indexes; supersede them with new append-only artifacts.
- Use the source-agnostic extraction machine and lean evidence policy. Do not create a source-specific provider worker or file-per-transition family when declarative configuration and the chained run ledger suffice.
- Use its zero-call `scaffold` workflow after identity-card approval to draft the next source's manifest, dispositions, chunk plan, prompt, schema, and provider-disabled configuration. Scaffolding is preparation, never pilot or run authority.
- Claude caching is mandatory for eligible sequential runs: one-hour stable-prefix caching, cache-aware accounting, and a halt when both cache-creation and cache-read telemetry are zero.
- Chunk count is a generated result, never a manifest input or preservation target. Calibrate acceptable provider-eligible target blocks per chunk, then re-apportion the complete source at that quantization with the generic `replan` workflow before freezing a new pilot.
- A semantic lead-in and its dependent list, table, code, quotation, or titled structural body form an indivisible semantic group. If such a group exceeds a calibrated token or target-block limit, halt and report the incompatibility; never split it or invent a workaround.
- `STATUS.md` is a concise, derived human dashboard and never execution authority. Refresh it after every accepted or rejected chunk, lifecycle halt, authorization or spend change, source milestone, and before every commit or push. Derive it from the active index, checkpoint, and spend record; its final nonblank line must show cumulative provider cost rounded upward to the cent. The active guard must reject a stale or contradictory dashboard.
- Keep user-facing execution reports concise: decisions, defects, spend exhaustion, milestones, and completion.

## Current Authorial Grammar quantized-pilot boundary

- The first full-source C0001 attempt halted after Anthropic returned `max_tokens` at the bound 6,000-token output limit. The rejected response and exact $0.081618 cost remain preserved.
- The prior five-call release remains revoked.
- Accepted R6 completed 27 dispositions in 5,665 output tokens; failed C0001 completed 23 before truncation. The accepted quantization is 20 provider-eligible targets per chunk.
- The quantized C0001 pilot completed cleanly at 4,876 output tokens, passed mechanical and substantive review, and is accepted as perfect-for-release for the 20-target quantization.
- The old-plan remaining-source run halted at C0002 because the quantizer split an ownership list from its semantic lead-in. B00047 and B00048 were returned `review_required`; the run failed substantive review and its release remains revoked.
- The generic planner now preserves indivisible semantic groups. Re-apportioning the complete source at 20 targets generated 13 chunks. All 51 detected lead-in/body groups remain within one chunk, all 13 chunks prepare and fake-validate, and the 120-test engine suite passes.
- New-plan C0002 (B00041-B00068, 18 targets) returned cleanly, used a 2,545-token cache read, passed mechanical and substantive review with no defect, and is accepted as perfect-for-release for the structurally grouped 20-target quantization. Exact cost was $0.054311.
- Cumulative provider spend is $0.254597. The active money-only envelope has $1.745403 remaining but grants no lifecycle authority.
- The old-plan accepted C0001 remains calibration evidence only and does not accept new-plan C0001; do not silently project it as new-plan completion.
- The authorized remaining-source run accepted new-plan C0001, then halted at C0003. B00071, the structural table header `Construction | Meaning | Example`, was incorrectly emitted as an atom about the table's columns. That is layout metadata, not an Authorial Grammar rule, and violates the lean evidence policy.
- The C0003 defect revoked the remaining release. C0004-C0013 were not called. Do not silently delete the rejected atom, retry, or modify the prompt, schema, or exclusion policy without a newly authorized calibration path.
- Source-run spend was $0.097858. Cumulative provider spend is $0.352455; the active money-only envelope has $1.647545 remaining but grants no lifecycle authority.
- The approved offline recalibration is complete. The generic prompt and validator now require every Markdown table header and delimiter row to be `no_substantive_claim`; substantive body rows remain eligible. This is not a B00071-specific patch.
- The structural plan remains 13 chunks. C0001 and C0002 pass compatibility replay; captured C0003 fails exactly one new table-structure check. The engine suite passes 121 tests.
- The lean-table C0003 pilot fixed B00071-B00073 as intended but was rejected because B00101 `Prefer:` and B00105 `Not:` became atoms merely stating that context-only examples follow. Their dependent blocks B00103 and B00107 are `context_only`; the labels are structural metadata, not authorial rules.
- The call created 2,698 one-hour cache tokens and cost $0.067362. Cumulative spend is $0.419817; the active money-only balance is $1.580183.
- Offline recalibration now marks all 14 pure example/polarity labels in bound payloads as requiring `no_substantive_claim`, with validator enforcement. Substantive colon-ended sentence lead-ins remain eligible; this is not a block-specific patch.
- C0001/C0002 pass newly bound replay; captured C0003 fails exactly B00101/B00105 under the new rule. All 13 chunks fake-validate and 122 tests pass.
- C0003 is frozen for a new pilot with a $0.120852 cache-miss ceiling. No provider call is authorized; spend remains $0.419817 with $1.580183 money-only balance.
