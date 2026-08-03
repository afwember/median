import json
from pathlib import Path

from median_gate5.rulings import build_human_rulings_reconstruction, parse_ledger


REPO_ROOT = Path(__file__).resolve().parents[4]
CARD_PATH = REPO_ROOT / "m050/extraction/control/source-identities/cards/M050_Human_Rulings_Source_Identity_Card_v0_4_MEDIANv0_5_0.json"
REPLAY_LEDGER_PATH = REPO_ROOT / "m050/extraction/replay/M050_Human_Rulings_Legacy_Replay_Ledger_v0_1_MEDIANv0_5_0.jsonl"
REPLAY_REPORT_PATH = REPO_ROOT / "m050/extraction/replay/M050_Human_Rulings_Legacy_Replay_Report_v0_1_MEDIANv0_5_0.json"
MIGRATION_RECEIPT_PATH = REPO_ROOT / "m050/archive/v0.5.0-orig/gate-4-source-identity-migration-20260802/M050_Gate_4_Source_Identity_Migration_Receipt_v0_1_MEDIANv0_5_0.yaml"
ACTIVE_SOURCE_PATH = REPO_ROOT / "m050/docs/v0.5/governance/M050_Human_Rulings_Ledger_v0_4_MEDIANv0_5_0.md"


def _build():
    return build_human_rulings_reconstruction(
        repo_root=REPO_ROOT,
        card=json.loads(CARD_PATH.read_text(encoding="utf-8")),
        card_path=CARD_PATH,
        replay_ledger_path=REPLAY_LEDGER_PATH,
        replay_report=json.loads(REPLAY_REPORT_PATH.read_text(encoding="utf-8")),
        replay_report_path=REPLAY_REPORT_PATH,
        migration_receipt_path=MIGRATION_RECEIPT_PATH,
        registry_relative_path="m050/extraction/reconstruction/registry.json",
        coordinate_ledger_relative_path="m050/extraction/reconstruction/coordinates.jsonl",
        rewrite_map_relative_path="m050/extraction/reconstruction/rewrites.json",
    )


def test_parser_preserves_multiline_labeled_field_payload():
    text = "# Domain\n\n## HR-X-001 — Example\n\n- **Exact statements:**\n  - First.\n  - Second.\n- **Date:** 2026-08-03\n"
    ruling = next(section for section in parse_ledger(text) if section.kind == "ruling")
    exact = ruling.fields[0]
    assert exact.label == "Exact statements"
    assert exact.value == "- First.\n  - Second."
    assert text[exact.value_start : exact.value_end] == exact.value
    assert exact.start_line == 5
    assert exact.end_line == 7


def test_active_ledger_has_complete_41_ruling_and_348_field_topology():
    sections = parse_ledger(ACTIVE_SOURCE_PATH.read_text(encoding="utf-8"))
    rulings = [section for section in sections if section.kind == "ruling"]
    assert len(rulings) == 41
    assert len({section.section_id for section in rulings}) == 41
    assert sum(len(section.fields) for section in rulings) == 348
    assert len([section for section in sections if section.kind == "open_item"]) == 2
    assert all(any(field.label.startswith("Exact ") for field in section.fields) for section in rulings)


def test_reconstruction_links_all_atoms_and_resolves_six_reference_rewrites():
    registry, coordinate_bytes, rewrite_map, report = _build()
    coordinates = [json.loads(line) for line in coordinate_bytes.splitlines()]
    expected_legacy_only = {
        "ATOM-HUMAN-RULINGS-DIRECT-0025",
        "ATOM-HUMAN-RULINGS-DIRECT-0027",
        "ATOM-HUMAN-RULINGS-DIRECT-0118",
        "ATOM-HUMAN-RULINGS-DIRECT-0121",
        "ATOM-HUMAN-RULINGS-DIRECT-0122",
        "ATOM-HUMAN-RULINGS-DIRECT-0169",
    }

    assert registry["ruling_count"] == 41
    assert registry["field_count"] == 348
    assert report["passed"] is True
    assert report["legacy_record_count"] == 173
    assert len(coordinates) == len({item["legacy_record_id"] for item in coordinates}) == 173
    assert rewrite_map["legacy_only_record_count"] == 6
    assert set(rewrite_map["legacy_only_record_ids"]) == expected_legacy_only
    assert {
        item["legacy_record_id"]
        for item in coordinates
        if item["coordinate_status"] == "active_reference_rewrite"
    } == expected_legacy_only
    assert all(
        item["legacy_coordinate"]["field_labels"]
        for item in coordinates
        if item["legacy_coordinate"]["ruling_id"] is not None
    )
    assert all(
        item["reference_rewrite_ids"] and item["active_coordinate"] is None
        for item in coordinates
        if item["legacy_record_id"] in expected_legacy_only
    )


def test_reconstruction_is_byte_deterministic():
    first = _build()
    second = _build()
    assert first == second
