class Gate5Error(Exception):
    """Base class for controlled Gate 5 failures."""


class IntegrityError(Gate5Error):
    """A frozen, immutable, or append-only invariant failed."""


class ContractError(Gate5Error):
    """An artifact or state transition violates its contract."""


class GroundingError(Gate5Error):
    """A proposed quotation cannot be grounded uniquely and safely."""
