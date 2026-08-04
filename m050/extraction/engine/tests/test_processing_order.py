import json
from pathlib import Path


M050 = Path(__file__).resolve().parents[3]
ORDER_PATH = M050 / "extraction/control/M050_Compile_Source_Processing_Order_v0_1_MEDIANv0_5_0.json"
MATRIX_PATH = M050 / "extraction/control/M050_Compile_Source_State_Matrix_v0_1_MEDIANv0_5_0.json"
STATE_PATH = M050 / "extraction/control/M050_Compile_State_MEDIANv0_5_0.json"


def _load(path):
    return json.loads(path.read_text(encoding="utf-8"))


def test_processing_order_is_complete_unique_and_bound_to_source_state_matrix():
    order = _load(ORDER_PATH)
    matrix = _load(MATRIX_PATH)
    sequence = order["sequence"]
    by_id = {source["source_id"]: source for source in matrix["sources"]}

    assert [item["order"] for item in sequence] == list(range(1, 25))
    assert len({item["source_id"] for item in sequence}) == 24
    assert {item["source_id"] for item in sequence} == set(by_id)
    for item in sequence:
        assert set(item) <= {"order", "source_id", "label", "pre_candidate_acceptance_control"}
        assert item["label"]


def test_processing_order_and_canonical_progress_form_one_prefix_and_queue():
    order = _load(ORDER_PATH)
    matrix = _load(MATRIX_PATH)
    state = _load(STATE_PATH)
    ordered_ids = [item["source_id"] for item in order["sequence"]]
    by_id = {source["source_id"]: source for source in matrix["sources"]}
    completed = set(state["progress"]["completed_source_ids"])
    compile_scope_ids = [
        source_id
        for source_id in ordered_ids
        if by_id[source_id]["in_compile_scope"]
    ]
    completed_prefix = [
        source_id for source_id in compile_scope_ids if source_id in completed
    ]
    expected_queue = [
        source_id for source_id in compile_scope_ids if source_id not in completed
    ]

    assert len(compile_scope_ids) == state["corpus"]["compile_scope_sources"]
    assert completed == set(completed_prefix)
    assert completed_prefix == compile_scope_ids[:len(completed_prefix)]
    assert expected_queue == compile_scope_ids[len(completed_prefix):]
    assert len(expected_queue) == state["corpus"]["outstanding_compile_scope_sources"]
    assert "next_source" not in order
    assert "outstanding_pre_reconciliation_order" not in order
    authorial = order["sequence"][0]["pre_candidate_acceptance_control"]
    assert authorial["higher_authority_source_id"] == "M050-SRC-HUMAN-RULINGS-001"
    assert authorial["provider_prompt_inclusion"] == "prohibited"
    assert "Layer E semantic acceptance" in authorial["effect"]
