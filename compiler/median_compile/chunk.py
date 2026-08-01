"""Phase 3 — deterministic structural segmentation.

Splits each lean source into bounded chunks for Phase 4 extraction. No model
calls; the point of this phase is to avoid ever asking an LLM to repair an
arbitrary text break.

Two invariants carry the phase:

1. **Blocks are never split.** Phase 1 already established the atomic unit — a
   paragraph, table, or list, each with a coordinate. A chunk is a run of whole
   blocks. This is what keeps tables, procedures and formulas intact for free
   rather than by special-casing them.

2. **Every block is owned by exactly one chunk.** Overlap exists, but overlapped
   blocks are carried as *context* and marked as such. Without the ownership
   distinction, a block appearing in two chunks would be extracted twice and
   inflate the coverage ledger with phantom duplicates.

A block larger than the ceiling is emitted as its own oversized chunk and
reported rather than broken. Splitting a 15k-token table would do more damage
than handing Phase 4 one large intact unit.
"""

from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass, field

CHUNKER_VERSION = "1.0"

ANCHOR_RE = re.compile(r"<!--@([^>]+?)-->")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*)$")

#: Characters per token. A heuristic, not a tokenizer — the ceiling is set well
#: below any model limit so the estimate never needs to be exact.
CHARS_PER_TOKEN = 4

#: How full a chunk must be before a heading is treated as a seam.
#:
#: Calibrated by sweeping the real corpus. Too low and chunks close early: 0.5
#: gave 62 chunks averaging 4.6k against a 10k target, roughly 1.6x the
#: necessary extraction calls. At 1.0 the seam rule never fires at all, because
#: the size rule closes the chunk first. 0.9 gives 39 chunks averaging 7.2k
#: while still preferring section boundaries.
#:
#:   seam  chunks  mean   median  max     tails <2k
#:   0.5   62      4,624  5,255   7,084   9
#:   0.7   48      5,883  7,169   8,314   3
#:   0.9   39      7,182  8,731  10,472   4
#:   1.0   38      7,375  8,711  10,510   3
DEFAULT_SEAM_FRACTION = 0.9


@dataclass
class Block:
    coord: str
    text: str
    heading_path: tuple[str, ...]
    is_heading: bool

    @property
    def tokens(self) -> int:
        return max(1, len(self.text) // CHARS_PER_TOKEN)


@dataclass
class Chunk:
    id: str
    source: str
    owned: list[str] = field(default_factory=list)
    context: list[str] = field(default_factory=list)
    heading_path: tuple[str, ...] = ()
    text: str = ""
    tokens: int = 0
    sha256: str = ""
    oversized: bool = False

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "source": self.source,
            "chunker": CHUNKER_VERSION,
            "heading_path": list(self.heading_path),
            "owned": self.owned,
            "context": self.context,
            "tokens": self.tokens,
            "sha256": self.sha256,
            "oversized": self.oversized,
            "text": self.text,
        }


@dataclass
class ChunkResult:
    source_id: str
    chunks: list[Chunk] = field(default_factory=list)
    blocks: int = 0
    oversized: list[str] = field(default_factory=list)

    @property
    def tokens(self) -> int:
        return sum(c.tokens for c in self.chunks)


def parse_blocks(text: str) -> list[Block]:
    """Recover coordinate-tagged blocks and the heading path each sits under."""
    blocks: list[Block] = []
    path: list[str] = []
    coord: str | None = None
    buf: list[str] = []

    def flush() -> None:
        if coord is None:
            return
        body = "\n".join(buf).strip()
        if not body:
            return
        head = HEADING_RE.match(body.splitlines()[0])
        if head:
            level = len(head.group(1))
            title = head.group(2).strip()
            del path[level - 1 :]
            path.append(title)
            blocks.append(Block(coord, body, tuple(path), True))
        else:
            blocks.append(Block(coord, body, tuple(path), False))

    for line in text.split("\n"):
        m = ANCHOR_RE.fullmatch(line.strip())
        if m:
            flush()
            coord, buf = m.group(1), []
        elif coord is not None:
            buf.append(line)
    flush()
    return blocks


def _emit(
    source_id: str,
    n: int,
    owned: list[Block],
    context: list[Block],
) -> Chunk:
    body = "\n\n".join(b.text for b in context + owned)
    return Chunk(
        id=f"{source_id}:C{n:03d}",
        source=source_id,
        owned=[b.coord for b in owned],
        context=[b.coord for b in context],
        heading_path=owned[0].heading_path if owned else (),
        text=body,
        tokens=max(1, len(body) // CHARS_PER_TOKEN),
        sha256=hashlib.sha256(body.encode()).hexdigest(),
    )


def chunk(
    text: str,
    source_id: str,
    target_tokens: int = 10_000,
    max_tokens: int = 14_000,
    overlap_tokens: int = 400,
    respect_headings: bool = True,
    seam_fraction: float = DEFAULT_SEAM_FRACTION,
) -> ChunkResult:
    blocks = parse_blocks(text)
    result = ChunkResult(source_id=source_id, blocks=len(blocks))

    current: list[Block] = []
    current_tokens = 0
    carry: list[Block] = []
    n = 1

    def close() -> None:
        nonlocal current, current_tokens, carry, n
        if not current:
            return
        c = _emit(source_id, n, current, carry)
        c.oversized = current_tokens > max_tokens
        if c.oversized:
            result.oversized.append(c.id)
        result.chunks.append(c)
        n += 1
        # Carry trailing blocks forward as context, newest last.
        carry, total = [], 0
        for b in reversed(current):
            if total + b.tokens > overlap_tokens:
                break
            carry.insert(0, b)
            total += b.tokens
        current, current_tokens = [], 0

    for b in blocks:
        # A top-level heading is a natural seam; prefer it once the chunk has
        # real content, so sections are not straddled unnecessarily.
        if (
            respect_headings
            and b.is_heading
            and len(b.heading_path) <= 2
            and current_tokens >= target_tokens * seam_fraction
        ):
            close()

        if current_tokens + b.tokens > target_tokens and current:
            close()

        current.append(b)
        current_tokens += b.tokens

        if current_tokens >= max_tokens:
            close()

    close()
    return result


def validate(result: ChunkResult, text: str) -> list[str]:
    """Every block owned exactly once; no coordinate lost or duplicated."""
    errors: list[str] = []
    expected = [b.coord for b in parse_blocks(text)]
    owned: list[str] = []
    for c in result.chunks:
        owned.extend(c.owned)

    if len(owned) != len(set(owned)):
        dupes = {c for c in owned if owned.count(c) > 1}
        errors.append(f"{result.source_id}: block(s) owned twice: {sorted(dupes)[:5]}")

    missing = set(expected) - set(owned)
    if missing:
        errors.append(
            f"{result.source_id}: {len(missing)} block(s) owned by no chunk: "
            f"{sorted(missing)[:5]}"
        )

    if owned != [c for c in expected if c in set(owned)]:
        errors.append(f"{result.source_id}: chunk ownership is out of document order")

    for c in result.chunks:
        if set(c.context) & set(c.owned):
            errors.append(f"{c.id}: a block is both context and owned")

    return errors
