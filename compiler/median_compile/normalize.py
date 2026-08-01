"""Phase 1 — faithful full Markdown normalization.

DOCX and Markdown in, coordinate-annotated Markdown out. Deterministic, no
model calls. Coordinates use the document's own section numbering where it
exists and positional numbering where it does not, so an extracted record's
`loc` can always be resolved back to a block of source text.
"""

from __future__ import annotations

import re
import subprocess
from dataclasses import dataclass, field
from pathlib import Path

ANCHOR_RE = re.compile(r"<!--@([^>]+?)-->")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*)$")
NUMBERED_RE = re.compile(r"^(\d+(?:\.\d+)*)[.)]?\s+")
IMAGE_RE = re.compile(r"!\[([^\]]*)\]\(([^)]+)\)")

PANDOC_ARGS = ["-t", "gfm+pipe_tables", "--wrap=none"]

#: Emitted only when the local pandoc understands them. Keeps the normalizer
#: working across pandoc versions without silently changing output shape.
OPTIONAL_ARGS = ["--markdown-headings=atx"]


def _supported(arg: str) -> bool:
    name = arg.split("=", 1)[0]
    try:
        help_text = subprocess.run(
            ["pandoc", "--help"], capture_output=True, text=True, check=False
        ).stdout
    except FileNotFoundError:  # pragma: no cover - environment guard
        return False
    return name in help_text


class PandocMissing(RuntimeError):
    pass


@dataclass
class Figure:
    id: str
    source_id: str
    loc: str
    alt: str
    path: str


@dataclass
class NormalizeResult:
    source_id: str
    text: str
    headings: int
    blocks: int
    tables: int
    promoted: int = 0
    figures: list[Figure] = field(default_factory=list)
    chars_in: int = 0
    chars_out: int = 0

    @property
    def char_delta(self) -> float:
        if not self.chars_in:
            return 0.0
        return (self.chars_out - self.chars_in) / self.chars_in


def _pandoc(src: Path, media_dir: Path) -> str:
    extra = [a for a in OPTIONAL_ARGS if _supported(a)]
    cmd = ["pandoc", str(src), *PANDOC_ARGS, *extra, "--extract-media", str(media_dir)]
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, check=False)
    except FileNotFoundError as exc:  # pragma: no cover - environment guard
        raise PandocMissing("pandoc is not installed") from exc
    if proc.returncode != 0:
        raise RuntimeError(f"pandoc failed on {src.name}: {proc.stderr.strip()[:400]}")
    return proc.stdout


def _blocks(text: str) -> list[list[str]]:
    """Split into blocks on blank lines, keeping fenced code and tables intact.

    A heading always starts a new block even when no blank line precedes it.
    Without this, a thematic break written tight against a heading (`---` then
    `# PART I`) swallows the heading into the preceding block and hides it from
    the section counter. That pattern carries every Part boundary in the v0.4.6
    baseline, so the omission would have been silent and structural.
    """
    out: list[list[str]] = []
    cur: list[str] = []
    fenced = False
    for line in text.split("\n"):
        if line.lstrip().startswith("```"):
            fenced = not fenced
        if not fenced and HEADING_RE.match(line) and cur:
            out.append(cur)
            cur = []
        if not line.strip() and not fenced:
            if cur:
                out.append(cur)
                cur = []
            continue
        cur.append(line)
    if cur:
        out.append(cur)
    return out


def _is_pseudo_heading(block: list[str]) -> str | None:
    """A single short line entirely bolded, used as structure by some sources.

    Opt-in per source. Word documents that never applied heading styles carry
    their structure this way; without promotion every block lands in section 0
    and chunking cannot find a boundary.
    """
    if len(block) != 1:
        return None
    line = block[0].strip()
    m = re.fullmatch(r"\*\*(.+?)\*\*:?", line)
    if not m:
        return None
    inner = m.group(1).strip()
    if len(inner) > 80 or inner.endswith((".", "!", "?")) or "**" in inner:
        return None
    return inner


class _Counter:
    """Tracks the current section path, preferring the document's own numbering."""

    def __init__(self) -> None:
        self.positional = [0] * 7
        self.explicit: str | None = None

    def heading(self, level: int, text: str) -> str:
        m = NUMBERED_RE.match(text.strip().lstrip("#").strip())
        if m:
            self.explicit = m.group(1)
            return self.explicit
        if self.explicit and level > 1:
            # Sub-heading under an explicitly numbered section.
            self.positional[level] += 1
            return f"{self.explicit}.{self.positional[level]}"
        self.explicit = None
        self.positional[level] += 1
        for deeper in range(level + 1, 7):
            self.positional[deeper] = 0
        return ".".join(str(n) for n in self.positional[1 : level + 1] if n)


def annotate(
    text: str, source_id: str, pseudo_headings: bool = False
) -> NormalizeResult:
    """Insert `<!--@SECTION¶N-->` anchors before every non-heading block."""
    counter = _Counter()
    section = "0"
    para = 0
    headings = tables = blocks = promoted = 0
    figures: list[Figure] = []
    lines: list[str] = []
    seen: dict[str, int] = {}

    def unique(coord: str) -> str:
        """Guarantee coordinate uniqueness.

        Section numbering repeats legitimately — appendices restart at 1, and
        several sources reuse `3.1` under different Parts. 95 duplicates
        appeared across the corpus before this. A `loc` that resolves to two
        places cannot be verified at Phase 5, so repeats take an occurrence
        suffix while keeping the human-readable path intact.
        """
        n = seen.get(coord, 0) + 1
        seen[coord] = n
        return coord if n == 1 else f"{coord}#{n}"

    for block in _blocks(text):
        if pseudo_headings and not HEADING_RE.match(block[0]):
            title = _is_pseudo_heading(block)
            if title:
                block = [f"## {title}"]
                promoted += 1

        head = HEADING_RE.match(block[0])
        if head:
            level = len(head.group(1))
            section = unique(counter.heading(level, head.group(2)))
            para = 0
            headings += 1
            lines.append(f"<!--@{section}-->")
            lines.extend(block)
            lines.append("")
            continue

        para += 1
        blocks += 1
        loc = unique(f"{section}¶{para}")
        joined = "\n".join(block)
        if joined.lstrip().startswith("|"):
            tables += 1
        for alt, path in IMAGE_RE.findall(joined):
            figures.append(
                Figure(
                    id=f"FIG-{source_id}-{len(figures) + 1:03d}",
                    source_id=source_id,
                    loc=loc,
                    alt=alt,
                    path=path,
                )
            )
        lines.append(f"<!--@{loc}-->")
        lines.extend(block)
        lines.append("")

    return NormalizeResult(
        source_id=source_id,
        text="\n".join(lines).rstrip() + "\n",
        headings=headings,
        blocks=blocks,
        tables=tables,
        promoted=promoted,
        figures=figures,
    )


def normalize(
    src: Path, source_id: str, media_dir: Path, pseudo_headings: bool = False
) -> NormalizeResult:
    if src.suffix.lower() in {".md", ".markdown"}:
        raw = src.read_text(encoding="utf-8", errors="replace")
    else:
        raw = _pandoc(src, media_dir)
    raw = raw.replace(str(media_dir) + "/", "").replace(str(media_dir), "")
    result = annotate(raw, source_id, pseudo_headings=pseudo_headings)
    result.chars_in = len(re.sub(r"\s+", "", raw))
    result.chars_out = len(re.sub(r"\s+", "", ANCHOR_RE.sub("", result.text)))
    return result


def strip_anchors(text: str) -> str:
    return "\n".join(l for l in text.split("\n") if not ANCHOR_RE.fullmatch(l.strip()))


def coordinates(text: str) -> list[str]:
    return ANCHOR_RE.findall(text)
