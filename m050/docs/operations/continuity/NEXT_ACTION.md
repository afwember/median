# MEDIAN Next Action

Action date: 2026-08-03

Transition: approved source identities to deterministic legacy-response replay

## Preconditions

1. confirm the identity-card approval checkpoint is committed and pushed;
2. confirm local `HEAD` and `origin/main` are identical and the worktree is
   clean;
3. read the legacy source identity approval receipt and active control index
   v0.3;
4. verify the four approved cards and all four block manifests still pass the
   bound control validator;
5. keep all review and follow-on work offline and source-preserving.

## Authorized transition

Replay the four preserved legacy response sets deterministically against the
approved identity cards for Crossing, Human Rulings, MSID Grammar, and
Governing Philosophy and Architecture. The replay must consume only frozen,
hash-bound local artifacts, produce reproducible reconciliation evidence, and
leave every legacy input unchanged.

After replay verification, the planned offline sequence is:

1. migration of the 913 grounded legacy records into Layer E candidates without
   modifying legacy artifacts;
2. reconstruction of all 41 Human Rulings sections and labeled fields;
3. retrospective block and exclusion ledgers for the four legacy sources;
4. risk-tiered migration bundles, including the 123 compound flags;
5. one fresh-source identity card, dry plan, human-effort estimate, and unsent
   calibration request.

## Stop conditions

Stop if replay is nondeterministic, an approved identity binding fails, any
legacy input would be modified, corpus drift appears, or the artifact/state
contracts cannot represent the result. Also stop before any provider request,
positive-cost work order, production mapping, reconciliation, or compilation.
Those require evidence review and, for paid work, new explicit author
authorization.
