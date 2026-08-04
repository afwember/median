# Gate 5 source identities

This directory holds reviewable, source-bound identity artifacts for MEDIAN
v0.5.0. They do not grant authority by filename or self-description and they do
not authorize a provider call.

## Layout

- `blocks/` contains deterministic structural block manifests generated from
  exact frozen source bytes.
- `cards/` contains immutable, content-derived source identity-card revisions.
  The four `v0_4` files are the active approved revisions; their `v0_2` draft
  and `v0_3` reviewed predecessors remain preserved as transition history.

Each v0.2 card binds the exact frozen source, block manifest, Gate 2 source
disposition, Gate 3 reuse disposition, applicable predecessor material, and
legacy candidate and acceptance report. The validator rejects hash drift,
unbound substituted controls, unknown block citations, stream expansion,
legacy-count drift, and migration-disposition drift.

## Offline validation

From the repository root, validate one card with:

```sh
.venv/bin/python -m median_gate5.cli profile \
  --repo-root . \
  --card CARD.json \
  --block-manifest BLOCK_MANIFEST.json \
  --frozen-manifest m050/extraction/control/M050_Frozen_Corpus_Manifest_v0_1_MEDIANv0_5_0.json \
  --source-disposition m050/extraction/audit/M050_Extraction_Gate_2_Source_Disposition_v0_1_MEDIANv0_5_0.yaml \
  --reuse-disposition m050/extraction/audit/M050_Extraction_Gate_3_Reuse_Disposition_v0_1_MEDIANv0_5_0.yaml
```

Run the full guard before any state transition:

```sh
.venv/bin/python m050/tools/m050_guard.py --with-tests
```

Never edit an approved card in place. Issue a new version with a new
content-derived card ID and a `supersedes_card_id` link.

The `profile-transition` command enforces the lifecycle
`draft -> reviewed -> approved`, issues a transition receipt, and requires
`Asa Wember` authority for approval. The receipts are under
`m050/extraction/audit/identity-transitions/`.
