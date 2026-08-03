# MEDIAN Current State

State date: 2026-08-03 (America/New_York)

Primary host: dedicated Apple-silicon Mac Mini

Repository: `https://github.com/afwember/median`

Branch: `main`

Verified predecessor checkpoint: `35e29d8d740eb0335620212680d370165088eab9`

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
- The source-independent engine, artifact contracts, lifecycle controls,
  deterministic tooling, locked runtime, and regression suite are implemented.
- The repository-local environment uses Python 3.12.7 with pip 26.2,
  setuptools 83.0.0, wheel 0.47.0, and pytest 9.1.1.
- The latest security check found no known third-party Python vulnerabilities;
  `pip check` passed and all 53 Gate 5 tests passed.
- No paid model or provider work is currently authorized.

Detailed Gate 5 evidence:

- `m050/extraction/audit/M050_Extraction_Gate_5_Foundation_Milestone_1_Report_v0_1_MEDIANv0_5_0.md`
- `m050/extraction/audit/M050_Extraction_Gate_5_Foundation_Milestone_1_Receipt_v0_1_MEDIANv0_5_0.json`
- `m050/extraction/audit/M050_Extraction_Gate_5_Technical_Contract_v0_1_MEDIANv0_5_0.md`

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

The Sheet is the phone-readable operational view; Git remains authoritative for
technical state and exact audit evidence. At the migration checkpoint it held
154 cost entries with operational totals of $11.01 confirmed, $0.27
unreconciled, and $11.28 maximum represented. Each entry is rounded upward to
the next cent for operational display; exact six-decimal amounts remain in the
audit data.

## Known pending transition

The host migration and controlled update are complete. The next project work is
the offline Gate 5 continuation in `NEXT_ACTION.md`. No paid model or provider
request is authorized.
