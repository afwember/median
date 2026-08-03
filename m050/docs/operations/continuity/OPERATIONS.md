# MEDIAN Continuity Operations

## Standard checkpoint

Create a checkpoint after a coherent material change and before a shutdown,
host update, risky configuration change, or task handoff.

1. Verify the actual host and repository state.
2. Update `CURRENT_STATE.md` with facts that are true now.
3. Update `NEXT_ACTION.md` with one exact next transition, prerequisites,
   expected interruption, verification, and stop conditions.
4. Add only durable author choices to `DECISIONS.md`.
5. Update authoritative Gate, cost, or source artifacts before summarizing them
   here.
6. Run the proportional test suite; use
   `./m050/tools/m050_verify_mac_mini.sh --deep` for host transitions.
7. Inspect the diff for secrets, transient output, and unsupported claims.
8. Commit and push the coherent checkpoint.
9. Verify `HEAD` equals `origin/main` and confirm the commit through the remote
   view when practical.

Never checkpoint a credential, token, provider response still in flight,
knowingly failing state, or fabricated completion merely to satisfy a timer.

## Planned restart

Before restart, ensure `NEXT_ACTION.md` names the post-restart checks and the
recovery path. A restart that breaks the active remote session must be the final
operation after all files are saved and pushed. Keep local recovery equipment
available until remote access has been tested from both primary client types.

After restart, verify live state before editing the records. A successful login
or visible desktop alone is insufficient: confirm OS version, remote host,
startup agent, power policy, project environment, tests, and Git alignment.

## Context-compaction response

Do not react to compaction by re-importing the full transcript. Re-read the five
continuity files, verify the claims that affect the next action, and continue.
If a detail is missing:

1. search current Git artifacts and history;
2. inspect the live host or external status surface;
3. search the historical transcript for that specific subject;
4. ask the author when evidence remains ambiguous;
5. record the resolved durable fact here or in `DECISIONS.md`.

## New-task handoff

Do not change tasks while a restart, provider request, merge, migration, or
other stateful operation is incomplete. At a stable boundary:

1. complete the standard checkpoint;
2. copy the bootstrap prompt from `HANDOFF.md` into the new task;
3. require the new task to report its reconstructed understanding before it
   changes state;
4. compare that report against `CURRENT_STATE.md` and `NEXT_ACTION.md`;
5. correct and commit any continuity defect before retiring the old task.

## Secret boundary

The support directory contains credentials and authenticated tool
configuration outside Git. Verification may check expected paths and restrictive
permissions but must not print or read secret contents. Never place credentials
in this package, Git, Google Sheets, logs, screenshots, or prompts.

## Related authoritative procedures

- Remote access, Sheet/Git authority, costs, and host baseline:
  `m050/docs/operations/M050_Remote_Operations_and_Status_Sync_v0_1_MEDIANv0_5_0.md`
- Repository write/freeze rules:
  `m050/extraction/control/M050_Repository_Write_Authority_and_Freeze_Policy_v0_1_MEDIANv0_5_0.md`
- Gate 5 technical behavior:
  `m050/extraction/audit/M050_Extraction_Gate_5_Technical_Contract_v0_1_MEDIANv0_5_0.md`
