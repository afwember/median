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
- `m050/reconciliation/rewrite/M050_Authorial_Rewrites_MEDIANv0_5_0.jsonl`
  is the sole canonical authorial rewrite record.
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

## Active phase profile — authorial rewrite

This profile governs source-grounded authorial replacement of the 98 immutable
accepted atoms whose completed canonical triage decision is `uncertain` with
route `rewrite_list`. It supplies accepted authorial expression for later
reconciliation. It does not alter extraction evidence, perform cross-atom
reconciliation, resolve other gaps, canonize claims, or produce compiled prose.

The phase has no provider calls, model spend, prompts, or calibration. The
author works through `m050/tools/m050_atom_rewrite.py`. The interface reads
immutable repository evidence and completed canonical triage, but writes its
noncanonical editor buffer only under
`Documents/Codex/median-support/rewrite-working/`; it holds no repository-write
authority. Before changing the rewrite tool, inputs, record form, controls, or
phase structure, stop the interface and checkpoint its completed source.

### Canonical input and rewrite record

- The completed canonical triage record is immutable phase input. Exactly its
  98 `rewrite_list` atoms enter this phase; retained atoms, excluded atoms, and
  any future source do not.
- Accepted extraction candidates remain immutable evidence. Every candidate is
  verified against its acceptance-report SHA-256 before use.
- `m050/reconciliation/rewrite/M050_Authorial_Rewrites_MEDIANv0_5_0.jsonl`
  is the sole canonical rewrite-disposition record. It contains at most one
  current disposition per selected atom; Git is its history.
- Every disposition binds the triage-record hash, source ID, atom ID, source block,
  accepted-candidate hash, and original normalized-claim hash. Binding drift is
  a hard failure.
- Submitting the unchanged normalized claim records `accept`; submitting edited
  text records `rewrite`. Either is authorially accepted and becomes the later
  reconciliation input in place of the uncertain atom. The immutable original
  remains evidence and must not also enter reconciliation as a parallel claim.
  `Exclude` records the existing
  `other_authorial_exclusion` reason, preserves the same immutable evidence, and
  removes that atom from later reconciliation.
- The out-of-repository working file is an editor buffer, not a second
  authority. It preserves every canonical rewrite exactly, writes atomically,
  and may add rewrites only for the one currently released source. Undo removes
  only the latest uncheckpointed rewrite in that source. Skip records nothing.

### Execution and boundaries

- Process rewrite-list atoms in canonical source and atom order. Resume at the
  first unwritten atom in the one source released by the latest canonical
  checkpoint.
- The interface may bind without another password only to loopback or an exact
  Tailscale IPv4 address. Wildcard, LAN, public bindings, and Tailscale Funnel
  are prohibited.
- Routine dispositions update only the external editor buffer. They require no
  per-rewrite STATUS refresh, commit, agent narration, or model review.
- Completing all rewrite-list atoms in a source is a hard checkpoint boundary.
  The next source remains closed until the Supervisor imports that source,
  refreshes canonical state and STATUS, runs the existing guard, commits and
  pushes, and confirms a clean synchronized worktree. The open interface polls
  canonical state and releases the next source automatically after publication.
- Halt for candidate, triage, block, or claim-hash drift; malformed or duplicate
  rewrites; input-count disagreement; unavailable canonical records; or an
  authorial need the single replacement-claim form cannot express. Do not add a
  category or workflow automatically; submit the smallest review question.
- Phase completion is exactly one canonical checkpointed accept, rewrite, or
  exclusion disposition for each of the 98 bound atoms. Then halt for the
  separately authorized reconciliation transition.
- `m051/`, the four later or conditional sources, Google Sheets, provider calls,
  model semantic acceptance, mapping, reconciliation, canonization, and
  compiled prose remain prohibited.
- A normal rewrite operation has no process delta.

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
