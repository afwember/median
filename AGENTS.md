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
- **Compile Worker:** executes one explicitly authorized phase and bounded action
  using the established method. Within an active work grant and cumulative budget
  it may handle ordinary phase details, including diagnosis, correction,
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

**Stopdown** is the universal Worker-side interrupt, safe halt, authority-key
removal, and formal handoff, not merely a pause in phase work. Asa may invoke it
at any time,
including before a tranche is complete. The Worker must stop new provider
activity, preserve and cost-reconcile all available evidence, retain the exact
incomplete boundary without marking it complete, set source-work,
repository-write, provider-call,
active spend, and applicable phase-work authority to false in canonical state,
preserve any unused author-approved balance, refresh
`STATUS.md`, run the required guard, commit and push that closing transition,
and confirm a clean worktree with local `HEAD` equal to `origin/main`. When the
tranche is complete, the same path records completion; there is no separate
pause or abort transition. The closing commit and push are the final repository
actions permitted by the expiring bounded grant and may publish only preserved
work, reconciled evidence or cost, and authority revocation. A cessation is not
a Stopdown while any applicable authority remains true. After the closing push
the Worker makes no further repository write unless Asa explicitly grants new
work.

Host-privileged operations must remain narrow and independently approvable.
Run status rendering, the full guard, Git staging, read-only Git inspection,
commit, and push as separate tool calls rather than one compound shell request.
When a command requires host elevation, that tool call must contain only the
single privileged operation and must request the narrow stable command prefix
for that operation. Repository authority does not replace host sandboxing, and
host sandboxing must not be turned into repeated authorial approval.

After confirming formal Stopdown, the Worker's final command action is exactly
`.venv/bin/python m050/tools/m050_notify_supervisor.py`. The script uses the
installed Codex CLI in the repository working directory to resume the task
named exactly `Compile Supervisor` and pass exactly `Worker has Stopped Down`
as its prompt. This replaces app-tool discovery and messaging; do not run a
second notification path. When host elevation is required, the elevated call
contains only that exact script invocation and requests only the narrow stable
prefix for it. After the script returns, the Worker may give its final stable
response but performs no further command, tool, or repository action.

The notification grants no authority. A nonzero script result is reported once
and is not retried automatically; it does not invalidate the Stopdown. On
receipt, the Supervisor performs the equivalent read-only assessment: it
verifies repository and handoff health, summarizes the Worker's actions,
identifies any defect or next decision, and pauses for discussion. It does not
begin queued repository work automatically.

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

`m050/docs/operations/M050_Compile_Worker_Best_Practices.md` is a
non-authoritative phase-construction reference. It may inform Supervisor/author
discussion, but it grants no authority and is not a Worker control. A practice
becomes operative only when it replaces or refines language in this contract,
the active profile, canonical state, or the sole guard.

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
- `m050/reconciliation/rewrite/M050_Authorial_Rewrites_MEDIANv0_5_0.jsonl`
  is the sole canonical authorial rewrite record.
- `m050/mapping/M050_MSID_Vocabulary_MEDIANv0_5_0.json` and
  `m050/mapping/M050_Atom_MSID_Mappings_MEDIANv0_5_0.jsonl` are respectively
  the sole Stage 4 vocabulary and current atom-mapping record.
- `m050/reconciliation/M050_Reconciled_Semantic_Units_MEDIANv0_5_0.jsonl` is
  the sole canonical Stage 5 reconciliation record.
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
   control/code release, provider-enabled configuration release, tranche
   acceptance, and commit/push. Invoke the renderer and full guard in separate
   tool calls. The active Stage 5 suite is provider-free and does not bind
   network ports. Routine provider capture uses the reconciliation tool’s focused
   packet, tranche, spend, cache, response, and prior-review checks. A read-only
   Spark Up assessment publishes nothing and does not itself trigger the
   renderer or full guard.
6. Report concisely: active phase; current target and completed/rejected
   boundary; pending Batch job if any; available and reserved spend; work and
   spend authority; halt conditions; prohibited transitions; next possible
   transition; STATUS freshness; and whether local `HEAD` equals `origin/main`.

No separate successor packet is required. These canonical files are the handoff.

## Authority model

- Asa Wember remains the sole authorial authority.
- Asa gives standing informed consent for repository material to be transmitted
  to OpenAI when an authorized compile task requires it, using the locally
  stored OpenAI API credential. This consent is repository-wide and does not
  require packet-, source-, or call-specific restatement. It permits the
  external transfer only; it does not select a source, activate work, authorize
  spend, widen a task, or permit transmission to another provider.
- Provider spend is never replenished automatically. If the conservative
  ceiling for a proposed call exceeds the remaining authorized balance, the
  Worker halts and reports the balance, ceiling, and exact shortfall. Only Asa's
  explicit approval of a stated dollar amount may refresh the balance. Unused
  balance persists across Stopdown and later attempts until spent or explicitly
  refreshed. Stopdown disables spend activity but does not erase that balance.
  A refresh replaces the available balance with the stated amount and sets
  `authorized_usd` to cumulative spend plus that amount; it does not add the
  stated amount to an unused balance. A submitted Batch request reserves its
  complete discounted conservative ceiling: authorized spend equals cumulative
  spend plus unreserved remaining spend plus reserved spend. Do not refresh the
  envelope while a Batch reservation is unresolved.
- Only one task may write the repository at a time. A successor task begins
  read-only until Asa explicitly grants a bounded repository task or
  active-profile work.
- A bounded repository task authorizes only its stated change.

## Active phase profile — Stage 5 semantic reconciliation

This profile governs comparison and unification of the 5,382 effective claims
that completed Stage 4. Reconciliation establishes a coherent semantic base: it
merges genuine duplicates, combines compatible partial claims, resolves grounded
conflicts and supersession, and preserves unresolved matters explicitly. It does
not write the v0.5 GDD, compare against the v0.4.6 baseline, process later or
conditional sources, fill m051 gaps, or decide document order and prose.

The profile is installed ready but not Worker-active. Installation grants no
reconciliation, provider-call, model-spend, semantic-acceptance, or repository-
write authority. Provider configuration is initially disabled. Asa must
separately authorize a provider model and positive Stage 5 cumulative spend
envelope before any call is possible.

Asa's instruction `Spark Up` is the universal Worker-side key insertion and
turn. It grants the bounded active-phase mandate, including reconciliation,
reviewed semantic acceptance, and repository writes, for the next action Asa
approves after the read-only assessment. Provider calls additionally require an
author-approved provider configuration and positive spend envelope at execution
release. The grant exists in task context while canonical execution authority
remains false during the assessment pause. Spark Up does not itself release
action.

Immediately on `Spark Up`, the Worker remains read-only, performs the complete
cold start, and runs `.venv/bin/python m050/tools/m050_reconciliation.py
--transition prepare-spark-up`. That command reports current lifecycle,
authority, target, progress, and spend facts; it does not build a packet, select
a target, change state, or reject startup merely because the prior target is
complete. The Worker then makes the actual assessment:

- If the repository is healthy and an incomplete tranche is preserved, state
  its continuation as the next action and halt for action approval.
- If the prior tranche is complete, select the next coherent functional tranche
  from existing vocabulary, mappings, and unaccounted atoms; state the exact
  tranche ID, MSID boundary, selector, rationale, first action, and material
  risks, then halt for action approval.
- If the repository is dirty, contradictory, or the next action is not
  understood, state exactly what was found or what is missing, then halt for
  discussion.

Multiple valid next tranches are not a halt condition. Choose one defensible,
bounded semantic group, preferring established dependencies before their
dependent mechanics and a scope that fits the current method. The choice need
not be globally optimal. Do not create a durable ordering, selection ledger, or
new priority system.

This read-only assessment pause is not a lifecycle state or publication
checkpoint. Do not refresh STATUS, run a publication guard, commit, push,
construct a provider packet, or repair the repository merely to represent it.
Retain the assessment and Git checkpoint in task context. If that context is
lost before action approval, require a new `Spark Up`.

`Proceed`, or an equally clear directive in response to the assessment,
approves and releases action; it does not insert the key or create authority.
When the next action was already understood, activate the preserved incomplete
tranche with `--expected-tranche-id` and `--expected-head`. For the Worker's
selected next tranche, `Proceed` approves that selection; pass
`--select-tranche-id`, `--select-msid-prefix`, `--select-selector`, and
`--expected-head`. Asa may instead override it with another exact functional
boundary. The same invocation may pass `--authorize-spend-usd` only to refresh
the persistent balance to a dollar amount Asa explicitly approved in that
response. Omit it to reuse an existing positive balance. Use exactly one
`.venv/bin/python m050/tools/m050_reconciliation.py --transition
activate-on-proceed ... --apply` invocation. It performs the narrow stale-check
and atomically binds and activates only the approved action. An incomplete
canonical tranche cannot be replaced. Do not precede activation with another
cold start, guard, Git check, dry run, inventory, or revalidation. If activation
fails, halt and report the drift; if it succeeds, begin work. Repeated `Spark
Up` repeats only the assessment. `Proceed` without the retained Spark Up grant
and assessment grants nothing.

### Canonical input and representation

- The 5,382 effective claims are immutable Stage 5 inputs. Their completed
  mappings and vocabulary are fixed during Worker execution. At a stopped
  boundary, an explicit authorial ontology correction may replace only the
  affected current mappings and vocabulary, must rebind their canonical hashes,
  preserve every prior packet and run unchanged, and resume through a successor
  tranche ID. Mapping metadata routes semantic context; it does not decide
  truth, canon, authority, conflict, or supersession.
- The corpus is unitary. Semantic tranches are bounded execution units, not
  source partitions or parallel corpora.
- `m050/reconciliation/M050_Reconciled_Semantic_Units_MEDIANv0_5_0.jsonl`
  is the one canonical reconciliation record. Each record is one semantic
  proposition and may contain atoms from multiple sources. Multiple propositions
  may share an MSID. Every eligible atom must ultimately appear exactly once as
  a primary member; cross-links never duplicate primary membership.
- Unit statuses are `reconciled`, `human_required`, and
  `authorially_deferred`. The latter is a terminal, intentionally noncanonical
  result. `human_required` is working state and must be zero at phase completion.
- Member dispositions are `basis`, `supporting`, `elaboration`, `superseded`,
  `conflicting`, and `deferred`. A reconciled unit requires one current MSID and
  one source-grounded canonical semantic claim. A deferred unit asserts no
  canonical claim.
- Accepted extraction, triage, rewrite, packet, raw-response, and semantic-review
  evidence remain immutable. A replaced current vocabulary or mapping remains
  recoverable through Git history rather than a parallel ledger. Do not create a
  filtered corpus, second reconciliation ledger, or prose view.

### Authority and semantic judgment

- Asa Wember remains sole authorial authority. Ordinary grounded model
  reconciliations may become canonical after independent semantic review without
  line-by-line author review. A model may not invent a rule, fill a gap, mint an
  ontology path, or hide uncertainty to complete coverage.
- Do not modify the Human Rulings Ledger. An applicable explicit ruling controls
  only the precise question and semantic scope it settles. Include only relevant
  ruling atoms in a packet. Affected-source metadata alone confers no priority;
  explanation, administration, provenance, and repetition confer no authority.
  Dedicated specifications remain detailed owners outside an exact ruling.
  Conflict with a demonstrably later or more specific accepted authorial action
  follows that action; otherwise preserve `human_required`.
- Stage 4 unresolved mappings do not automatically require author review.
  Cross-source context may attach them to grounded reconciled units. A surviving
  canonical proposition must have a valid current MSID. If the necessary
  vocabulary path does not exist, halt for Supervisor/author adjudication.

### Hybrid API method and evidence closure

- Provider calls are direct API calls made by Python, not Codex model turns.
  Python constructs hash-bound packets, preserves the raw response before parse,
  enforces schema and exact atom coverage, validates bindings and cost, and emits
  compact status. It never makes semantic equivalence, authority, conflict, or
  synthesis judgments.
- Every candidate packet receives two semantic passes: a strong reconciler
  proposes units; a fresh reviewer compares that unchanged proposal against the
  complete packet for lost nuance, invention, false equivalence, unresolved
  conflict, authority error, and improper Human Rulings weight. Only an `accept`
  review or an explicit authorial disposition may enter the canonical record.
  Review rejection routes to bounded revision, `human_required`, or halt.
- Provider model is a replaceable canonical configuration value. The active
  configuration is GPT-5.6 Sol at medium reasoning. Reuse the proven OpenAI
  request/capture, caching, failure classification, exact-cost,
  and pessimistic-ceiling disciplines; do not reactivate extraction prompts,
  chunks, streams, or source-specific controls. A different provider requires
  explicit transfer permission and the smallest replacement adapter; do not
  build a generic provider framework.
- Raw packets and responses are write-once evidence. API stdout must remain a
  compact summary so ordinary results do not enter the Worker conversation.
  Transport, refusal, truncation, JSON, schema, coverage, grounding, semantic,
  and authorial failures remain distinct. Retry only a narrowly classified
  transient or correctable failure; a clean call is never repeated speculatively.
- The current `Citizen.Guest` proposal and, if mechanically valid, its review
  are the one-request OpenAI Batch transport pilot. Batch changes delivery and
  price only: each request remains an independent existing hash-bound proposal
  or review request and returns through the existing validator, ledger, cost,
  and promotion path. The canonical state carries at most one pending Batch job
  and its reserved discounted ceiling. The input JSONL, upload, submission,
  cancellation, and output wrappers live beside the existing request/response
  evidence; they are not a new semantic artifact family.
- A successful pilot may support a later author-approved overnight proposal
  wave. Such a wave may combine transport for multiple independent, coherent
  tranches but may not combine their semantic packets. Only mechanically valid
  proposals enter a separate review wave. Batch rejects and revisions return to
  the existing one-at-a-time direct path. The pilot request limit remains one
  until the Supervisor and Asa assess the completed pilot and replace that
  limit; the Worker does not widen it automatically.
- Cache hits never fund authority. Debit every response with known usage,
  including unusable responses. No call may exceed the remaining cumulative
  envelope under its conservative cache-miss ceiling. Checkpoint coherent
  tranches, not individual calls.

### Execution, halt, and completion

- The initial tranche is the exact `Away.Crossing` MSID group. Descendant,
  related, same-block, and mapping-basis atoms are context only unless listed as
  required packet members. The pilot uses the permanent Stage 5 method; it is
  not a separate artifact family.
- Use `m050/tools/m050_reconciliation.py` for deterministic inventory, packet,
  record, and lifecycle operations. `prepare-spark-up` is read-only and rejects
  `--apply`. `activate-on-proceed` requires the assessed checkpoint and either
  the preserved incomplete tranche or the Worker's action-approved next
  functional boundary.
  `prepare-stopdown --apply` is the universal interrupt: it always revokes
  authority, preserves the current target, and records completion only when
  exact tranche coverage exists. STATUS rendering, the full guard, Git
  operations, synchronization, and Stopdown notification remain separate formal
  actions.
- Batch submission reserves the complete discounted ceiling before upload.
  Collection preserves the provider output before parse, debits known usage at
  the configured Batch multiplier, releases the unused reservation, and clears
  the pending job. Stopdown first requests cancellation of a submitted Batch;
  if cancellation is still pending, it preserves the job and reservation while
  revoking all authority. A later Spark Up assessment must identify collection
  and cost reconciliation as the next action before new provider work. A Batch
  prepared locally but not submitted may be abandoned and fully unreserved.
- After execution release, the Worker operates autonomously within the tranche
  and budget. It may diagnose and correct local implementation, validate and
  review calls, maintain canonical state, make coherent checkpoints, and select
  the next functional tranche during a later Spark Up assessment. Tranche
  selection may schedule only existing unaccounted Stage 5 content; it may not
  mint an ontology path, change tranche or selector semantics, abandon an
  incomplete boundary, change the representation or authority policy, weaken
  semantic review, enter another phase, or transmit to another provider.
- Halt for input or vocabulary drift, packet or evidence-binding defect,
  incomplete or duplicate atom coverage, ungrounded synthesis, unresolved
  authority, ontology defect, exhausted authority or spend, repeated provider
  failure, or need to change the phase method.
- Stopdown returns to Supervisor read-only adjudication. Unless that assessment
  finds a defect requiring discussion, a fresh Spark Up lets the Worker select
  the next functional boundary. Stage 5 completes only when all 5,382 atoms have
  exactly one primary home, every canonical unit is grounded and valid, zero
  `human_required` units remain, all remaining conflicts are resolved or
  authorially deferred, and the global cross-domain consistency audit passes.
- The v0.4.6 baseline GDD, four later or conditional sources, `m051/`, Google
  Sheets, baseline audit, manifestation processing, canonization, document
  structure, and compiled prose remain prohibited.
- A normal reconciliation tranche has no process delta.

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
timestamp rounded to the nearest second. The final nonblank line is the
remaining provider balance rounded downward to the cent so it never overstates
authority; it is explicitly labeled inactive during provider-free phases.
Exact cumulative spend and balance remain in machine evidence. The guard
rejects a stale or contradictory dashboard.
