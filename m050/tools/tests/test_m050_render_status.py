import json
from pathlib import Path
import sys


TOOLS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))
try:
    from m050_render_status import render_status
finally:
    sys.path.remove(str(TOOLS))


def test_renderer_atomically_replaces_dashboard_without_changing_state(tmp_path):
    state_path = tmp_path / "state.json"
    status_path = tmp_path / "STATUS.md"
    state = {
        "dashboard": {
            "updated_human": "August 4, 2026 at 5:46:07 PM EDT",
            "status": "Stopped",
            "phase": "Atomic extraction",
            "source": "Guest",
            "chunk": "C0018",
            "now": "Supervisor handoff",
            "next": "Await authorization",
        },
        "spend": {"remaining_usd": "0.2167150"},
    }
    state_path.write_text(json.dumps(state), encoding="utf-8")
    original_state = state_path.read_bytes()
    status_path.write_text("stale dashboard\n", encoding="utf-8")

    rendered = render_status(state_path, status_path)

    assert status_path.read_text(encoding="utf-8") == rendered
    assert rendered.endswith("**SPEND REMAINING:** $0.21\n")
    assert state_path.read_bytes() == original_state
    assert set(tmp_path.iterdir()) == {state_path, status_path}
