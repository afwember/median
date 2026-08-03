# MEDIAN v0.5.0 Gate 5 Human Rulings Reconstruction Report

Date: 2026-08-03

Status: **PASS — deterministic ruling reconstruction complete; Gate 5 remains in progress**

## Result

The historical Human Rulings Ledger is now reconstructed as a source-bound,
field-preserving structure. The offline engine parsed all 41 `HR-*` sections
and all 348 labeled ruling fields from the active frozen ledger. It preserved
the exact field payloads, including multiline exact-human wording, separately
from normalized rulings and every other labeled field.

All 173 records in the accepted legacy candidate now have deterministic source
coordinates:

- 137 records are linked to a ruling ID and one or more labeled ruling fields;
- 36 records are linked to an explicit non-ruling document region;
- 138 records have a labeled-field coordinate, including one open-item field;
- 167 records remain exact matches in the active frozen ledger; and
- six records are linked through the Gate 4 source-identity reference rewrite.

No legacy record was edited, dropped, or split. The two Human Rulings records
that cross structural block boundaries remain intact and still require the
separate compound-disposition step.

## Reference-rewrite result

The engine compared the preserved pre-reference-rewrite ledger with the active
frozen ledger line by line. It required one-for-one line topology and emitted
24 exact replacement entries. Every entry binds the old and new line text,
hashes, coordinates, ruling/field context when applicable, and the executed
Gate 4 source-identity migration receipt.

This map resolves exactly the six replay records that existed only in the
legacy source bytes:

| Legacy record | Legacy coordinate | Deterministic active destination |
| --- | --- | --- |
| `ATOM-HUMAN-RULINGS-DIRECT-0025` | `HR-LIN-001` / `Normalized ruling` | Home Mode, Colony, and DWELL reference rewrite |
| `ATOM-HUMAN-RULINGS-DIRECT-0027` | `HR-LIN-002` / `Normalized ruling` | v0.4.7 Cross-System Carryforward reference rewrite |
| `ATOM-HUMAN-RULINGS-DIRECT-0118` | `HR-AWAY-001` / `Authority effect` | v0.4.6 GDD Coverage-Gap Development reference rewrite |
| `ATOM-HUMAN-RULINGS-DIRECT-0121` | `HR-AUTH-001` / `Adopted proposition` | v0.4.6 GDD Coverage-Gap Development reference rewrite |
| `ATOM-HUMAN-RULINGS-DIRECT-0122` | `HR-AUTH-001` / `Normalized ruling` | v0.4.6 GDD Coverage-Gap Development reference rewrite |
| `ATOM-HUMAN-RULINGS-DIRECT-0169` | Operational consequences | source-identity and reconciliation control-language rewrite |

The map explains recorded source-identity changes. It does not reinterpret a
ruling, generate substitute author language, or promote any legacy atom into
Layer E.

## Immutable outputs

| Artifact | SHA-256 |
| --- | --- |
| Section and field registry | `27fd7fa1eebbb50c41e1fc22587ac0e142533a83c49a801ef33ef81a1a3dce80` |
| Legacy atom coordinate ledger | `8dd32794421599c625738aabfbce85df46e836cd52d42d8bae279339bc8cdfb2` |
| Active-to-legacy reference rewrite map | `407556afd59859255b2bd6d3b18996064f5bbe63e56714fb02fb9d8ba611923e` |
| Machine reconstruction report | `012fc06bf84be7ee8a804757ab6b56a025658eda55175fc3894af3d1bb2666b6` |

## Boundary and cost

- Provider calls: **0**
- Accounted cost: **$0.00**
- Google Sheets interactions: **0**
- Layer E migration: **not started**
- Production mapping, reconciliation, and compilation: **not started**

## Next authorized transition

The six reference-rewrite exceptions are resolved by this reconstruction. The
remaining repair overlay contains 18 records: 17 exact quotations crossing
structural block boundaries and one repeated MSID quotation. Prepare explicit,
source-preserving compound dispositions next, without splitting their legacy
records. Then resolve the MSID occurrence and repeat all four deterministic
replays before any Layer E migration.
