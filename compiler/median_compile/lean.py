"""Phase 2 — lean Markdown.

The compiler spec calls this "the most important early engineering phase"
because every later LLM operation inherits both its token savings and its
omissions. That rationale assumed PDF-shaped sources carrying running headers,
footers, page numbers and repeated title blocks.

Measured against the actual DOCX corpus, only 1.13% of tokens are removable:
pandoc never emits Word headers, footers or page numbers at all, because Word
stores them in separate XML that the DOCX reader drops. The ruleset here is
therefore deliberately tiny.

Its justification is extraction quality, not token economy. A table of contents
left in a chunk is atomized by Phase 4 into records that look like canon and
are not. Removing it prevents fabricated records; the token saving is
incidental.

Every removal is reversible: coordinate, rule, line range and SHA-256 are
logged, and the full normalized source is never modified.
"""

from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass, field

RULESET_VERSION = "1.0"

ANCHOR_RE = re.compile(r"<!--@([^>]+?)-->")
CONTENTS_HEADING = re.compile(r"^#{1,3}\s*(?:table of )?contents\s*$", re.IGNORECASE)
SEPARATOR = re.compile(r"^[-*_]{3,}$")
PAGE_NUMBER = re.compile(r"^(?:page\s+)?\d{1,4}$", re.IGNORECASE)
ARTIFACT = re.compile(r"^(?:<!-- -->|&nbsp;|\\)+$")

#: Compiler spec §6.3. A block matching any of these is never removed, whatever
#: rule fired. Checked before rules, not after.
PROTECTED: dict[str, re.Pattern] = {
    "precedence": re.compile(
        r"\bprecedence\b|\bcontrols?\b|\boverrides?\b|\btakes priority\b", re.I
    ),
    "scope": re.compile(r"\bscope\b|\bexclusion\b|\bexcept\b|\bdoes not apply\b", re.I),
    "supersession": re.compile(r"\bsupersed|\breplaces?\b|\bretired\b", re.I),
    "definition": re.compile(
        r"\bdefinition\b|\bis defined as\b|\bmeans\b|\bterminology\b|\bcanonical\b", re.I
    ),
    "non_goal": re.compile(r"\bnon-goal\b|\bnot a goal\b|\bwe do not\b", re.I),
    "example": re.compile(r"\bexample\b|\be\.g\.\b|\bfor instance\b", re.I),
    "open_question": re.compile(
        r"\bopen question\b|\bunresolved\b|\bdeferred?\b|\bto be decided\b|\bTBD\b", re.I
    ),
    "formula": re.compile(r"[=×÷±≤≥]|\b\d+\s*[+\-*/]\s*\d+"),
    "table": re.compile(r"^\s*\|"),
    "figure": re.compile(r"!\[|\bfigure\b|\bplate\b|\bcaption\b", re.I),
    "adopted": re.compile(r"\*\*Adopted|Not STATE|Designer commentary", re.I),
}


@dataclass
class Removal:
    coord: str
    rule: str
    lines: str
    sha256: str
    chars: int
    preview: str


@dataclass
class Spared:
    coord: str
    rule: str
    protected_by: str


@dataclass
class LeanResult:
    source_id: str
    text: str = ""
    removals: list[Removal] = field(default_factory=list)
    spared: list[Spared] = field(default_factory=list)
    chars_full: int = 0
    chars_lean: int = 0

    @property
    def reduction(self) -> float:
        if not self.chars_full:
            return 0.0
        return (self.chars_full - self.chars_lean) / self.chars_full


def _parse(text: str) -> list[tuple[str, list[str], int]]:
    """Split annotated Markdown into (coordinate, lines, start_line) triples."""
    out: list[tuple[str, list[str], int]] = []
    coord: str | None = None
    buf: list[str] = []
    start = 0
    for i, line in enumerate(text.split("\n"), 1):
        m = ANCHOR_RE.fullmatch(line.strip())
        if m:
            if coord is not None:
                out.append((coord, buf, start))
            coord, buf, start = m.group(1), [], i
        elif coord is not None:
            buf.append(line)
    if coord is not None:
        out.append((coord, buf, start))
    return out


def _protected_by(body: str) -> str | None:
    for name, pattern in PROTECTED.items():
        if pattern.search(body):
            return name
    return None


def _rule_for(body: str, in_contents: bool) -> str | None:
    if not body.strip():
        return "empty"
    stripped = body.strip()
    if in_contents:
        return "contents"
    if SEPARATOR.fullmatch(stripped):
        return "separator"
    if PAGE_NUMBER.fullmatch(stripped):
        return "page_number"
    if ARTIFACT.fullmatch(stripped):
        return "artifact"
    return None


def lean(text: str, source_id: str) -> LeanResult:
    result = LeanResult(source_id=source_id)
    kept: list[str] = []
    in_contents = False

    for coord, lines, start in _parse(text):
        body = "\n".join(lines).strip()
        is_heading = body.startswith("#")

        if is_heading:
            in_contents = bool(CONTENTS_HEADING.match(body.splitlines()[0].strip()))

        result.chars_full += len(body)
        rule = _rule_for(body, in_contents and not is_heading) or (
            "contents" if is_heading and in_contents else None
        )

        if rule and rule != "empty":
            guard = _protected_by(body)
            if guard:
                result.spared.append(Spared(coord, rule, guard))
                rule = None

        if rule:
            result.removals.append(
                Removal(
                    coord=coord,
                    rule=rule,
                    lines=f"{start}-{start + len(lines)}",
                    sha256=hashlib.sha256(body.encode()).hexdigest(),
                    chars=len(body),
                    preview=body[:120].replace("\n", " "),
                )
            )
            continue

        result.chars_lean += len(body)
        kept.append(f"<!--@{coord}-->")
        kept.extend(lines)

    result.text = "\n".join(kept).rstrip() + "\n"
    return result
