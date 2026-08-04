# MEDIAN v0.5.0 Remote Operations and Status Sync

Record ID: `M050-REMOTE-OPS-0.1`  
Effective date: 2026-08-03  
Primary host: dedicated M4 Mac Mini  
Repository: `https://github.com/afwember/median`  
Paused historical status workbook: `https://docs.google.com/spreadsheets/d/1dCSzZNDzAHy9yIRPXRRvSL_9z9fP2CC18GNK2hPspXQ/edit`

Canonical repository and task-handoff entry points are root `AGENTS.md`,
`m050/extraction/control/M050_Compile_State_MEDIANv0_5_0.json`, and `STATUS.md`.
Google Sheets synchronization is paused; the repository dashboard is the active
phone-readable status view.

## Operating model

`STATUS.md` is the phone-readable operational view, derived from the canonical
compile-state JSON. Git remains authoritative for source material, extraction
artifacts, exact cost entries, audit evidence, and executable behavior. The
Google Sheet is paused historical presentation only and must not be updated or
treated as authority without a new explicit decision.

The workbook contains three tabs:

1. `Progress & Stages` — control-gate and processing-stage status.
2. `Document Status` — the 24-source processing sequence, evidence status,
   next action, repository path, and operator notes.
3. `Cost Tracking` — one row per machine-readable cost entry, with live totals
   in row 1.

## Authority by subject

| Subject | Authoritative record | Remote view |
|---|---|---|
| Source files, engine, schemas, reports, accepted evidence | Git repository | GitHub Mobile |
| Exact provider charges and unreconciled bounds | Provider outcomes and spend records | Canonical compile state |
| Operational cost total | Upward-cent display derived from exact spend | Final line of `STATUS.md` |
| Current compile coordination | Canonical compile state | `STATUS.md` |
| Source processing sequence | Source processing-order control | Canonical state and `STATUS.md` |

## Cost display rule

Exact provider amounts remain at six-decimal precision in audit columns. Each
billable entry is separately rounded upward to the next cent before it is added
to an operational total. Confirmed and unreconciled values remain separate;
the maximum represented amount is their sum.

At the 2026-08-03 migration checkpoint, the workbook contains 154 cost entries:

- exact confirmed charges: `$10.249100`;
- operational confirmed total: `$11.01`;
- exact unreconciled upper bounds: `$0.257710`;
- operational unreconciled ceiling: `$0.27`;
- maximum operational amount represented: `$11.28`.

## Checkpoint protocol

A Git checkpoint is required after a material, internally coherent unit of work
and before a planned shutdown, relocation, risky environment change, or handoff.
The operator should be able to confirm the new commit in GitHub Mobile. Partial,
failing, secret-bearing, or provider-in-flight state must not be committed merely
to satisfy a timer.

After a material status or cost change:

1. update the authoritative repository artifact first when the change concerns
   source, evidence, code, or exact costs;
2. update the canonical compile state and derive `STATUS.md`;
3. run the active guard;
4. record and push the coherent repository checkpoint;
5. confirm `origin/main` resolves to the intended local commit.

The Gate 5 foundation checkpoint published during this migration is
`62148e77d605566795f50ecad30f348f5c65213c`.

## Mac Mini remote baseline

The following baseline was established and verified on 2026-08-03:

- Chrome Remote Desktop provides the primary unattended desktop path and was
  tested successfully from both a laptop and an iPhone over cellular data.
- macOS Screen Sharing remains the independent Mac-to-Mac fallback.
- Google Chrome `151.0.7922.72` and Chrome Remote Desktop Host
  `151.0.7922` were installed from Google-signed, Apple-notarized packages.
- automatic login targets the dedicated `ambulatoryworld` account;
- `/Users/ambulatoryworld/Library/LaunchAgents/com.median.open-chatgpt.plist`
  opens `/Applications/ChatGPT Classic.app` at login;
- system sleep is disabled on AC power, wake for network access is enabled,
  and automatic restart after power loss is enabled;
- FileVault is disabled by explicit operator decision to permit unattended
  cold-boot recovery. Physical possession of the Mini therefore permits
  substantially easier access to its local data and saved sessions;
- Apple Command Line Tools `26.6` are installed;
- the MEDIAN environment uses Python `3.12.7`; patched build/test tooling is
  `pip 26.2`, `setuptools 83.0.0`, `wheel 0.47.0`, and `pytest 9.1.1`;
- the post-update Python vulnerability audit reported no known third-party
  package vulnerabilities, and all 53 Gate 5 engine tests passed.

macOS Tahoe `26.6` build `25G72` was installed through a controlled restart on
2026-08-03. The Mini booted at 01:31 EDT; automatic login completed, the ChatGPT
startup agent returned success, Chrome Remote Desktop remained available, all
required power settings persisted, Python dependency consistency passed, Git
remained clean and aligned with `origin/main`, and all 53 Gate 5 tests passed.
The KVM is no longer required for routine operation and remains emergency
recovery equipment only.

## Cost and security boundaries

Remote operations must use only free or already-included capabilities. No paid
remote-access, monitoring, automation, or cloud service may be subscribed to or
enabled without a new, explicit user decision. Paid model and provider calls
remain separately approval-gated; remote infrastructure work does not authorize
them.

Credentials and provider secrets belong in macOS Keychain or protected support
configuration outside the repository. They must never be copied into this file,
the Google Sheet, issue text, committed logs, or model prompts. Remote access
configuration, power-loss recovery, and host health monitoring are separate
infrastructure controls and must be audited before system settings are changed.
