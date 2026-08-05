#!/usr/bin/env python3
"""Render STATUS.md atomically from the canonical MEDIAN compile state."""

from __future__ import annotations

import json
import os
import stat
import tempfile
from datetime import datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

from m050_guard import STATE, STATUS, expected_status


EASTERN = ZoneInfo("America/New_York")


def _atomic_write(path: Path, content: str) -> None:
    mode = stat.S_IMODE(path.stat().st_mode) if path.exists() else 0o644
    descriptor, temporary_name = tempfile.mkstemp(
        dir=path.parent,
        prefix=f".{path.name}.",
    )
    temporary_path = Path(temporary_name)
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8") as handle:
            handle.write(content)
            handle.flush()
            os.fsync(handle.fileno())
        os.chmod(temporary_path, mode)
        os.replace(temporary_path, path)
    except BaseException:
        temporary_path.unlink(missing_ok=True)
        raise


def _rounded_timestamp(now: datetime | None = None) -> datetime:
    exact = now or datetime.now(EASTERN)
    if exact.tzinfo is None:
        raise ValueError("STATUS timestamp must be timezone-aware")
    if exact.microsecond >= 500_000:
        exact += timedelta(seconds=1)
    return exact.astimezone(EASTERN).replace(microsecond=0)


def _human_timestamp(exact: datetime) -> str:
    return (
        f"{exact.strftime('%B')} {exact.day}, {exact.year} at "
        f"{exact.strftime('%I').lstrip('0')}:{exact.strftime('%M:%S %p %Z')}"
    )


def render_status(
    state_path: Path = STATE,
    status_path: Path = STATUS,
    *,
    now: datetime | None = None,
) -> str:
    """Timestamp canonical state and replace its derived dashboard atomically."""
    state = json.loads(state_path.read_text(encoding="utf-8"))
    if not isinstance(state, dict):
        raise ValueError("canonical compile state must be a JSON object")

    exact = _rounded_timestamp(now)
    state["updated"] = exact.isoformat()
    state.setdefault("dashboard", {})["updated_human"] = _human_timestamp(exact)
    _atomic_write(
        state_path,
        json.dumps(state, indent=2, ensure_ascii=False) + "\n",
    )
    rendered = expected_status(state)
    _atomic_write(status_path, rendered)
    return rendered


def main() -> int:
    render_status()
    print("STATUS.md refreshed from canonical compile state.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
