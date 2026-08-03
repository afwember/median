from __future__ import annotations

from decimal import Decimal, InvalidOperation, ROUND_CEILING

from .errors import ContractError


def account_cost_cents(provider_cost_usd_raw: str | None) -> int:
    """Convert provider-reported USD to whole cents, always rounding upward."""
    if provider_cost_usd_raw is None:
        return 0
    try:
        value = Decimal(provider_cost_usd_raw)
    except InvalidOperation as exc:
        raise ContractError("provider cost is not a valid decimal") from exc
    if not value.is_finite() or value < 0:
        raise ContractError("provider cost must be a finite nonnegative decimal")
    return int((value * 100).to_integral_value(rounding=ROUND_CEILING))
