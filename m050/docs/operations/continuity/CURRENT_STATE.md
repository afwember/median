# MEDIAN Current State

State date: 2026-08-03 (America/New_York)

Primary host: dedicated Apple-silicon Mac Mini

Repository: `https://github.com/afwember/median`

Branch: `main`

Verified predecessor checkpoint: `afac46242b0bbd86530197c8a4fd26f21afdc75d`

This file describes the verified post-macOS-26.6-restart state. Pre-update
continuity checkpoint `68857afd9d02e33ff30622042dcac8c13ce38450` is the
recovery baseline. The commit containing this revision is the post-update
checkpoint; verify its exact hash with `git rev-parse HEAD` rather than copying
a self-referential hash into the file.

## Project state

- Gates 1–4 are complete.
- Gate 5 is in progress.
- Gate 5 Foundation Milestone 1 passed as an offline implementation milestone;
  it is not Gate 5 completion and does not authorize provider calls.
- Gate 5 Milestone 2 identity approval is complete: Asa Wember approved all
  four legacy source identity cards. Immutable draft, reviewed, and approved
  revisions plus linked transition receipts are preserved.
- Deterministic legacy replay is complete for all 913 records. Repeated builds
  produced byte-identical ledgers and reports, all quotations remain grounded,
  and there are zero grounding failures. Layer E migration has not begun.
- Replay exposed a bounded 24-record repair queue: 17 cross-block compounds,
  six Human Rulings active-to-legacy reference rewrites, and one ambiguous MSID
  occurrence. Human Rulings reconstruction has now resolved the six reference
  rewrites, leaving an 18-record repair overlay: 17 cross-block compounds and
  one ambiguous MSID occurrence. The raw replay artifacts remain unchanged and
  continue to show the original 24-record queue until all repairs are complete
  and all four replays are repeated.
- Human Rulings reconstruction accounts for all 41 historical ruling sections,
  all 348 labeled ruling fields, and all 173 accepted legacy records. Of those,
  137 records are ruling-field bounded, 36 are bound to explicit non-ruling
  document regions, 167 remain exact in the active source, and six use the
  Gate 4 reference-rewrite map. No record was modified or split. Layer E
  migration has not begun.
- The source-independent engine, artifact contracts, lifecycle controls,
  deterministic tooling, locked runtime, and regression suite are implemented.
- The repository-local environment uses Python 3.12.7 with pip 26.2,
  setuptools 83.0.0, wheel 0.47.0, and pytest 9.1.1.
- The latest security check found no known third-party Python vulnerabilities;
  `pip check` passed and the current offline Gate 5 suite passes its standing
  regression tests.
- No paid model or provider work is currently authorized.

Detailed Gate 5 evidence:

- `m050/extraction/audit/M050_Extraction_Gate_5_Foundation_Milestone_1_Report_v0_1_MEDIANv0_5_0.md`
- `m050/extraction/audit/M050_Extraction_Gate_5_Foundation_Milestone_1_Receipt_v0_1_MEDIANv0_5_0.json`
- `m050/extraction/audit/M050_Extraction_Gate_5_Technical_Contract_v0_1_MEDIANv0_5_0.md`
- `m050/extraction/audit/M050_Extraction_Gate_5_Legacy_Source_Identity_Card_Review_Brief_v0_1_MEDIANv0_5_0.md`
- `m050/extraction/audit/M050_Extraction_Gate_5_Legacy_Source_Identity_Draft_Validation_v0_1_MEDIANv0_5_0.json`
- `m050/extraction/audit/M050_Extraction_Gate_5_Legacy_Source_Identity_Approval_Receipt_v0_1_MEDIANv0_5_0.json`
- `m050/extraction/audit/M050_Extraction_Gate_5_Legacy_Replay_Milestone_Report_v0_1_MEDIANv0_5_0.md`
- `m050/extraction/audit/M050_Extraction_Gate_5_Legacy_Replay_Milestone_Receipt_v0_1_MEDIANv0_5_0.json`
- `m050/extraction/audit/M050_Extraction_Gate_5_Human_Rulings_Reconstruction_Report_v0_1_MEDIANv0_5_0.md`
- `m050/extraction/audit/M050_Extraction_Gate_5_Human_Rulings_Reconstruction_Receipt_v0_1_MEDIANv0_5_0.json`
- `m050/extraction/control/M050_Active_Control_Index_v0_5_MEDIANv0_5_0.json`

## Remote operating state

- Chrome Remote Desktop is the primary unattended path and was verified from a
  laptop and an iPhone over cellular data.
- macOS Screen Sharing is the independent Mac-to-Mac fallback.
- The first controlled operating-system update reboot completed and remote
  operation returned. The KVM can now be removed from routine availability;
  retain it only as emergency recovery equipment.
- Automatic login targets `ambulatoryworld`.
- LaunchAgent `com.median.open-chatgpt` opens
  `/Applications/ChatGPT Classic.app` at login.
- AC system sleep and display sleep are disabled, wake-on-network and automatic
  restart after power loss are enabled.
- FileVault is disabled by explicit author decision to permit unattended cold
  boot. This increases physical-access exposure to local data and saved
  sessions.
- macOS 26.6 build 25G72 is running. The system booted at 2026-08-03 01:31 EDT;
  automatic login, ChatGPT startup, remote access, power controls, repository
  alignment, Python dependency consistency, and all 53 Gate 5 tests passed in
  the post-reboot check.

Full infrastructure record:
`m050/docs/operations/M050_Remote_Operations_and_Status_Sync_v0_1_MEDIANv0_5_0.md`.

## Remote status surface

Google Sheet:
`https://docs.google.com/spreadsheets/d/1dCSzZNDzAHy9yIRPXRRvSL_9z9fP2CC18GNK2hPspXQ/edit`

Tabs:

- `Progress & Stages`
- `Document Status`
- `Cost Tracking`

The Sheet is a phone-readable operational view; Git remains authoritative for
technical state and exact audit evidence. All Google Sheets reads, writes,
metadata checks, and verification calls are paused by author direction until a
smaller-footprint policy is specified. At the last Sheet checkpoint it held
154 cost entries with operational totals of $11.01 confirmed, $0.27
unreconciled, and $11.28 maximum represented. Each entry is rounded upward to
the next cent for operational display; exact six-decimal amounts remain in the
audit data.

## Known pending transition

The host migration, controlled update, source identity approval, legacy replay,
and Human Rulings reconstruction are complete. The next project action is to
prepare explicit source-preserving dispositions for all 17 cross-block legacy
records, then resolve the one ambiguous MSID occurrence and repeat all four
replays, as specified in `NEXT_ACTION.md`. No paid model or provider request is
authorized.
