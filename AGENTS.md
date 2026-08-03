# MEDIAN repository operating contract

Read this file before changing the repository. The repository, not a task transcript, is the durable source of operational truth.

## Compile scope

- “The compile” means the complete controlled pipeline: evidence preparation and atomization, semantic review, mapping, reconciliation, and final document production.
- Gate 2 registers 24 sources. Two are non-atomic companions. The compile scope is 22 sources.
- Current state is 4 atomized legacy-seed sources and 18 outstanding compile-scope sources: 14 pre-reconciliation and 4 later or conditional.
- Never describe the four-source legacy migration or its review queues as whole-corpus completion.

## Required cold start

1. Read `m050/extraction/control/M050_Active_Control_Index_v0_10_MEDIANv0_5_0.json`.
2. Read `m050/extraction/control/M050_Compile_Source_State_Matrix_v0_1_MEDIANv0_5_0.md`.
3. Run `.venv/bin/python m050/tools/m050_guard_v0_5.py --with-tests` before a repository write.
4. Report the exact `24 / 22 / 4 / 18 = 14 + 4` corpus vector and the next authorized transition.

## Hard controls

- One explicitly authorized repository-writing task at a time. Never infer that write authority transferred.
- A successor task begins read-only until Asa Wember explicitly transfers write authority.
- The v0.9 legacy semantic-review artifacts are preserved but dormant. Do not execute them until a later guarded transition authorizes review.
- Semantic acceptance, mapping, reconciliation, and compiled prose are prohibited while corpus atomization is incomplete.
- Provider/model calls are prohibited. Google Sheets interaction is paused.
- Preserve old receipts and control indexes as historical records; supersede them with new append-only artifacts.
