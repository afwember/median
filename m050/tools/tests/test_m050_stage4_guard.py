"""Current cross-cutting regression surface for the Stage 4 full guard."""

import copy
from datetime import datetime
import hashlib
import json
from pathlib import Path
import sys

import pytest
import yaml


ROOT = Path(__file__).parents[3]
TOOLS = ROOT / "m050/tools"
sys.path.insert(0, str(TOOLS))
try:
    import m050_guard as guard
    import m050_render_status as renderer
    from m050_atom_rewrite import RewriteCorpus, RewriteStore, TriageError as RewriteError
    from m050_atom_triage import DecisionStore, TriageError, load_corpus
finally:
    sys.path.remove(str(TOOLS))

from median_gate5.canonical import sha256_file
from median_gate5.corpus import derive_compile_source_state
from median_gate5.errors import ContractError


GATE_2 = ROOT / "m050/extraction/audit/M050_Extraction_Gate_2_Source_Disposition_v0_1_MEDIANv0_5_0.yaml"
MATRIX = ROOT / "m050/extraction/control/M050_Compile_Source_State_Matrix_v0_1_MEDIANv0_5_0.json"
ORDER = ROOT / "m050/extraction/control/M050_Compile_Source_Processing_Order_v0_1_MEDIANv0_5_0.json"
STATE = ROOT / "m050/extraction/control/M050_Compile_State_MEDIANv0_5_0.json"
HOME_CONFIG = ROOT / "m050/extraction/control/M050_Home_Extraction_Machine_Config_v0_1_MEDIANv0_5_0.json"
HOME_REPORT = ROOT / "m050/extraction/accepted/home/M050_Home_Full_Extraction_Acceptance_Report_v0_1_MEDIANv0_5_0.json"
HOME_LEDGER = "m050/extraction/runs/home-pilot/M050_Home_Run_Ledger_v0_1_MEDIANv0_5_0.jsonl"


def _json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def _gate_2():
    return yaml.safe_load(GATE_2.read_text(encoding="utf-8"))


def _home_acceptance_fixture():
    report = _json(HOME_REPORT)
    source = {
        "id": report["source_id"],
        "accepted_chunk_ids": report["accepted_chunk_ids"],
    }
    calibration = {
        "accepted_evidence": [
            {
                "chunk_id": item["chunk_id"],
                "outcome": item["outcome_path"],
                "run_ledger": HOME_LEDGER,
            }
            for item in report["accepted_inputs"]
        ],
        "candidate_acceptance": {
            "candidate": report["candidate_path"],
            "candidate_sha256": report["candidate_sha256"],
            "report": HOME_REPORT.relative_to(ROOT).as_posix(),
            "report_sha256": hashlib.sha256(HOME_REPORT.read_bytes()).hexdigest(),
        },
    }
    return source, _json(HOME_CONFIG), calibration


@pytest.fixture(scope="module")
def triage_corpus():
    return load_corpus(ROOT)


@pytest.fixture(scope="module")
def rewrite_corpus():
    return RewriteCorpus(ROOT)


def test_compile_scope_is_derived_as_24_22_4_18_14_4():
    gate_2 = _gate_2()
    state = derive_compile_source_state(
        gate_2,
        manifest_path=str(GATE_2.relative_to(ROOT)),
        manifest_sha256="0" * 64,
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
    gate_2 = _gate_2()
    unknown = copy.deepcopy(gate_2)
    unknown["sources"][0]["disposition"] = "invented_disposition"
    with pytest.raises(ContractError, match="unrecognized"):
        derive_compile_source_state(
            unknown, manifest_path="gate2.yaml", manifest_sha256="0" * 64
        )
    duplicate = copy.deepcopy(gate_2)
    duplicate["sources"][1]["source_id"] = duplicate["sources"][0]["source_id"]
    with pytest.raises(ContractError, match="duplicate"):
        derive_compile_source_state(
            duplicate, manifest_path="gate2.yaml", manifest_sha256="0" * 64
        )


def test_committed_compile_scope_matrix_matches_authoritative_gate_2():
    expected = derive_compile_source_state(
        _gate_2(),
        manifest_path=str(GATE_2.relative_to(ROOT)),
        manifest_sha256=sha256_file(GATE_2),
    )
    assert _json(MATRIX) == expected


def test_processing_order_is_complete_unique_and_bound_to_source_state_matrix():
    order = _json(ORDER)
    matrix = _json(MATRIX)
    sequence = order["sequence"]
    by_id = {source["source_id"]: source for source in matrix["sources"]}
    assert [item["order"] for item in sequence] == list(range(1, 25))
    assert len({item["source_id"] for item in sequence}) == 24
    assert {item["source_id"] for item in sequence} == set(by_id)
    for item in sequence:
        assert set(item) <= {
            "order", "source_id", "label", "pre_candidate_acceptance_control"
        }
        assert item["label"]


def test_processing_order_and_canonical_progress_form_one_prefix_and_queue():
    order = _json(ORDER)
    matrix = _json(MATRIX)
    state = _json(STATE)
    ordered_ids = [item["source_id"] for item in order["sequence"]]
    by_id = {source["source_id"]: source for source in matrix["sources"]}
    completed = set(state["progress"]["completed_source_ids"])
    compile_scope_ids = [
        source_id for source_id in ordered_ids if by_id[source_id]["in_compile_scope"]
    ]
    completed_prefix = [source_id for source_id in compile_scope_ids if source_id in completed]
    expected_queue = [source_id for source_id in compile_scope_ids if source_id not in completed]
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


def test_completed_source_has_exact_hash_bound_candidate_acceptance():
    source, config, calibration = _home_acceptance_fixture()
    errors = []
    guard.validate_candidate_acceptance(
        source, config, calibration, source["accepted_chunk_ids"],
        calibration["accepted_evidence"], errors,
    )
    assert errors == []


def test_completed_source_rejects_missing_candidate_acceptance_pair():
    source, config, calibration = _home_acceptance_fixture()
    calibration.pop("candidate_acceptance")
    errors = []
    guard.validate_candidate_acceptance(
        source, config, calibration, source["accepted_chunk_ids"],
        calibration["accepted_evidence"], errors,
    )
    assert errors == ["completed source lacks a hash-bound candidate/report pair"]


def test_accepted_candidate_rejects_missing_coverage_and_duplicate_identifiers():
    expected = [
        ("C0001", {"proposal_id": "P1", "source_id": "S1"}),
        ("C0002", {"proposal_id": "P1", "source_id": "S1"}),
    ]
    errors = []
    guard.validate_accepted_candidate_records(
        [{"proposal_id": "P1", "source_id": "S1"}], expected, errors
    )
    assert any("coverage drifted" in error for error in errors)
    errors = []
    guard.validate_accepted_candidate_records(
        [
            {"proposal_id": "P1", "source_id": "S1"},
            {"proposal_id": "P1", "source_id": "S1"},
        ],
        expected,
        errors,
    )
    assert "accepted candidate record identifiers are not candidate-wide unique" in errors


@pytest.mark.parametrize(
    ("status", "mapping_status", "dashboard_status", "authority_active"),
    [
        ("MSID_MAPPING_READY", "READY", "READY — Stage 4 MSID mapping", False),
        ("MSID_MAPPING_ACTIVE", "ACTIVE", "ACTIVE — Stage 4 MSID mapping", True),
    ],
)
def test_stage_4_lifecycle_has_only_ready_and_active_repository_states(
    status, mapping_status, dashboard_status, authority_active
):
    state = {
        "status": status,
        "execution_state": status,
        "mapping": {"status": mapping_status},
        "dashboard": {"status": dashboard_status},
        "authority": {
            "repository_writes_authorized": authority_active,
            "source_work_authorized": authority_active,
            "triage_authorized": False,
            "rewrite_authorized": False,
            "google_sheets_interaction_authorized": False,
            "semantic_acceptance_authorized": False,
            "mapping_authorized": authority_active,
            "reconciliation_authorized": False,
            "compiled_prose_authorized": False,
        },
    }
    errors = []
    guard.validate_msid_mapping_lifecycle(state, errors)
    assert errors == []


def test_stage_4_rejects_retired_durable_fermata_state():
    state = {
        "status": "MSID_MAPPING_AUTHORIZED_AWAITING_PROCEED",
        "execution_state": "MSID_MAPPING_AUTHORIZED_AWAITING_PROCEED",
        "mapping": {"status": "AUTHORIZED_AWAITING_PROCEED"},
        "dashboard": {
            "status": "AUTHORIZED — Stage 4 MSID mapping; awaiting Proceed"
        },
        "authority": {
            "repository_writes_authorized": False,
            "source_work_authorized": False,
            "triage_authorized": False,
            "rewrite_authorized": False,
            "google_sheets_interaction_authorized": False,
            "semantic_acceptance_authorized": False,
            "mapping_authorized": False,
            "reconciliation_authorized": False,
            "compiled_prose_authorized": False,
        },
    }
    state["authority"]["repository_writes_authorized"] = True
    state["authority"]["source_work_authorized"] = True
    state["authority"]["mapping_authorized"] = True
    errors = []
    guard.validate_msid_mapping_lifecycle(state, errors)
    assert "canonical Stage 4 lifecycle state is invalid" in errors


def test_status_uses_unlabeled_timestamp_and_safe_remaining_balance():
    state = {
        "dashboard": {
            "updated_human": "August 4, 2026 at 5:46:07 PM EDT",
            "status": "Stopped",
            "phase": "MSID mapping",
            "source": "Source A",
            "progress": "Complete",
            "now": "Stopped",
            "next": "Await authorization",
        },
        "spend": {"remaining_usd": "0.6576584"},
    }
    status = guard.expected_status(state)
    assert "**UPDATED:**" not in status
    assert "TOTAL COST" not in status
    assert "August 4, 2026 at 5:46:07 PM EDT<br>" in status
    assert status.endswith("**SPEND REMAINING:** $0.65\n")


def test_status_renderer_rounds_and_updates_canonical_timestamp(tmp_path):
    state_path = tmp_path / "state.json"
    status_path = tmp_path / "STATUS.md"
    state = {
        "updated": "2026-01-01T00:00:00-05:00",
        "dashboard": {
            "updated_human": "stale",
            "status": "Stopped",
            "phase": "MSID mapping",
            "source": "Source A",
            "progress": "Complete",
            "now": "Stopped",
            "next": "Await authorization",
        },
        "spend": {"remaining_usd": "0.2745620"},
    }
    state_path.write_text(json.dumps(state), encoding="utf-8")
    renderer.render_status(
        state_path,
        status_path,
        now=datetime.fromisoformat("2026-08-05T09:12:13.600000-04:00"),
    )
    updated = _json(state_path)
    assert updated["updated"] == "2026-08-05T09:12:14-04:00"
    assert updated["dashboard"]["updated_human"] == "August 5, 2026 at 9:12:14 AM EDT"
    assert status_path.read_text(encoding="utf-8") == renderer.expected_status(updated)


def test_loads_every_completed_candidate_with_unique_bound_atoms(triage_corpus):
    assert len(triage_corpus.atoms) == 6550
    assert len(triage_corpus.candidate_hashes) == 18
    assert len(triage_corpus.source_labels) == 18
    assert len(triage_corpus.by_key) == 6550
    assert {atom.source_id for atom in triage_corpus.atoms} == set(
        triage_corpus.candidate_hashes
    )


def test_candidate_hash_drift_invalidates_existing_decision(tmp_path, triage_corpus):
    atom = triage_corpus.atoms[0]
    path = tmp_path / "bad.jsonl"
    store = DecisionStore(path, triage_corpus)
    store.apply((atom,), "retain")
    record = json.loads(path.read_text(encoding="utf-8"))
    record["candidate_sha256"] = "0" * 64
    path.write_text(json.dumps(record) + "\n", encoding="utf-8")
    with pytest.raises(TriageError, match="binding drifted"):
        DecisionStore(path, triage_corpus)


def test_input_is_exact_completed_rewrite_list(rewrite_corpus):
    assert len(rewrite_corpus.atoms) == 98
    assert len(rewrite_corpus.by_key) == 98
    assert all(atom in rewrite_corpus.full_corpus.atoms for atom in rewrite_corpus.atoms)
    assert not any("m051" in atom.source_id.lower() for atom in rewrite_corpus.atoms)


def test_rewrite_is_trimmed_bound_and_authorially_accepted(tmp_path, rewrite_corpus):
    atom = rewrite_corpus.atoms[0]
    path = tmp_path / "rewrites.jsonl"
    store = RewriteStore(path, rewrite_corpus)
    store.apply(atom.key, "  A clearer source-grounded replacement.  ")
    record = RewriteStore(path, rewrite_corpus).rewrites[atom.key]
    assert record["resolution"] == "rewrite"
    assert record["replacement_claim"] == "A clearer source-grounded replacement."
    assert record["authorially_accepted"] is True
    assert record["candidate_sha256"] == atom.candidate_sha256
    assert record["triage_decision_sha256"] == rewrite_corpus.triage_sha256
    assert record["original_claim_sha256"] == hashlib.sha256(
        atom.normalized_claim.encode("utf-8")
    ).hexdigest()


def test_empty_claim_is_rejected_and_unchanged_claim_is_accepted(tmp_path, rewrite_corpus):
    atom = rewrite_corpus.atoms[0]
    store = RewriteStore(tmp_path / "rewrites.jsonl", rewrite_corpus)
    with pytest.raises(RewriteError, match="nonempty"):
        store.apply(atom.key, "  ")
    store.apply(atom.key, atom.normalized_claim)
    record = RewriteStore(store.path, rewrite_corpus).rewrites[atom.key]
    assert record["resolution"] == "accept"
    assert record["replacement_claim"] == atom.normalized_claim


def test_exclusion_uses_existing_authorial_reason(tmp_path, rewrite_corpus):
    atom = rewrite_corpus.atoms[0]
    store = RewriteStore(tmp_path / "exclusions.jsonl", rewrite_corpus)
    store.exclude(atom.key)
    record = RewriteStore(store.path, rewrite_corpus).rewrites[atom.key]
    assert record["resolution"] == "exclude"
    assert record["replacement_claim"] is None
    assert record["exclusion_reason"] == "other_authorial_exclusion"
    assert store.counts()["excluded"] == 1
    assert store.counts()["resolved"] == 1


def test_binding_drift_is_rejected(tmp_path, rewrite_corpus):
    atom = rewrite_corpus.atoms[0]
    path = tmp_path / "rewrites.jsonl"
    store = RewriteStore(path, rewrite_corpus)
    store.apply(atom.key, "A valid replacement.")
    record = json.loads(path.read_text(encoding="utf-8"))
    record["original_claim_sha256"] = "0" * 64
    path.write_text(json.dumps(record) + "\n", encoding="utf-8")
    with pytest.raises(RewriteError, match="binding drifted"):
        RewriteStore(path, rewrite_corpus)
