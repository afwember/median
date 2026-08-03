import copy
import json
from pathlib import Path

import pytest
import yaml

from median_gate5.corpus import derive_compile_source_state
from median_gate5.errors import ContractError


REPO_ROOT = Path(__file__).resolve().parents[4]


def _gate_2():
    path = REPO_ROOT / "m050/extraction/audit/M050_Extraction_Gate_2_Source_Disposition_v0_1_MEDIANv0_5_0.yaml"
    return path, yaml.safe_load(path.read_text(encoding="utf-8"))


def test_compile_scope_is_derived_as_24_22_4_18_14_4():
    path, gate_2 = _gate_2()
    state = derive_compile_source_state(
        gate_2, manifest_path=str(path.relative_to(REPO_ROOT)), manifest_sha256="0" * 64
    )
    assert state["summary"] == {
        "registered_sources": 24,
        "atomic_compile_exclusions": 2,
        "compile_scope_sources": 22,
        "atomized_legacy_seed_sources": 4,
        "outstanding_compile_scope_sources": 18,
        "outstanding_pre_reconciliation_sources": 14,
        "outstanding_later_or_conditional_sources": 4,
    }
    assert len(state["sources"]) == 24
    assert all(not allowed for allowed in state["transition_constraints"].values())


def test_compile_scope_fails_closed_on_unknown_or_duplicate_source():
    _, gate_2 = _gate_2()
    unknown = copy.deepcopy(gate_2)
    unknown["sources"][0]["disposition"] = "invented_disposition"
    with pytest.raises(ContractError, match="unrecognized"):
        derive_compile_source_state(unknown, manifest_path="gate2.yaml", manifest_sha256="0" * 64)

    duplicate = copy.deepcopy(gate_2)
    duplicate["sources"][1]["source_id"] = duplicate["sources"][0]["source_id"]
    with pytest.raises(ContractError, match="duplicate"):
        derive_compile_source_state(duplicate, manifest_path="gate2.yaml", manifest_sha256="0" * 64)


def test_committed_compile_scope_matrix_matches_authoritative_gate_2():
    path, gate_2 = _gate_2()
    matrix_path = REPO_ROOT / "m050/extraction/control/M050_Compile_Source_State_Matrix_v0_1_MEDIANv0_5_0.json"
    committed = json.loads(matrix_path.read_text(encoding="utf-8"))
    from median_gate5.canonical import sha256_file

    expected = derive_compile_source_state(
        gate_2,
        manifest_path=str(path.relative_to(REPO_ROOT)),
        manifest_sha256=sha256_file(path),
    )
    assert committed == expected
