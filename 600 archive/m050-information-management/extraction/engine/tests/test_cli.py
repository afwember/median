import json
from pathlib import Path
import subprocess
import sys


def run_cli(*args):
    return subprocess.run(
        [sys.executable, "-m", "median_gate5.cli", *args],
        text=True,
        capture_output=True,
        check=False,
    )


def test_offline_cli_block_plan_validate_round_trip(tmp_path):
    source_dir = tmp_path / "m050" / "docs" / "v0.5"
    output_dir = tmp_path / "m050" / "extraction" / "runs" / "fixture"
    source_dir.mkdir(parents=True)
    source = source_dir / "source.md"
    source.write_text("# Home\n\nColonists must rest.\n", encoding="utf-8")

    blocks_path = output_dir / "blocks.json"
    block_result = run_cli(
        "block",
        "--repo-root",
        str(tmp_path),
        "--source-id",
        "SRC-HOME",
        "--source-path",
        "m050/docs/v0.5/source.md",
        "--output",
        str(blocks_path),
    )
    assert block_result.returncode == 0, block_result.stderr
    blocks = json.loads(blocks_path.read_text())

    chunks_path = output_dir / "chunks.json"
    plan_result = run_cli(
        "plan",
        "--repo-root",
        str(tmp_path),
        "--block-manifest",
        str(blocks_path),
        "--max-tokens",
        "100",
        "--max-claim-blocks",
        "2",
        "--output",
        str(chunks_path),
    )
    assert plan_result.returncode == 0, plan_result.stderr
    assert json.loads(chunks_path.read_text())["chunks"]

    claim_block = next(block for block in blocks["blocks"] if block["claim_bearing"])
    proposal = {
        "schema_version": "M050-EVIDENCE-PROPOSAL-0.1",
        "proposal_set_id": "proposal-set-1",
        "request_id": "request-1",
        "source_id": "SRC-HOME",
        "dispositions": [
            {
                "block_id": claim_block["block_id"],
                "kind": "atoms",
                "atoms": [
                    {
                        "proposal_id": "proposal-1",
                        "source_id": "SRC-HOME",
                        "block_id": claim_block["block_id"],
                        "exact_source_text": "Colonists must rest.",
                        "normalized_claim": "Colonists must rest.",
                        "claim_kind": "mechanic",
                        "stream": "evidence_game_semantic",
                    }
                ],
            }
        ],
    }
    proposal_path = output_dir / "proposal.json"
    proposal_path.write_text(json.dumps(proposal), encoding="utf-8")
    report_path = output_dir / "validation.json"
    validate_result = run_cli(
        "validate-proposal",
        "--repo-root",
        str(tmp_path),
        "--block-manifest",
        str(blocks_path),
        "--proposal",
        str(proposal_path),
        "--output",
        str(report_path),
    )
    assert validate_result.returncode == 0, validate_result.stderr
    assert json.loads(report_path.read_text())["passed"]


def test_cli_refuses_artifact_overwrite(tmp_path):
    source_dir = tmp_path / "m050" / "docs" / "v0.5"
    source_dir.mkdir(parents=True)
    source = source_dir / "source.md"
    source.write_text("Rule.", encoding="utf-8")
    output = tmp_path / "m050" / "extraction" / "blocks.json"
    args = (
        "block",
        "--repo-root",
        str(tmp_path),
        "--source-id",
        "SRC",
        "--source-path",
        "m050/docs/v0.5/source.md",
        "--output",
        str(output),
    )
    assert run_cli(*args).returncode == 0
    second = run_cli(*args)
    assert second.returncode == 2
    assert "output already exists" in second.stderr


def test_cli_rejects_output_escape(tmp_path):
    source_dir = tmp_path / "m050" / "docs" / "v0.5"
    source_dir.mkdir(parents=True)
    source = source_dir / "source.md"
    source.write_text("Rule.", encoding="utf-8")
    result = run_cli(
        "block",
        "--repo-root",
        str(tmp_path),
        "--source-id",
        "SRC",
        "--source-path",
        "m050/docs/v0.5/source.md",
        "--output",
        str(tmp_path / "outside.json"),
    )
    assert result.returncode == 2
    assert "escapes m050/extraction" in result.stderr
