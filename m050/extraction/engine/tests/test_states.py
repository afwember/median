import pytest

from median_gate5.errors import ContractError
from median_gate5.schema import validate_artifact
from median_gate5.states import transition_receipt


def receipt(machine, prior, new, authority="Codex"):
    return transition_receipt(
        machine=machine,
        artifact_id="artifact-1",
        prior_state=prior,
        new_state=new,
        authority=authority,
        reason="controlled transition",
        tool_version="0.1.0",
        predecessor_receipt_hash=None,
        timestamp="2026-08-02T00:00:00Z",
    )


def test_positive_work_order_requires_author():
    with pytest.raises(ContractError, match="author authority"):
        receipt("work_order", "awaiting_authorization", "authorized")
    result = receipt(
        "work_order", "awaiting_authorization", "authorized", authority="Asa Wember"
    )
    validate_artifact("transition_receipt", result)


def test_ruling_confirmation_requires_author():
    with pytest.raises(ContractError, match="author authority"):
        receipt("ruling", "drafted_by_codex", "author_confirmed")


def test_identity_approval_requires_author():
    with pytest.raises(ContractError, match="author authority"):
        receipt("identity_card", "reviewed", "approved")
    result = receipt(
        "identity_card", "reviewed", "approved", authority="Asa Wember"
    )
    validate_artifact("transition_receipt", result)


def test_invalid_transition_fails_closed():
    with pytest.raises(ContractError, match="prohibited"):
        receipt("evidence", "proposed", "accepted")


@pytest.mark.parametrize(
    ("machine", "prior", "new"),
    [
        ("identity_card", "draft", "reviewed"),
        ("request", "rendered", "verified"),
        ("mapping", "proposed", "validated"),
        ("bundle", "constructed", "completeness_verified"),
        ("question", "open", "prepared"),
        ("compile", "drafted", "mechanically_validated"),
    ],
)
def test_each_state_machine_has_a_valid_path(machine, prior, new):
    validate_artifact("transition_receipt", receipt(machine, prior, new))
