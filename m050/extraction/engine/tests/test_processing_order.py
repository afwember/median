import json
from pathlib import Path


M050 = Path(__file__).resolve().parents[3]
ORDER_PATH = M050 / "extraction/control/M050_Compile_Source_Processing_Order_v0_1_MEDIANv0_5_0.json"
MATRIX_PATH = M050 / "extraction/control/M050_Compile_Source_State_Matrix_v0_1_MEDIANv0_5_0.json"


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
        source = by_id[item["source_id"]]
        assert item["matrix_position"] == source["position"]
        assert item["current_state"] == source["current_state"]
        assert item["processing_phase"] == source["processing_phase"]


def test_processing_order_selects_authorial_grammar_then_exact_14_source_queue():
    order = _load(ORDER_PATH)
    matrix = _load(MATRIX_PATH)
    ordered_ids = [item["source_id"] for item in order["sequence"]]
    by_id = {source["source_id"]: source for source in matrix["sources"]}
    expected_queue = [
        source_id
        for source_id in ordered_ids
        if by_id[source_id]["current_state"] == "outstanding"
        and by_id[source_id]["processing_phase"] == "pre_reconciliation_atomization"
    ]

    assert order["next_source"]["source_id"] == "M050-SRC-AUTHORIAL-GRAMMAR-001"
    assert order["outstanding_pre_reconciliation_order"] == expected_queue
    assert len(expected_queue) == 14
    authorial = order["sequence"][0]["pre_candidate_acceptance_control"]
    assert authorial["higher_authority_source_id"] == "M050-SRC-HUMAN-RULINGS-001"
    assert authorial["provider_prompt_inclusion"] == "prohibited"
    assert "Layer E semantic acceptance" in authorial["effect"]
