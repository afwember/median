from __future__ import annotations

from datetime import datetime
import json
from pathlib import Path
import sys
from zoneinfo import ZoneInfo


TOOLS = Path(__file__).resolve().parents[1]
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

import m050_guard as guard
import m050_render_status as renderer


def test_renderer_updates_state_and_dashboard_together(tmp_path: Path) -> None:
    state_path = tmp_path / "state.json"
    status_path = tmp_path / "STATUS.md"
    state = json.loads(guard.STATE.read_text(encoding="utf-8"))
    state_path.write_text(json.dumps(state), encoding="utf-8")
    exact = datetime(2026, 9, 12, 10, 0, 0, 600000, tzinfo=ZoneInfo("America/New_York"))

    rendered = renderer.render_status(state_path, status_path, now=exact)

    updated = json.loads(state_path.read_text(encoding="utf-8"))
    assert updated["updated"] == "2026-09-12T10:00:01-04:00"
    assert updated["dashboard"]["updated_human"] == "September 12, 2026 at 10:00:01 AM EDT"
    assert status_path.read_text(encoding="utf-8") == rendered
    assert renderer.check_status(state_path, status_path)
