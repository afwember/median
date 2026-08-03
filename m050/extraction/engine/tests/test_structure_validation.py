import pytest

from median_gate5.errors import ContractError
from median_gate5.structure import parse_markdown, plan_chunks
from median_gate5.validation import validate_atoms, validate_block_dispositions


SOURCE = """# Home

Colonists must rest; they cannot travel while exhausted.

| Tier | Capacity |
| --- | ---: |
| I | 4 |

STATE: SILENT
Historical note.
"""


def test_parser_preserves_complete_source_and_table_rows():
    blocks = parse_markdown("SRC-HOME", SOURCE)
    assert "".join(block.text for block in blocks) == SOURCE
    assert sum(block.block_type == "table_row" for block in blocks) == 3
    assert len({block.block_id for block in blocks}) == len(blocks)
    assert all(block.local_disposition for block in blocks)
    whitespace = [block for block in blocks if block.block_type == "whitespace"]
    assert all(block.local_reason_code == "whitespace_separator" for block in whitespace)


def test_chunk_plan_honors_status_boundary_and_limits():
    blocks = parse_markdown("SRC-HOME", SOURCE)
    chunks = plan_chunks(blocks, max_tokens=80, max_claim_blocks=2)
    assert all(chunk["estimated_tokens"] <= 80 for chunk in chunks)
    assert all(chunk["claim_bearing_blocks"] <= 2 for chunk in chunks)
    silent_id = next(block.block_id for block in blocks if block.status_markers)
    silent_chunk = next(chunk for chunk in chunks if silent_id in chunk["block_ids"])
    assert silent_chunk["block_ids"][-1] == silent_id


def test_oversized_block_fails_closed():
    blocks = parse_markdown("SRC", "word " * 100)
    with pytest.raises(ContractError, match="exceeds"):
        plan_chunks(blocks, max_tokens=2, max_claim_blocks=1)


def test_disposition_completeness_and_under_extraction_signal():
    blocks = [block.to_dict() for block in parse_markdown("SRC-HOME", SOURCE)]
    eligible = [block for block in blocks if block["claim_bearing"]]
    dispositions = []
    for index, block in enumerate(eligible):
        if index == 0:
            dispositions.append(
                {
                    "block_id": block["block_id"],
                    "kind": "atoms",
                    "atoms": [
                        {
                            "proposal_id": "p1",
                            "source_id": "SRC-HOME",
                            "block_id": block["block_id"],
                            "exact_source_text": "Colonists must rest",
                        }
                    ],
                }
            )
        else:
            dispositions.append(
                {"block_id": block["block_id"], "kind": "no_substantive_claim"}
            )
    assert validate_block_dispositions(blocks, dispositions)["passed"]
    result = validate_atoms("SRC-HOME", blocks, dispositions)
    assert result["passed"]
    assert eligible[0]["block_id"] in result["low_yield_review"]


def test_duplicate_and_missing_dispositions_fail():
    blocks = [block.to_dict() for block in parse_markdown("SRC", "One rule.\n\nTwo rules.")]
    eligible = [block["block_id"] for block in blocks if block["claim_bearing"]]
    dispositions = [
        {"block_id": eligible[0], "kind": "no_substantive_claim"},
        {"block_id": eligible[0], "kind": "no_substantive_claim"},
    ]
    result = validate_block_dispositions(blocks, dispositions)
    assert not result["passed"]
    assert result["errors"]["duplicates"] == [eligible[0]]
    assert eligible[1] in result["errors"]["missing"]
