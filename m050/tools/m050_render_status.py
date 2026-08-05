#!/usr/bin/env python3
"""Render STATUS.md atomically from the canonical MEDIAN compile state."""

from __future__ import annotations

import json
import os
import stat
import tempfile
from pathlib import Path

from m050_guard import STATE, STATUS, expected_status


def render_status(state_path: Path = STATE, status_path: Path = STATUS) -> str:
    """Replace the derived dashboard without changing canonical state."""
    state = json.loads(state_path.read_text(encoding="utf-8"))
    if not isinstance(state, dict):
        raise ValueError("canonical compile state must be a JSON object")

    rendered = expected_status(state)
    mode = stat.S_IMODE(status_path.stat().st_mode) if status_path.exists() else 0o644
    descriptor, temporary_name = tempfile.mkstemp(
        dir=status_path.parent,
        prefix=f".{status_path.name}.",
    )
    temporary_path = Path(temporary_name)
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8") as handle:
            handle.write(rendered)
            handle.flush()
            os.fsync(handle.fileno())
        os.chmod(temporary_path, mode)
        os.replace(temporary_path, status_path)
    except BaseException:
        temporary_path.unlink(missing_ok=True)
        raise
    return rendered


def main() -> int:
    render_status()
    print("STATUS.md refreshed from canonical compile state.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
