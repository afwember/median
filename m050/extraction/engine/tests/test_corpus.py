import copy
import json
from pathlib import Path

import pytest
import yaml

from median_gate5.corpus import derive_compile_source_state
from median_gate5.errors import ContractError
from median_gate5.extraction_machine import (
    build_anthropic_request,
    build_generic_response_schema,
    draft_block_dispositions,
    plan_source_chunks,
)
from median_gate5.schema import validate_artifact
from median_gate5.structure import parse_markdown


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


def test_all_compile_scope_sources_parse_and_enter_generic_chunk_planner():
    matrix_path = REPO_ROOT / "m050/extraction/control/M050_Compile_Source_State_Matrix_v0_1_MEDIANv0_5_0.json"
    matrix = json.loads(matrix_path.read_text(encoding="utf-8"))
    compile_sources = [source for source in matrix["sources"] if source["in_compile_scope"]]
    assert len(compile_sources) == 22

    for source in compile_sources:
        path = REPO_ROOT / source["path"]
        blocks = parse_markdown(
            source["source_id"], path.read_text(encoding="utf-8", errors="strict")
        )
        manifest = {
            "schema_version": "M050-BLOCK-MANIFEST-0.1",
            "manifest_id": "bm_corpus_compatibility",
            "source_id": source["source_id"],
            "source_sha256": source["sha256"],
            "normalization_version": "M050-NORMALIZATION-0.1",
            "blocks": [block.to_dict() for block in blocks],
        }
        validate_artifact("block_manifest", manifest)
        dispositions = draft_block_dispositions(manifest)
        plan = plan_source_chunks(
            manifest,
            dispositions,
            max_input_tokens=10_000_000,
            target_blocks_per_chunk=1_000_000,
            quantization_basis="all-source structural compatibility smoke test",
        )
        assert [block_id for chunk in plan["chunks"] for block_id in chunk["block_ids"]] == [
            block["block_id"] for block in manifest["blocks"]
        ]
        target_ids = [
            item["block_id"]
            for item in dispositions
            if item["disposition"] == "eligible"
        ][:2]
        assert target_ids
        request = build_anthropic_request(
            prompt="Stable all-source compatibility policy",
            response_schema=build_generic_response_schema(
                source["source_id"], ["evidence_game_semantic"]
            ),
            payload={
                "source_id": source["source_id"],
                "required_target_disposition_count": len(target_ids),
                "target_blocks": [
                    {"block_id": block_id} for block_id in target_ids
                ],
            },
            model="claude-sonnet-5",
            reasoning_effort="low",
            maximum_output_tokens=6000,
            cache_ttl="1h",
        )
        disposition_schema = request["output_config"]["format"]["schema"][
            "properties"
        ]["dispositions"]
        assert disposition_schema["items"]["properties"]["block_id"] == {
            "type": "string",
            "pattern": (
                f"^{source['source_id']}__B[0-9]{{5}}_[0-9a-f]{{12}}$"
            ),
        }
