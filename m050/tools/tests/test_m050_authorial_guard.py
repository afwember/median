from __future__ import annotations

import json
from pathlib import Path
import sys


TOOLS = Path(__file__).resolve().parents[1]
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

import m050_guard as guard


def test_authorial_structure_repository_passes() -> None:
    errors: list[str] = []
    state = guard.read_json(guard.STATE, errors)
    guard.validate_operating_contract(errors)
    guard.validate_topology(errors)
    guard.validate_state(state, errors)
    assert guard.validate_manifest_and_corpus(state, errors) == (5382, 18)
    assert errors == []


def test_provisional_structure_preserves_approved_spine() -> None:
    errors: list[str] = []
    guard.validate_gdd_structure(errors)
    assert errors == []


def test_status_stays_on_direct_authorial_surface() -> None:
    state = json.loads(guard.STATE.read_text(encoding="utf-8"))
    rendered = guard.expected_status(state)
    for retired_surface in ("SPEND", "PROVIDER", "TRANCHE", "WORKER"):
        assert retired_surface not in rendered
    assert "Direct authorial GDD creation" in rendered
    assert "provisional GDD structure" in rendered
