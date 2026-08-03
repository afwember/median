# MEDIAN Current State

> **Superseded operational snapshot — do not use the milestones below as current authority.**
> The current state is controlled by
> `m050/extraction/control/M050_Active_Control_Index_v0_10_MEDIANv0_5_0.json`
> and `m050/extraction/control/M050_Current_State_Checkpoint_v0_1_MEDIANv0_5_0.md`.
> The controlling corpus vector is **24 registered / 22 compile scope / 4 atomized
> legacy seed / 18 outstanding = 14 pre-reconciliation + 4 later or conditional**.
> The legacy review queues are preserved but dormant.

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
  occurrence. All 24 now have explicit mechanical dispositions: six reference
  rewrites, 17 preserved indivisible compounds, and one pinned exact whole-line
  occurrence. The raw replay artifacts remain unchanged and still show the
  original queue by design. Rebuilding all four replays produced byte-identical
  ledgers and reports, and there are zero unresolved grounding or coordinate
  repairs.
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
  `pip check` passed and the current offline Gate 5 suite passes all 77 tests.
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
- `m050/extraction/audit/M050_Extraction_Gate_5_Legacy_Repair_Closure_Report_v0_1_MEDIANv0_5_0.md`
- `m050/extraction/audit/M050_Extraction_Gate_5_Legacy_Repair_Closure_Receipt_v0_1_MEDIANv0_5_0.json`
- `m050/extraction/control/M050_Active_Control_Index_v0_6_MEDIANv0_5_0.json`

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
Human Rulings reconstruction, and the 24-record mechanical repair overlay are
complete. The next project action is deterministic Layer E migration-candidate
design and construction, preserving all risk and pending-review states, as
specified in `NEXT_ACTION.md`. No semantic acceptance, paid model, or provider
request is authorized.
