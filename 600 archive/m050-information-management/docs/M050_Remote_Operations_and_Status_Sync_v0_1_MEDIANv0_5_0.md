# MEDIAN remote operations

Effective date: 2026-08-03  
Primary host: dedicated M4 Mac Mini  
Repository: `https://github.com/afwember/median`

This file records remote-access facts only. It does not define compile
authority, source order, spend authority, lifecycle transitions, or repository
write permission. Those are controlled solely by root `AGENTS.md`, the
canonical compile-state JSON, and the canonical source processing order.

## Active remote model

- Chrome Remote Desktop is the primary unattended desktop path and has been
  tested from both laptop and iPhone.
- macOS Screen Sharing is the independent Mac-to-Mac fallback.
- Automatic login, network wake, restart after power loss, disabled system
  sleep on AC power, and the ChatGPT login item support headless recovery.
- FileVault is disabled by explicit operator decision. Physical possession of
  the Mini therefore carries increased local-data and saved-session risk.
- The repository, GitHub Mobile, and root `STATUS.md` provide the remote view of
  work and checkpoints.
- Google Sheets synchronization is paused and has no operational authority.
- No paid remote-access, monitoring, automation, or cloud service may be added
  without a separate explicit decision.

## Recovery check

Run the read-only host check when remote access or host continuity is in doubt:

```sh
m050/tools/m050_verify_mac_mini.sh --deep
```

After a coherent repository checkpoint, confirm the intended commit is visible
on GitHub and local `HEAD` equals `origin/main`. Never commit provider-in-flight,
failing, partial, or secret-bearing state merely to satisfy a timer.

Credentials remain in Keychain or protected support configuration outside the
repository. They must not enter source files, prompts, receipts, reports, issue
text, or task messages.
