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
2. Read `m050/extraction/control/M050_Active_Control_Index_v0_13_MEDIANv0_5_0.json` completely.
3. Read `m050/extraction/control/M050_Current_State_Checkpoint_v0_4_MEDIANv0_5_0.md` completely.
4. Read `m050/extraction/control/M050_Compile_Source_Processing_Order_v0_1_MEDIANv0_5_0.json` completely.
5. Read `m050/extraction/control/M050_Source_Atomization_Pilot_Calibration_Protocol_v0_1_MEDIANv0_5_0.md` completely.
6. Read `m050/extraction/control/M050_Compile_Execution_Standard_v0_1_MEDIANv0_5_0.md` completely.
7. Run `.venv/bin/python m050/tools/m050_guard_v0_8.py --with-tests` before control/code checkpoints, provider-enabled configuration release, whole-source acceptance, and commit/push. Routine append-only provider capture uses the execution standard's focused preflight and validation.
8. Report the exact `24 / 22 / 4 / 18 = 14 + 4` corpus vector; the next source; the accepted-pilot boundary; the source-run and spend-envelope boundary; the required cadence and halt conditions; all prohibited later stages; the next authorized transition; and whether local `HEAD` equals `origin/main`.

The paste-ready successor-thread audit is
`m050/extraction/control/M050_New_Task_Bootstrap_v0_3_MEDIANv0_5_0.md`.

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
- Keep user-facing execution reports concise: decisions, defects, spend exhaustion, milestones, and completion.
