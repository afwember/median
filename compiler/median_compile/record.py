"""Build Record — append-only log of every phase run.

Required by the compiler spec (§A3 artifact set, §A23 build record, §12 phase
gates). Without it the build is a pile of artifacts with no provenance: you can
see *what* a phase produced but not when it ran, against which source hashes,
or with which ruleset version.

It also supplies the input to staleness detection (§7). A phase is stale when
the hashes it consumed no longer match what is on disk. That is computable only
if each run wrote down what it consumed.

One JSON object per line in `logs/build_record.jsonl`. Never rewritten.
"""

from __future__ import annotations

import getpass
import json
import platform
import subprocess
import time
from contextlib import contextmanager
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path

RECORD_VERSION = "1.0"


#: `git status` takes .git/index.lock to refresh cached stat information, even
#: though it is a read. Running it once per phase left an orphaned lock that
#: blocked the next real git command. --no-optional-locks tells git to skip
#: exactly that write, which is what we want from a logging call: observing the
#: repository must never mutate it.
GIT_READONLY = ["git", "--no-optional-locks"]


def _git(repo: Path, *args: str) -> str:
    try:
        out = subprocess.run(
            [*GIT_READONLY, "-C", str(repo), *args],
            capture_output=True,
            text=True,
            check=False,
            timeout=10,
        )
    except (FileNotFoundError, subprocess.TimeoutExpired):  # pragma: no cover
        return ""
    return out.stdout.strip()


def git_sha(repo: Path) -> str:
    """Short HEAD SHA, suffixed `-dirty` when the tree has uncommitted changes."""
    sha = _git(repo, "rev-parse", "--short", "HEAD")
    if not sha:
        return "unknown"
    return f"{sha}-dirty" if _git(repo, "status", "--porcelain") else sha


@dataclass
class Run:
    phase: str
    command: str
    versions: dict = field(default_factory=dict)
    inputs: dict = field(default_factory=dict)
    outputs: dict = field(default_factory=dict)
    metrics: dict = field(default_factory=dict)
    notes: str = ""
    status: str = "ok"

    def to_dict(self) -> dict:
        return {"record": RECORD_VERSION, **self.__dict__}


@contextmanager
def record(build, phase: str, command: str, versions: dict | None = None):
    """Wrap a phase run so it is logged whether it succeeds or fails.

    A failed run is logged too. A build record that only contains successes
    hides exactly the history worth keeping.
    """
    run = Run(phase=phase, command=command, versions=versions or {})
    started = time.time()
    try:
        yield run
    except BaseException as exc:  # noqa: BLE001 - re-raised below
        run.status = "error"
        run.notes = f"{type(exc).__name__}: {exc}"[:300]
        raise
    finally:
        entry = run.to_dict()
        entry.update(
            {
                "timestamp": datetime.now(timezone.utc).isoformat(timespec="seconds"),
                "duration_s": round(time.time() - started, 2),
                "git": git_sha(build.repo),
                "operator": _operator(),
                "host": platform.node(),
                "python": platform.python_version(),
            }
        )
        path = build.logs / "build_record.jsonl"
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("a", encoding="utf-8") as fh:
            fh.write(json.dumps(entry, ensure_ascii=False) + "\n")


def _operator() -> str:
    try:
        return getpass.getuser()
    except Exception:  # pragma: no cover - environment guard
        return "unknown"


def history(build) -> list[dict]:
    path = build.logs / "build_record.jsonl"
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line]


def last_run(build, phase: str) -> dict | None:
    runs = [r for r in history(build) if r["phase"] == phase and r["status"] == "ok"]
    return runs[-1] if runs else None


def accumulated_inputs(build, phase: str) -> dict[str, str]:
    """Latest recorded hash per input across every successful run of a phase.

    A run scoped to one source (`--source SPEC_CROSS`) records only that
    source's input. Reading the last run alone would then report the other 21
    sources as new on the next check. Accumulating, with later runs overriding
    earlier ones per key, describes what the build actually knows.
    """
    inputs: dict[str, str] = {}
    for run in history(build):
        if run["phase"] == phase and run["status"] == "ok":
            inputs.update(run.get("inputs", {}))
    return inputs


def staleness(build, current_by_phase: dict[str, dict[str, str]]) -> dict[str, list[str]]:
    """Which phases consumed inputs that have since changed.

    Compiler spec §7: a changed raw-source hash invalidates normalization and
    everything downstream of it.

    Each phase consumes a different artifact — `normalize-lean` consumes
    normalized_full, `chunk` consumes lean — so the caller supplies one current
    hash map per phase. Comparing every phase against raw source hashes reports
    the whole pipeline stale on a clean build.
    """
    stale: dict[str, list[str]] = {}
    for phase, current in current_by_phase.items():
        recorded = accumulated_inputs(build, phase)
        if not recorded:
            continue
        changed = [k for k, sha in recorded.items() if k in current and current[k] != sha]
        vanished = [k for k in recorded if k not in current]
        added = [k for k in current if k not in recorded]
        if changed or vanished or added:
            stale[phase] = (
                [f"{k} (changed)" for k in changed]
                + [f"{k} (missing)" for k in vanished]
                + [f"{k} (new)" for k in added]
            )
    return stale
