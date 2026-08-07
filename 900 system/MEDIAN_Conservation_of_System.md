# Conservation of System

## A governing principle for the MEDIAN Compiler

Conservation of System, or CoS, is the principle that difficulty should not
automatically produce machinery.

When a process encounters a problem, its first response should be to constrain,
combine, correct, simplify, or reuse what already exists. A new stage,
document, schema, role, or supervisory mechanism is justified only when the
existing system genuinely cannot perform the necessary function. Even then,
the proposed addition should replace or eliminate at least as much machinery as
it introduces.

CoS does not mean resistance to change. It means that change must pay for
itself.

For the MEDIAN Compiler, this principle is particularly important because
procedural expansion can be deceptively reasonable. A failed extraction
suggests a new review. The review suggests a new classification. The
classification suggests a ledger. The ledger suggests a reconciliation pass.
Each addition may be defensible in isolation while the complete process becomes
slower, harder to understand, and increasingly dependent on its own
bureaucracy.

CoS prevents the Compiler from solving complexity by manufacturing more
complexity.

## The four conservation principles

### 1. Conservation of Process

Do not create a new stage, pass, procedure, role, or workflow branch when an
existing operation can be corrected, constrained, combined, or simplified.

A proposed process addition must identify:

- The exact failure it addresses.
- Why existing machinery cannot safely address it.
- What existing machinery it replaces, merges, or removes.
- Its net effect on stages, handoffs, and persistent artifacts.

An addition that merely sits beside existing machinery is presumptively
rejected.

### 2. Conservation of Representation

Every authoritative fact should have one canonical home.

Derived dashboards, packets, and summaries may present canonical information,
but they must not become parallel sources of authority. When several files
independently represent the same state, every change creates a synchronization
problem. Adding another synchronization mechanism only compounds the defect.

In the current Compiler, canonical compile state carries source authority,
progress, and cumulative spend. `STATUS.md` is a human-readable mirror, not a
second authority. Git supplies history, so the repository does not need a new
versioned control document for every transition.

### 3. Conservation of Mandate

Every actor and operation must remain within its assigned transformation.

The Compile Worker may solve ordinary problems inside the active Phase, but it
may not convert those problems into permission to redesign the Compiler. The
Supervisor may change the Compiler's structure after discussion and
authorization, but that authority is not permission to expand the system
casually.

When a problem falls outside an actor's mandate, the correct output is a halt
and a bounded review request—not unilateral expansion.

### 4. Conservation of Authority

Authority should be explicit, singular, and no broader than necessary.

The repository has one writer at a time. Authority is not duplicated across
threads, inferred from activity, or carried indefinitely from one Phase or
source to another. Provider permission is derived from the active source-work
grant and cumulative budget rather than represented through multiple receipts
and approval flags.

This principle prevents both conflicting writes and the gradual accumulation
of overlapping authority systems.

## The dual-thread paradigm

MEDIAN uses two long-running threads connected to the same repository:

- The Supervisor
- The Compile Worker

This is a division of responsibility, not a hierarchy of agents and not an
additional workflow layer.

Both threads may understand and inspect the same repository. Only one may write
at a time.

### The Supervisor

The Supervisor owns structural change.

It works conversationally with Asa to evaluate the Compiler, revise its
governing contract, simplify its architecture, retire obsolete machinery, and
prepare transitions between overall Phases. It does not automatically redesign
the system and does not perform active Phase work merely because it can see the
repository.

The Supervisor is fully bound by CoS. Indeed, because it can modify the
architecture, its obligation is especially strong. A structural proposal
should normally reduce or consolidate machinery. Any net increase requires
explicit discussion and authorization.

### The Compile Worker

The Compile Worker owns operational control of the currently authorized Phase
duties.

Its mandate is wide within that boundary. During atomic extraction, it may:

- Prepare and validate source material.
- Plan and recalibrate chunks.
- Make sequential provider calls when source and budget authority permit.
- Review returned material.
- Diagnose ordinary failures.
- Correct or simplify prompts, schemas, configuration, chunking, validation,
  tests, and source-agnostic engine behavior.
- Replay affected evidence offline.
- Refreeze and retry failed chunks.
- Maintain canonical state and `STATUS.md`.
- Commit and push coherent checkpoints.

This freedom is deliberate. The Worker should not require human intervention
for every inexpensive call or ordinary calibration defect.

Its freedom nevertheless has hard borders. It may not:

- Advance to a new source without explicit authorization.
- Advance to another overall Phase.
- Add a new stage or artifact family.
- Change cross-Phase architecture.
- Relax an invariant.
- Introduce a source-specific workaround into the generic machine.
- Resolve an issue requiring authorial judgment.
- Continue when the authorized budget cannot cover the next conservative call
  ceiling.

The Worker therefore has broad execution authority but narrow architectural
authority.

## Formal handovers

Because both threads share the same working repository, their separation is
enforced through two explicit handovers.

### Stopdown

Stopdown is the process by which the Compile Worker finishes its current
operation and relinquishes repository control.

A complete Stopdown consists of:

1. Stopping further provider activity.
2. Preserving any in-flight response and reconciling its exact cost.
3. Completing the current required review or recording the precise unresolved
   boundary.
4. Updating canonical compile state and `STATUS.md`.
5. Running the required guard and tests.
6. Committing and pushing the complete checkpoint.
7. Confirming a clean worktree and equality between local `HEAD` and
   `origin/main`.
8. Relinquishing repository-writing and Phase-work authority.

After Stopdown, the Worker may discuss or observe, but it may not continue
writing.

### Sparkup

Sparkup is the process by which the Supervisor returns operational control to
the Compile Worker.

A complete Sparkup consists of:

1. Completing the authorized structural work.
2. Updating the governing contract and canonical controls in place.
3. Running the complete guard and tests.
4. Committing and pushing a clean checkpoint.
5. Relinquishing Supervisor writing authority.
6. Having the Worker perform a cold start from that exact checkpoint.
7. Confirming the active Phase, source, boundary, budget, prohibitions, and next
   transition.
8. Completing Asa's explicit transfer of repository-writing and named
   Phase/source authority to the Worker.

The Supervisor prepares and communicates the handover, but it does not silently
manufacture Asa's authority.

There is never a period in which both threads may write. Stopdown must finish
before Supervisor writing begins, and Sparkup must finish before Worker writing
resumes.

## CoS evaluation

“CoS eval” is a standing analytical request.

When Asa asks for a CoS eval, the current discussion, proposal, or
implementation is examined for:

- New stages, roles, artifacts, schemas, or handoffs.
- Duplicated representations of authority or state.
- Expansion beyond the current mandate.
- Unnecessary persistence of temporary machinery.
- Opportunities to constrain, combine, correct, simplify, reuse, or remove.
- Whether new complexity replaces existing complexity or merely joins it.
- Whether authority remains singular and properly bounded.
- The net process delta.

A CoS eval is analytical by default. It does not authorize changes. Its
preferred outcome is the smallest correction that preserves the required
invariants.

## What CoS has changed in the Compiler

The recent provider-readiness retool is a direct application of CoS.

Previously, provider execution involved source authority, a cumulative spend
envelope, lifecycle receipts, per-call authorization, chunk authorization
lists, full-source flags, successor spend files, and repeated human approvals.
Several artifacts represented overlapping aspects of the same decision.

The simplified model uses:

- One named source-work grant.
- One canonical cumulative budget.
- One validated packet and configuration.
- One sequential review invariant.
- One canonical compile state.
- Existing raw responses, outcomes, and run ledgers as evidence.

Provider readiness is now derived from these facts. It is not stored as another
permission flag.

A failed chunk consumes its actual spend and pauses further calls until
correction and replay pass. It does not automatically revoke the source mandate
or require a new transaction approval. This allows the Worker to exercise
meaningful judgment while preserving the boundaries that require human
involvement.

The result is a smaller process with greater operational autonomy and no
relaxation of its important safeguards.

## Addendum: CoS in the real world

CoS is not a physical conservation law. It is a synthesis of several durable
real-world practices.

In engineering, it resembles simplicity and minimum-parts design: every
additional component creates another failure mode, maintenance burden, and
interface.

In software, it appears as single-source-of-truth architecture, separation of
concerns, least privilege, and resistance to speculative abstraction. A mature
system often improves by deleting layers rather than adding them.

In manufacturing, it resembles lean practice: remove steps that do not
transform the product, enforce quality, or preserve necessary evidence.

In accounting and records management, it appears as canonical ledgers and
controlled derived reports. Parallel authoritative books are dangerous because
reconciliation becomes a permanent industry of its own.

In constitutional and organizational design, it appears as divided powers,
explicit jurisdiction, and formal transfer of authority. Separation is useful
only when domains are clear and concurrent control is prevented.

In aviation, medicine, and other safety-critical fields, it appears in bounded
procedures and explicit handoffs. Operators receive meaningful autonomy within
their competence, while unusual conditions trigger escalation rather than
improvisational system redesign.

In science and philosophy, it resembles parsimony: an explanation should not
multiply entities beyond necessity. But CoS adds an operational concern. Every
new concept introduced into a living process must be maintained, synchronized,
taught, and governed.

The broad real-world lesson is simple:

> Complexity should be treated as a liability that must earn its continued
> existence.

For MEDIAN, the corresponding rule is:

> A normal compilation operation should change the content while leaving the
> Compiler unchanged.
