import json
from pathlib import Path

from median_gate5.extraction_machine import (
    build_anthropic_request,
    build_generic_response_schema,
    draft_block_dispositions,
    plan_source_chunks,
)
from median_gate5.schema import validate_artifact
from median_gate5.structure import parse_markdown


REPO_ROOT = Path(__file__).resolve().parents[4]


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
