from __future__ import annotations

from collections import Counter
from decimal import Decimal, InvalidOperation, ROUND_CEILING
import hashlib
import json
import os
from pathlib import Path
import re
from typing import Any

from jsonschema import Draft202012Validator

from .errors import ContractError
from .validation import validate_atoms, validate_block_dispositions


SUPPORTED_CACHE_TTLS = {"5m", "1h"}
SUPPORTED_LIFECYCLE_STATES = {"pilot_call_authorized", "source_run_authorized"}
HEADING_LEVEL = re.compile(r"^ {0,3}(#{1,6})(?:\s+|$)")
TABLE_DELIMITER_CELL = re.compile(r"^:?-{3,}:?$")
PURE_STRUCTURAL_LABEL = re.compile(
    r"^(?:examples?|prefer|preferred|avoid|not|correct|incorrect):$",
    re.IGNORECASE,
)


def _decimal(value: Any, field: str) -> Decimal:
    try:
        result = Decimal(str(value))
    except (InvalidOperation, ValueError) as exc:
        raise ContractError(f"{field} is not a valid decimal") from exc
    if not result.is_finite() or result < 0:
        raise ContractError(f"{field} must be finite and nonnegative")
    return result


def canonical_json_bytes(value: Any) -> bytes:
    return (
        json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
        + "\n"
    ).encode("utf-8")


def _block_record(block: dict[str, Any]) -> dict[str, Any]:
    record = {
        "block_id": block["block_id"],
        "block_type": block["block_type"],
        "status_markers": block.get("status_markers", []),
        "text": block["text"],
    }
    if "estimated_claims" in block:
        record["estimated_claims"] = block["estimated_claims"]
    return record


def build_chunk_payload(
    manifest: dict[str, Any],
    dispositions: list[dict[str, Any]],
    chunk: dict[str, Any],
) -> dict[str, Any]:
    """Build one source-bounded payload from declarative, source-specific data."""
    source_id = manifest.get("source_id")
    source_hash = manifest.get("source_sha256")
    if not source_id or not source_hash:
        raise ContractError("block manifest lacks source identity")

    by_block = {item.get("block_id"): item for item in dispositions}
    if None in by_block or len(by_block) != len(dispositions):
        raise ContractError("disposition ledger has missing or duplicate block IDs")
    manifest_blocks = {item["block_id"]: item for item in manifest.get("blocks", [])}
    block_ids = chunk.get("block_ids")
    if not isinstance(block_ids, list) or not block_ids:
        raise ContractError("chunk must bind a nonempty block_ids list")
    if len(block_ids) != len(set(block_ids)):
        raise ContractError("chunk repeats a block ID")
    unknown = sorted(set(block_ids) - set(manifest_blocks))
    if unknown:
        raise ContractError("chunk contains unknown block IDs: " + ", ".join(unknown))
    missing_dispositions = sorted(set(block_ids) - set(by_block))
    if missing_dispositions:
        raise ContractError(
            "chunk blocks lack offline dispositions: " + ", ".join(missing_dispositions)
        )

    repeated_context_ids = chunk.get("context_block_ids", [])
    if not isinstance(repeated_context_ids, list) or len(repeated_context_ids) != len(set(repeated_context_ids)):
        raise ContractError("chunk context_block_ids must be a unique list")
    unknown_context = sorted(set(repeated_context_ids) - set(manifest_blocks))
    if unknown_context:
        raise ContractError("chunk contains unknown context block IDs: " + ", ".join(unknown_context))
    context_blocks: list[dict[str, Any]] = []
    target_blocks: list[dict[str, Any]] = []
    excluded_block_ids: list[str] = []
    for block_id in repeated_context_ids:
        if block_id in block_ids:
            continue
        if by_block.get(block_id, {}).get("disposition") != "context_only":
            raise ContractError(f"repeated context is not context_only: {block_id}")
        context_blocks.append(_block_record(manifest_blocks[block_id]))
    for block_id in block_ids:
        block = manifest_blocks[block_id]
        disposition = by_block[block_id].get("disposition")
        if disposition == "context_only":
            context_blocks.append(_block_record(block))
        elif disposition in {"eligible", "review_required"}:
            record = _block_record(block)
            if PURE_STRUCTURAL_LABEL.fullmatch(block.get("text", "").strip()):
                record["structural_role"] = "pure_example_or_polarity_label"
                record["required_disposition"] = "no_substantive_claim"
            target_blocks.append(record)
        elif disposition == "excluded":
            excluded_block_ids.append(block_id)
        else:
            raise ContractError(f"unsupported offline disposition for {block_id}: {disposition}")
    if not target_blocks:
        raise ContractError("chunk has no provider-eligible target blocks")

    body = {
        "schema_version": "M050-EXTRACTION-CHUNK-PAYLOAD-0.1",
        "chunk_id": str(chunk.get("chunk_id") or f"C{int(chunk.get('ordinal', 0)):04d}"),
        "source_id": source_id,
        "source_sha256": source_hash,
        "required_target_disposition_count": len(target_blocks),
        "context_blocks": context_blocks,
        "target_blocks": target_blocks,
        "excluded_block_ids": excluded_block_ids,
    }
    body["payload_sha256"] = hashlib.sha256(canonical_json_bytes(body)).hexdigest()
    return body


def draft_block_dispositions(manifest: dict[str, Any]) -> list[dict[str, Any]]:
    """Create a conservative review draft; never claim source-specific approval."""
    output: list[dict[str, Any]] = []
    for block in manifest.get("blocks", []):
        kind = block.get("block_type")
        if kind == "whitespace":
            disposition, reason = "excluded", "nonsemantic_whitespace_draft"
        elif kind == "heading":
            disposition, reason = "context_only", "structural_heading_draft"
        elif kind == "code_fence":
            disposition, reason = "review_required", "code_or_example_requires_source_review"
        else:
            disposition, reason = "eligible", "substantive_by_default_requires_source_review"
        output.append(
            {
                "block_id": block["block_id"],
                "block_sha256": block["raw_sha256"],
                "block_type": kind,
                "disposition": disposition,
                "reason_code": reason,
                "status_markers": block.get("status_markers", []),
                "draft_requires_identity_review": True,
            }
        )
    if len(output) != len({item["block_id"] for item in output}):
        raise ContractError("draft disposition ledger contains duplicate block IDs")
    return output


def plan_source_chunks(
    manifest: dict[str, Any],
    dispositions: list[dict[str, Any]],
    *,
    max_input_tokens: int,
    target_blocks_per_chunk: int,
    quantization_basis: str,
) -> dict[str, Any]:
    """Re-apportion a complete source at one calibrated target-block quantization."""
    if max_input_tokens < 1 or target_blocks_per_chunk < 1:
        raise ContractError("chunk limits must be positive")
    if not quantization_basis.strip():
        raise ContractError("chunk quantization requires a calibration basis")
    blocks = manifest.get("blocks", [])
    blocks_by_id = {block.get("block_id"): block for block in blocks}
    if None in blocks_by_id or len(blocks_by_id) != len(blocks):
        raise ContractError("chunk planning requires unique nonempty block IDs")
    by_disposition = {item.get("block_id"): item for item in dispositions}
    if len(by_disposition) != len(dispositions) or set(by_disposition) != {
        block.get("block_id") for block in blocks
    }:
        raise ContractError("chunk planning requires exactly one disposition per block")

    def disposition(block: dict[str, Any]) -> str:
        return by_disposition[block["block_id"]]["disposition"]

    def is_semantic_lead_in(block: dict[str, Any]) -> bool:
        return (
            block.get("block_type") in {"paragraph", "list_item"}
            and disposition(block) != "excluded"
            and block.get("text", "").rstrip().endswith(":")
        )

    def dependent_body_kind(block: dict[str, Any]) -> str | None:
        block_type = block.get("block_type")
        if block_type in {"list_item", "table_row", "code_fence"}:
            return block_type
        if block_type == "paragraph" and block.get("text", "").lstrip().startswith(">"):
            return "quotation"
        return None

    def after_whitespace(start: int) -> int:
        cursor = start
        while cursor < len(blocks) and blocks[cursor].get("block_type") == "whitespace":
            cursor += 1
        return cursor

    def dependent_body_end(start: int, kind: str) -> int:
        if kind == "code_fence":
            return start + 1
        cursor = start + 1
        while cursor < len(blocks):
            if dependent_body_kind(blocks[cursor]) == kind:
                cursor += 1
                continue
            if blocks[cursor].get("block_type") == "whitespace":
                next_body = after_whitespace(cursor)
                if next_body < len(blocks) and dependent_body_kind(blocks[next_body]) == kind:
                    cursor = next_body
                    continue
            break
        return cursor

    groups: list[list[dict[str, Any]]] = []
    index = 0
    while index < len(blocks):
        block = blocks[index]
        if is_semantic_lead_in(block):
            body_start = after_whitespace(index + 1)
            # A title-bearing lead-in may bind a heading and the structural body
            # immediately beneath it (for example, a titled reference table).
            if body_start < len(blocks) and blocks[body_start].get("block_type") == "heading":
                after_heading = after_whitespace(body_start + 1)
                heading_body_kind = (
                    dependent_body_kind(blocks[after_heading])
                    if after_heading < len(blocks)
                    else None
                )
                if heading_body_kind is not None:
                    end = dependent_body_end(after_heading, heading_body_kind)
                    groups.append(blocks[index:end])
                    index = end
                    continue
                groups.append(blocks[index : body_start + 1])
                index = body_start + 1
                continue
            body_kind = (
                dependent_body_kind(blocks[body_start])
                if body_start < len(blocks)
                else None
            )
            if body_kind is not None:
                end = dependent_body_end(body_start, body_kind)
                groups.append(blocks[index:end])
                index = end
                continue
        body_kind = dependent_body_kind(block)
        if body_kind is not None:
            end = dependent_body_end(index, body_kind)
            groups.append(blocks[index:end])
            index = end
            continue
        groups.append([block])
        index += 1

    chunks: list[dict[str, Any]] = []
    current: list[dict[str, Any]] = []
    current_tokens = 0
    current_targets = 0
    current_context: list[str] = []
    heading_stack: dict[int, str] = {}

    def measures(group: list[dict[str, Any]]) -> tuple[int, int]:
        tokens = 0
        targets = 0
        for block in group:
            disposition = by_disposition[block["block_id"]]["disposition"]
            if disposition != "excluded":
                tokens += max(1, (len(block["text"]) + 3) // 4)
            if disposition in {"eligible", "review_required"}:
                targets += 1
        return tokens, targets

    def flush() -> None:
        nonlocal current, current_tokens, current_targets, current_context
        if not current:
            return
        chunks.append(
            {
                "ordinal": len(chunks) + 1,
                "chunk_id": f"C{len(chunks) + 1:04d}",
                "block_ids": [block["block_id"] for block in current],
                "context_block_ids": current_context,
                "estimated_input_tokens": current_tokens,
                "target_blocks": current_targets,
            }
        )
        current = []
        current_tokens = 0
        current_targets = 0
        current_context = []

    for group in groups:
        group_tokens, group_targets = measures(group)
        if group_tokens > max_input_tokens or group_targets > target_blocks_per_chunk:
            raise ContractError(f"indivisible structural group exceeds chunk limits: {group[0]['block_id']}")
        would_exceed = current and (
            current_tokens + group_tokens > max_input_tokens
            or current_targets + group_targets > target_blocks_per_chunk
        )
        if would_exceed:
            flush()
            current_context = [heading_stack[level] for level in sorted(heading_stack)]
            context_tokens = sum(
                max(1, (len(blocks_by_id[block_id]["text"]) + 3) // 4)
                for block_id in current_context
            )
            current_tokens = context_tokens
        for block in group:
            if block.get("block_type") == "heading":
                match = HEADING_LEVEL.match(block.get("text", ""))
                if match:
                    level = len(match.group(1))
                    heading_stack = {
                        existing: block_id
                        for existing, block_id in heading_stack.items()
                        if existing < level
                    }
                    heading_stack[level] = block["block_id"]
        current.extend(group)
        current_tokens += group_tokens
        current_targets += group_targets
    flush()
    if not chunks:
        raise ContractError("source chunk plan is empty")
    primary_ids = [block_id for chunk in chunks for block_id in chunk["block_ids"]]
    expected_ids = [block["block_id"] for block in blocks]
    if primary_ids != expected_ids:
        raise ContractError("chunk plan does not preserve exact source block order")
    if any(chunk["estimated_input_tokens"] > max_input_tokens for chunk in chunks):
        raise ContractError("repeated heading context causes a chunk to exceed its input limit")
    return {
        "schema_version": "M050-SOURCE-CHUNK-PLAN-DRAFT-0.1",
        "status": "DRAFT_REQUIRES_SOURCE_REVIEW",
        "source_id": manifest.get("source_id"),
        "source_sha256": manifest.get("source_sha256"),
        "max_input_tokens": max_input_tokens,
        "quantization": {
            "unit": "provider_eligible_target_blocks",
            "target_blocks_per_chunk": target_blocks_per_chunk,
            "basis": quantization_basis,
            "generated_chunk_count": len(chunks),
            "chunk_count_is_input": False,
        },
        "chunks": chunks,
    }


def build_generic_response_schema(
    source_id: str, allowed_streams: list[str]
) -> dict[str, Any]:
    if not source_id or not allowed_streams or len(allowed_streams) != len(set(allowed_streams)):
        raise ContractError("generic response schema requires a source and unique streams")
    return {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "type": "object",
        "additionalProperties": False,
        "required": ["schema_version", "proposal_set_id", "request_id", "source_id", "dispositions"],
        "properties": {
            "schema_version": {"const": "M050-EVIDENCE-PROPOSAL-0.1"},
            "proposal_set_id": {"type": "string"},
            "request_id": {"type": "string"},
            "source_id": {"const": source_id},
            "dispositions": {
                "type": "array",
                "items": {
                    "type": "object",
                    "additionalProperties": False,
                    "required": ["block_id", "kind", "atoms"],
                    "properties": {
                        "block_id": {"type": "string"},
                        "kind": {"enum": ["atoms", "no_substantive_claim", "review_required"]},
                        "atoms": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "additionalProperties": False,
                                "required": [
                                    "proposal_id", "source_id", "block_id", "exact_source_text",
                                    "normalized_claim", "claim_kind", "stream"
                                ],
                                "properties": {
                                    "proposal_id": {"type": "string"},
                                    "source_id": {"const": source_id},
                                    "block_id": {"type": "string"},
                                    "exact_source_text": {"type": "string"},
                                    "normalized_claim": {"type": "string"},
                                    "claim_kind": {"type": "string"},
                                    "stream": {"enum": allowed_streams},
                                },
                            },
                        },
                    },
                },
            },
        },
    }


def build_generic_source_prompt(
    source_id: str, allowed_streams: list[str], approved_identity_boundary: str
) -> str:
    if not source_id or not allowed_streams or len(allowed_streams) != len(set(allowed_streams)):
        raise ContractError("generic source prompt requires a source and unique streams")
    if not approved_identity_boundary.strip():
        raise ContractError("approved source identity boundary is empty")
    streams = ", ".join(f"`{stream}`" for stream in allowed_streams)
    return f"""# MEDIAN source-bounded atomic extraction

Allowed source: `{source_id}` only
Allowed streams: {streams}

Convert every supplied target block into exactly one grounded disposition. Context blocks may guide interpretation but never receive dispositions. Excluded blocks are omitted offline. Use only `SOURCE_BLOCKS`; do not import other MEDIAN sources, prior atoms, background knowledge, mapping, reconciliation, canonization, or inferred authority.

## Approved content/provenance boundary

{approved_identity_boundary.strip()}

## Extraction contract

Split independent claims into separate atoms and keep dependent qualifications with the claim they qualify. Copy every `exact_source_text` exactly and contiguously from its target block. Preserve provisional, historical, rejected, example, negative, conditional, scope, ownership, and authority qualifiers. Use `review_required` instead of guessing. Never silently repair source text or invent identifiers, statuses, definitions, owners, or authorities.

Return JSON only under the bound response schema. `atoms` must be nonempty only when kind is `atoms`; it must be empty otherwise. Every atom must use the supplied source ID, its target block ID, one allowed stream, a unique proposal ID, exact source text, a concise normalized claim, and a source-faithful claim kind.
"""


def build_anthropic_request(
    *,
    prompt: str,
    response_schema: dict[str, Any],
    payload: dict[str, Any],
    model: str,
    reasoning_effort: str,
    maximum_output_tokens: int,
    cache_ttl: str,
) -> dict[str, Any]:
    """Render a request whose stable system prefix is explicitly cached."""
    if not prompt.strip():
        raise ContractError("extraction prompt is empty")
    if cache_ttl not in SUPPORTED_CACHE_TTLS:
        raise ContractError("cache TTL must be '5m' or '1h'")
    if not model:
        raise ContractError("provider model is required")
    if reasoning_effort not in {"low", "medium", "high"}:
        raise ContractError("unsupported reasoning effort")
    if not isinstance(maximum_output_tokens, int) or maximum_output_tokens < 1:
        raise ContractError("maximum output tokens must be positive")
    schema = {
        key: value
        for key, value in response_schema.items()
        if key not in {"$schema", "$id"}
    }
    Draft202012Validator.check_schema(schema)
    schema_contract = (
        "BOUND_RESPONSE_SCHEMA\n"
        + json.dumps(schema, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
        + "\nEND_BOUND_RESPONSE_SCHEMA"
    )
    user_text = (
        "SOURCE_BLOCKS\n"
        + json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
        + "\nEND_SOURCE_BLOCKS"
    )
    return {
        "model": model,
        "max_tokens": maximum_output_tokens,
        "thinking": {"type": "adaptive"},
        "output_config": {
            "effort": reasoning_effort,
            "format": {"type": "json_schema", "schema": schema},
        },
        "system": [
            {"type": "text", "text": prompt},
            {
                "type": "text",
                "text": schema_contract,
                "cache_control": {"type": "ephemeral", "ttl": cache_ttl},
            },
        ],
        "messages": [{"role": "user", "content": user_text}],
    }


def validate_extraction_response(
    *,
    payload: dict[str, Any],
    response: dict[str, Any],
    response_schema: dict[str, Any],
    allowed_streams: list[str],
) -> dict[str, Any]:
    """Mechanically validate any source profile without source-specific code."""
    errors: list[str] = []
    schema_errors = sorted(
        Draft202012Validator(response_schema).iter_errors(response),
        key=lambda error: list(error.absolute_path),
    )
    errors.extend(f"schema: {error.message}" for error in schema_errors)
    source_id = payload.get("source_id")
    if not source_id or response.get("source_id") != source_id:
        errors.append("response source_id violates the bound source")
    if not allowed_streams:
        errors.append("allowed output streams are empty")

    targets = [
        {**block, "claim_bearing": True}
        for block in payload.get("target_blocks", [])
    ]
    context_ids = {
        block.get("block_id") for block in payload.get("context_blocks", [])
    }
    excluded_ids = set(payload.get("excluded_block_ids", []))
    dispositions = response.get("dispositions", [])
    if not isinstance(dispositions, list):
        dispositions = []
    coverage = validate_block_dispositions(targets, dispositions)
    if not coverage["passed"]:
        errors.append(f"coverage: {json.dumps(coverage['errors'], sort_keys=True)}")

    proposal_ids: list[str] = []
    review_required = 0
    conditional_errors = 0
    table_structure_errors = 0
    required_disposition_errors = 0
    by_id = {block["block_id"]: block for block in targets}
    structural_table_ids: set[str] = set()
    for index, block in enumerate(targets):
        if block.get("block_type") != "table_row":
            continue
        cells = [cell.strip() for cell in block.get("text", "").strip().strip("|").split("|")]
        if cells and all(TABLE_DELIMITER_CELL.fullmatch(cell) for cell in cells):
            structural_table_ids.add(block["block_id"])
            if index > 0 and targets[index - 1].get("block_type") == "table_row":
                structural_table_ids.add(targets[index - 1]["block_id"])
    for disposition in dispositions:
        block_id = disposition.get("block_id")
        kind = disposition.get("kind")
        atoms = disposition.get("atoms", [])
        if block_id in context_ids:
            errors.append(f"context-only block was dispositioned: {block_id}")
        if block_id in excluded_ids or kind == "excluded":
            errors.append(f"excluded material entered provider output: {block_id}")
        if kind == "atoms" and not atoms:
            conditional_errors += 1
            errors.append(f"atoms disposition lacks atoms: {block_id}")
        if kind != "atoms" and atoms:
            conditional_errors += 1
            errors.append(f"non-atoms disposition carries atoms: {block_id}")
        if kind == "review_required":
            review_required += 1
        if block_id in structural_table_ids and kind != "no_substantive_claim":
            table_structure_errors += 1
            errors.append(
                f"structural table header/delimiter must be no_substantive_claim: {block_id}"
            )
        required_kind = by_id.get(block_id, {}).get("required_disposition")
        if required_kind and kind != required_kind:
            required_disposition_errors += 1
            errors.append(
                f"payload-required disposition {required_kind} not satisfied: {block_id}"
            )
        block = by_id.get(block_id, {})
        required_statuses = {
            str(marker).split(":", 1)[-1].strip().upper()
            for marker in block.get("status_markers", [])
        }
        for atom in atoms:
            proposal_ids.append(str(atom.get("proposal_id")))
            if atom.get("source_id") != source_id:
                errors.append("atom source_id violates the bound source")
            if atom.get("block_id") != block_id:
                errors.append("atom block_id differs from its disposition block")
            if atom.get("stream") not in allowed_streams:
                errors.append("atom stream violates the source output-stream allowlist")
            normalized = str(atom.get("normalized_claim", "")).upper()
            for status in required_statuses:
                if status and status not in normalized:
                    errors.append(
                        f"status qualifier {status} missing from atom {atom.get('proposal_id')}"
                    )

    grounding = validate_atoms(str(source_id), targets, dispositions)
    if not grounding["passed"]:
        errors.append("one or more atoms failed exact contiguous grounding")
    duplicates = sorted(
        key for key, count in Counter(proposal_ids).items() if count > 1
    )
    if duplicates:
        errors.append("duplicate proposal IDs: " + ", ".join(duplicates))

    low_yield = grounding["low_yield_review"]
    return {
        "passed": not errors,
        "decision_required": bool(errors or review_required or low_yield),
        "checks": {
            "schema_errors": len(schema_errors),
            "coverage_errors": 0 if coverage["passed"] else 1,
            "conditional_atoms_errors": conditional_errors,
            "table_structure_errors": table_structure_errors,
            "required_disposition_errors": required_disposition_errors,
            "grounding_errors": sum(
                not result["passed"] for result in grounding["atom_results"]
            ),
            "review_required_blocks": review_required,
            "low_yield_review_blocks": low_yield,
        },
        "errors": errors,
    }


def extract_anthropic_structured_response(
    provider_response: dict[str, Any],
) -> dict[str, Any]:
    """Extract exactly one structured text block from a successful Messages response."""
    if provider_response.get("type") != "message":
        raise ContractError("Anthropic response is not a message")
    if provider_response.get("role") != "assistant":
        raise ContractError("Anthropic response role is not assistant")
    if provider_response.get("stop_reason") != "end_turn":
        raise ContractError(
            f"Anthropic response did not end cleanly: {provider_response.get('stop_reason')}"
        )
    text_blocks = [
        item.get("text")
        for item in provider_response.get("content", [])
        if item.get("type") == "text"
    ]
    if len(text_blocks) != 1 or not isinstance(text_blocks[0], str):
        raise ContractError("Anthropic response must contain exactly one text block")
    try:
        structured = json.loads(text_blocks[0])
    except json.JSONDecodeError as exc:
        raise ContractError(f"Anthropic structured text is invalid JSON: {exc}") from exc
    if not isinstance(structured, dict):
        raise ContractError("Anthropic structured response root must be an object")
    return structured


def anthropic_usage_cost(
    usage: dict[str, Any], pricing: dict[str, Any], *, cache_ttl: str
) -> dict[str, str]:
    """Compute exact cost, including explicit 5m/1h cache pricing."""
    if cache_ttl not in SUPPORTED_CACHE_TTLS:
        raise ContractError("cache TTL must be '5m' or '1h'")
    input_rate = _decimal(pricing.get("input_usd_per_million_tokens"), "input rate")
    output_rate = _decimal(pricing.get("output_usd_per_million_tokens"), "output rate")
    read_multiplier = _decimal(pricing.get("cache_read_multiplier", "0.1"), "cache read multiplier")
    write_5m_multiplier = _decimal(pricing.get("cache_5m_write_multiplier", "1.25"), "5m cache write multiplier")
    write_1h_multiplier = _decimal(pricing.get("cache_1h_write_multiplier", "2"), "1h cache write multiplier")

    uncached = _decimal(usage.get("input_tokens", 0), "input tokens")
    output = _decimal(usage.get("output_tokens", 0), "output tokens")
    cache_read = _decimal(usage.get("cache_read_input_tokens", 0), "cache read tokens")
    creation_total = _decimal(
        usage.get("cache_creation_input_tokens", 0), "cache creation tokens"
    )
    creation = usage.get("cache_creation", {}) or {}
    write_5m = _decimal(creation.get("ephemeral_5m_input_tokens", 0), "5m cache tokens")
    write_1h = _decimal(creation.get("ephemeral_1h_input_tokens", 0), "1h cache tokens")
    accounted_creation = write_5m + write_1h
    if accounted_creation > creation_total:
        raise ContractError("cache creation token breakdown exceeds total")
    remainder = creation_total - accounted_creation
    if cache_ttl == "1h":
        write_1h += remainder
    else:
        write_5m += remainder

    million = Decimal(1_000_000)
    costs = {
        "uncached_input_usd": uncached * input_rate / million,
        "cache_5m_write_usd": write_5m * input_rate * write_5m_multiplier / million,
        "cache_1h_write_usd": write_1h * input_rate * write_1h_multiplier / million,
        "cache_read_usd": cache_read * input_rate * read_multiplier / million,
        "output_usd": output * output_rate / million,
    }
    total = sum(costs.values(), Decimal(0))
    return {
        **{key: format(value, "f") for key, value in costs.items()},
        "total_usd": format(total, "f"),
        "display_usd_rounded_up": format(
            total.quantize(Decimal("0.01"), rounding=ROUND_CEILING), "f"
        ),
    }


def conservative_call_ceiling(
    request: dict[str, Any], pricing: dict[str, Any]
) -> Decimal:
    """Forecast a cache-write miss conservatively; cache hits never fund authority."""
    request_bytes = len(canonical_json_bytes(request))
    # UTF-8 bytes are a safe tokenizer-independent upper bound for input tokens.
    # The whole request is also priced at the cache-write multiplier below, even
    # though only the stable prefix is written, so a cache hit never funds scope.
    input_tokens = Decimal(request_bytes)
    output_tokens = Decimal(request.get("max_tokens", 0))
    input_rate = _decimal(pricing.get("input_usd_per_million_tokens"), "input rate")
    output_rate = _decimal(pricing.get("output_usd_per_million_tokens"), "output rate")
    input_multiplier = Decimal(1)
    system = request.get("system", [])
    cache_control = system[-1].get("cache_control", {}) if system else {}
    if cache_control.get("ttl") == "1h":
        input_multiplier = _decimal(
            pricing.get("cache_1h_write_multiplier", "2"),
            "1h cache write multiplier",
        )
    elif cache_control.get("ttl") == "5m":
        input_multiplier = _decimal(
            pricing.get("cache_5m_write_multiplier", "1.25"),
            "5m cache write multiplier",
        )
    return (
        input_tokens * input_rate * input_multiplier + output_tokens * output_rate
    ) / Decimal(1_000_000)


def spend_preflight(
    *,
    envelope: dict[str, Any],
    lifecycle_receipt: dict[str, Any],
    source_id: str,
    completed_calls: int,
    call_ceiling_usd: Decimal,
    required_binding: dict[str, Any] | None = None,
) -> dict[str, str]:
    """Require independent lifecycle authority and cumulative monetary authority."""
    if envelope.get("authority") != "Asa Wember":
        raise ContractError("spend envelope requires Asa Wember authority")
    if envelope.get("scope") != "provider_spend_only":
        raise ContractError("spend envelope must be money-only")
    if envelope.get("active") is not True:
        raise ContractError("spend envelope is not active")
    authorized = _decimal(envelope.get("authorized_usd"), "authorized spend")
    spent = _decimal(envelope.get("spent_usd", 0), "spent amount")
    if spent > authorized:
        raise ContractError("spend envelope is already overdrawn")

    state = lifecycle_receipt.get("state")
    if state not in SUPPORTED_LIFECYCLE_STATES:
        raise ContractError("call lacks an authorized extraction lifecycle transition")
    if lifecycle_receipt.get("authority") != "Asa Wember":
        raise ContractError("lifecycle receipt requires Asa Wember authority")
    binding = lifecycle_receipt.get("binding", {})
    if binding.get("source_id") != source_id:
        raise ContractError("lifecycle authority does not cover this source")
    if lifecycle_receipt.get("revoked") is True:
        raise ContractError("lifecycle authority was revoked")
    if state == "source_run_authorized" and lifecycle_receipt.get("execution_cadence") != "sequential_one_call_review":
        raise ContractError("source-run lifecycle authority must preserve sequential review")
    required_binding = required_binding or {}
    drift = [
        field
        for field, value in required_binding.items()
        if binding.get(field) != value
    ]
    if drift:
        raise ContractError(
            "lifecycle authority does not bind the exact execution configuration: "
            + ", ".join(drift)
        )
    call_limit = lifecycle_receipt.get("provider_call_limit")
    if not isinstance(call_limit, int) or completed_calls >= call_limit:
        raise ContractError("lifecycle provider-call limit is exhausted")

    ceiling = _decimal(call_ceiling_usd, "call ceiling")
    remaining = authorized - spent
    if ceiling > remaining:
        raise ContractError("spend envelope cannot cover the next cache-miss ceiling")
    return {
        "authorized_usd": format(authorized, "f"),
        "spent_usd": format(spent, "f"),
        "remaining_before_call_usd": format(remaining, "f"),
        "reserved_call_ceiling_usd": format(ceiling, "f"),
        "remaining_after_reservation_usd": format(remaining - ceiling, "f"),
    }


def debit_spend_envelope(
    envelope: dict[str, Any], actual_cost_usd: str
) -> dict[str, Any]:
    """Return a successor envelope; never mutate the authorized receipt in place."""
    updated = dict(envelope)
    authorized = _decimal(updated.get("authorized_usd"), "authorized spend")
    spent = _decimal(updated.get("spent_usd", 0), "spent amount")
    actual = _decimal(actual_cost_usd, "actual cost")
    if spent + actual > authorized:
        raise ContractError("actual cost would overdraw the spend envelope")
    updated["spent_usd"] = format(spent + actual, "f")
    updated["remaining_usd"] = format(authorized - spent - actual, "f")
    return updated


def ledger_event_hash(event: dict[str, Any]) -> str:
    return hashlib.sha256(canonical_json_bytes(event)).hexdigest()


def read_run_ledger(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    events: list[dict[str, Any]] = []
    for line_number, line in enumerate(
        path.read_text(encoding="utf-8").splitlines(), start=1
    ):
        if not line.strip():
            continue
        try:
            event = json.loads(line)
        except json.JSONDecodeError as exc:
            raise ContractError(
                f"run ledger has invalid JSON on line {line_number}"
            ) from exc
        if not isinstance(event, dict):
            raise ContractError(f"run ledger line {line_number} is not an object")
        events.append(event)
    previous: str | None = None
    for sequence, event in enumerate(events, start=1):
        if event.get("sequence") != sequence:
            raise ContractError("run ledger sequence is not contiguous")
        if event.get("predecessor_event_sha256") != previous:
            raise ContractError("run ledger predecessor chain is invalid")
        previous = ledger_event_hash(event)
    return events


def append_run_ledger_event(path: Path, event_body: dict[str, Any]) -> dict[str, Any]:
    events = read_run_ledger(path)
    event = {
        "schema_version": "M050-EXTRACTION-RUN-EVENT-0.1",
        "sequence": len(events) + 1,
        "predecessor_event_sha256": ledger_event_hash(events[-1]) if events else None,
        **event_body,
    }
    event["event_id"] = "evt_" + hashlib.sha256(canonical_json_bytes(event)).hexdigest()[:24]
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(canonical_json_bytes(event).decode("utf-8"))
        handle.flush()
        os.fsync(handle.fileno())
    read_run_ledger(path)
    return event


def require_run_ready_for_next_call(
    events: list[dict[str, Any]], source_id: str
) -> int:
    captured = [event for event in events if event.get("state") == "call_captured"]
    if not events:
        return 0
    last = events[-1]
    if last.get("source_id") != source_id:
        raise ContractError("run ledger belongs to another source")
    if last.get("state") != "review_passed":
        raise ContractError("next call is blocked until the prior outcome passes review")
    return len(captured)


def require_authorized_chunk(
    lifecycle_receipt: dict[str, Any], chunk_id: str, completed_calls: int
) -> None:
    authorized = lifecycle_receipt.get("authorized_chunk_ids")
    limit = lifecycle_receipt.get("provider_call_limit")
    if (
        not isinstance(authorized, list)
        or not authorized
        or any(not isinstance(value, str) or not value for value in authorized)
        or len(authorized) != len(set(authorized))
    ):
        raise ContractError("lifecycle receipt lacks an exact unique chunk sequence")
    if not isinstance(limit, int) or limit != len(authorized):
        raise ContractError("provider-call limit does not match the authorized chunk sequence")
    if completed_calls < 0 or completed_calls >= len(authorized):
        raise ContractError("authorized chunk sequence is exhausted")
    if authorized[completed_calls] != chunk_id:
        raise ContractError(
            f"next authorized chunk is {authorized[completed_calls]}, not {chunk_id}"
        )
