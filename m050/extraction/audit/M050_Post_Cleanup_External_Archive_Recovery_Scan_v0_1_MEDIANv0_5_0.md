# MEDIAN v0.5.0 Post-Cleanup External Archive Recovery Scan

Date: 2026-08-03

Status: complete; one narrow control recovered; no retired file restored wholesale

## Recovery source and scope

The scan used the verified external recovery bundle at `/Users/ambulatoryworld/Documents/Codex/median-support/MEDIAN_Pre_Archive_Art_Rewrite_2026-08-03.bundle` (SHA-256 `d97bdabb8bf3ea26702637af1ee2eaa78d0b6963804a72b5db9a3b02aedbaab2`). The bundle is a complete Git history; the inspected pre-retirement head was `4a0fed13302ef30cb1e366ac96df5e04f3868889`.

The scan was read-only. It excluded DOCX/PDF source copies, artwork and media binaries, generated chunks and caches, raw provider traffic, accepted-candidate payloads already covered by the relocation manifest, spreadsheet build intermediates, and obvious superseded version families. Standalone Markdown, YAML, JSON, runbook, registry, ordering, lane, audit, receipt, and recovery/control material was compared with the current repository and its Gate 4 currentness and Gate 5 archive-retirement dispositions.

## Relevant candidates

| Archived standalone artifact | Finding | Disposition |
|---|---|---|
| `M050_Canonical_Rule_Document_Processing_Order_v0_1_MEDIANv0_5_0.yaml` | Substantive. It confirms Authorial Grammar as the next uncompleted source and preserves the same pending order through the then-known specification set. It also records the Authorial Grammar/Human Rulings conformance rule. However, it contains retired source IDs, pre-reference-rewrite hashes, only 16 extraction entries, obsolete stream names, and old acceptance classifications. | Do not restore wholesale. The current 24-source order is reconstructed from the tracker and Gate 2. Recover only the still-valid Authorial Grammar post-extraction conformance rule under current identities and acceptance boundaries. Archived blob `ff927ed4ce40bdca6f635ea5f6e530163a307372`; content SHA-256 `238424b326bb30a00f400f0a9ce5bfebf12121c86c5fb2d6f806db5853bde67e`. |
| `M050_Extraction_Execution_Lanes_v0_1_MEDIANv0_5_0.yaml` | Substantive historical handoff discipline: predictable one-source work only; anomalies and control changes return to the controlling task. Its fixed “primary/secondary” task labels and current-source claims are obsolete. | Do not restore. Its valid behavior is already stronger in the one-writer rule, read-only successor bootstrap, defect revocation, source reset, and explicit-authority requirements. Archived blob `41bcc8c8585ff7bfed5dd30a18686e97ffa21a68`; content SHA-256 `9a004d9be61766519fdfebc9447d2e566ebdf8799ff1bb8416f6c67bc2099ae4`. |
| Atomic Extraction runbook, source registry, Claude provisioning/bootstrap, prompts, schemas, and source-specific workers | Historically substantial but explicitly classified by Gate 4 as a superseded overloaded extraction process. | Do not restore or treat as execution authority. The current technical contract, calibration protocol, engine, bootstrap, and source-state controls supersede them. |
| Authoring Thread Recovery Packet | Large historical context packet, but it predates the Gate 4 identity rewrite, Gate 5 technical controls, corpus-scope correction, and this amendment. | Do not restore. Current repository checkpoints and cold-start bootstrap are smaller, current, and hash-bound. |
| Active Corpus and Authority Manifest, Owner Conformance Directive, filename-identity audit draft, legacy rename/equivalence maps | Important migration evidence, but they contain old identities or completed migration instructions. | Do not restore as active controls. Gate 2, the frozen manifest, source identity cards, Gate 4 completion records, and relocation receipts preserve the applicable results. |
| Abandoned Claude compiler/build architecture and generated reports | Old method explicitly retired by author decision. | Exclude. No executable or planning authority recovered. |

## Recovered control

The only missing current obligation found was source-specific:

> After Authorial Grammar extraction and local validation, compare the source-bounded candidate against applicable Human Rulings authorial evidence before candidate acceptance. Never place Human Rulings content in the extraction prompt.

The amendment translates that historical rule into current controls with three safeguards the old file lacked:

1. use the active frozen Human Rulings source, approved identity/coordinate controls, and mechanically valid reconstruction evidence—not the retired v0.2 partition as active authority;
2. treat conflicts, omissions, or status mismatches as extraction defects that return to calibration; and
3. prohibit this comparison from becoming Layer E semantic acceptance or cross-source reconciliation.

## Processing-order reconciliation

The archived YAML is a historical partial order, not the current corpus authority. It listed three then-accepted sources before Authorial Grammar and ended after the then-known specification set. The current tracker and Gate-2-derived matrix expand the control to all 24 registered sources, including the two later provenance sources and later/conditional documents. After already completed legacy seeds are skipped, the archived and current controls agree that Authorial Grammar is next and agree on the pending specification sequence through the old coverage-gap endpoint.

## Conclusion

No other standalone archive file is needed in the active repository. Restoring the retired controls would reintroduce stale identities and process drift. The bundle remains the recoverable historical source; the present amendment retains the one still-valid missing obligation in current, tested, hash-bound controls.
