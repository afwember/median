# MEDIAN v0.5.0 Repository Write Authority and Freeze Policy

**Status:** Active

**Effective:** 2026-08-02

**Author and root of design authority:** Asa Wember

**Repository operator:** Codex, acting under Asa Wember's explicit direction

## Decision

MEDIAN v0.5.0 is frozen.

The files under `m050/docs/baseline/` and `m050/docs/v0.5/`, including their attached media, are immutable source evidence. Their exact paths and hashes are recorded in `M050_Frozen_Corpus_Manifest_v0_1_MEDIANv0_5_0.json`.

New game development belongs under `m051/`. It does not enter the v0.5.0 compile.

## Authority model

Asa Wember remains the root of design authority. He may issue decisions and rulings conversationally. Codex records approved decisions in the appropriate append-only repository artifact.

Asa Wember will not edit the repository directly during the v0.5.0 compile. This is an operational discipline, not a transfer of authorship or authority.

Only one Codex task may hold repository write authority at a time. Other tasks may inspect, analyze, red-team, or advise, but are read-only unless the author explicitly transfers write authority and the receiving task verifies the repository state first.

## Permitted writes

Under an explicitly approved scope, the active writer may add or supersede:

- audit and control records;
- work orders and receipts;
- extracted evidence and later-layer records;
- progress and cost records;
- tests and source-independent tooling;
- new human-ruling records;
- compilation outputs.

Every correction is append-only. Existing accepted evidence and frozen sources are never edited in place.

## Prohibited writes

- Modification, deletion, renaming, or addition within the frozen v0.5.0 source roots
- Modification of an immutable accepted candidate or acceptance report
- Use of `m051/` material in a v0.5.0 work order
- Silent replacement of an archived artifact
- Concurrent repository mutation by multiple tasks
- A repository change broader than the author's approved scope

## Writer handoff

Before writing, a task must:

1. confirm the previous writer is no longer acting;
2. begin from a clean or fully understood Git state;
3. run `python3 m050/tools/m050_guard.py`;
4. identify its approved scope;
5. stop if any frozen or immutable integrity check fails.

At handoff or completion, the writer must:

1. rerun the guard;
2. record material decisions and receipts;
3. update progress records when applicable;
4. commit and push the completed coherent unit when authorized;
5. report the commit and any remaining uncommitted changes.

## Enforcement

`m050/tools/m050_guard.py` verifies the frozen source inventory and hashes, immutable accepted-evidence hashes, archive snapshot, Gate 2 source agreement, and the separation of `m051/` from the frozen corpus.

The guard makes accidental mutation detectable. Git history and the frozen manifest preserve the recovery point. A failed guard is a hard stop, not an invitation to update the expected hash.
