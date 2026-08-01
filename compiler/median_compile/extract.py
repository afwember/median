"""Phase 4 — Claude extraction, Pass A.

Bounded, schema-constrained calls: one chunk in, atomic records out. The
program does the file handling, caching, validation and accounting; the model
does only source-local decomposition.

Caching is the spec's §7 requirement and the reason a re-run is cheap. A call
is keyed by the chunk hash, prompt version, schema version, provider and model
ID. Change any of those and the cache misses; change nothing and no tokens are
spent.

The provider is an interface with a deterministic fake behind it, so every
behaviour below is testable without network access or an API key.
"""

from __future__ import annotations

import hashlib
import json
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Protocol

from .records import AtomicRecord, RECORD_SCHEMA_VERSION

PROMPT_VERSION = "3.1"


class ExtractionError(RuntimeError):
    """A call completed but its result is unusable. The raw text is kept."""


class Truncated(ExtractionError):
    """The model hit the output ceiling; the JSON is cut off mid-token."""


class MalformedResponse(ExtractionError):
    """The response parsed as text but is not a valid records payload."""

#: USD per million tokens. A configuration value, not a fact: override in
#: config.yaml under providers.extraction.pricing to match the model actually
#: in use. Affects the estimate only; the call log records real token counts.
#: Derived from a real spend: 36k input + 76k output cost $2.16, which matches
#: $5/$25 and rules out the $3/$15 I originally assumed. Verify against your
#: own console pricing and override in config.yaml if the model changes.
PRICING = {
    "input_per_mtok": 5.00,
    "output_per_mtok": 25.00,
}

#: Calibrated against the first real call: SPEC_HOME:C001, 9,449 input tokens,
#: 89 owned blocks, 193 projected records. My seeded guesses were 4.0 and 180,
#: which under-costed the corpus by 6.6x. Extraction output is dense JSON and
#: tokenizes at roughly 1.9 chars/token, not the 4.0 that prose does.
RECORDS_PER_1K_TOKENS = 20.4
#: 283 under schema 1.0. Schema 2.0 drops quote/id/src/terms/deps, measured at
#: 47% of the v1.0 record, leaving ~169.
OUTPUT_TOKENS_PER_RECORD = 169

#: Output tokens a chunk of a given size will produce. Used to size chunks so
#: a call fits under the ceiling rather than discovering it does not.
OUTPUT_EXPANSION = RECORDS_PER_1K_TOKENS * OUTPUT_TOKENS_PER_RECORD / 1000  # ~5.8x

#: Output ceiling per call. The first real run truncated at 12,000: a 9k-token
#: chunk yields on the order of 100 records, and at ~180 tokens each that is
#: 18k of output. Set well clear of the observed need — this is a ceiling, not
#: a spend, and unused headroom costs nothing.
DEFAULT_MAX_OUTPUT_TOKENS = 32_000

#: Chunk size that keeps projected output comfortably under the ceiling.
#: 9.4k in produced ~55k out and truncated at 32k. 3.5k in projects to ~20k.
SAFE_CHUNK_TOKENS = 5_500


class Provider(Protocol):
    name: str
    model: str

    def complete(self, system: str, user: str, max_tokens: int) -> tuple[str, dict]:
        """Return (text, usage). usage carries input_tokens / output_tokens."""


@dataclass
class FakeProvider:
    """Deterministic stand-in. Emits one record per owned block.

    Exists so extraction logic — caching, validation, coverage, accounting —
    is testable without network access, and so `--dry-run` can exercise the
    whole path.
    """

    name: str = "fake"
    model: str = "fake-1"
    calls: int = 0

    def complete(self, system: str, user: str, max_tokens: int) -> tuple[str, dict]:
        self.calls += 1
        src = re.search(r"SOURCE_ID:\s*(\S+)", user)
        start = re.search(r"START_NUMBER:\s*(\d+)", user)
        source_id = src.group(1) if src else "SPEC_X"
        n = int(start.group(1)) if start else 1

        owned = re.search(r"OWNED:\s*(.+)", user)
        coords = owned.group(1).split(", ") if owned else []
        blocks = _blocks_from_prompt(user)

        records = []
        for coord in coords:
            body = blocks.get(coord, "")
            if not body or body.lstrip().startswith("#"):
                continue
            words = body.split()
            if len(words) < 6:
                continue
            records.append(
                {
                    "loc": coord,
                    "q0": " ".join(words[:4]),
                    "q1": " ".join(words[-3:]),
                    "claim": f"Fake claim for {coord}.",
                    "type": "REQ",
                    "voice": "world",
                    "status": "canonical",
                    "owner": "meta",
                }
            )
            n += 1
        return json.dumps({"records": records}), {
            "input_tokens": len(user) // 4,
            "output_tokens": len(records) * 60,
        }


def _blocks_from_prompt(user: str) -> dict[str, str]:
    blocks: dict[str, str] = {}
    coord = None
    buf: list[str] = []
    for line in user.split("\n"):
        m = re.fullmatch(r"<!--@([^>]+?)-->", line.strip())
        if m:
            if coord:
                blocks[coord] = "\n".join(buf).strip()
            coord, buf = m.group(1), []
        elif coord is not None:
            buf.append(line)
    if coord:
        blocks[coord] = "\n".join(buf).strip()
    return blocks


@dataclass
class Call:
    call_id: str
    provider: str
    model: str
    task: str
    source: str
    chunk: str
    input_hash: str
    prompt_version: str
    schema_version: str
    input_tokens: int
    output_tokens: int
    status: str
    cached: bool = False
    notes: str = ""


@dataclass
class ExtractResult:
    source_id: str
    records: list[AtomicRecord] = field(default_factory=list)
    calls: list[Call] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)

    @property
    def input_tokens(self) -> int:
        return sum(c.input_tokens for c in self.calls if not c.cached)

    @property
    def output_tokens(self) -> int:
        return sum(c.output_tokens for c in self.calls if not c.cached)

    @property
    def cost(self) -> float:
        return (
            self.input_tokens / 1e6 * PRICING["input_per_mtok"]
            + self.output_tokens / 1e6 * PRICING["output_per_mtok"]
        )


def cache_key(
    chunk_sha: str,
    prompt_version: str,
    schema_version: str,
    provider: str,
    model: str,
    effort: str | None = None,
    namespace_sha: str = "",
) -> str:
    """Everything that can change the answer belongs in the key.

    Reasoning effort included because it does: without it, an A/B of effort on
    against effort off silently serves the cached run and compares a result
    with itself.

    The namespace vocabulary is included for the same reason, and the omission
    was live until 1 August 2026. The whole list is injected into every user
    prompt, so renaming a namespace changes what the model can answer — that is
    the entire finding behind removing `away.crossing.risk`. Without the
    vocabulary in the key, editing `owner_namespaces.yaml` and re-running would
    serve the pre-edit records, report `cached` and $0.00, and look like the
    model had agreed with the change.
    """
    raw = "|".join(
        [
            chunk_sha,
            prompt_version,
            schema_version,
            provider,
            model,
            effort or "none",
            namespace_sha or "none",
        ]
    )
    return hashlib.sha256(raw.encode()).hexdigest()[:32]


def namespace_sha(namespaces: list[str]) -> str:
    """Hash the rendered namespace block exactly as the prompt will carry it.

    Rendered, not raw YAML: comments and key order in the source file do not
    change the answer, and must not invalidate a cache that cost real money.
    Descriptions do change the answer, and are included.
    """
    return hashlib.sha256("\n".join(namespaces).encode()).hexdigest()[:16]


def build_user_prompt(
    chunk: dict,
    source_meta: dict,
    namespaces: list[str],
    start_number: int,
) -> str:
    """Assemble the bounded per-call payload. Compiler spec §10."""
    return "\n".join(
        [
            f"SOURCE_ID: {chunk['source']}",
            f"SOURCE_CLASS: {source_meta.get('source_class', '')}",
            f"WORDING_FIDELITY: {source_meta.get('wording_fidelity', 'SEMANTIC')}",
            f"CHUNK_ID: {chunk['id']}",
            f"HEADING_PATH: {' > '.join(chunk.get('heading_path') or []) or '(root)'}",
            f"START_NUMBER: {start_number}",
            "",
            "HANDLING NOTES:",
            source_meta.get("notes", "").strip() or "(none)",
            "",
            "NAMESPACES (name — what it owns):",
            "\n".join(namespaces),
            "",
            f"OWNED: {', '.join(chunk['owned'])}",
            f"CONTEXT: {', '.join(chunk.get('context') or []) or '(none)'}",
            "",
            "CHUNK:",
            chunk["text"],
        ]
    )


#: Prompt plus 86 namespace descriptions, sent with every call.
PER_CALL_OVERHEAD_TOKENS = 3_000


def estimate(chunks: list[dict], ceiling: int = DEFAULT_MAX_OUTPUT_TOKENS) -> dict:
    """Cost estimate for a dry run, from coefficients observed in a real call."""
    in_tok = sum(c["tokens"] for c in chunks)
    billed_in = in_tok + PER_CALL_OVERHEAD_TOKENS * len(chunks)
    est_records = int(in_tok / 1000 * RECORDS_PER_1K_TOKENS)
    out_tok = est_records * OUTPUT_TOKENS_PER_RECORD
    wont_fit = [c["id"] for c in chunks if c["tokens"] * OUTPUT_EXPANSION > ceiling]
    return {
        "chunks": len(chunks),
        "chunk_tokens": in_tok,
        "billed_input_tokens": billed_in,
        "est_records": est_records,
        "est_output_tokens": out_tok,
        "est_cost_usd": round(
            billed_in / 1e6 * PRICING["input_per_mtok"]
            + out_tok / 1e6 * PRICING["output_per_mtok"],
            2,
        ),
        "chunks_over_ceiling": len(wont_fit),
    }


def parse_response(text: str) -> list[dict]:
    """Tolerate a fenced code block; reject anything else non-JSON."""
    body = text.strip()
    fence = re.match(r"^```(?:json)?\s*(.+?)\s*```$", body, re.DOTALL)
    if fence:
        body = fence.group(1)
    data = json.loads(body)
    if not isinstance(data, dict) or "records" not in data:
        raise ValueError("response must be an object with a 'records' array")
    return data["records"]


def extract_chunk(
    chunk: dict,
    source_meta: dict,
    namespaces: list[str],
    start_number: int,
    system_prompt: str,
    provider: Provider,
    cache_dir: Path,
    max_tokens: int = DEFAULT_MAX_OUTPUT_TOKENS,
) -> tuple[list[dict], Call]:
    user = build_user_prompt(chunk, source_meta, namespaces, start_number)
    key = cache_key(
        chunk["sha256"],
        PROMPT_VERSION,
        RECORD_SCHEMA_VERSION,
        provider.name,
        provider.model,
        getattr(provider, "effort", None),
        namespace_sha(namespaces),
    )
    cache_path = cache_dir / f"{key}.json"

    if cache_path.exists():
        payload = json.loads(cache_path.read_text(encoding="utf-8"))
        call = Call(
            call_id=key,
            provider=provider.name,
            model=provider.model,
            task="extract",
            source=chunk["source"],
            chunk=chunk["id"],
            input_hash=chunk["sha256"],
            prompt_version=PROMPT_VERSION,
            schema_version=RECORD_SCHEMA_VERSION,
            input_tokens=payload.get("usage", {}).get("input_tokens", 0),
            output_tokens=payload.get("usage", {}).get("output_tokens", 0),
            status="ok",
            cached=True,
        )
        return payload["records"], call

    text, usage = provider.complete(system_prompt, user, max_tokens)

    # Persist the raw response BEFORE parsing. A paid call must never be lost
    # to a parse failure: the first real extraction run hit the output ceiling,
    # crashed in json.loads, and threw away tokens that had already been
    # charged. The raw file is also what makes a truncation diagnosable.
    cache_dir.mkdir(parents=True, exist_ok=True)
    (cache_dir / f"{key}.raw.txt").write_text(text, encoding="utf-8")

    if usage.get("stop_reason") == "max_tokens":
        raise Truncated(
            f"{chunk['id']}: response hit the {max_tokens:,}-token output ceiling "
            f"and is incomplete. The raw text is kept at {key}.raw.txt. Raise "
            "providers.extraction.max_output_tokens in config.yaml, or lower "
            "chunking.target_tokens so each call produces fewer records."
        )

    try:
        raw = parse_response(text)
    except (json.JSONDecodeError, ValueError) as exc:
        raise MalformedResponse(
            f"{chunk['id']}: response was not valid record JSON ({exc}). "
            f"Raw text kept at {key}.raw.txt."
        ) from exc

    cache_path.write_text(
        json.dumps({"records": raw, "usage": usage}, ensure_ascii=False, indent=1),
        encoding="utf-8",
    )
    call = Call(
        call_id=key,
        provider=provider.name,
        model=provider.model,
        task="extract",
        source=chunk["source"],
        chunk=chunk["id"],
        input_hash=chunk["sha256"],
        prompt_version=PROMPT_VERSION,
        schema_version=RECORD_SCHEMA_VERSION,
        input_tokens=usage.get("input_tokens", 0),
        output_tokens=usage.get("output_tokens", 0),
        status="ok",
        notes=_usage_note(usage),
    )
    return raw, call


def _usage_note(usage: dict) -> str:
    """Flag output tokens that did not become text.

    Text runs about 2 characters per token. A response billed far above that
    is spending tokens on blocks the text stream never yields.
    """
    out = usage.get("output_tokens") or 0
    chars = usage.get("text_chars") or 0
    kinds = usage.get("block_types") or {}
    note = f"blocks={kinds}" if kinds else ""
    if out and chars and chars / out < 1.4:
        note += f" UNSEEN_OUTPUT chars/token={chars/out:.2f}"
    return note.strip()
