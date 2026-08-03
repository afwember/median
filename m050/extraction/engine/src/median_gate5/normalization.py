from __future__ import annotations

from dataclasses import dataclass
import unicodedata

from .errors import GroundingError


SPACE_CHARS = {"\u00a0", "\u2007", "\u2009", "\u202f"}
QUOTE_MAP = {
    "\u2018": "'",
    "\u2019": "'",
    "\u201a": "'",
    "\u201b": "'",
    "\u201c": '"',
    "\u201d": '"',
    "\u201e": '"',
    "\u201f": '"',
}
DASH_MAP = {
    "\u2010": "-",
    "\u2011": "-",
    "\u2012": "-",
    "\u2013": "-",
    "\u2014": "-",
    "\u2212": "-",
}
LIGATURE_MAP = {
    "\ufb00": "ff",
    "\ufb01": "fi",
    "\ufb02": "fl",
    "\ufb03": "ffi",
    "\ufb04": "ffl",
}


@dataclass(frozen=True)
class LocatedQuote:
    raw_text: str
    start: int
    end: int
    method: str
    transformations: tuple[str, ...]


def structural_text(raw: str) -> str:
    return unicodedata.normalize("NFC", raw.replace("\r\n", "\n").replace("\r", "\n"))


def _clusters(text: str):
    start = 0
    for index, char in enumerate(text):
        if index and not unicodedata.combining(char):
            yield start, index, text[start:index]
            start = index
    if text:
        yield start, len(text), text[start:]


def locator_text(text: str) -> tuple[str, list[tuple[int, int]], tuple[str, ...]]:
    output: list[str] = []
    spans: list[tuple[int, int]] = []
    events: set[str] = set()
    previous_space = False
    for start, end, cluster in _clusters(text):
        value = unicodedata.normalize("NFC", cluster)
        if value != cluster:
            events.add("unicode_nfc")
        folded: list[str] = []
        for char in value:
            if char == "\u00ad":
                events.add("soft_hyphen_removed")
                continue
            if char in SPACE_CHARS or char.isspace():
                if char != " ":
                    events.add("unicode_whitespace_folded")
                folded.append(" ")
            elif char in QUOTE_MAP:
                events.add("typographic_quote_folded")
                folded.append(QUOTE_MAP[char])
            elif char in DASH_MAP:
                events.add("dash_variant_folded")
                folded.append(DASH_MAP[char])
            elif char in LIGATURE_MAP:
                events.add("presentation_ligature_expanded")
                folded.append(LIGATURE_MAP[char])
            else:
                folded.append(char)
        for char in "".join(folded):
            if char == " ":
                if previous_space:
                    events.add("whitespace_run_collapsed")
                    if spans:
                        old_start, _ = spans[-1]
                        spans[-1] = (old_start, end)
                    continue
                previous_space = True
            else:
                previous_space = False
            output.append(char)
            spans.append((start, end))
    return "".join(output), spans, tuple(sorted(events))


def locate_quote(block_raw: str, proposed: str) -> LocatedQuote:
    if not proposed:
        raise GroundingError("quotation is empty")
    exact_count = block_raw.count(proposed)
    if exact_count == 1:
        start = block_raw.index(proposed)
        return LocatedQuote(proposed, start, start + len(proposed), "exact", ())
    if exact_count > 1:
        raise GroundingError("quotation has multiple exact matches in block")

    block_locator, spans, block_events = locator_text(block_raw)
    proposed_locator, _, proposal_events = locator_text(proposed)
    if not proposed_locator:
        raise GroundingError("quotation is empty after locator normalization")
    matches: list[int] = []
    start = 0
    while True:
        index = block_locator.find(proposed_locator, start)
        if index < 0:
            break
        matches.append(index)
        start = index + 1
    if len(matches) != 1:
        reason = "no" if not matches else "multiple"
        raise GroundingError(f"quotation has {reason} safe normalized match in block")
    loc_start = matches[0]
    loc_end = loc_start + len(proposed_locator)
    raw_start = spans[loc_start][0]
    raw_end = spans[loc_end - 1][1]
    events = tuple(sorted(set(block_events) | set(proposal_events)))
    return LocatedQuote(block_raw[raw_start:raw_end], raw_start, raw_end, "locator", events)
