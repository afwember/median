# MEDIAN Next Action

Action date: 2026-08-03

Transition: pre-update checkpoint to verified macOS 26.6 remote operation

## Preconditions

Before initiating the restart:

1. confirm Apple still reports the completed macOS 26.6 download as available;
2. run `./m050/tools/m050_verify_mac_mini.sh --deep` and investigate failures;
3. confirm the continuity files are committed and pushed to `origin/main`;
4. confirm local `HEAD` and `origin/main` are identical and the worktree is
   clean;
5. leave the KVM connected or immediately available;
6. confirm the user is finished for the night and explicitly ready to lose the
   remote session.

## Authorized transition

Install the already-reviewed macOS 26.6 update and restart. Do not combine the
restart with unrelated software installation or project work.

## Expected interruption

Chrome Remote Desktop and this task will disconnect. The Mini should restart,
automatically log in to `ambulatoryworld`, restore networking, start the Chrome
Remote Desktop host, and open ChatGPT Classic through the LaunchAgent.

## Post-reboot verification order

1. Connect from the laptop through Chrome Remote Desktop.
2. Connect from the iPhone over cellular data.
3. Confirm `sw_vers` reports macOS 26.6 and the expected build.
4. Confirm automatic login reached the desktop without local intervention.
5. Confirm Chrome Remote Desktop and ChatGPT Classic are available.
6. Run `./m050/tools/m050_verify_mac_mini.sh --deep`.
7. Confirm the repository is clean and synchronized with `origin/main`.
8. Update `CURRENT_STATE.md`, this file, and the remote-operations record with
   the verified post-update state; commit and push that checkpoint.
9. Remove the KVM from routine availability only after all checks pass.

## Stop conditions

Stop and use the KVM or local assistance if any of these occur:

- the Mini remains unreachable for a reasonable update window;
- macOS presents an interactive setup, recovery, or credential screen;
- automatic login does not complete;
- networking or Chrome Remote Desktop does not return;
- the host check reports a required control failure;
- Git state differs unexpectedly from `origin/main`.

Do not guess through an unexpected security, recovery, or migration prompt.
