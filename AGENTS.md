# MEDIAN repository operating contract

This is the sole active root operating contract. If `AGENTS.override.md`
exists, stop: the repository contract is ambiguous. Repository state—not task
memory—is the durable source of operational truth.

## Purpose and scope

The MEDIAN v0.5.0 compile has returned to creation. Its immediate purpose is to
write one coherent authorial Game Design Document from the completed source
library, using human judgment to resolve contradiction, supersession, emphasis,
and final expression.

- The registered source set contains 24 documents: 22 are in compile scope and
  two are non-atomic companions.
- Eighteen sources produced the frozen 5,382-atom authorial library. Four
  in-scope sources remain later or conditional inputs.
- The source documents and atom library are evidence, not final canon.
- MEDIAN v0.5.0 is locked scope. `m051/` is outside it and must not be read,
  searched, summarized, indexed, or used during m050 work unless Asa separately
  authorizes a bounded cross-version task.

## Conservation of System

1. **Conservation of Process:** use the smallest process that safely advances
   the GDD. Automate only a demonstrated repetitive need.
2. **Conservation of Representation:** every authoritative fact has one
   canonical home. Indexes and dashboards are derived aids, never parallel
   authority.
3. **Conservation of Mandate:** perform only the explicitly authorized
   structural or writing task. An unresolved matter is a valid authorial
   outcome.

A component must transform content, enforce an invariant, or preserve necessary
evidence. Otherwise remove or fuse it. Do not create a registry, lifecycle,
handoff, approval, or synchronization layer merely to describe another one.

## Roles and authority

Asa Wember is the sole authorial authority. The Compile Supervisor discusses
structure and method with Asa before changing them, and edits repository state
or GDD material only after Asa grants an explicit bounded task. “The Worker
should…” normally expresses a proposal, not execution authority.

No Compile Worker participates in ordinary authorial creation. A future Worker
would begin read-only and require an expressly installed mandate. Repository
write authority and authorial prose authority are separate; neither follows
from a task title or from access to the filesystem.

Only one task writes the repository at a time. Before a publishing checkpoint,
refresh `STATUS.md`, run the sole full guard, review the diff, then commit and
push. Host sandbox approval remains separate from repository authority.

## Canonical controls

- `m050/control/M050_Compile_State_MEDIANv0_5_0.json` is the sole mutable
  machine-readable current state.
- `STATUS.md` is the sole derived human dashboard.
- `m050/corpus/M050_Authorial_Atom_Corpus_Manifest_MEDIANv0_5_0.json` binds the
  frozen source documents and the authorial atom library.
- `m050/corpus/M050_Authorial_Atom_Corpus_MEDIANv0_5_0.jsonl` is the sole active
  atom-level authorial source library.
- `m050/gdd/M050_GDD_Provisional_Structure_MEDIANv0_5_0.md` is the sole active
  provisional GDD structure.
- `m050/tools/m050_guard.py` is the sole active repository guard.
- `m050/tools/m050_render_status.py` is the sole writer of `STATUS.md`.

The corpus records effective claims after completed authorial triage and
rewrite. It does not carry the retired MSID classifications or partial
reconciliation results; those remain available only in the historical archive.
Corpus atoms do not decide truth, ownership, precedence, document structure, or
final wording.

The Human Rulings source remains frozen and must not be edited as part of
composition preparation. A ruling controls only the precise question it
settles; its presence in the corpus does not give unrelated claims greater
weight.

## Historical archive

`600 archive/m050-information-management/README.md` describes the archive that
preserves the retired extraction,
triage, rewrite, MSID mapping, semantic-reconciliation, provider-call, spend,
Worker-lifecycle, and regression machinery at the final stopped checkpoint.
It grants no authority and is not an active input during ordinary composition.
Consult it only for a specific provenance question or explicit historical
investigation. Do not restore an archived mechanism merely because it exists;
Git history preserves the executable former system.

There is no active tranche, provider configuration, model-spend envelope,
semantic-promotion pipeline, or automatic API authority. Reintroducing any of
them is an architectural change requiring prior discussion and explicit
authorization from Asa.

## Required cold start

At the beginning of a repository-writing session or a newly selected authorial
boundary:

1. Confirm `AGENTS.override.md` is absent.
2. Read this contract and the canonical compile state.
3. Read `STATUS.md` and confirm that it exactly mirrors canonical state.
4. Confirm a clean worktree and local `HEAD` equal to `origin/main`.
5. Confirm the active authority and prohibited inputs before acting.

The frozen corpus manifest does not need to be reread during every chapter
discussion. Read it completely when the source-library boundary is in question,
before corpus-related work, or when the guard reports drift. Surface a cold-start
discrepancy before continuing; a healthy check is not a separate approval gate.

A read-only discussion does not refresh state or run publication tests. Before
releasing changed controls, corpus bindings, structure, or prose, run the
renderer and `.venv/bin/python m050/tools/m050_guard.py --with-tests` as
separate actions.

## Active working method — direct authorial structure

The seven-Part spine of the v0.5 GDD is authorially approved. Asa and the
Compile Supervisor refine the selected chapters and sections directly in
conversation, using
`m050/gdd/M050_GDD_Provisional_Structure_MEDIANv0_5_0.md` as the sole working
structure.

Current approval progress, the selected authorial boundary, and the next legal
transition live only in canonical compile state and derived `STATUS.md`. Do not
copy them into this contract, `README.md`, or the structure document's status
header.

This working method grants the Compile Supervisor repository-write and
GDD-structure authority only for the approved provisional-structure refinement.
It grants no corpus modification or compiled-prose authority.

During structure work:

- derive a provisional organization from design needs and the governing source
  documents, not from MSID completeness;
- use the atom corpus to retrieve evidence for each section;
- let Asa resolve contradictions, supersession, omissions, emphasis, and final
  wording in the context where they matter;
- preserve source and atom traceability as a writing aid;
- permit the structure to evolve through explicit author discussion; and
- defer later or conditional source use until its intended authorial moment.

The working cadence is deliberately small:

1. Asa selects or reopens a structural question.
2. The Supervisor retrieves only the evidence needed to discuss it.
3. Asa resolves or approves the structure in conversation.
4. The Supervisor writes only the approved result.
5. One publication checkpoint updates canonical state and `STATUS.md`, runs the
   guard, reviews the diff, commits, and pushes.

The approved seven-Part spine remains stable unless Asa reopens it. Chapter and
section titles remain provisional until authorially approved. Discussion may
leave a question unresolved without creating another workflow or holding file.

Do not require every atom to acquire a semantic unit or perfect classification
before prose can be written. Do not create an automated discernment system,
section-assignment ledger, or authoring interface until observed writing work
shows that it is necessary.

## Gates and halt conditions

The active repository has three gates:

1. **Integrity gate:** the guard verifies the frozen source files, corpus hash,
   5,382 unique atom records, state shape, archive separation, m051 exclusion,
   and exact STATUS rendering.
2. **Authorial gate:** structure, contradiction resolution, and final prose
   require Asa’s explicit judgment or approval.
3. **Publication gate:** any control, structure, or prose checkpoint requires a
   refreshed dashboard, passing full guard, reviewed diff, commit, push, clean
   worktree, and local/remote equality.

Halt for source or corpus drift, a dirty or unsynchronized cold start,
contradictory authority, an attempted m051 input, uncertainty that would alter
structure without author discussion, or any proposal to restore retired API or
reconciliation machinery. Ordinary unresolved content should be surfaced to Asa
inside the writing process rather than converted into a new workflow.

## STATUS contract

`m050/tools/m050_render_status.py` derives `STATUS.md` deterministically from
canonical state. Agents must not patch dashboard prose manually. The dashboard
contains the current preparation or composition state, source-library boundary,
progress, present activity, and next legal transition. It carries no provider
spend field because provider execution is retired.
