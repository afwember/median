import copy
from collections import Counter
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


def test_stage_5_provider_and_manual_spend_window_are_bound():
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
    if state["spend"]["active"]:
        assert refresh_window > Decimal("0")
    assert state["spend"]["active"] is (
        state["execution_state"] == "RECONCILIATION_ACTIVE"
    )
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
    assert "`boundary_required` instead of rejecting Spark Up" in text


def test_authorial_ontology_correction_is_bounded_and_canonical():
    state = _state()
    vocabulary = json.loads(
        (ROOT / "m050/mapping/M050_MSID_Vocabulary_MEDIANv0_5_0.json").read_text(
            encoding="utf-8"
        )
    )
    assert "Citizen" in vocabulary["settled_tlds"]
    assert "Citizen" not in vocabulary["provisional_tlds"]
    assert {
        "Citizen.Citizen",
        "Citizen.Core",
        "Citizen.Core.Mouse",
        "Citizen.Core.Rabbit",
        "Citizen.Core.Squirrel",
        "Citizen.Guest",
        "Citizen.Guest.Expedition",
        "Citizen.Guest.Resident",
        "Away.Cargo",
        "Away.Cargo.Strained",
    } <= set(vocabulary["settled_paths"])
    assert state["reconciliation"]["target"] == {
        "tranche_id": "away-crossing-squirrel-002",
        "msid_prefix": "Away.Crossing.Squirrel",
        "selector": "exact",
    }
    completed = state["reconciliation"]["completed_tranche_ids"]
    assert "away-crossing-pilot" in completed
    assert "away-crossing-squirrel-001" not in completed
    mappings = [
        json.loads(line)
        for line in (
            ROOT / "m050/mapping/M050_Atom_MSID_Mappings_MEDIANv0_5_0.jsonl"
        ).read_text(encoding="utf-8").splitlines()
    ]
    corrections = [
        row for row in mappings
        if row["mapper"] == "Compile Supervisor — authorial ontology correction"
    ]
    assert len(corrections) == 26
    assert Counter(row["primary_msid"] for row in corrections) == {
        "Citizen.Core.Squirrel": 8,
        "Away.Cargo.Strained": 13,
        "Away.Crossing.Squirrel": 5,
    }
    assert all("GUEST" not in row["atom_key"] for row in corrections)


def test_status_is_exact_derived_view():
    state = _state()
    assert guard.STATUS.read_text(encoding="utf-8") == guard.expected_status(state)
