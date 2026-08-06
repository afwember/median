import json
from pathlib import Path
import sys


TOOLS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))
try:
    from m050_render_status import check_status
finally:
    sys.path.remove(str(TOOLS))


def test_check_status_does_not_change_state_or_dashboard(tmp_path):
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
    from m050_guard import expected_status

    status_path.write_text(expected_status(state), encoding="utf-8")
    original_status = status_path.read_bytes()

    assert check_status(state_path, status_path)
    assert state_path.read_bytes() == original_state
    assert status_path.read_bytes() == original_status


def test_check_status_rejects_stale_dashboard_without_changing_files(tmp_path):
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
    status_path.write_text("stale dashboard\n", encoding="utf-8")
    original_state = state_path.read_bytes()
    original_status = status_path.read_bytes()

    assert not check_status(state_path, status_path)
    assert state_path.read_bytes() == original_state
    assert status_path.read_bytes() == original_status
