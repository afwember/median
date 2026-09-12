# MEDIAN Compile Worker Best Practices

Date: 2026-09-08
Status: `NON_AUTHORITATIVE_PHASE_CONSTRUCTION_REFERENCE`

## Use of this document

This document is a reusable design reference for constructing or revising a
Compile Worker at a phase boundary. It records practices that evolved
successfully during late Atomization and lessons recovered during later phases.

It is not execution authority. It does not grant work, spend, provider, source,
or repository-write permission; it does not override the root `AGENTS.md`, the
canonical compile state, or the one active phase profile. A Worker must not be
instructed to treat this file as another operating contract.

When a practice is adopted for an active phase, its necessary rule belongs in
the existing root contract, canonical state, phase profile, or sole guard as
appropriate. Replace or refine conflicting language in place. Do not layer this
document on top of those controls.

## 1. The Worker relationship

The Compile Worker is an autonomous executor inside a bounded mandate. It is
not a second Supervisor and not a passive command runner.

Within one Sparked-Up phase mandate and approved bounded action, it should be
able to:

- identify the current target from canonical controls and, when the active
  profile makes work ordering functional, select the next target;
- perform the phase's ordinary work without transaction-by-transaction
  approval;
- diagnose and correct local execution defects;
- simplify or refactor immediate, phase-local mechanics when the established
  method requires it;
- validate every result proportionately;
- maintain canonical state and its single derived dashboard;
- create coherent checkpoints; and
- finish through formal Stopdown.

It may not redesign the phase, change a cross-phase interface, add an artifact
family, relax an invariant, redefine target semantics, make a target choice the
active profile reserves to Asa, infer authorial judgment, or turn ordinary
difficulty into a wider mandate.

The Supervisor designs and tunes the operating system conversationally with
Asa. Asa manually starts the Worker. The Supervisor does not automatically
Spark Up, queue, or message the Worker.

## 2. Preferred human cadence

The successful late-Atomization cadence separates **authority** from
**execution release**.

### `Spark Up` — insert the key and assess

`Spark Up` is Asa's active, informed grant of the phase-defined mandate. It is
the universal Worker-side key insertion and turn. It does not depend on a next
target already being selected and does not itself release action. The grant is
retained in task context while canonical execution authority remains false
during the assessment pause.

On receipt, the Worker should immediately:

1. remain read-only while performing the complete cold start;
2. inspect repository synchronization, lifecycle, phase, current boundary,
   authority, budget, inputs, outputs, halt conditions, and prohibited
   transitions;
3. determine whether the repository is healthy and whether it understands the
   next action, selecting the next functional target when the active profile
   permits;
4. retain the clean Git checkpoint and assessment in task context; and
5. halt without changing the repository and before substantive work, provider
   calls, packet construction, or record changes.

If the repository is healthy and the next action is understood, the Worker
states that action, any selected target and rationale, and its material risks,
then awaits approval. Functional target selection is ordinary scheduling, not a
structural or authorial decision. If the repository is dirty or contradictory,
or no target can be selected without changing structure or exercising authorial
judgment, the Worker states exactly what it found or needs and awaits
discussion. The assessment is the thread's reasoned reading of repository
state, not another formal lifecycle checkpoint.

Several valid functional targets do not create an ambiguity that requires
escalation. Select one defensible bounded unit, state why, and continue through
action approval. Do not add an ordering ledger or priority system merely to
make that ordinary choice deterministic.

### `Proceed` — execution release

`Proceed`, or an equally clear directive in direct response to the assessment,
releases execution of the already-authorized action and approves any functional
target the Worker stated. It is not a new authority grant. Asa may override the
selection or supply an action that genuinely required authorial direction.

The Worker should accept it only when:

- the preceding `Spark Up` grant remains active;
- the approved action and any target are exact;
- the repository remains at the expected clean checkpoint; and
- no new halt condition has appeared.

The phase's activation operation should test those conditions and change the
lifecycle atomically in one invocation. Boundary selection or an explicitly
approved spend refresh may be recorded in that same operation. Unused approved
balance should persist across Stopdown and later attempts until spent or
explicitly refreshed; a refresh replaces the available balance rather than
adding to it. Do not precede activation
with a second cold start, full guard, separate synchronization check, dry-run
transition, preview, inventory, or general revalidation. A failed atomic
activation returns to LLM adjudication; a successful one should proceed directly
into the approved work. The read-only pause itself should not be represented by
mutable canonical state, a STATUS refresh, a guard run required only for
publication, or a commit/push. If task continuity is lost before action
approval, require a new `Spark Up` assessment.

After `Proceed`, the Worker acts autonomously through ordinary phase work. It
does not ask for repeated permission for routine calls, retries, validation,
local correction, commits, or pushes already covered by the grant.

### Idempotence and invalid transitions

- Repeated `Spark Up` while awaiting action approval repeats the same read-only
  assessment; it does not stack authority, change repository state, or start
  work.
- `Proceed` without the retained unconsumed grant and assessment does not create
  authority.
- Discussion such as “the Worker should...” normally proposes behavior; it
  does not activate the Worker.
- If action, inputs, budget, or repository state drift between the assessment
  and approval, the Worker halts and reports the exact difference.
- Cancelling before `Proceed` requires no repository transition because the
  assessment created no canonical execution state; a later attempt begins with
  a new `Spark Up`.

The intended engine cadence is:

```text
STOPPED — key removed
  -> Spark Up inserts and turns the key
READ-ONLY ASSESSMENT — repository remains unchanged
  -> known action: state it and await approval
  -> dirty state or unknown action: report it and await discussion
ACTION APPROVAL
  -> atomically record ACTIVE execution
ACTIVE BOUNDED WORK
  -> Stop Down may be invoked at any time
STOPDOWN — preserve evidence, revoke authority, publish safe halt
  -> STOPPED — key removed
```

This cadence adds one human launch gate, not one approval per operation.

## 3. Cold-start standard

A Worker reconstructs its mandate from the repository rather than relying on
conversation memory.

At minimum it should:

- confirm the root contract is unambiguous;
- read canonical state and every active-phase control completely;
- validate the derived human dashboard;
- verify immutable input hashes and identify the current target, if any;
- run only the checks the active contract requires for a read-only assessment;
- confirm a clean worktree and local/remote equality;
- report the completed boundary and whether the next action is understood;
- report active and inactive authorities separately;
- report provider and spend readiness separately from target authority;
- report halt conditions and prohibited transitions; and
- stop for discussion if the repository is dirty or contradictory, or the next
  action is unknown or ambiguous.

The cold-start report should be concise. The checking may be extensive, but the
stable response should expose decisions and boundaries rather than terminal
transcript.

## 4. Target-bounded autonomy

One target grant should cover the established bounded lifecycle. When the phase
permits it, this includes:

- offline preparation and exact inventory;
- focused packet or batch construction;
- fake-response and replay testing;
- sequential provider calls within a separate positive spend envelope;
- substantive and mechanical review;
- preservation of failed or interrupted evidence;
- correction of generic local mechanics;
- refreezing and retry of affected work;
- canonical state and dashboard maintenance; and
- coherent repository checkpoints.

Avoid converting derivable readiness into a collection of receipts, flags, or
per-call approvals. Source mandate, cumulative budget, validated inputs, prior
review, and the current phase controls should be sufficient whenever they can
determine readiness unambiguously.

Provider consent, provider-call readiness, source authority, spend authority,
and execution release are distinct facts. Never let one silently imply another
unless the active repository contract expressly defines that implication.

## 5. Conservation of System in Worker operation

When ordinary execution becomes difficult, the Worker first seeks to:

1. constrain the current operation;
2. combine duplicated mechanics;
3. correct the existing implementation;
4. simplify it;
5. reuse an established representation; or
6. remove an unnecessary component.

It may repair how the phase operates, but not what the phase is.

A proposed addition must say what it replaces, merges, or removes. If it only
adds a stage, representation, registry, prompt layer, approval, checkpoint,
worker, or synchronization mechanism, it is presumptively the wrong repair.

Every authoritative fact has one canonical home. Dashboards, previews,
inventories, interfaces, task messages, and reports are derived views or
evidence; they do not become parallel authority.

## 6. Semantic quality, not merely schema validity

Passing a schema and filling every row do not establish semantic quality.

Worker implementations should avoid:

- broad default classifications that silently absorb hard cases;
- ordinal or section-range assignment without atom-level verification;
- lexical keyword heuristics standing in for semantic judgment;
- boilerplate rationales that merely restate the chosen answer;
- treating complete coverage as evidence of correctness;
- forcing provisional ontology into tidy settled paths; and
- importing legacy candidate fields as current decisions when the phase marks
  them untrusted.

For semantic work, every record should make it possible to answer:

- Why is this the primary owner rather than a nearby broader or narrower unit?
- Why is the selected relation correct?
- What ontology evidence grounds the decision?
- Which alternatives were considered when the path is open?
- Would an unresolved status preserve truth better than a neat assignment?

Mechanical validation should enforce stable facts such as shape, hashes,
coverage, ordering, controlled values, prohibited paths, and contamination
boundaries. It should not pretend to mechanize judgments it cannot decide.

## 7. Review and correction discipline

The Worker reviews each result before moving past the phase's safe correction
boundary. A failed result is evidence, not disposable inconvenience.

- Preserve provider responses and exact cost before retrying.
- Never silently repair model output and present it as captured output.
- Distinguish transport failure, schema failure, grounding failure, semantic
  failure, and authorial uncertainty.
- Correct the smallest responsible component.
- Re-run the existing focused tests and compatibility checks.
- Halt when correction would change a stage boundary, invariant, authority
  rule, artifact class, or cross-source interpretation.
- Use the phase's unresolved status instead of guessing.

If a Supervisor audit finds completed work mechanically valid but semantically
defective, reopen only that bounded target or record set. Do not advance merely
because the next target derives cleanly.

### Direct-API semantic work

For high-volume semantic work, the provider model should normally run through a
bounded Python caller rather than through repeated Codex turns. This keeps bulk
packet and response tokens out of the Worker's conversational context and makes
provider billing, model selection, raw evidence, and retry behavior explicit.

Python may assemble hash-bound context, preserve raw responses, validate shape
and exact coverage, account for cost, and route exceptions. It must not decide
semantic equivalence, authority, conflict, or synthesis. Where subtle meaning
matters, use one model pass to propose and a fresh pass to audit the unchanged
proposal; only reviewed results enter canonical state. Keep routine stdout to a
compact outcome summary and return abnormalities to LLM adjudication.

## 8. Checkpoint cadence

Checkpoint coherent lifecycle facts, not every micro-operation.

A good checkpoint:

- preserves recoverable evidence;
- advances one canonical representation;
- updates canonical state consistently;
- refreshes the sole dashboard through its renderer;
- passes the required guard and tests;
- has a narrow, truthful commit message;
- pushes successfully; and
- ends with a clean synchronized worktree.

Keep host-privileged operations independently approvable:

- run status rendering and the full guard as separate tool calls;
- put only the exact full-guard command in an elevated call and request its
  narrow stable command prefix;
- run Git staging, read-only inspection, commit, and push as separate tool
  calls belonging to their own narrow approval families; and
- never bundle unlike privileged operations into one escalated shell request.

This preserves the distinction between authorial repository authority and the
Codex host sandbox without converting an authorized source lifecycle into
repeated human permission prompts.

Do not create checkpoint artifact families when Git already provides history.
Do not leave authority activation, source completion, or Stopdown only in an
uncommitted worktree.

## 9. Formal Stopdown

Stopdown is the universal author-invoked safe halt, authority-key removal, and
formal handoff—not merely cessation of activity. It must remain available
before, during, or after bounded work; an incomplete boundary is preserved
rather than marked complete, and no separate pause or abort lifecycle is added.

The Worker should:

1. stop new provider activity;
2. preserve and reconcile any in-flight evidence and cost;
3. complete review or record the exact unresolved boundary;
4. validate the source package or phase output;
5. revoke source-work, phase-work, repository-write, provider-call, and active
   spend authority as applicable in canonical state while preserving any unused
   author-approved balance;
6. refresh the derived dashboard;
7. run the required guard and tests;
8. commit and push the closing transition;
9. confirm a clean worktree and local/remote equality;
10. perform no further repository write; and
11. as its final command action, run exactly `.venv/bin/python
    m050/tools/m050_notify_supervisor.py`. The script uses the installed Codex
    CLI to resume the task named exactly `Compile Supervisor` in the current
    repository and pass exactly `Worker has Stopped Down`. It replaces
    app-tool discovery and messaging rather than adding a fallback path.

A nonzero script result does not invalidate an otherwise valid Stopdown. The
Worker reports it once and does not retry automatically. After the script
returns, the Worker may give its final stable response but performs no further
command, tool, or repository action.

Receipt of the message starts the Supervisor's equivalent read-only assessment.
The Supervisor verifies repository and handoff health, summarizes the Worker's
actions, identifies any defect or next decision, and pauses for discussion. It
does not authorize repair, queued work, another source, or another phase.

## 10. Stable communication

The Worker should keep commentary short and operational:

- what it is checking;
- what boundary it has established;
- what changed materially;
- what is blocked; and
- what it will do next within the active grant.

Meaningful reasoning, decisions, unresolved questions, final counts, costs,
commit identity, and handoff state belong in stable responses. They should not
exist only in transient commentary or terminal output.

When requesting human attention, ask the smallest question that changes the
next legal action. Do not present a broad redesign when one bounded ruling is
enough.

## 11. Phase-construction checklist

Before constructing a Worker thread for a new phase, the Supervisor and Asa
should settle the following in discussion:

### Purpose and boundary

- What transformation does the phase perform?
- What does it explicitly not decide?
- What exact event completes the phase?
- What is the next prohibited transition?

### Canonical representation

- What immutable inputs are hash-bound?
- What one canonical mutable output advances?
- Which views are derived and non-authoritative?
- Which older representations are replaced or retired?

### Deterministic selection

- How is exactly one current source or unit selected?
- Is the next-target choice functional Worker scheduling or an authorial or
  structural decision?
- What completed/rejected boundary is derived?
- What happens if selection is empty, multiple, or drifted?

### Authority and cadence

- What exactly does `Spark Up` grant within the bounded phase mandate?
- What remains separately controlled, especially spend and provider use?
- What must the read-only assessment report?
- What does the read-only assessment establish before action approval?
- What does action approval release without granting anew?
- How is an unused grant cancelled?

### Execution mechanics

- What routine operations are autonomous?
- What local refactoring is permitted?
- What must remain source-agnostic?
- Where is the sequential review boundary?

### Quality and unresolved work

- What statuses preserve uncertainty?
- Which invariants are mechanically decidable?
- Which judgments require semantic or authorial review?
- What samples or distributions expose broad-fallback behavior?

### Halt and Stopdown

- What exact conditions force a halt?
- What evidence must be preserved?
- What authority is revoked at completion?
- What guard, commit, push, synchronization, and notification steps close the
  handoff?

### Conservation accounting

- What existing mechanism is being reused or corrected?
- What language or machinery is replaced?
- Does the proposal add stages, artifacts, representations, handoffs, or
  supervisory machinery?
- If it adds anything, why is that increase necessary and explicitly approved?

## 12. Thread-construction guidance

A new Worker thread should be told to begin read-only and reconstruct its state
from the repository. Its opening instructions should identify:

- its role as the sole Compile Worker, not another supervisory layer;
- the root contract as authoritative;
- the requirement to perform the complete cold start;
- the currently installed phase profile;
- the `Spark Up` / assessment / `Proceed` cadence;
- the one-writer rule;
- the boundaries of local repair under Conservation of System;
- the Stopdown protocol and notification target;
- the prohibition on automatic next-source work; and
- the requirement to preserve meaningful reasoning in stable responses.

Do not copy historical task transcripts into the new Worker as operational
context. If a learning matters, express it through the current contract,
canonical state, phase profile, guard, or a concise non-authoritative
construction note whose status is unmistakable.

## 13. Current integration note

The Atomization-derived two-step cadence is integrated into the active Stage 4
profile: `Spark Up` grants one-source authority, performs a read-only assessment,
and pauses without a repository checkpoint; `Proceed` atomically records and
releases active execution without granting new authority. The root contract,
canonical state, and sole guard remain the operative controls. This reference
does not independently change Worker behavior.
