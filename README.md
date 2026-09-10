# MEDIAN

[Current compile status](STATUS.md)

**MEDIAN** is an atmospheric animal colony-builder set on highway median strips. Players guide a small civilization of rabbits, squirrels, or wood mice: establishing a persistent colony, crossing live traffic, exploring a changing corridor, and bringing discoveries home.

The project’s primary deliverable is an illustrated, system-complete sourcebook. It is conceived by Asa Wember.

## Current work

MEDIAN v0.5.0 is being assembled from a substantial set of system specifications developed after the v0.4.6 Game Design Document. Eighteen pre-reconciliation sources have been atomized, authorially triaged and rewritten where necessary, and mapped to MSIDs. The current phase reconciles their 5,382 eligible claims into one coherent semantic base before the v0.4.6 baseline audit and final compilation.

Verified legacy extractions are retained alongside candidates produced by the current source-agnostic extraction engine. Every accepted candidate preserves one source's testimony; acceptance at this stage does not establish semantic authority or final canon.

Current status:

- The registered corpus contains 24 sources, of which 22 are in compile scope and two are non-atomic companions.
- Live progress, the current semantic boundary, the next permitted transition, and remaining spend authority are reported in [STATUS.md](STATUS.md).
- The canonical reconciliation record assigns each eligible atom to exactly one reviewed semantic proposition or explicit unresolved disposition.
- Direct API models perform semantic proposal and independent review; deterministic Python binds inputs, validates coverage and evidence, and keeps routine model output outside the Codex conversation.
- Baseline comparison and compiled prose remain blocked until reconciliation is complete.
- MEDIAN v0.5.1 material is isolated under `m051/` and excluded from the v0.5.0 compile.

## Repository map

```text
m050/docs/                 Current v0.5.0 sources and the v0.4.6 baseline
m050/extraction/accepted/  Immutable source-bounded accepted candidates
m050/extraction/control/   Canonical state, source order, identities, manifests, and configuration
m050/extraction/engine/    Source-agnostic extraction implementation and regression tests
m050/extraction/evidence/  Preserved evidence supporting extraction and later reconciliation
m050/extraction/runs/      Call packets, raw responses, compact outcomes, and source ledgers
m050/mapping/              Completed Stage 4 vocabulary and atom-to-MSID mappings
m050/reconciliation/       Authorial decisions and the canonical Stage 5 semantic units
m050/tools/                Active reconciliation tool, guard, and deterministic STATUS renderer
m051/                      Post-v0.5.0 development; excluded from the current compile

100 canon/ – 600 archive/  Earlier project organization and sourcebook-production history
```

Artwork development, manifests, and thumbnails now live in the separate
`median-support` Studio repository.

For recovery after a restart, context compaction, or task handoff, start with
root `AGENTS.md`, then read the canonical compile state, its named active-phase
controls, and `STATUS.md`. The repository controls execution; chat
transcripts and the derived dashboard do not. There is no successor packet,
active-index chain, or second process constitution.

## Core rule

A filename, title, or document’s internal claim of authority does not establish its identity or precedence. Sources are classified from their contents and genealogy; extraction preserves their testimony, and authority is resolved only during reconciliation.
