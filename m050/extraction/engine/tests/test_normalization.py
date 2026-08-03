import pytest

from median_gate5.errors import GroundingError
from median_gate5.normalization import locate_quote, structural_text


def test_structural_normalization_is_named_and_conservative():
    assert structural_text("Cafe\u0301\r\nNext") == "Café\nNext"


def test_locator_recovers_exact_raw_span():
    block = "The fox’s state—ready\u00a0now—uses the ﬁeld."
    proposal = "fox's state-ready now-uses the field"
    located = locate_quote(block, proposal)
    assert located.raw_text == "fox’s state—ready\u00a0now—uses the ﬁeld"
    assert located.method == "locator"
    assert "typographic_quote_folded" in located.transformations
    assert "presentation_ligature_expanded" in located.transformations


def test_ambiguous_normalized_match_is_rejected():
    with pytest.raises(GroundingError, match="multiple"):
        locate_quote("fox’s state / fox‘s state", "fox's state")


def test_non_contiguous_or_missing_quote_is_rejected():
    with pytest.raises(GroundingError, match="no safe"):
        locate_quote("first block only", "first second")
