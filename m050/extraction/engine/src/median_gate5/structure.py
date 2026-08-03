from __future__ import annotations

from dataclasses import asdict, dataclass
import re
from typing import Iterable

from .canonical import sha256_bytes
from .errors import ContractError
from .normalization import structural_text


HEADING = re.compile(r"^ {0,3}#{1,6}(?:\s+|$)")
LIST_ITEM = re.compile(r"^\s*(?:[-+*]|\d+[.)])\s+")
STATUS_MARKER = re.compile(
    r"\b(?:STATE|STATUS|REGISTER|MODE)\s*:\s*(?:SILENT|PROVISIONAL|HISTORICAL|EXAMPLE|REJECTED)\b",
    re.IGNORECASE,
)


@dataclass(frozen=True)
class Block:
    block_id: str
    source_id: str
    ordinal: int
    block_type: str
    start: int
    end: int
    raw_sha256: str
    text: str
    parent_heading: str | None
    status_markers: tuple[str, ...]
    claim_bearing: bool
    estimated_claims: int
    local_disposition: str
    local_reason_code: str

    def to_dict(self) -> dict:
        value = asdict(self)
        value["status_markers"] = list(self.status_markers)
        return value


def _line_kind(line: str, in_fence: bool) -> str:
    stripped = line.strip("\r\n")
    if in_fence or stripped.lstrip().startswith("```"):
        return "code_fence"
    if not stripped.strip():
        return "whitespace"
    if HEADING.match(stripped):
        return "heading"
    if stripped.lstrip().startswith("|") and stripped.rstrip().endswith("|"):
        return "table_row"
    if LIST_ITEM.match(stripped):
        return "list_item"
    return "paragraph"


def _estimated_claims(kind: str, text: str) -> int:
    if kind in {"whitespace", "heading", "code_fence"}:
        return 0
    markers = len(re.findall(r"[.!?;](?:\s|$)", text))
    conjunctions = len(re.findall(r"\b(?:must|shall|cannot|never|except|unless)\b", text, re.I))
    return max(1, min(8, markers + max(0, conjunctions - 1)))


def parse_markdown(source_id: str, raw: str) -> list[Block]:
    if not source_id:
        raise ContractError("source_id is required")
    text = structural_text(raw)
    lines = text.splitlines(keepends=True)
    if not lines and text == "":
        return []
    if lines and "".join(lines) != text:
        lines.append(text[sum(len(line) for line in lines) :])

    groups: list[tuple[str, int, int, str]] = []
    position = 0
    current_kind: str | None = None
    current_start = 0
    current_parts: list[str] = []
    in_fence = False

    def flush(end: int) -> None:
        nonlocal current_kind, current_start, current_parts
        if current_kind is not None:
            groups.append((current_kind, current_start, end, "".join(current_parts)))
        current_kind = None
        current_parts = []

    for line in lines:
        kind = _line_kind(line, in_fence)
        standalone = kind in {"heading", "table_row", "list_item"}
        if standalone or (current_kind is not None and kind != current_kind):
            flush(position)
        if current_kind is None:
            current_kind = kind
            current_start = position
        current_parts.append(line)
        position += len(line)
        if kind == "code_fence" and line.strip().startswith("```"):
            in_fence = not in_fence
        if standalone:
            flush(position)
    flush(position)

    blocks: list[Block] = []
    parent_heading: str | None = None
    for ordinal, (kind, start, end, block_text) in enumerate(groups, start=1):
        digest = sha256_bytes(block_text.encode("utf-8"))
        block_id = f"{source_id}__B{ordinal:05d}_{digest[:12]}"
        markers = tuple(sorted({match.group(0) for match in STATUS_MARKER.finditer(block_text)}))
        if kind == "heading":
            parent_heading = block_text.strip()
        claims = _estimated_claims(kind, block_text)
        if claims:
            local_disposition = "eligible"
            local_reason = "claim_bearing_content"
        elif kind == "heading":
            local_disposition = "context_only"
            local_reason = "structural_heading"
        elif kind == "whitespace":
            local_disposition = "excluded"
            local_reason = "whitespace_separator"
        else:
            local_disposition = "review_required"
            local_reason = "nonprose_structural_block"
        blocks.append(
            Block(
                block_id=block_id,
                source_id=source_id,
                ordinal=ordinal,
                block_type=kind,
                start=start,
                end=end,
                raw_sha256=digest,
                text=block_text,
                parent_heading=parent_heading,
                status_markers=markers,
                claim_bearing=claims > 0,
                estimated_claims=claims,
                local_disposition=local_disposition,
                local_reason_code=local_reason,
            )
        )
    if "".join(block.text for block in blocks) != text:
        raise ContractError("structural parser did not preserve the complete source text")
    return blocks


def plan_chunks(
    blocks: Iterable[Block], *, max_tokens: int, max_claim_blocks: int
) -> list[dict]:
    if max_tokens <= 0 or max_claim_blocks <= 0:
        raise ContractError("chunk limits must be positive")
    chunks: list[dict] = []
    current: list[Block] = []
    tokens = 0
    claim_blocks = 0

    def flush() -> None:
        nonlocal current, tokens, claim_blocks
        if not current:
            return
        chunks.append(
            {
                "ordinal": len(chunks) + 1,
                "block_ids": [block.block_id for block in current],
                "estimated_tokens": tokens,
                "claim_bearing_blocks": claim_blocks,
            }
        )
        current = []
        tokens = 0
        claim_blocks = 0

    for block in blocks:
        block_tokens = max(1, (len(block.text) + 3) // 4)
        block_claim = int(block.claim_bearing)
        if block_tokens > max_tokens or block_claim > max_claim_blocks:
            raise ContractError(f"block exceeds chunk limits: {block.block_id}")
        boundary = bool(block.status_markers) and current
        would_exceed = tokens + block_tokens > max_tokens or claim_blocks + block_claim > max_claim_blocks
        if boundary or would_exceed:
            flush()
        current.append(block)
        tokens += block_tokens
        claim_blocks += block_claim
        if block.status_markers:
            flush()
    flush()
    return chunks
