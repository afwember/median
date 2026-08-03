# MEDIAN Durable Decisions

This register contains author decisions that should survive task compaction and
handoff. It does not replace domain rulings recorded in Gate evidence.

## Working relationship

- Use a conversational approach: discuss consequential plans with the author,
  then execute after direction is clear.
- Prefer thoroughness and precision over efficiency within reason.
- Make reasonable, low-risk implementation choices without repeatedly stopping
  for minor preferences; surface consequential tradeoffs explicitly.
- If the sandbox blocks a needed in-scope resource, request approval rather than
  silently reducing the work.

## Cost and external services

- Round each operational cost entry upward to the next cent; preserve exact
  provider amounts separately for audit.
- Use no paid remote-access, monitoring, automation, or cloud service without a
  new explicit author decision.
- External model calls and any positive-cost provider work require a separate,
  exact work order and explicit authorization. Infrastructure work does not
  authorize provider spending.

## Operating model

- The dedicated M4 Mac Mini is MEDIAN's primary operating host for the
  foreseeable future.
- Work should be remotely observable from iPhone and laptop through GitHub,
  Google Sheets, and remote desktop.
- Git is authoritative for project artifacts, exact technical state, costs, and
  audit evidence. Google Sheets is the phone-readable status view.
- Chrome Remote Desktop is the primary unattended desktop path; macOS Screen
  Sharing is the fallback and the KVM is recovery equipment.
- FileVault is intentionally disabled to permit unattended recovery after a
  cold boot. The author accepted the resulting physical-access risk for this
  dedicated, low-stakes host.
- Automatic login and automatic ChatGPT Classic opening are intentional.
- The first macOS update in this configuration requires KVM availability until
  both laptop and cellular-phone recovery have been proven.

## Continuity and task changes

- Do not use the full historical transcript as routine context.
- Keep this continuity package compact, evidence-linked, and current before
  risky transitions.
- Do not move active work to a new task during a machine transition.
- A future task must bootstrap from `HANDOFF.md`, verify live state, and consult
  the historical transcript only for a specific unresolved question.
- Context summaries are navigation aids, not authoritative project records.
