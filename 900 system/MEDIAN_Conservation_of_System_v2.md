# Conservation of System

## A governing principle for the MEDIAN Compiler

> A normal compilation operation should change the content while leaving the
> Compiler unchanged.

Conservation of System, or **CoS**, is the principle that difficulty should not
automatically produce machinery.

When a process encounters a problem, its first response should be to constrain,
combine, correct, simplify, divide, or reuse what already exists. A new stage,
document, schema, role, or supervisory mechanism is justified only when the
existing system genuinely cannot perform the necessary function. Even then,
the proposed addition should replace, merge, or eliminate enough existing
machinery to justify its continued cost.

CoS is not resistance to change, nor is it a demand that every system remain
small. It treats complexity as a liability that must earn its existence. A
change pays for itself when it makes the whole system more coherent,
understandable, and capable—not merely when it solves the immediate local
problem.

This principle matters especially in an agent-operated Compiler. Faced with a
difficulty, a capable language model can readily invent a review pass,
classification scheme, ledger, exception family, or supervisory procedure.
Each invention may appear responsible in isolation. Taken together, they can
turn a direct transformation into a process whose primary output is the
maintenance of its own bureaucracy.

CoS prevents the Compiler from solving complexity by manufacturing more
complexity.

## The four conservation principles

### 1. Conservation of Process

Do not create a new stage, pass, procedure, role, or workflow branch when an
existing operation can be constrained, combined, corrected, simplified,
divided, or reused.

A proposed process addition must identify:

- the exact failure it addresses;
- why existing machinery cannot safely address that failure;
- what existing machinery it replaces, merges, or removes; and
- its net effect on stages, handoffs, persistent artifacts, and maintenance.

An addition that merely sits beside existing machinery is presumptively
rejected.

This does not prohibit refactoring. Dividing an overloaded component into two
clearer components may conserve the system when it reduces total coupling,
special cases, and coordination cost. CoS judges the resulting system, not the
raw number of files or functions.

### 2. Conservation of Representation

Every authoritative fact should have one canonical home.

Derived dashboards, packets, indexes, and summaries may present canonical
information, but they must not become parallel sources of authority. When
several files independently represent the same state, every change creates a
synchronization obligation. Adding another synchronization mechanism compounds
the defect.

In the MEDIAN Compiler, canonical compile state carries operational progress,
authority, and cumulative spend. The human-readable status document mirrors
that state but does not govern execution. Git preserves history, so the working
tree does not require a new versioned control document for every transition.

Derived readiness follows the same principle. Provider readiness is computed
from canonical facts—current source authority, validated material, sequential
review, and sufficient budget—instead of being stored as another permission
flag. A derived fact can still be wrong if its inputs or derivation are wrong,
but it cannot independently drift away from those inputs.

### 3. Conservation of Mandate

Every actor and operation must remain within its assigned transformation.

The Compile Worker may solve ordinary problems inside the active Phase, but it
may not convert those problems into permission to redesign the Compiler. The
Supervisor may change the Compiler's structure after discussion and explicit
authorization, but structural authority is not permission to expand the system
casually.

When a problem falls outside an actor's mandate, the correct output is a halt
and a bounded review request—not unilateral expansion. An unresolved matter is
a legitimate result.

Mandate conservation is particularly important for fuzzy boundaries. A model
can often justify a convenient local fix as harmless. Bright prohibitions
therefore remain explicit: no unapproved source or Phase transition, no
overspending, no relaxation of invariants, and no source-specific workaround
embedded in the generic machine.

### 4. Conservation of Authority

Authority should be explicit, singular, and no broader than necessary.

The repository has one writer at a time. Authority is not duplicated across
threads, inferred from activity, or carried indefinitely from one Phase or
source to another. Provider permission derives from an active source-work grant
and sufficient cumulative budget rather than from overlapping receipts,
per-call approvals, and permission flags.

Conservation of Authority separates broad operational freedom from structural
freedom. The Worker can act independently within its assigned duty without
acquiring the right to change the terms of that duty.

## The closed Compiler

The MEDIAN compilation method is closed during execution.

A compile operation executes the established method. It may repair or simplify
the existing mechanics of its authorized Phase, but it does not redesign Phase
structure, stage boundaries, artifact classes, authority rules, or cross-Phase
interfaces in response to ordinary difficulty.

Repeated failure does not automatically justify new machinery. It does,
however, provide evidence. Recurring halts of the same material type indicate
that the current system may be under-capable. That pattern warrants Supervisor
review. It does not itself authorize an addition.

This distinction provides CoS with a release valve: restraint remains the
default, while persistent evidence can demonstrate that genuine structural
change is needed.

## The dual-thread paradigm

MEDIAN uses two long-running tasks connected to the same repository:

- the **Supervisor**; and
- the **Compile Worker**.

This is a division of mandate, not an agent hierarchy and not another pipeline
stage. Both tasks may understand and inspect the repository. Only one may write
at a time.

### The Supervisor

The Supervisor owns structural change.

It works conversationally with the human operator to evaluate the Compiler,
revise its governing contract, simplify its architecture, retire obsolete
machinery, and prepare transitions between overall Phases. It does not
automatically redesign the system and does not gain source-work or provider
authority merely because it can see the repository.

The Supervisor is fully bound by CoS. Because it can modify the architecture,
its obligation is especially strong. A structural proposal should first seek
reduction, reuse, constraint, correction, division, or fusion of existing
machinery. A net increase requires explicit discussion and authorization.

The Supervisor may discuss and perform read-only inspection while the Worker
operates. It must never write the repository while the Worker holds authority.

### The Compile Worker

The Compile Worker owns operational control of the currently authorized Phase
duties.

Its mandate is intentionally broad inside that boundary. During atomic
extraction, it may:

- prepare and validate source material;
- plan, quantize, and recalibrate chunks;
- make sequential provider calls when source and budget authority permit;
- preserve and review returned material;
- diagnose ordinary failures;
- correct or simplify existing prompts, schemas, configuration, chunking,
  validation, tests, and source-agnostic engine behavior;
- replay affected evidence offline;
- refreeze and retry failed chunks;
- reconcile state, status, and exact spend; and
- commit and push coherent checkpoints.

This breadth is deliberate. The Worker should not require human intervention
for every inexpensive call, local correction, or routine calibration defect.

Its architectural authority remains narrow. It may not:

- advance to a new source without explicit authorization;
- advance to another overall Phase;
- add a stage or artifact family;
- change cross-Phase architecture or authority rules;
- relax an invariant;
- alter the structural controls used to judge its own work;
- introduce a source-specific workaround into the generic machine; or
- resolve a matter that requires human authorial judgment.

The Worker therefore has wide duty control but no general system-design
mandate.

## One writer and the human mutex

The single-writer rule is presently a logical and human-enforced mutex. It is
implemented through explicit authority transfers, canonical state, clean Git
checkpoints, and the Stopdown and Sparkup handovers. It is not an operating-
system lock.

That limitation is intentional and should be understood plainly. A lockfile or
coordination service would introduce ownership, recovery, and stale-lock
machinery. Such a mechanism should be considered only if concurrent-writing
failures actually recur. Until then, explicit handover and human discipline are
the proportionate control.

## Formal handovers

Because both tasks share one repository, their separation depends on two named
handover processes.

### Stopdown

**Stopdown** is the process by which the Compile Worker safely finishes its
current operation and relinquishes control.

A complete Stopdown consists of:

1. stopping further provider activity;
2. preserving any in-flight response and reconciling its exact cost;
3. completing the required review or recording the precise unresolved
   boundary;
4. updating canonical compile state and the human status mirror;
5. running the required guard and tests;
6. committing and pushing the complete checkpoint;
7. confirming a clean worktree and equality between local and remote heads; and
8. relinquishing repository-writing and Phase-work authority.

After Stopdown, the Worker may discuss or observe, but it may not write.

### Sparkup

**Sparkup** is the process by which the Supervisor returns operational control
to the Compile Worker.

A complete Sparkup consists of:

1. completing the authorized structural work;
2. updating governing controls in place;
3. running the complete guard and tests;
4. committing and pushing a clean checkpoint;
5. relinquishing Supervisor writing authority;
6. having the Worker perform a cold-start audit from that checkpoint;
7. confirming the active Phase, source boundary, budget, prohibitions, and next
   possible transition; and
8. completing the human operator's explicit transfer of repository-writing and
   named Phase or source authority to the Worker.

Sparkup never silently authorizes the next source. If the prior source is
complete, beginning another source requires its own explicit grant.

There is never a period in which both tasks may write. Stopdown must finish
before Supervisor writing begins. Sparkup must finish before Worker writing
resumes.

## Cold-start audit and fresh-task creation

A **cold-start audit** is a deliberate reconstruction of operating state from
the repository. It requires the Worker to reread canonical controls and verify
the current boundary rather than relying on conversational memory.

It does not necessarily require a newly created task. A continuing Worker must
perform the same audit after Sparkup. A fresh Worker task is useful as an
occasional continuity test, particularly at a Phase boundary, but requiring one
at every handover would discard valuable operational context and repeatedly
create avoidable transfer risk.

The durable invariant is:

> Any qualified Worker, continuing or fresh, must be able to reconstruct the
> authorized operating state from the repository alone.

Conversation can improve execution, but it must never be the sole home of
operational truth.

## CoS evaluation

“CoS eval” is a standing analytical request.

When a CoS eval is requested, the current discussion, proposal, or
implementation is examined for:

- new stages, roles, artifacts, schemas, or handoffs;
- duplicated representations of authority or state;
- expansion beyond the current mandate;
- unnecessary persistence of temporary machinery;
- opportunities to constrain, combine, correct, simplify, divide, reuse, or
  remove;
- whether new complexity replaces existing complexity or merely joins it;
- whether authority remains singular and properly bounded; and
- the net process delta.

A CoS eval is read-only analysis by default. It does not authorize changes. Its
preferred result is the smallest correction that preserves the necessary
invariants.

## Mechanical enforcement and judgment

CoS cannot depend entirely on an actor judging its own compliance. A capable
model can provide a persuasive but mistaken explanation for why new machinery
is necessary.

The Compiler therefore enforces concrete invariants mechanically where they
already have stable definitions: canonical-state consistency, artifact
topology, frozen evidence, source order, budget arithmetic, provider bindings,
and prohibited authorities. Mechanical enforcement should strengthen the
existing guard rather than create a second CoS enforcement system.

Not every boundary can be reduced to a path or count. A raw file-count rule can
punish useful refactoring, while a broad path allowlist can permit semantic
mandate drift inside an approved directory. Human review remains necessary for
structural judgment.

The correct balance is to mechanize clear invariants, preserve explicit human
authority at fuzzy boundaries, and add no control merely because it is
possible.

## Case study: provider-readiness simplification, August 2026

An early provider workflow represented overlapping aspects of authority through
source grants, a cumulative spend envelope, lifecycle receipts, per-call
approval, chunk authorization lists, full-source flags, and successor spend
files. The result was safe but cumbersome: low-cost routine calls repeatedly
returned to the human operator, while several artifacts described nearly the
same permission state.

Applying CoS produced a smaller model:

- one named source-work grant;
- one canonical cumulative budget;
- one validated packet and configuration;
- one sequential review invariant;
- one canonical compile state; and
- existing responses, outcomes, and run ledgers as evidence.

Provider readiness became a derived fact rather than a stored permission flag.
A failed chunk consumes its actual spend and pauses calls until correction and
replay pass, but it does not automatically revoke the source mandate or require
a new transaction approval.

The change removed redundant artifacts and handoffs while retaining budget
enforcement, packet binding, sequential review, failure preservation, and human
control of source transitions. It is an example of CoS increasing operational
autonomy by reducing process.

## Addendum: CoS in the real world

CoS is not a physical conservation law. It is a synthesis of several durable
real-world practices.

In engineering, it resembles simplicity and minimum-parts design: every
additional component creates another failure mode, maintenance burden, and
interface.

In software, it appears as single-source-of-truth architecture, separation of
concerns, least privilege, and resistance to speculative abstraction. Mature
systems often improve by deleting or consolidating layers rather than adding
them.

In manufacturing, it resembles lean practice: remove steps that do not
transform the product, enforce quality, or preserve necessary evidence.

In accounting and records management, it appears as canonical ledgers and
controlled derived reports. Parallel authoritative books are dangerous because
reconciliation can become a permanent industry of its own.

In constitutional and organizational design, it appears as divided powers,
explicit jurisdiction, and formal transfer of authority. Separation is useful
only when domains are clear and concurrent control is prevented.

In aviation, medicine, and other safety-critical fields, it appears in bounded
procedures and explicit handoffs. Operators receive meaningful autonomy within
their competence, while unusual conditions trigger escalation rather than
improvisational system redesign.

In science and philosophy, it resembles parsimony: an explanation should not
multiply entities beyond necessity. CoS adds an operational concern. Every new
concept introduced into a living process must be maintained, synchronized,
taught, and governed.

The broad real-world lesson is simple:

> Complexity should be treated as a liability that must earn its continued
> existence.

For MEDIAN, the practical expression remains:

> A normal compilation operation should change the content while leaving the
> Compiler unchanged.
