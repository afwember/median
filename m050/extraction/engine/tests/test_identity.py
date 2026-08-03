import json
from pathlib import Path
import subprocess
import sys

import yaml

from median_gate5.canonical import content_id, sha256_file
from median_gate5.identity import identity_card_errors
from median_gate5.structure import parse_markdown


def _write_json(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, sort_keys=True) + "\n", encoding="utf-8")


def _binding(root: Path, relative: str, role: str) -> dict:
    return {"path": relative, "sha256": sha256_file(root / relative), "role": role}


def identity_fixture(tmp_path: Path):
    source_relative = "m050/docs/v0.5/source.md"
    source = tmp_path / source_relative
    source.parent.mkdir(parents=True)
    source.write_text("# Purpose\n\nThis source defines a rule.\n", encoding="utf-8")
    source_sha = sha256_file(source)
    blocks = parse_markdown("SRC-1", source.read_text(encoding="utf-8"))
    block_body = {
        "source_id": "SRC-1",
        "source_sha256": source_sha,
        "normalization_version": "M050-NORMALIZATION-0.1",
        "blocks": [block.to_dict() for block in blocks],
    }
    block_manifest = {
        "schema_version": "M050-BLOCK-MANIFEST-0.1",
        "manifest_id": content_id("bm", block_body),
        **block_body,
    }
    block_relative = "m050/extraction/control/blocks/source.json"
    _write_json(tmp_path / block_relative, block_manifest)

    candidate_relative = "m050/extraction/accepted/source.jsonl"
    report_relative = "m050/extraction/accepted/source-report.json"
    (tmp_path / candidate_relative).parent.mkdir(parents=True, exist_ok=True)
    (tmp_path / candidate_relative).write_text("{}\n", encoding="utf-8")
    _write_json(tmp_path / report_relative, {"accepted": True})

    frozen_manifest = {
        "frozen_files": [
            {"path": source_relative, "sha256": source_sha, "source_id": "SRC-1"}
        ]
    }
    frozen_relative = "m050/extraction/control/frozen.json"
    _write_json(tmp_path / frozen_relative, frozen_manifest)
    source_disposition = {
        "sources": [
            {
                "source_id": "SRC-1",
                "path": source_relative,
                "sha256": source_sha,
                "output_streams": ["evidence_game_semantic"],
            }
        ]
    }
    reuse_disposition = {
        "sources": [
            {
                "source_id": "SRC-1",
                "candidate_path": candidate_relative,
                "candidate_sha256": sha256_file(tmp_path / candidate_relative),
                "records": 1,
                "distinct_source_locations": 1,
                "likely_compound_review_flags": 0,
                "reuse": "migrate_grounded_evidence_to_layer_e",
                "paid_reextraction": False,
                "mandatory_repairs": ["retrospective_block_disposition_ledger"],
            }
        ]
    }
    source_disposition_relative = "m050/extraction/audit/source-disposition.yaml"
    reuse_disposition_relative = "m050/extraction/audit/reuse-disposition.yaml"
    (tmp_path / source_disposition_relative).parent.mkdir(parents=True, exist_ok=True)
    (tmp_path / source_disposition_relative).write_text(
        yaml.safe_dump(source_disposition), encoding="utf-8"
    )
    (tmp_path / reuse_disposition_relative).write_text(
        yaml.safe_dump(reuse_disposition), encoding="utf-8"
    )
    cited_block = next(block for block in blocks if block.claim_bearing)
    body = {
        "schema_version": "M050-SOURCE-IDENTITY-CARD-0.2",
        "version": 1,
        "status": "draft",
        "source_id": "SRC-1",
        "source_path": source_relative,
        "source_sha256": source_sha,
        "frozen_manifest_binding": _binding(tmp_path, frozen_relative, "frozen_source_registry"),
        "block_manifest_binding": _binding(tmp_path, block_relative, "structural_block_registry"),
        "source_disposition_binding": _binding(
            tmp_path, source_disposition_relative, "gate_2_source_disposition"
        ),
        "reuse_disposition_binding": _binding(
            tmp_path, reuse_disposition_relative, "gate_3_reuse_disposition"
        ),
        "genealogy_summary": "Fixture source with no predecessor material.",
        "predecessor_bindings": [],
        "predecessor_coverage_warnings": [
            {
                "subject": "fixture_predecessor",
                "coverage_status": "no_direct_predecessor_identified",
                "warning": "No direct predecessor was identified for this fixture.",
                "extraction_effect": "warning_only_no_extraction_influence",
            }
        ],
        "roles": [
            {
                "role": "game_rule_source",
                "scope": "The one fixture rule only.",
                "allowed_streams": ["evidence_game_semantic"],
                "supporting_block_ids": [cited_block.block_id],
            }
        ],
        "allowed_streams": ["evidence_game_semantic"],
        "authority_boundary": "Identity describes content and does not grant cross-source authority.",
        "mixed_status_regions": [],
        "supporting_block_ids": [cited_block.block_id],
        "exclusions": [],
        "legacy_extraction": {
            "lineage_summary": "One grounded legacy candidate.",
            "source_bindings": [
                {"path": source_relative, "sha256": source_sha, "role": "active_frozen_source"}
            ],
            "candidate": _binding(tmp_path, candidate_relative, "immutable_legacy_candidate"),
            "acceptance_report": _binding(tmp_path, report_relative, "legacy_acceptance_report"),
            "record_count": 1,
            "distinct_source_locations": 1,
            "likely_compound_review_flags": 0,
            "evidence_status": "immutable_legacy_candidate",
            "reuse_disposition": "migrate_grounded_evidence_to_layer_e",
            "partition_warning": None,
        },
        "migration": {
            "eligibility": "eligible_after_offline_repairs",
            "paid_reextraction_required": False,
            "mandatory_repairs": ["retrospective_block_disposition_ledger"],
            "prerequisites": ["identity_card_review"],
        },
        "supersedes_card_id": None,
    }
    card = {"card_id": content_id("sic", body), **body}
    return card, block_manifest, frozen_manifest, source_disposition, reuse_disposition


def test_v02_identity_card_cross_checks_all_controls(tmp_path):
    values = identity_fixture(tmp_path)
    assert identity_card_errors(tmp_path, *values) == []


def test_v02_identity_card_detects_content_id_and_block_drift(tmp_path):
    card, *controls = identity_fixture(tmp_path)
    card["card_id"] = "sic_000000000000000000000000"
    card["supporting_block_ids"] = ["SRC-1__B99999_missing"]
    errors = identity_card_errors(tmp_path, card, *controls)
    assert any("content-derived card ID mismatch" in error for error in errors)
    assert any("unknown block IDs" in error for error in errors)


def test_v02_identity_card_rejects_unbound_supplied_control(tmp_path):
    card, block_manifest, frozen_manifest, source_disposition, reuse_disposition = identity_fixture(tmp_path)
    supplied = {**source_disposition, "unbound_note": "not in the card-bound file"}
    errors = identity_card_errors(
        tmp_path,
        card,
        block_manifest,
        frozen_manifest,
        supplied,
        reuse_disposition,
    )
    assert any("supplied control does not match bound artifact" in error for error in errors)


def test_profile_cli_validates_identity_card(tmp_path):
    card, block_manifest, frozen_manifest, source_disposition, reuse_disposition = identity_fixture(tmp_path)
    card_path = tmp_path / "m050/extraction/control/card.json"
    source_disposition_path = tmp_path / "m050/extraction/audit/source-disposition.yaml"
    reuse_disposition_path = tmp_path / "m050/extraction/audit/reuse-disposition.yaml"
    _write_json(card_path, card)
    source_disposition_path.parent.mkdir(parents=True, exist_ok=True)
    source_disposition_path.write_text(yaml.safe_dump(source_disposition), encoding="utf-8")
    reuse_disposition_path.write_text(yaml.safe_dump(reuse_disposition), encoding="utf-8")
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "median_gate5.cli",
            "profile",
            "--repo-root",
            str(tmp_path),
            "--card",
            str(card_path),
            "--block-manifest",
            str(tmp_path / "m050/extraction/control/blocks/source.json"),
            "--frozen-manifest",
            str(tmp_path / "m050/extraction/control/frozen.json"),
            "--source-disposition",
            str(source_disposition_path),
            "--reuse-disposition",
            str(reuse_disposition_path),
        ],
        text=True,
        capture_output=True,
        check=False,
    )
    assert result.returncode == 0, result.stderr
    assert json.loads(result.stdout)["passed"] is True
