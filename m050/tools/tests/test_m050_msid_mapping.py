import importlib.util
import json
from pathlib import Path
import sys
from types import SimpleNamespace

import pytest


ROOT = Path(__file__).parents[3]
TOOL = ROOT / "m050/tools/m050_msid_mapping.py"


def _module():
    spec = importlib.util.spec_from_file_location("m050_msid_mapping_for_tests", TOOL)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    try:
        spec.loader.exec_module(module)
    finally:
        sys.modules.pop(spec.name, None)
    return module


@pytest.fixture(scope="module")
def mapping():
    return _module()


@pytest.fixture(scope="module")
def corpus(mapping):
    return mapping.MappingCorpus(ROOT)


@pytest.fixture(scope="module")
def vocabulary(mapping):
    return mapping.MSIDVocabulary(ROOT)


def test_mapping_corpus_is_exact_authorial_input(corpus):
    origins = [item.effective_claim_origin for item in corpus.atoms]
    assert len(corpus.atoms) == 5382
    assert len(corpus.source_ids) == 18
    assert origins.count("triage_retained_normalized_claim") == 5313
    assert origins.count("authorial_accept") == 28
    assert origins.count("authorial_rewrite") == 41
    assert not any("m051" in item.atom.source_id.lower() for item in corpus.atoms)


def test_authorial_rewrite_is_the_effective_mapping_claim(corpus):
    rewritten = next(item for item in corpus.atoms if item.effective_claim_origin == "authorial_rewrite")
    assert rewritten.effective_claim != rewritten.atom.normalized_claim
    assert rewritten.effective_claim_sha256 != mapping_sha(rewritten.atom.normalized_claim)


def mapping_sha(value):
    import hashlib
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def test_vocabulary_enforces_settled_provisional_alias_and_rejected_paths(vocabulary):
    assert vocabulary.classify("Home.Colony") == "settled"
    assert vocabulary.classify("Home.Colony.Role.Leader") == "candidate"
    assert vocabulary.classify("Narrative.Memory") == "provisional"
    assert vocabulary.classify("Away.Crossing.Phase.Planning") == "provisional"
    assert vocabulary.classify("Away.Travel") == "alias"
    assert vocabulary.classify("Architecture.Register.Risk") == "rejected"
    assert vocabulary.classify("Home") == "invalid"
    assert vocabulary.classify("Home.Home.Colony") == "invalid"
    assert vocabulary.classify("Home.Colony.Colony") == "rejected"
    assert vocabulary.classify("Architecture.Register.DWELL") == "invalid"
    assert vocabulary.classify("Architecture.Register.Risk") == "rejected"
    assert vocabulary.classify("Home.Colony.Role.Gardener.Bramble#R002") == "rejected"


def test_mapping_store_binds_effective_claim_and_ontology_evidence(tmp_path, mapping, corpus, vocabulary):
    store = mapping.MappingStore(tmp_path / "mappings.jsonl", corpus, vocabulary)
    item = corpus.atoms[0]
    basis = next(iter(store.ontology_basis_keys))
    record = store.make_record(
        item.key,
        mapping_status="mapped",
        primary_msid="Home.Colony.Role.Leader",
        related_msids=["Home.Colony"],
        semantic_relation="defines",
        rationale="The claim principally defines a Home Colony Role.",
        ontology_basis_atom_keys=[basis],
    )
    store.replace([record])
    loaded = mapping.MappingStore(store.path, corpus, vocabulary)
    assert loaded.mappings[item.key]["effective_claim_sha256"] == item.effective_claim_sha256
    assert loaded.counts()["mapped"] == 1


def test_unmapped_and_ambiguous_states_remain_explicit(tmp_path, mapping, corpus, vocabulary):
    store = mapping.MappingStore(tmp_path / "mappings.jsonl", corpus, vocabulary)
    basis = [next(iter(store.ontology_basis_keys))]
    unmapped = store.make_record(
        corpus.atoms[0].key,
        mapping_status="unmapped",
        rationale="No stable game property is asserted by this claim.",
        ontology_basis_atom_keys=basis,
    )
    ambiguous = store.make_record(
        corpus.atoms[1].key,
        mapping_status="ambiguous",
        alternate_primary_msids=["Home.Encounter.Homecoming", "Home.Colony.View.Homecoming"],
        rationale="The source mixes Encounter and View terminology.",
        ontology_basis_atom_keys=basis,
    )
    store.replace([unmapped, ambiguous])
    assert store.counts()["unmapped"] == 1
    assert store.counts()["ambiguous"] == 1


def test_mapped_status_rejects_provisional_or_legacy_paths(tmp_path, mapping, corpus, vocabulary):
    store = mapping.MappingStore(tmp_path / "mappings.jsonl", corpus, vocabulary)
    basis = [next(iter(store.ontology_basis_keys))]
    for path in ("Narrative.Memory", "Away.Travel", "Architecture.Register.Risk"):
        with pytest.raises(mapping.TriageError, match="non-current MSID"):
            store.make_record(
                corpus.atoms[0].key,
                mapping_status="mapped",
                primary_msid=path,
                semantic_relation="references",
                rationale="This deliberately invalid proposal must be rejected.",
                ontology_basis_atom_keys=basis,
            )


def test_zero_call_inventory_accounts_for_every_input(tmp_path, mapping, corpus, vocabulary):
    store = mapping.MappingStore(tmp_path / "mappings.jsonl", corpus, vocabulary)
    result = mapping.inventory(corpus, vocabulary, store)
    assert result["external_calls"] == 0
    assert result["input_atoms"] == 5382
    assert result["input_sources"] == 18
    assert result["mapping_counts"]["mapped_records"] == 0
    assert result["mapping_counts"]["remaining"] == 5382
    assert result["legacy_semantic_shell_atoms_ignored"] > 0


def _assert_consistent_mapping_lifecycle(mapping, state):
    assert state["status"] in mapping.MSID_MAPPING_LIFECYCLE
    assert state["execution_state"] == state["status"]
    expected_mapping_status, expected_dashboard_status, authority_active = (
        mapping.MSID_MAPPING_LIFECYCLE[state["status"]]
    )
    assert state["mapping"]["status"] == expected_mapping_status
    assert state["dashboard"]["status"] == expected_dashboard_status
    assert state["authority"]["mapping_authorized"] is authority_active
    assert state["authority"]["source_work_authorized"] is authority_active
    assert state["authority"]["repository_writes_authorized"] is authority_active
    assert state["spend"]["active"] is False


def test_repository_state_has_consistent_mapping_lifecycle_and_no_provider_authority(mapping):
    state = json.loads(
        (ROOT / "m050/extraction/control/M050_Compile_State_MEDIANv0_5_0.json").read_text()
    )
    _assert_consistent_mapping_lifecycle(mapping, state)
    assert state["mapping"]["input_atom_count"] == 5382
    assert state["mapping"]["input_source_count"] == 18


def _lifecycle_fixture():
    source_ids = ("SOURCE-A", "SOURCE-B", "SOURCE-C")
    atoms = tuple(
        SimpleNamespace(key=f"{source_id}-{index}", atom=SimpleNamespace(source_id=source_id))
        for source_id in source_ids
        for index in range(1, 3)
    )
    corpus = SimpleNamespace(
        atoms=atoms,
        source_ids=source_ids,
        source_labels={
            "SOURCE-A": "Source A",
            "SOURCE-B": "Source B",
            "SOURCE-C": "Source C",
        },
        source_totals={source_id: 2 for source_id in source_ids},
    )
    store = _store_with_keys({"SOURCE-A-1", "SOURCE-A-2"})
    state = {
        "status": "MSID_MAPPING_READY",
        "execution_state": "MSID_MAPPING_READY",
        "mapping": {"status": "READY"},
        "spend": {"active": False},
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
        "dashboard": {
            "status": "READY — Stage 4 MSID mapping",
            "phase": "MSID mapping — semantic address assignment",
            "source": "Source A (SOURCE-A) — 2 / 2 mappings complete",
            "progress": "2 / 6 Stage 4 mappings recorded",
            "now": "Source A Stage 4 mapping is complete and the Compile Worker has Stopped Down",
            "next": "Await Asa's Spark Up",
            "updated_human": "September 9, 2026 at 10:00:00 AM EDT",
        },
        "next_possible_transition": "Spark Up may prepare Source B.",
    }
    return state, corpus, store


def _store_with_keys(keys):
    return SimpleNamespace(mappings={key: {} for key in keys})


def test_lifecycle_prepare_spark_up_is_bounded_and_idempotent(mapping):
    state, corpus, store = _lifecycle_fixture()
    replacement, report = mapping.plan_lifecycle_transition(
        state, corpus, store, "prepare-spark-up"
    )
    assert replacement == state
    assert replacement["status"] == "MSID_MAPPING_READY"
    assert report["source_id"] == "SOURCE-B"
    assert report["changed"] is False
    assert report["next_required_operations"] == [
        "report the exact assessed boundary",
        "halt awaiting Proceed",
    ]
    repeated, repeated_report = mapping.plan_lifecycle_transition(
        state, corpus, store, "prepare-spark-up"
    )
    assert repeated == state
    assert repeated_report["changed"] is False


def test_lifecycle_proceed_activates_only_the_assessed_boundary(mapping):
    state, corpus, store = _lifecycle_fixture()
    active, report = mapping.plan_lifecycle_transition(
        state,
        corpus,
        store,
        "activate-on-proceed",
        expected_source_id="SOURCE-B",
    )
    assert active["status"] == "MSID_MAPPING_ACTIVE"
    assert active["mapping"]["status"] == "ACTIVE"
    assert report["source_id"] == "SOURCE-B"
    assert report["external_calls"] == 0
    _assert_consistent_mapping_lifecycle(mapping, active)


def test_lifecycle_proceed_rejects_missing_or_drifted_assessment(mapping):
    state, corpus, store = _lifecycle_fixture()
    with pytest.raises(mapping.TriageError, match="assessed source"):
        mapping.plan_lifecycle_transition(state, corpus, store, "activate-on-proceed")
    with pytest.raises(mapping.TriageError, match="assessed source"):
        mapping.plan_lifecycle_transition(
            state,
            corpus,
            store,
            "activate-on-proceed",
            expected_source_id="SOURCE-C",
        )


def test_proceed_cli_rejects_redundant_dry_run(mapping, capsys):
    assert mapping.main(["--transition", "activate-on-proceed"]) == 2
    assert "one atomic --apply invocation" in capsys.readouterr().err
    assert mapping.main(["--transition", "activate-on-proceed", "--apply"]) == 2
    assert "source ID and HEAD" in capsys.readouterr().err


def test_spark_up_cli_rejects_repository_mutation(mapping, capsys):
    assert mapping.main(["--transition", "prepare-spark-up", "--apply"]) == 2
    assert "read-only" in capsys.readouterr().err


def test_proceed_checkpoint_rejects_head_drift(mapping, monkeypatch, tmp_path):
    outputs = iter(["", "b" * 40, "b" * 40])

    def completed(*args, **kwargs):
        return SimpleNamespace(stdout=next(outputs))

    monkeypatch.setattr(mapping.subprocess, "run", completed)
    with pytest.raises(mapping.TriageError, match="changed since the Spark Up assessment"):
        mapping._require_clean_synchronized_checkpoint(
            tmp_path, expected_head="a" * 40
        )


def test_lifecycle_stopdown_requires_complete_granted_source(mapping):
    state, corpus, store = _lifecycle_fixture()
    active, _ = mapping.plan_lifecycle_transition(
        state,
        corpus,
        store,
        "activate-on-proceed",
        expected_source_id="SOURCE-B",
    )
    with pytest.raises(mapping.TriageError, match="complete source coverage"):
        mapping.plan_lifecycle_transition(active, corpus, store, "prepare-stopdown")


def test_lifecycle_stopdown_revokes_authority_and_selects_no_new_work(mapping):
    state, corpus, store = _lifecycle_fixture()
    active, _ = mapping.plan_lifecycle_transition(
        state,
        corpus,
        store,
        "activate-on-proceed",
        expected_source_id="SOURCE-B",
    )
    complete_store = _store_with_keys(set(store.mappings) | {"SOURCE-B-1", "SOURCE-B-2"})
    stopped, report = mapping.plan_lifecycle_transition(
        active, corpus, complete_store, "prepare-stopdown"
    )
    assert stopped["status"] == "MSID_MAPPING_READY"
    assert stopped["mapping"]["status"] == "READY"
    assert stopped["authority"]["mapping_authorized"] is False
    assert stopped["authority"]["source_work_authorized"] is False
    assert stopped["authority"]["repository_writes_authorized"] is False
    assert "Source C" in stopped["dashboard"]["next"]
    assert report["source_id"] == "SOURCE-B"


def test_lifecycle_pre_execution_cancellation_needs_no_repository_transition(mapping):
    state, corpus, store = _lifecycle_fixture()
    assessed, assessment = mapping.plan_lifecycle_transition(
        state, corpus, store, "prepare-spark-up"
    )
    assert assessed == state
    assert assessment["source_id"] == "SOURCE-B"
    stopped, report = mapping.plan_lifecycle_transition(state, corpus, store, "prepare-stopdown")
    assert stopped == state
    assert report["changed"] is False


def test_lifecycle_rejects_mapping_beyond_the_current_source(mapping):
    state, corpus, store = _lifecycle_fixture()
    drifted_store = _store_with_keys(set(store.mappings) | {"SOURCE-C-1"})
    with pytest.raises(mapping.TriageError, match="later mapping source was entered early"):
        mapping.plan_lifecycle_transition(
            state, corpus, drifted_store, "prepare-spark-up"
        )


def test_lifecycle_final_source_stopdown_halts_at_stage_boundary(mapping):
    state, corpus, _ = _lifecycle_fixture()
    store = _store_with_keys({
        "SOURCE-A-1", "SOURCE-A-2", "SOURCE-B-1", "SOURCE-B-2",
    })
    state["dashboard"].update({
        "source": "Source B (SOURCE-B) — 2 / 2 mappings complete",
        "progress": "4 / 6 Stage 4 mappings recorded",
        "now": "Source B Stage 4 mapping is complete and the Compile Worker has Stopped Down",
    })
    active, _ = mapping.plan_lifecycle_transition(
        state,
        corpus,
        store,
        "activate-on-proceed",
        expected_source_id="SOURCE-C",
    )
    complete_store = _store_with_keys({item.key for item in corpus.atoms})
    stopped, _ = mapping.plan_lifecycle_transition(
        active, corpus, complete_store, "prepare-stopdown"
    )
    assert "Stage 4 mapping is complete" in stopped["dashboard"]["next"]
    assert "separately authorizes Stage 5" in stopped["next_possible_transition"]
