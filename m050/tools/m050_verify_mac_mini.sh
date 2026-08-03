#!/bin/sh

# Read-only continuity check for the dedicated MEDIAN Mac Mini.
# This script prints configuration and project health; it makes no changes.

set -u

MEDIAN_REPO_ROOT=$(CDPATH= cd -- "$(dirname -- "$0")/../.." && pwd)
MEDIAN_EXPECTED_USER=${MEDIAN_EXPECTED_USER:-ambulatoryworld}
MEDIAN_EXPECTED_MACOS=${MEDIAN_EXPECTED_MACOS:-26.6}
MEDIAN_CHATGPT_APP=${MEDIAN_CHATGPT_APP:-/Applications/ChatGPT Classic.app}
MEDIAN_LAUNCH_AGENT=${MEDIAN_LAUNCH_AGENT:-com.median.open-chatgpt}
MEDIAN_DEEP=0
MEDIAN_FAILURES=0
MEDIAN_WARNINGS=0

if [ "${1:-}" = "--deep" ]; then
    MEDIAN_DEEP=1
elif [ "$#" -gt 0 ]; then
    echo "Usage: $0 [--deep]" >&2
    exit 2
fi

pass() { printf 'PASS  %s\n' "$1"; }
warn() { printf 'WARN  %s\n' "$1"; MEDIAN_WARNINGS=$((MEDIAN_WARNINGS + 1)); }
fail() { printf 'FAIL  %s\n' "$1"; MEDIAN_FAILURES=$((MEDIAN_FAILURES + 1)); }
info() { printf 'INFO  %s\n' "$1"; }

version_at_least() {
    awk -v actual="$1" -v expected="$2" 'BEGIN {
        split(actual, a, "."); split(expected, e, ".");
        for (i = 1; i <= 3; i++) {
            av = (a[i] == "" ? 0 : a[i]) + 0;
            ev = (e[i] == "" ? 0 : e[i]) + 0;
            if (av > ev) exit 0;
            if (av < ev) exit 1;
        }
        exit 0;
    }'
}

echo "MEDIAN Mac Mini continuity verification"
info "repository: $MEDIAN_REPO_ROOT"
info "timestamp: $(date '+%Y-%m-%d %H:%M:%S %Z')"

if [ "$(uname -s)" = "Darwin" ] && [ "$(uname -m)" = "arm64" ]; then
    pass "host is arm64 macOS"
else
    fail "expected arm64 macOS; found $(uname -s) $(uname -m)"
fi

MEDIAN_OS_VERSION=$(sw_vers -productVersion 2>/dev/null || printf 'unknown')
MEDIAN_OS_BUILD=$(sw_vers -buildVersion 2>/dev/null || printf 'unknown')
info "macOS: $MEDIAN_OS_VERSION ($MEDIAN_OS_BUILD)"
if version_at_least "$MEDIAN_OS_VERSION" "$MEDIAN_EXPECTED_MACOS"; then
    pass "macOS meets expected minimum $MEDIAN_EXPECTED_MACOS"
else
    warn "macOS is below expected post-update minimum $MEDIAN_EXPECTED_MACOS"
fi

MEDIAN_AUTO_USER=$(defaults read /Library/Preferences/com.apple.loginwindow autoLoginUser 2>/dev/null || true)
if [ "$MEDIAN_AUTO_USER" = "$MEDIAN_EXPECTED_USER" ]; then
    pass "automatic login targets $MEDIAN_EXPECTED_USER"
else
    fail "automatic login target is '${MEDIAN_AUTO_USER:-unavailable}'"
fi

MEDIAN_FV_STATUS=$(fdesetup status 2>/dev/null || true)
case "$MEDIAN_FV_STATUS" in
    *"FileVault is Off"*) pass "FileVault is off as explicitly configured" ;;
    *"FileVault is On"*) fail "FileVault is on; unattended cold boot may stop before login" ;;
    "") warn "FileVault status unavailable without additional local privilege" ;;
    *) warn "unrecognized FileVault status: $MEDIAN_FV_STATUS" ;;
esac

MEDIAN_PMSET=$(pmset -g custom 2>/dev/null || true)
for MEDIAN_SETTING in "sleep:0" "displaysleep:0" "womp:1" "autorestart:1"; do
    MEDIAN_SETTING_NAME=${MEDIAN_SETTING%:*}
    MEDIAN_SETTING_VALUE=${MEDIAN_SETTING#*:}
    if printf '%s\n' "$MEDIAN_PMSET" | grep -Eq "[[:space:]]${MEDIAN_SETTING_NAME}[[:space:]]+${MEDIAN_SETTING_VALUE}$"; then
        pass "power setting $MEDIAN_SETTING_NAME $MEDIAN_SETTING_VALUE"
    else
        fail "power setting missing: $MEDIAN_SETTING_NAME $MEDIAN_SETTING_VALUE"
    fi
done

MEDIAN_AGENT_PLIST="$HOME/Library/LaunchAgents/$MEDIAN_LAUNCH_AGENT.plist"
if [ -f "$MEDIAN_AGENT_PLIST" ] && \
   plutil -lint "$MEDIAN_AGENT_PLIST" >/dev/null 2>&1 && \
   grep -Fq "$MEDIAN_CHATGPT_APP" "$MEDIAN_AGENT_PLIST"; then
    pass "ChatGPT startup LaunchAgent is installed and valid"
else
    fail "ChatGPT startup LaunchAgent is absent, invalid, or targets another app"
fi

if launchctl print "gui/$(id -u)/$MEDIAN_LAUNCH_AGENT" >/dev/null 2>&1; then
    pass "ChatGPT startup LaunchAgent is loaded"
else
    fail "ChatGPT startup LaunchAgent is not loaded"
fi

if [ -d "$MEDIAN_CHATGPT_APP" ]; then
    MEDIAN_CHATGPT_VERSION=$(/usr/libexec/PlistBuddy -c 'Print :CFBundleShortVersionString' "$MEDIAN_CHATGPT_APP/Contents/Info.plist" 2>/dev/null || printf 'unknown')
    pass "ChatGPT Classic app exists (version $MEDIAN_CHATGPT_VERSION)"
else
    fail "ChatGPT Classic app is missing at $MEDIAN_CHATGPT_APP"
fi

MEDIAN_CRD_VERSION=$(pkgutil --pkg-info com.google.pkg.ChromeRemoteDesktopHost 2>/dev/null | awk '/^version:/ {print $2}')
if [ -n "$MEDIAN_CRD_VERSION" ] && [ -d /Library/PrivilegedHelperTools/ChromeRemoteDesktopHost.app ]; then
    pass "Chrome Remote Desktop host is installed (version $MEDIAN_CRD_VERSION)"
else
    fail "Chrome Remote Desktop host installation is incomplete"
fi

if ! git -C "$MEDIAN_REPO_ROOT" rev-parse --is-inside-work-tree >/dev/null 2>&1; then
    fail "repository is not a Git worktree"
else
    MEDIAN_BRANCH=$(git -C "$MEDIAN_REPO_ROOT" branch --show-current)
    MEDIAN_HEAD=$(git -C "$MEDIAN_REPO_ROOT" rev-parse HEAD)
    info "Git: $MEDIAN_BRANCH $MEDIAN_HEAD"
    [ "$MEDIAN_BRANCH" = "main" ] && pass "active branch is main" || warn "active branch is $MEDIAN_BRANCH"
    [ -z "$(git -C "$MEDIAN_REPO_ROOT" status --porcelain=v1)" ] && pass "worktree is clean" || warn "worktree has uncommitted changes"

    if git -C "$MEDIAN_REPO_ROOT" show-ref --verify --quiet refs/remotes/origin/main; then
        MEDIAN_DIVERGENCE=$(git -C "$MEDIAN_REPO_ROOT" rev-list --left-right --count HEAD...origin/main)
        set -- $MEDIAN_DIVERGENCE
        if [ "${1:-}" = "0" ] && [ "${2:-}" = "0" ]; then
            pass "HEAD and cached origin/main are aligned"
        else
            warn "HEAD and cached origin/main divergence: $MEDIAN_DIVERGENCE"
        fi
    else
        fail "cached origin/main reference is missing"
    fi
fi

MEDIAN_PYTHON="$MEDIAN_REPO_ROOT/.venv/bin/python"
if [ -x "$MEDIAN_PYTHON" ]; then
    MEDIAN_PY_VERSION=$($MEDIAN_PYTHON --version 2>&1)
    pass "repository environment exists ($MEDIAN_PY_VERSION)"
else
    fail "repository .venv Python is missing"
fi

if [ "$MEDIAN_DEEP" -eq 1 ] && [ -x "$MEDIAN_PYTHON" ]; then
    if "$MEDIAN_PYTHON" -m pip check >/dev/null; then
        pass "Python dependency consistency check"
    else
        fail "Python dependency consistency check"
    fi
    if "$MEDIAN_PYTHON" -m pytest -q "$MEDIAN_REPO_ROOT/m050/extraction/engine/tests"; then
        pass "Gate 5 regression suite"
    else
        fail "Gate 5 regression suite"
    fi
fi

printf '\nResult: %s failure(s), %s warning(s)\n' "$MEDIAN_FAILURES" "$MEDIAN_WARNINGS"
[ "$MEDIAN_FAILURES" -eq 0 ]
