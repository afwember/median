#!/usr/bin/env python3
"""Deliver the formal Stopdown message through the installed Codex CLI."""

from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
TARGET = "Compile Supervisor"
MESSAGE = "Worker has Stopped Down"


def notification_command(codex: str) -> list[str]:
    return [codex, "exec", "resume", TARGET, MESSAGE]


def notify() -> int:
    codex = shutil.which("codex")
    if codex is None:
        print("Stopdown notification failed: codex CLI is unavailable", file=sys.stderr)
        return 127
    result = subprocess.run(
        notification_command(codex),
        cwd=ROOT,
        stdin=subprocess.DEVNULL,
        check=False,
    )
    if result.returncode:
        print(
            f"Stopdown notification failed with exit status {result.returncode}",
            file=sys.stderr,
        )
    return result.returncode


if __name__ == "__main__":
    sys.exit(notify())
