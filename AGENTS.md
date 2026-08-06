# MEDIAN repository operating contract

This is the sole active root operating contract. If `AGENTS.override.md`
exists, stop: the repository contract is ambiguous. The repository—not a task
transcript—is the durable source of operational truth.

## Purpose and scope

- “The compile” is the complete controlled pipeline: evidence preparation and
  atomization, semantic review, mapping, reconciliation, and final document
  production.
- Gate 2 registers 24 sources. Two are non-atomic companions, so compile scope
  is 22. The atomic-extraction baseline was 4 completed legacy seeds and 18
  outstanding sources, comprising 14 pre-reconciliation and 4 later or
  conditional sources. Current completed and outstanding counts derive from
  canonical compile state and advance without rewriting this contract.
- Never describe the four-source legacy seed or its dormant review artifacts as
  whole-corpus completion.
- MEDIAN v0.5.0 sources are frozen. `m051/` is outside the compile.

## Conservation of System

The compilation method is closed during execution. A compile task executes the
method; it does not redesign the method in response to ordinary difficulty.

1. **Conservation of Process:** within the current authorized phase mechanics,
   constrain, combine, correct, simplify, or reuse existing implementation
   before proposing anything new. This permits a Compile Worker to repair how
   the established phase operates; it does not permit changes to phase
   structure, stage boundaries, artifact classes, authority rules, or
   cross-phase interfaces.
2. **Conservation of Representation:** every authoritative fact has one
   canonical home. Derived views never become parallel authority.
3. **Conservation of Mandate:** perform only the authorized source and lifecycle
   work. An unresolved matter is a valid output; it is not permission to widen
   the task.

Procedural machinery includes stages, passes, roles, artifact types, schemas,
taxonomies, registries, prompt layers, review procedures, exception classes,
and supervisory workflows. A proposed addition must identify what it replaces,
merges, or removes. A change that only adds another layer is presumptively
rejected.

A component must transform canonical content, enforce an invariant, or preserve
necessary evidence or an unresolved exception. Otherwise remove or fuse it.
Do not repair synchronization trouble by creating another synchronization
layer.

## Task roles and phase handoff

Task titles do not confer authority. The two permitted working roles are a
division of mandate, not another workflow layer:

- **Supervisor:** works in discussion with Asa and may change the compilation
  architecture or this contract only after Asa explicitly authorizes the
  proposed system change. It never redesigns the system automatically and does
  not gain source-work or provider authority from its role. The Supervisor is
  equally bound by Conservation of System. Authority to change the system is
  not authority to expand it freely. Every proposed system change must first
  seek reduction, reuse, constraint, correction, or fusion of existing
  machinery and state its net process delta. Any increase in total stages,
  artifact classes, representations, handoffs, or supervisory machinery
  requires specific discussion with Asa and explicit approval.
- **Compile Worker:** executes one explicitly authorized phase and source using
  the established method. Within an active source-work grant and cumulative budget
  it may handle ordinary extraction details, including diagnosis, correction,
  simplification, validation, retry, state maintenance, and coherent repository
  checkpoints, without transaction-by-transaction approval.

The Compile Worker may not alter cross-phase architecture, add a stage or
artifact family, relax an invariant, advance to another source or phase, or
reinterpret CoS to enlarge its mandate. If it concludes that the existing
structure cannot safely do the work, it must halt and submit a concise human
review request stating the exact obstruction and the smallest change it thinks
is necessary. Difficulty is not permission to self-redesign.

Only one role writes the repository at a time. When the Supervisor is changing
the system, the Compile Worker remains paused. It resumes only from a clean,
committed, pushed checkpoint after completing the required cold start. At an
overall phase boundary, the Supervisor may retool the contract in discussion
with Asa; the Compile Worker begins the new phase only after Asa explicitly
authorizes it.

**Stopdown** is the Worker-side formal handoff, not merely a pause in source
work. At source completion the Worker must finish candidate packaging and
validation, set both source-work and repository-write authority to false in
canonical state, refresh `STATUS.md`, run the required guard, commit and push
that closing transition, and confirm a clean worktree with local `HEAD` equal
to `origin/main`. The closing commit and push are the final repository actions
permitted by the expiring source grant and may publish only the prepared source
completion and authority revocation. A source-completion halt is not a
Stopdown while either authority remains true. After the closing push the Worker
makes no further repository write unless Asa explicitly grants new work.

After confirming formal Stopdown, the Worker uses cross-task messaging when
available to send exactly `Worker has Stopped Down` to the one task titled
`Compile Supervisor` on the same project and host. The notification grants no
authority. If exactly one matching task cannot be found, report the ambiguity
in the Worker task, do not retry automatically, and do not invalidate the
Stopdown. On receipt, the Supervisor adjudicates the Stopdown read-only,
reports pass or defect, and awaits Asa's direction; it does not begin queued
repository work automatically.

## Phase model

The permanent constitution is phase-neutral. Exactly one replaceable active
phase profile defines the Worker’s current mechanics, invariants, evidence
closure, completion condition, and prohibited transitions. A phase profile is
execution authority only when Asa has explicitly authorized that phase.

At a phase boundary, the Worker halts. In discussion with Asa, the Supervisor
replaces the active profile in place and adapts only the phase-specific guard
validation. It must preserve the permanent CoS, role, authority,
canonical-state, STATUS, and one-writer rules. Do not preserve the retired
profile as another active file or accumulate profiles into a workflow stack;
Git is the history.

## Canonical controls

- `m050/extraction/control/M050_Compile_State_MEDIANv0_5_0.json` is the sole
  mutable machine-readable current state. Update it in place; Git is its
  history.
- `STATUS.md` is the only derived human dashboard. It is never execution
  authority.
- `m050/extraction/control/M050_Compile_Source_Processing_Order_v0_1_MEDIANv0_5_0.json`
  controls source order. Completed progress and the next outstanding source are
  derived from canonical compile state rather than duplicated in the order.
- `m050/tools/m050_guard.py` is the sole active repository guard.
- Historical checkpoints, bootstrap packets, active-index versions, execution
  standards, authority policies, and versioned guard wrappers are retired.
  Do not recreate those families.

## Required cold start

1. Confirm `AGENTS.override.md` is absent.
2. Read the canonical compile state completely.
3. Read every active-phase control named by this contract and the canonical
   state completely.
4. Read `STATUS.md` and confirm it exactly mirrors the canonical state.
5. Run `.venv/bin/python m050/tools/m050_guard.py --with-tests` before
   control/code release, provider-enabled configuration release, whole-source
   acceptance, and commit/push. Routine provider capture uses the extraction
   machine’s focused packet, source, spend, cache, response, and prior-review
   checks.
6. Report concisely: active phase; current target and completed/rejected
   boundary; work and spend authority; halt conditions; prohibited transitions;
   next possible transition; STATUS freshness; and whether local `HEAD` equals
   `origin/main`.

No separate successor packet is required. These canonical files are the handoff.

## Authority model

- Asa Wember remains the sole authorial authority.
- Asa gives standing informed consent for repository material to be transmitted
  to Anthropic when an authorized compile task requires it, using the locally
  stored Anthropic API credential. This consent is repository-wide and does not
  require packet-, source-, or call-specific restatement. It permits the
  external transfer only; it does not select a source, activate work, authorize
  spend, widen a task, or permit transmission to another provider.
- Only one task may write the repository at a time. A successor task begins
  read-only until Asa explicitly grants a bounded repository task or
  active-profile work.
- A bounded repository task authorizes only its stated change.

## Active phase profile — atomic extraction

This profile governs atomic extraction only. Its completion condition is
source-bounded candidate acceptance for all compile-scope sources assigned to
this phase. It grants no semantic acceptance, mapping, reconciliation, or
compiled-prose authority. At completion, or before any transition to another
overall phase, the Compile Worker halts for the phase handoff above.

For this profile, the canonical source processing order is a required cold-start
control. The Worker reports the exact corpus vector, selected and next source,
accepted/rejected chunk boundary, source-work and spend authority, and all
prohibited later stages.

- A clear instruction from Asa to resume, continue, begin, or proceed with
  Compile Worker activity is a sufficient explicit source-work grant for
  exactly one source. No prescribed wording or source-name restatement is
  required. The Worker derives the current or next source deterministically
  from canonical compile state and processing order and reports that source
  during cold start. If those controls do not select exactly one source, halt.
  Source completion ends the grant and must close through formal Stopdown;
  starting the following source requires a later human instruction.
- Within an active source-work grant, an active cumulative spend budget with
  enough remaining balance for the next conservative cache-miss ceiling is
  provider-call permission. No separate call receipt, call limit, chunk
  authorization list, full-source flag, or transaction-level provider approval
  exists. Spend never selects or advances a source.
- Standing repository-wide Anthropic transmission consent covers every
  validated frozen packet, including ordinary corrected or refrozen retries.
  A newly frozen packet is not a new approval boundary. Actual transmission
  remains limited by the active task mandate, source grant, call readiness, and
  spend budget; the credential may authenticate the call but must not be
  disclosed as provider content.
- Call readiness is derived from the named source grant, the current validated
  packet and configuration, completed offline/replay gates, sequential review,
  and sufficient cumulative budget. Do not store a parallel
  `provider_call_authorized` fact.

Within an active source-work grant and cumulative budget, the task may proceed
without transaction-by-transaction permission through:

- offline parsing, chunk planning, fake-response testing, and validation;
- bounded sequential provider calls;
- mechanical and substantive review after each call;
- diagnosis of ordinary defects;
- correction or simplification of existing prompt, schema, configuration,
  chunking, engine, validator, or tests;
- compatibility replay, refreezing, and retry of the affected chunk;
- current-state and STATUS maintenance; and
- coherent commits and pushes.

Changes to the generic engine, artifact schema, or validator must remain
source-agnostic and pass the all-source offline compatibility check. A
source-ID branch, source-specific worker, new artifact class, or changed
cross-source invariant requires a Supervisor halt.

Deciding whether context semantically qualifies a target, redefining the
target/context/grounding boundary, or otherwise interpreting source structure
is not an ordinary phase repair. Preserve the evidence and halt for authorial
or Supervisor review rather than changing that boundary during source work.

A defect pauses further provider calls until its correction passes the existing
offline and replay gates. It does not revoke the source-work grant merely
because correction is required. No task may waive a defect, silently repair a
provider response, or skip review.

Halt for Asa only when:

1. remaining authorized spend cannot cover the next conservative call ceiling;
2. an unusual issue requires authorial judgment, mandate expansion, cross-source
   authority, new procedural machinery, an unresolved transport/cost decision,
   or a change that cannot pass existing guards; or
3. the authorized source is complete.

### Source lifecycle invariants

- Follow the approved processing order; never choose by filename or task memory.
- Every new provider-eligible source begins with a content/provenance identity
  card, complete offline preparation, and representative pilot calibration.
  Prior-source success is evidence, not source transfer.
- Maintain an approved identity card in place and bind its exact hash in the
  active source configuration. Git records its approval history; do not create
  a separate identity-transition receipt family.
- Keep each identity card minimal and source-bounded because its complete text
  is provider-visible. It may contain only exact identity and provenance,
  source-declared role, scope, and status, allowed streams, media and exclusion
  rules, and handling necessary to preserve that source's own qualifications.
  Exclude repository history, alternate representation filenames or hashes,
  external-source inventories, design or literary influence discussion, and
  source summaries that do not change provider handling. Source-declared
  lineage may be recorded as provenance, but do not quote, summarize,
  interpret, or apply substantive content from Human Rulings or any other
  external source. Do not enumerate external authorities merely to preserve
  lineage. If an external authority must be identified to enforce a provider
  handling boundary, use only its canonical ID; its meaning, precedence, and
  effect remain deferred to reconciliation.
- Freeze the exact source, identity, disposition, streams, chunk, prompt,
  schema, engine, validator, normalization, exclusion policy, model, reasoning,
  cache, and cost bindings before a call.
- Run sequentially: one call, preservation, validation, and extraction-quality
  review before the next call.
- Provider prompts expose extractable content from exactly one source.
- Every figure, caption, and media reference receives an explicit disposition.
- Claude caching is mandatory when eligible: one-hour stable-prefix caching,
  cache-aware accounting, and a halt when both cache-creation and cache-read
  telemetry are zero.
- Chunk count is generated from calibrated target density. Preserve indivisible
  semantic lead-in/body groups. If one exceeds machine limits, halt rather than
  split it or invent a workaround.
- Whole-document coverage and extraction-quality review are required before
  source-bounded candidate acceptance.
- Authorial Grammar additionally requires post-extraction, pre-candidate
  conformance review against applicable Human Rulings evidence. Human Rulings
  content remains outside its provider payload.
- Source-bounded candidate acceptance is not Layer E semantic acceptance,
  mapping, reconciliation, canonization, or compiled prose.

### Artifact and state discipline

- Frozen sources and accepted evidence are immutable.
- Preserve raw provider responses, compact outcomes, exact usage/cost, rejected
  attempts, and hash-chained run ledgers. Canonical state and Git history
  preserve source and spend authorization.
- Reuse the source-agnostic extraction machine. Source differences belong in
  declarative configuration, not source-specific workers.
- Ordinary provider attempts use the existing call packet, raw response,
  compact outcome, canonical spend state, and one source ledger. Update
  cumulative spend in canonical state in place after capture; do not create
  lifecycle receipts, successor spend files, or another file-per-transition
  family.
- Active operating instructions, guard code, and current state are maintained
  in place. Do not version them inside the working tree; Git supplies history.
- Update the configured active-source prompt in place. Do not create a
  successor prompt file for an ordinary correction.
- Within one unchanged state revision, read active controls and stable bindings
  once. Batch independent read-only checks, and do not repeatedly inspect whole
  packets, schemas, raw responses, or unchanged files when their hashes and the
  compact outcome establish the required facts.
- For routine chunk review, inspect the exact target dispositions and their
  source/claim pairs plus mechanical findings, usage, cache, and cost. Compact
  inspection does not replace source-grounded substantive review or any
  mechanical gate.
- Keep routine narration and command output to the information needed for a
  decision, defect, spend boundary, or milestone. Successful internal
  bookkeeping does not require a running user-facing transcript.
- At every halt, begin the user-facing report with `WORKER STATE: STOPDOWN`
  only when both authorities are false and the closing checkpoint is clean,
  pushed, and synchronized. Otherwise begin with `WORKER STATE: NOT STOPDOWN —
  <reason>`. Follow it with `SOURCE PROGRESS: <current chunk> / <total chunks>`,
  deriving the denominator from canonical state and the active chunk plan.
- Record exceptional material in the existing outcome and ledger unless that is
  genuinely unsafe or impossible.
- A normal compile operation has no process delta.

### Active-phase hard boundaries

- A deterministic-only source never enters provider calibration. A non-atomic
  companion never enters atomization.
- Semantic acceptance, mapping, reconciliation, and compiled prose remain
  prohibited until corpus atomization is complete and separately released.
- Google Sheets interaction remains paused.
- Credentials never enter the repository, prompts, receipts, or reports.
- Keep user-facing reports to decisions, defects, spend exhaustion, source
  milestones, and completion.

## STATUS contract

`m050/tools/m050_render_status.py` is the sole writer of `STATUS.md`. It derives
the complete dashboard deterministically from canonical compile state; agents
must not compose or patch dashboard prose manually.

`STATUS.md` is a full-guard and publication checkpoint, not live execution
state. Routine accepted or rejected chunks do not require regeneration. Run
the renderer immediately before every full-guard invocation and before any
push not already preceded by a refreshed full guard. Between refreshes,
canonical state and the active run ledger remain authoritative.

The first line below the dashboard title is an unlabeled human-readable
timestamp rounded to the nearest second. The final nonblank line is the active
spend balance rounded downward to the cent so it never overstates remaining
authority; exact cumulative spend and balance remain in machine evidence. The
guard rejects a stale or contradictory dashboard.
