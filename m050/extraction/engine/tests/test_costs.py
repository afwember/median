import pytest

from median_gate5.costs import account_cost_cents
from median_gate5.errors import ContractError


@pytest.mark.parametrize(
    ("raw", "cents"),
    [
        (None, 0),
        ("0", 0),
        ("0.000001", 1),
        ("0.010000", 1),
        ("0.010001", 2),
        ("1.234567", 124),
        ("10.249100", 1025),
    ],
)
def test_provider_costs_round_up_to_whole_cents(raw, cents):
    assert account_cost_cents(raw) == cents


@pytest.mark.parametrize("raw", ["-0.01", "NaN", "Infinity", "not-money"])
def test_invalid_provider_costs_fail_closed(raw):
    with pytest.raises(ContractError):
        account_cost_cents(raw)
