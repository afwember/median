import copy
from decimal import Decimal
import json
from pathlib import Path
import sys


ROOT = Path(__file__).parents[3]
TOOLS = ROOT / "m050/tools"
sys.path.insert(0, str(TOOLS))
try:
    import m050_guard as guard
finally:
    sys.path.remove(str(TOOLS))


def _state():
    return json.loads(guard.STATE.read_text(encoding="utf-8"))


def test_repository_stage_5_profile_is_valid():
    errors = []
    guard.validate_reconciliation_profile(errors)
    assert errors == []


def test_stage_5_provider_and_refreshable_window_are_bound():
    state = _state()
    provider = state["reconciliation"]["provider"]
    assert provider["enabled"] is True
    assert provider["name"] == "OpenAI"
    assert provider["model"] == "gpt-5.6-sol"
    assert provider["reasoning_effort"] == "medium"
    assert provider["maximum_output_tokens"] == {"proposal": 36000, "review": 8000}
    assert provider["cache_ttl"] == "30m"
    refresh_window = Decimal(state["spend"]["refresh_window_usd"])
    remaining = Decimal(state["spend"]["remaining_usd"])
    assert refresh_window > Decimal("0")
    assert Decimal("0") <= remaining <= refresh_window


def test_stage_5_lifecycle_rejects_provider_authority_while_disabled(monkeypatch):
    state = _state()
    state["reconciliation"]["provider"]["enabled"] = False
    state["authority"]["provider_calls_authorized"] = True
    monkeypatch.setattr(guard, "read_json", lambda path, errors: copy.deepcopy(state))
    errors = []
    guard.validate_reconciliation_profile(errors)
    assert "canonical Stage 5 authority disagrees with lifecycle" in errors


def test_operating_contract_names_only_stage_5_profile():
    text = guard.AGENTS.read_text(encoding="utf-8")
    assert "## Active phase profile — Stage 5 semantic reconciliation" in text
    assert "## Active phase profile — Stage 4 MSID mapping" not in text
    assert "m050/tools/m050_reconciliation.py" in text


def test_status_is_exact_derived_view():
    state = _state()
    assert guard.STATUS.read_text(encoding="utf-8") == guard.expected_status(state)
