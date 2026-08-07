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

## Active phase profile — authorial triage

This profile governs deterministic authorial triage of the immutable accepted
atoms from the 18 completed pre-reconciliation sources. Its purpose is to
reduce later model work by recording which atoms remain eligible for active
reconciliation. It does not perform semantic acceptance, mapping,
reconciliation, canonization, or compiled prose.

The phase has no provider calls, model spend, prompts, schemas, or calibration.
The author works through `m050/tools/m050_atom_triage.py`; no Compile Worker is
active while the author-directed interface holds repository-write authority.
Before the Supervisor changes code, controls, or structure, stop the interface
and checkpoint its decisions so the one-writer rule remains exact.

### Canonical input and decision record

- Accepted extraction candidates remain immutable evidence. The triage tool
  verifies every candidate against its acceptance-report SHA-256 before use.
- `m050/reconciliation/triage/M050_Authorial_Triage_Decisions_MEDIANv0_5_0.jsonl`
  is the sole canonical triage decision record. It contains at most one current
  decision per accepted atom; Git is its history.
- Every decision binds the source ID, atom ID, source block, and accepted
  candidate hash. Binding drift is a hard failure.
- The tool writes the complete current decision record atomically. It may undo
  the latest atom or whole-block event without creating an event-log family.
- Source text, normalized claims, sibling atoms, and provenance are read-only
  views. Triage never rewrites accepted evidence.

### Authorial decisions

- `retain` means eligible for later reconciliation. It does not mean the atom
  is true, current, nonduplicative, or accepted into final canon.
- `exclude` removes the atom from active v0.5.0 reconciliation while preserving
  its immutable evidence. It requires exactly one existing reason:
  `obsolete_or_superseded`, `administrative_or_provenance_only`,
  `outside_v0_5_scope`, `true_duplicate`, or `other_authorial_exclusion`.
- `uncertain` reserves the atom for explicit later model-assisted or authorial
  review. It is not an implicit retain or exclude.
- A whole-block decision applies one reversible authorial event to every atom
  in the displayed source block. Skip records nothing.
- Editorial or semantic grammar that governs the authoritative presentation of
  the specification remains reconciliation-eligible even when it is not a game
  mechanic. Administrative/provenance-only is for project-history or process
  material, not normative specification rules.

### Execution and boundaries

- Process atoms in canonical source order unless the author deliberately uses
  the source filter. Resume at the first undecided atom in the selected scope.
- The mobile interface may bind without another password only to loopback or an
  exact Tailscale IPv4 address. Wildcard, LAN, and public bindings are
  prohibited. Tailscale Funnel is prohibited.
- Routine decisions update only the canonical decision record. They do not
  require per-decision STATUS refreshes, commits, agent narration, or model
  review.
- At an author-requested checkpoint or before system tuning, stop the interface,
  refresh canonical state and STATUS, run the existing guard, commit and push,
  and confirm a clean synchronized worktree before further structural writes.
- Halt for candidate/hash drift, malformed or duplicate decisions, corpus
  coverage disagreement, an unavailable canonical record, or a requested
  decision category the current form cannot express. Do not add a category or
  workflow in response; submit the smallest review question.
- Phase completion is exactly one valid decision for each of the 6,550 accepted
  atoms currently bound to this phase. The four later or conditional sources
  remain outside this triage input set unless a later phase transition changes
  their canonical disposition.
- Google Sheets, provider calls, semantic acceptance, mapping, reconciliation,
  canonization, and compiled prose remain prohibited.
- A normal triage operation has no process delta.

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
