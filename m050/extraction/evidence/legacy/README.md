# MEDIAN v0.5.0 Legacy Evidence Bundle

This directory contains the small set of byte-identical historical artifacts
that remains necessary to reproduce or audit the Gate 5 legacy migration.

The former `m050/archive/` tree was a 9,921-file recovery snapshot. It is not
an execution surface and has been retired. Older immutable controls still name
the artifacts by their original archive paths because those paths are part of
the historical record. The relocation manifest maps each such path to its
current repository location without changing its bytes or SHA-256 identity.

Current code must resolve historical bindings through
`M050_Legacy_Evidence_Relocation_Manifest_v0_1_MEDIANv0_5_0.json`. Unlisted
archive paths are historical-only and must never be treated as active inputs.
