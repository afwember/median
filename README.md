# MEDIAN

[Current compile status](STATUS.md)

**MEDIAN** is an atmospheric animal colony-builder set on highway median strips. Players guide a small civilization of rabbits, squirrels, or wood mice: establishing a persistent colony, crossing live traffic, exploring a changing corridor, and bringing discoveries home.

The project’s primary deliverable is an illustrated, system-complete sourcebook. It is conceived by Asa Wember.

## Current work

MEDIAN v0.5.0 is being assembled from a substantial set of system specifications developed after the v0.4.6 Game Design Document. The current effort is building a source-preserving atomic evidence corpus before MSID mapping, cross-source reconciliation, comparison with the v0.4.6 baseline, and final compilation.

Completed legacy extractions are being retained where their source quotations remain verifiable; the extraction process itself is being simplified and rebuilt with stronger boundaries and auditability.

Current status:

- The corpus boundary is `24 / 22 / 4 / 18 = 14 + 4`.
- Four accepted legacy source candidates are preserved; Authorial Grammar is the first outstanding source.
- The source-agnostic extraction engine, current configuration, exact provider evidence, and focused tests are active.
- Later semantic acceptance, mapping, reconciliation, and compiled prose remain blocked until atomization is complete.
- MEDIAN v0.5.1 material is isolated under `m051/` and excluded from the v0.5.0 compile.

## Repository map

```text
m050/docs/                 Current v0.5.0 sources and the v0.4.6 baseline
m050/extraction/accepted/  Four immutable accepted legacy source candidates
m050/extraction/control/   Canonical state, source order, manifests, and active configuration
m050/extraction/engine/    Source-agnostic extraction code and focused regression tests
m050/extraction/evidence/  Human Rulings evidence needed by Authorial conformance
m050/extraction/runs/      Current accepted/rejected provider evidence and frozen pilot packet
m051/                      Post-v0.5.0 development; excluded from the current compile

100 canon/ – 600 archive/  Earlier project organization and sourcebook-production history
300 art/                   Splash image plus thumbnail-backed external artwork manifest
```

For recovery after a restart, context compaction, or task handoff, start with
root `AGENTS.md`, then read the canonical compile state, the canonical source
processing order, and `STATUS.md`. There is no spreadsheet, successor packet,
active-index chain, or second process constitution.

## Core rule

A filename, title, or document’s internal claim of authority does not establish its identity or precedence. Sources are classified from their contents and genealogy; extraction preserves their testimony, and authority is resolved only during reconciliation.
