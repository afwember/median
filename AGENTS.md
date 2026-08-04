# MEDIAN repository operating contract

This is the sole active root operating contract. If `AGENTS.override.md`
exists, stop: the repository contract is ambiguous. The repository—not a task
transcript—is the durable source of operational truth.

## Purpose and scope

- “The compile” is the complete controlled pipeline: evidence preparation and
  atomization, semantic review, mapping, reconciliation, and final document
  production.
- Gate 2 registers 24 sources. Two are non-atomic companions. Compile scope is
  22 sources: 4 atomized legacy seeds and 18 outstanding, comprising 14
  pre-reconciliation sources and 4 later or conditional sources.
- Never describe the four-source legacy seed or its dormant review artifacts as
  whole-corpus completion.
- MEDIAN v0.5.0 sources are frozen. `m051/` is outside the compile.

## Conservation of System

The compilation method is closed during execution. A compile task executes the
method; it does not redesign the method in response to ordinary difficulty.

1. **Conservation of Process:** constrain, combine, correct, simplify, or reuse
   existing machinery before proposing anything new.
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

## Canonical controls

- `m050/extraction/control/M050_Compile_State_MEDIANv0_5_0.json` is the sole
  mutable machine-readable current state. Update it in place; Git is its
  history.
- `STATUS.md` is the only derived human dashboard. It is never execution
  authority.
- `m050/extraction/control/M050_Compile_Source_Processing_Order_v0_1_MEDIANv0_5_0.json`
  controls source order.
- `m050/tools/m050_guard.py` is the sole active repository guard.
- Historical checkpoints, bootstrap packets, active-index versions, execution
  standards, authority policies, and versioned guard wrappers are retired.
  Do not recreate those families.

## Required cold start

1. Confirm `AGENTS.override.md` is absent.
2. Read the canonical compile state completely.
3. Read the source processing order completely.
4. Read `STATUS.md` and confirm it exactly mirrors the canonical state.
5. Run `.venv/bin/python m050/tools/m050_guard.py --with-tests` before
   control/code release, provider-enabled configuration release, whole-source
   acceptance, and commit/push. Routine provider capture uses the extraction
   machine’s focused packet, source, spend, cache, response, and prior-review
   checks.
6. Report concisely: corpus vector; selected and next source; accepted/rejected
   chunk boundary; source-work and spend authority; halt conditions; prohibited
   later stages; next possible transition; STATUS freshness; and whether local
   `HEAD` equals `origin/main`.

No separate successor packet is required. These canonical files are the handoff.

## Authority model

- Asa Wember remains the sole authorial authority.
- Only one task may write the repository at a time. A successor task begins
  read-only until Asa explicitly grants a bounded repository task or names one
  Spec Doc for source work.
- A bounded repository task authorizes only its stated change.
- A source-work grant is confined to one named source and ends when that source
  reaches source-bounded candidate acceptance. Starting the next source always
  requires a new explicit grant from Asa.
- The task may derive exact, machine-consumable lifecycle receipts from an
  active source-work grant. Those receipts bind calls and configurations for
  enforcement; they are not additional user-approval checkpoints.
- Provider calls additionally require an active cumulative spend envelope with
  enough remaining balance for the next conservative cache-miss ceiling.
  Spend authority never selects or advances a source.

Within an active source-work grant and spend envelope, the task may proceed
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

## Source lifecycle invariants

- Follow the approved processing order; never choose by filename or task memory.
- Every new provider-eligible source begins with a content/provenance identity
  card, complete offline preparation, and representative pilot calibration.
  Prior-source success is evidence, not source transfer.
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

## Artifact and state discipline

- Frozen sources and accepted evidence are immutable.
- Preserve raw provider responses, compact outcomes, exact usage/cost, rejected
  attempts, authorizations, and hash-chained run ledgers.
- Reuse the source-agnostic extraction machine. Source differences belong in
  declarative configuration, not source-specific workers.
- Ordinary provider attempts use the existing call packet, raw response,
  compact outcome, spend record, and one source ledger. Do not create a
  file-per-transition family.
- Active operating instructions, guard code, and current state are maintained
  in place. Do not version them inside the working tree; Git supplies history.
- Record exceptional material in the existing outcome and ledger unless that is
  genuinely unsafe or impossible.
- A normal compile operation has no process delta.

## Hard boundaries

- A deterministic-only source never enters provider calibration. A non-atomic
  companion never enters atomization.
- Semantic acceptance, mapping, reconciliation, and compiled prose remain
  prohibited until corpus atomization is complete and separately released.
- Google Sheets interaction remains paused.
- Credentials never enter the repository, prompts, receipts, or reports.
- Keep user-facing reports to decisions, defects, spend exhaustion, source
  milestones, and completion.

## STATUS contract

Refresh `STATUS.md` after every accepted or rejected chunk, lifecycle halt,
authorization or spend change, source milestone, and before commit or push.
Derive it only from the canonical compile state. The first line below its title
is a human-readable timestamp rounded to the nearest second. Its final nonblank
line is cumulative provider cost rounded upward to the cent; exact cost remains
in machine evidence. The guard rejects a stale or contradictory dashboard.
