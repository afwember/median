# MEDIAN

[Current compile status](STATUS.md)

**MEDIAN** is an atmospheric animal colony-builder set on highway median strips. Players guide a small civilization of rabbits, squirrels, or wood mice: establishing a persistent colony, crossing live traffic, exploring a changing corridor, and bringing discoveries home.

The project’s primary deliverable is an illustrated, system-complete sourcebook. It is conceived by Asa Wember.

## Current work

MEDIAN v0.5.0 is being assembled from a substantial set of system specifications developed after the v0.4.6 Game Design Document. The current effort is building a source-preserving atomic evidence corpus before MSID mapping, cross-source reconciliation, comparison with the v0.4.6 baseline, and final compilation.

Completed legacy extractions are being retained where their source quotations remain verifiable; the extraction process itself is being simplified and rebuilt with stronger boundaries and auditability.

Current status:

- Gates 1–4 are complete: process diagnosis, target-process definition, legacy-extraction reuse review, source identity correction, and repository cleanup.
- Gate 5 is in progress. Its locked Mac Mini runtime, artifact contracts, source-independent offline engine foundation, and regression suite are implemented and verified.
- The v0.5.0 corpus is frozen by exact path and hash; only Codex changes the repository under explicit author direction.
- External model extraction remains paused until Gate 5 completes and the author separately approves an exact positive-cost work order.
- MEDIAN v0.5.1 material is isolated under `m051/` and excluded from the v0.5.0 compile.

## Repository map

```text
m050/docs/                 Current v0.5.0 sources and the v0.4.6 baseline
m050/extraction/           Accepted evidence, audits, progress, and compact legacy evidence
m050/extraction/engine/    Gate 5 schemas, deterministic tooling, and offline regression suite
m050/extraction/progress/  Human-readable trackers and compile cost ledger
m051/                      Post-v0.5.0 development; excluded from the current compile

100 canon/ – 600 archive/  Earlier project organization and sourcebook-production history
300 art/                   Splash image plus thumbnail-backed external artwork manifest
```

Start with the two workbooks and cost ledger in `m050/extraction/progress/`. The active control index and frozen-corpus manifest are in `m050/extraction/control/`; the process decisions and Gate receipts are in `m050/extraction/audit/`.

For recovery after a restart, context compaction, or task handoff, start with
root `AGENTS.md`, then read the canonical
`m050/extraction/control/M050_Compile_State_MEDIANv0_5_0.json`, the processing
order, and `STATUS.md`. No separate successor packet is used.

## Core rule

A filename, title, or document’s internal claim of authority does not establish its identity or precedence. Sources are classified from their contents and genealogy; extraction preserves their testimony, and authority is resolved only during reconciliation.
