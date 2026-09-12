# Source identity controls

This directory contains only identity material consumed by the current
compile.

- `blocks/` holds deterministic structural manifests.
- `cards/` holds the current source's author-reviewed content/provenance card.

An identity card describes one source; it does not authorize source work or a
provider call. The active extraction configuration binds the exact card,
manifest, and Asa Wember approval receipt by SHA-256. Git preserves superseded
versions outside the active tree.

Human Rulings conformance uses its frozen source, accepted candidate, block
manifest, and the reconstruction records under
`m050/extraction/evidence/human-rulings/`. No legacy migration identity family
is active.

Run the full guard before a control release:

```sh
.venv/bin/python m050/tools/m050_guard.py --with-tests
```
