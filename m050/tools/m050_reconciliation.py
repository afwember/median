#!/usr/bin/env python3
"""Stage 5 semantic reconciliation corpus, packets, records, and lifecycle."""

from __future__ import annotations

import argparse
import copy
from dataclasses import dataclass
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import stat
import subprocess
import tempfile
from typing import Iterable
import urllib.error
import urllib.request
import uuid

try:
    from m050.tools.m050_atom_triage import TriageError, _read_jsonl, _sha256
    from m050.tools.m050_msid_mapping import (
        DEFAULT_MAPPINGS,
        DEFAULT_VOCABULARY,
        MSIDVocabulary,
        MappingCorpus,
        MappingStore,
    )
except ModuleNotFoundError:  # Direct execution from m050/tools.
    from m050_atom_triage import TriageError, _read_jsonl, _sha256
    from m050_msid_mapping import (
        DEFAULT_MAPPINGS,
        DEFAULT_VOCABULARY,
        MSIDVocabulary,
        MappingCorpus,
        MappingStore,
    )

try:
    from median_gate5.extraction_machine import (
        anthropic_usage_cost,
        conservative_call_ceiling,
        debit_compile_state_spend,
        extract_anthropic_structured_response,
    )
    from median_gate5.errors import ContractError
except ModuleNotFoundError:
    import sys
    sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "extraction/engine/src"))
    from median_gate5.extraction_machine import (
        anthropic_usage_cost,
        conservative_call_ceiling,
        debit_compile_state_spend,
        extract_anthropic_structured_response,
    )
    from median_gate5.errors import ContractError


STATE = Path("m050/extraction/control/M050_Compile_State_MEDIANv0_5_0.json")
DEFAULT_RECONCILIATIONS = Path(
    "m050/reconciliation/M050_Reconciled_Semantic_Units_MEDIANv0_5_0.jsonl"
)
RUNS = Path("m050/reconciliation/runs")
ANTHROPIC_ENDPOINT = "https://api.anthropic.com/v1/messages"
ANTHROPIC_VERSION = "2023-06-01"
SCHEMA_VERSION = "M050-RECONCILED-SEMANTIC-UNIT-0.1"
PACKET_SCHEMA_VERSION = "M050-RECONCILIATION-PACKET-0.1"
PROPOSAL_SCHEMA_VERSION = "M050-RECONCILIATION-PROPOSAL-0.1"
REVIEW_SCHEMA_VERSION = "M050-RECONCILIATION-REVIEW-0.1"
UNIT_STATUSES = {"reconciled", "human_required", "authorially_deferred"}
MEMBER_DISPOSITIONS = {
    "basis", "supporting", "elaboration", "superseded", "conflicting", "deferred"
}
DECISION_ORIGINS = {"provider_reviewed", "authorial"}
RECONCILIATION_LIFECYCLE = {
    "RECONCILIATION_READY": ("READY", "READY — Stage 5 reconciliation", False),
    "RECONCILIATION_ACTIVE": ("ACTIVE", "ACTIVE — Stage 5 reconciliation", True),
}
TRANSITIONS = {"prepare-spark-up", "activate-on-proceed", "prepare-stopdown"}

PROPOSER_PROMPT = """You reconcile the bounded MEDIAN v0.5.0 atom packet into semantic
propositions. Compare meanings rather than wording. Preserve material scope, conditions,
exceptions, ownership, and normative force. Merge true duplicates and compatible partial
claims; expose conflicts and supersession. A Human Rulings atom controls only the precise
question it explicitly settles. Source repetition never increases authority. Mapping metadata
routes context but does not decide truth. Do not invent rules, MSIDs, or prose outside the
packet. Every required atom must appear exactly once as a primary member. Use human_required
when the supplied evidence cannot support one grounded result. Return schema-bound JSON only.
"""

REVIEWER_PROMPT = """Independently audit a proposed MEDIAN v0.5.0 semantic reconciliation
against its complete bound packet. Reject lost nuance, invented synthesis, false equivalence,
unresolved contradiction, excessive Human Rulings weight, unsupported authority, invalid MSID
ownership, or any required atom not represented exactly once. Do not rewrite the proposal.
Return accept only when it is safe to promote unchanged; otherwise identify concise defects in
schema-bound JSON.
"""


def _text_sha256(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def _canonical_bytes(value: object) -> bytes:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")


def _atomic_write_json(path: Path, value: dict) -> None:
    mode = stat.S_IMODE(path.stat().st_mode) if path.exists() else 0o644
    descriptor, name = tempfile.mkstemp(dir=path.parent, prefix=f".{path.name}.")
    temporary = Path(name)
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8") as handle:
            json.dump(value, handle, indent=2, ensure_ascii=False)
            handle.write("\n")
            handle.flush()
            os.fsync(handle.fileno())
        os.chmod(temporary, mode)
        os.replace(temporary, path)
    except BaseException:
        temporary.unlink(missing_ok=True)
        raise


def _write_new_bytes(path: Path, content: bytes) -> None:
    """Preserve call evidence without permitting silent replacement."""
    path.parent.mkdir(parents=True, exist_ok=True)
    try:
        with path.open("xb") as handle:
            handle.write(content)
            handle.flush()
            os.fsync(handle.fileno())
    except FileExistsError as exc:
        raise TriageError(f"write-once Stage 5 evidence already exists: {path}") from exc


def _write_new_json(path: Path, value: object) -> None:
    _write_new_bytes(path, json.dumps(value, indent=2, ensure_ascii=False).encode("utf-8") + b"\n")


def _append_ledger(path: Path, event: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    events = _ledger_events(path)
    event = dict(event)
    event["previous_event_sha256"] = events[-1]["event_sha256"] if events else None
    event["event_sha256"] = hashlib.sha256(_canonical_bytes(event)).hexdigest()
    with path.open("ab") as handle:
        handle.write(_canonical_bytes(event) + b"\n")
        handle.flush()
        os.fsync(handle.fileno())


@dataclass(frozen=True)
class ReconciliationAtom:
    atom: object
    effective_claim: str
    effective_claim_sha256: str
    effective_claim_origin: str
    mapping: dict

    @property
    def key(self) -> str:
        return self.atom.key


class ReconciliationCorpus:
    """The exact, fully mapped Stage 4 output presented to Stage 5."""

    def __init__(self, repo_root: Path):
        self.repo_root = repo_root
        mapping_corpus = MappingCorpus(repo_root)
        self.vocabulary = MSIDVocabulary(repo_root)
        mapping_path = repo_root / DEFAULT_MAPPINGS
        mapping_store = MappingStore(mapping_path, mapping_corpus, self.vocabulary)
        if len(mapping_store.mappings) != len(mapping_corpus.atoms):
            raise TriageError("Stage 5 requires complete Stage 4 mapping coverage")
        self.mapping_sha256 = _sha256(mapping_path)
        self.vocabulary_sha256 = _sha256(repo_root / DEFAULT_VOCABULARY)
        self.triage_sha256 = mapping_corpus.triage_sha256
        self.rewrite_sha256 = mapping_corpus.rewrite_sha256
        self.atoms = tuple(
            ReconciliationAtom(
                item.atom,
                item.effective_claim,
                item.effective_claim_sha256,
                item.effective_claim_origin,
                mapping_store.mappings[item.key],
            )
            for item in mapping_corpus.atoms
        )
        self.by_key = {item.key: item for item in self.atoms}
        if len(self.atoms) != 5382 or len(self.by_key) != 5382:
            raise TriageError("Stage 5 input must contain exactly 5,382 unique atoms")

    def target_atoms(
        self, msid_prefix: str, *, selector: str = "subtree"
    ) -> tuple[ReconciliationAtom, ...]:
        prefix = f"{msid_prefix}."

        def intersects(mapping: dict) -> bool:
            candidates = []
            primary = mapping.get("primary_msid")
            if isinstance(primary, str):
                candidates.append(primary)
            candidates.extend(mapping.get("alternate_primary_msids", []))
            if selector == "exact":
                return any(value == msid_prefix for value in candidates)
            if selector != "subtree":
                raise TriageError("Stage 5 target selector must be exact or subtree")
            return any(value == msid_prefix or value.startswith(prefix) for value in candidates)

        return tuple(item for item in self.atoms if intersects(item.mapping))

    def context_atoms(
        self, msid_prefix: str, targets: Iterable[ReconciliationAtom], *, selector: str
    ) -> tuple[ReconciliationAtom, ...]:
        target_items = tuple(targets)
        target_keys = {item.key for item in target_items}
        target_blocks = {item.atom.block_key for item in target_items}
        ontology_basis = {
            key
            for item in target_items
            for key in item.mapping.get("ontology_basis_atom_keys", [])
        }
        prefix = f"{msid_prefix}."
        context: list[ReconciliationAtom] = []
        for item in self.atoms:
            if item.key in target_keys:
                continue
            related = item.mapping.get("related_msids", [])
            related_match = any(
                value == msid_prefix or value.startswith(prefix)
                for value in related
            )
            same_block = item.atom.block_key in target_blocks
            candidates = [item.mapping.get("primary_msid")]
            candidates.extend(item.mapping.get("alternate_primary_msids", []))
            descendant = selector == "exact" and any(
                isinstance(value, str) and value.startswith(prefix) for value in candidates
            )
            if related_match or same_block or descendant or item.key in ontology_basis:
                context.append(item)
        return tuple(context)


class ReconciliationStore:
    """One canonical Stage 5 home for reviewed semantic units."""

    def __init__(self, path: Path, corpus: ReconciliationCorpus):
        self.path = path
        self.corpus = corpus
        self.units: list[dict] = []
        self.primary_members: dict[str, str] = {}
        if path.exists():
            self._load()

    def _validate_unit(self, record: dict) -> None:
        required = {
            "schema_version", "unit_id", "unit_status", "primary_msid",
            "canonical_claim", "members", "authority_basis_atom_keys",
            "related_unit_ids", "rationale", "decision_origin", "evidence",
            "recorded_by", "recorded_at",
        }
        if set(record) != required:
            raise TriageError("Stage 5 reconciliation unit shape is invalid")
        if record.get("schema_version") != SCHEMA_VERSION:
            raise TriageError("Stage 5 reconciliation schema version is invalid")
        unit_id = record.get("unit_id")
        if not isinstance(unit_id, str) or not unit_id.startswith("reconciliation_"):
            raise TriageError("Stage 5 reconciliation unit ID is invalid")
        status = record.get("unit_status")
        if status not in UNIT_STATUSES:
            raise TriageError("Stage 5 reconciliation unit status is invalid")
        primary = record.get("primary_msid")
        claim = record.get("canonical_claim")
        if status == "reconciled":
            if not isinstance(primary, str) or self.corpus.vocabulary.classify(primary) not in {
                "settled", "candidate"
            }:
                raise TriageError("reconciled unit requires one current MSID")
            if not isinstance(claim, str) or not claim.strip() or claim != claim.strip():
                raise TriageError("reconciled unit requires a trimmed canonical claim")
        elif claim is not None:
            raise TriageError("unresolved unit cannot assert a canonical claim")
        elif primary is not None and (
            not isinstance(primary, str)
            or self.corpus.vocabulary.classify(primary) not in {"settled", "candidate", "provisional"}
        ):
            raise TriageError("unresolved unit contains an invalid optional MSID")
        members = record.get("members")
        if not isinstance(members, list) or not members:
            raise TriageError("Stage 5 reconciliation unit has no primary members")
        member_keys: list[str] = []
        for member in members:
            if not isinstance(member, dict) or set(member) != {
                "atom_key", "effective_claim_sha256", "disposition"
            }:
                raise TriageError("Stage 5 reconciliation member shape is invalid")
            item = self.corpus.by_key.get(member.get("atom_key"))
            if item is None or member.get("effective_claim_sha256") != item.effective_claim_sha256:
                raise TriageError("Stage 5 reconciliation member binding drifted")
            if member.get("disposition") not in MEMBER_DISPOSITIONS:
                raise TriageError("Stage 5 reconciliation member disposition is invalid")
            member_keys.append(item.key)
        if len(member_keys) != len(set(member_keys)):
            raise TriageError("Stage 5 reconciliation unit repeats a primary member")
        if status == "authorially_deferred" and any(
            member["disposition"] != "deferred" for member in members
        ):
            raise TriageError("authorially deferred unit must defer every member")
        basis = record.get("authority_basis_atom_keys")
        if (
            not isinstance(basis, list)
            or len(basis) != len(set(basis))
            or not set(basis) <= set(self.corpus.by_key)
        ):
            raise TriageError("Stage 5 authority basis is invalid")
        related = record.get("related_unit_ids")
        if (
            not isinstance(related, list)
            or len(related) != len(set(related))
            or any(not isinstance(value, str) or not value.startswith("reconciliation_") for value in related)
        ):
            raise TriageError("Stage 5 related units are invalid")
        if unit_id in related:
            raise TriageError("Stage 5 unit cannot relate to itself")
        rationale = record.get("rationale")
        if not isinstance(rationale, str) or not rationale.strip() or rationale != rationale.strip():
            raise TriageError("Stage 5 rationale must be nonempty and trimmed")
        origin = record.get("decision_origin")
        evidence = record.get("evidence")
        if origin not in DECISION_ORIGINS or not isinstance(evidence, dict):
            raise TriageError("Stage 5 decision origin or evidence is invalid")
        if origin == "provider_reviewed":
            if set(evidence) != {
                "packet_sha256", "proposal_response_sha256", "review_response_sha256"
            } or any(
                not isinstance(value, str) or len(value) != 64 for value in evidence.values()
            ):
                raise TriageError("provider-reviewed unit lacks three evidence hashes")
        elif set(evidence) != {"authorial_instruction_sha256"} or (
            not isinstance(evidence.get("authorial_instruction_sha256"), str)
            or len(evidence["authorial_instruction_sha256"]) != 64
        ):
            raise TriageError("authorial unit lacks its instruction hash")
        if not isinstance(record.get("recorded_by"), str) or not record["recorded_by"].strip():
            raise TriageError("Stage 5 recorder is absent")
        try:
            timestamp = datetime.fromisoformat(record.get("recorded_at", ""))
        except (TypeError, ValueError) as exc:
            raise TriageError("Stage 5 timestamp is invalid") from exc
        if timestamp.tzinfo is None:
            raise TriageError("Stage 5 timestamp lacks a timezone")

    def _load(self) -> None:
        unit_ids: set[str] = set()
        for record in _read_jsonl(self.path):
            self._validate_unit(record)
            unit_id = record["unit_id"]
            if unit_id in unit_ids:
                raise TriageError(f"duplicate Stage 5 reconciliation unit: {unit_id}")
            unit_ids.add(unit_id)
            for member in record["members"]:
                key = member["atom_key"]
                if key in self.primary_members:
                    raise TriageError(f"atom has multiple canonical Stage 5 homes: {key}")
                self.primary_members[key] = unit_id
            self.units.append(record)

    def counts(self) -> dict[str, int]:
        result = {status: 0 for status in sorted(UNIT_STATUSES)}
        for unit in self.units:
            result[unit["unit_status"]] += 1
        result.update({
            "units": len(self.units),
            "accounted_atoms": len(self.primary_members),
            "remaining_atoms": len(self.corpus.atoms) - len(self.primary_members),
            "total_atoms": len(self.corpus.atoms),
        })
        return result


def _packet_atom(item: ReconciliationAtom) -> dict:
    atom = item.atom
    mapping = item.mapping
    return {
        "atom_key": item.key,
        "atom_id": atom.atom_id,
        "source_id": atom.source_id,
        "block_key": atom.block_key,
        "section": atom.section,
        "block_type": atom.block_type,
        "effective_claim": item.effective_claim,
        "effective_claim_sha256": item.effective_claim_sha256,
        "effective_claim_origin": item.effective_claim_origin,
        "mapping_status": mapping["mapping_status"],
        "primary_msid": mapping["primary_msid"],
        "related_msids": mapping["related_msids"],
        "alternate_primary_msids": mapping["alternate_primary_msids"],
        "semantic_relation": mapping["semantic_relation"],
        "ontology_basis_atom_keys": mapping["ontology_basis_atom_keys"],
    }


def build_packet(
    corpus: ReconciliationCorpus,
    store: ReconciliationStore,
    *,
    tranche_id: str,
    msid_prefix: str,
    selector: str = "subtree",
) -> dict:
    candidates = corpus.target_atoms(msid_prefix, selector=selector)
    targets = tuple(item for item in candidates if item.key not in store.primary_members)
    if not targets:
        raise TriageError("selected Stage 5 tranche has no unaccounted target atoms")
    context = corpus.context_atoms(msid_prefix, targets, selector=selector)
    packet_items = (*targets, *context)
    sources = {
        item.atom.source_id: item.atom.source_label for item in packet_items
    }
    blocks: dict[str, dict] = {}
    for item in packet_items:
        blocks.setdefault(
            item.atom.block_key,
            {
                "block_key": item.atom.block_key,
                "source_id": item.atom.source_id,
                "section": item.atom.section,
                "block_type": item.atom.block_type,
                "source_text": item.atom.source_text,
            },
        )
    body = {
        "schema_version": PACKET_SCHEMA_VERSION,
        "packet_id": f"packet_{tranche_id}",
        "tranche_id": tranche_id,
        "semantic_boundary": {"msid_prefix": msid_prefix, "selector": selector},
        "input_bindings": {
            "mapping_sha256": corpus.mapping_sha256,
            "vocabulary_sha256": corpus.vocabulary_sha256,
            "triage_sha256": corpus.triage_sha256,
            "rewrite_sha256": corpus.rewrite_sha256,
        },
        "required_atom_keys": [item.key for item in targets],
        "sources": dict(sorted(sources.items())),
        "source_blocks": [blocks[key] for key in sorted(blocks)],
        "atoms": [_packet_atom(item) for item in targets],
        "context_atoms": [_packet_atom(item) for item in context],
    }
    body["packet_sha256"] = hashlib.sha256(_canonical_bytes(body)).hexdigest()
    return body


def proposal_response_schema() -> dict:
    """Stable provider schema; exact packet coverage is enforced after capture."""
    nullable_string = {"anyOf": [{"type": "string"}, {"type": "null"}]}
    return {
        "type": "object",
        "additionalProperties": False,
        "required": ["schema_version", "packet_id", "packet_sha256", "units"],
        "properties": {
            "schema_version": {"const": PROPOSAL_SCHEMA_VERSION},
            "packet_id": {"type": "string"},
            "packet_sha256": {"type": "string"},
            "units": {
                "type": "array", "minItems": 1,
                "items": {
                    "type": "object", "additionalProperties": False,
                    "required": [
                        "unit_local_id", "unit_status", "primary_msid", "canonical_claim",
                        "members", "authority_basis_atom_keys", "related_local_ids",
                        "rationale", "human_question",
                    ],
                    "properties": {
                        "unit_local_id": {"type": "string"},
                        "unit_status": {"enum": ["reconciled", "human_required"]},
                        "primary_msid": nullable_string,
                        "canonical_claim": nullable_string,
                        "members": {
                            "type": "array", "minItems": 1,
                            "items": {
                                "type": "object", "additionalProperties": False,
                                "required": ["atom_key", "disposition"],
                                "properties": {
                                    "atom_key": {"type": "string"},
                                    "disposition": {"enum": sorted(MEMBER_DISPOSITIONS - {"deferred"})},
                                },
                            },
                        },
                        "authority_basis_atom_keys": {
                            "type": "array", "items": {"type": "string"}
                        },
                        "related_local_ids": {
                            "type": "array", "items": {"type": "string"}
                        },
                        "rationale": {"type": "string"},
                        "human_question": nullable_string,
                    },
                },
            },
        },
    }


def review_response_schema() -> dict:
    return {
        "type": "object", "additionalProperties": False,
        "required": [
            "schema_version", "packet_id", "packet_sha256", "proposal_sha256",
            "verdict", "defects",
        ],
        "properties": {
            "schema_version": {"const": REVIEW_SCHEMA_VERSION},
            "packet_id": {"type": "string"},
            "packet_sha256": {"type": "string"},
            "proposal_sha256": {"type": "string"},
            "verdict": {"enum": ["accept", "revise", "human_required"]},
            "defects": {"type": "array", "items": {"type": "string"}},
        },
    }


def build_anthropic_request(
    *, prompt: str, schema: dict, payload: dict, model: str,
    reasoning_effort: str, maximum_output_tokens: int, cache_ttl: str,
) -> dict:
    """Build a provider request without sending it or exposing it to Codex context."""
    if not isinstance(model, str) or not model:
        raise TriageError("provider model is not configured")
    if reasoning_effort not in {"low", "medium", "high"}:
        raise TriageError("provider reasoning effort is invalid")
    if not isinstance(maximum_output_tokens, int) or maximum_output_tokens < 1:
        raise TriageError("provider maximum output tokens are not configured")
    if cache_ttl not in {"5m", "1h"}:
        raise TriageError("provider cache TTL is invalid")
    return {
        "model": model,
        "max_tokens": maximum_output_tokens,
        "thinking": {"type": "adaptive"},
        "output_config": {
            "effort": reasoning_effort,
            "format": {"type": "json_schema", "schema": schema},
        },
        "system": [{
            "type": "text", "text": prompt,
            "cache_control": {"type": "ephemeral", "ttl": cache_ttl},
        }],
        "messages": [{
            "role": "user",
            "content": json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False),
        }],
    }


def build_proposer_request(packet: dict, provider: dict) -> dict:
    return build_anthropic_request(
        prompt=PROPOSER_PROMPT,
        schema=proposal_response_schema(),
        payload=packet,
        model=provider.get("model"),
        reasoning_effort=provider.get("reasoning_effort"),
        maximum_output_tokens=provider.get("maximum_output_tokens"),
        cache_ttl=provider.get("cache_ttl"),
    )


def build_reviewer_request(packet: dict, proposal: dict, provider: dict) -> dict:
    payload = {
        "packet": packet,
        "proposal": proposal,
        "proposal_sha256": hashlib.sha256(_canonical_bytes(proposal)).hexdigest(),
    }
    return build_anthropic_request(
        prompt=REVIEWER_PROMPT,
        schema=review_response_schema(),
        payload=payload,
        model=provider.get("model"),
        reasoning_effort=provider.get("reasoning_effort"),
        maximum_output_tokens=provider.get("maximum_output_tokens"),
        cache_ttl=provider.get("cache_ttl"),
    )


def _run_paths(repo_root: Path, tranche_id: str, role: str, attempt: int) -> dict[str, Path]:
    run_dir = repo_root / RUNS / tranche_id
    stem = f"{role}_{attempt:03d}"
    return {
        "run_dir": run_dir,
        "packet": run_dir / "packet.json",
        "request": run_dir / f"{stem}_request.json",
        "raw": run_dir / f"{stem}_raw_response.json",
        "structured": run_dir / f"{stem}_structured_response.json",
        "ledger": run_dir / "run_ledger.jsonl",
    }


def _ledger_events(path: Path) -> list[dict]:
    events = _read_jsonl(path) if path.exists() else []
    previous = None
    for event in events:
        claimed = event.get("event_sha256")
        body = dict(event)
        body.pop("event_sha256", None)
        if event.get("previous_event_sha256") != previous or claimed != hashlib.sha256(
            _canonical_bytes(body)
        ).hexdigest():
            raise TriageError("Stage 5 run ledger hash chain drifted")
        previous = claimed
    return events


def _next_attempt(path: Path, role: str) -> int:
    attempts = [
        event.get("attempt") for event in _ledger_events(path)
        if event.get("role") == role and isinstance(event.get("attempt"), int)
    ]
    return max(attempts, default=0) + 1


def _latest_valid_proposal(repo_root: Path, tranche_id: str) -> tuple[dict, Path]:
    ledger = repo_root / RUNS / tranche_id / "run_ledger.jsonl"
    for event in reversed(_ledger_events(ledger)):
        if event.get("role") != "proposal" or event.get("result") != "mechanically_valid":
            continue
        relative = event.get("structured_response")
        if not isinstance(relative, str):
            continue
        path = repo_root / relative
        proposal = json.loads(path.read_text(encoding="utf-8"))
        if _sha256(path) != event.get("structured_response_sha256"):
            raise TriageError("latest proposal evidence hash drifted")
        return proposal, path
    raise TriageError("semantic review requires a mechanically valid proposal")


def _send_anthropic(request_body: dict, api_key_file: Path, timeout: float) -> tuple[int, bytes]:
    key = api_key_file.read_text(encoding="utf-8").strip()
    if not key:
        raise TriageError("Anthropic API key file is empty")
    request = urllib.request.Request(
        ANTHROPIC_ENDPOINT,
        data=_canonical_bytes(request_body),
        method="POST",
        headers={
            "content-type": "application/json",
            "anthropic-version": ANTHROPIC_VERSION,
            "x-api-key": key,
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            return response.status, response.read()
    except urllib.error.HTTPError as exc:
        return exc.code, exc.read()


def _provider_preflight(state: dict, request: dict) -> tuple[dict, object]:
    active, provider_enabled = _validate_lifecycle(state)
    if not active or not provider_enabled:
        raise TriageError("Stage 5 provider call is not active")
    provider = state["reconciliation"]["provider"]
    if provider.get("name") != "Anthropic":
        raise TriageError("installed Stage 5 adapter supports only Anthropic")
    pricing = provider.get("pricing")
    if not isinstance(pricing, dict):
        raise TriageError("Stage 5 Anthropic pricing is not configured")
    try:
        ceiling = conservative_call_ceiling(request, pricing)
    except ContractError as exc:
        raise TriageError(str(exc)) from exc
    from decimal import Decimal
    remaining = Decimal(state.get("spend", {}).get("remaining_usd", "0"))
    if ceiling > remaining:
        raise TriageError(
            f"provider call ceiling {ceiling} exceeds remaining authority {remaining}"
        )
    return provider, ceiling


def _debit_response(state: dict, raw: dict, provider: dict) -> tuple[dict, dict]:
    usage = raw.get("usage")
    if not isinstance(usage, dict):
        raise TriageError("provider response lacks billable usage")
    try:
        cost = anthropic_usage_cost(
            usage, provider["pricing"], cache_ttl=provider["cache_ttl"]
        )
        updated = debit_compile_state_spend(state, cost["total_usd"])
    except ContractError as exc:
        raise TriageError(str(exc)) from exc
    return updated, cost


def _promote_reviewed_proposal(
    store: ReconciliationStore,
    packet: dict,
    proposal: dict,
    *,
    proposal_path: Path,
    review_path: Path,
    provider: dict,
) -> None:
    local_to_global = {
        unit["unit_local_id"]: "reconciliation_" + hashlib.sha256(
            f"{packet['packet_id']}::{unit['unit_local_id']}".encode("utf-8")
        ).hexdigest()[:24]
        for unit in proposal["units"]
    }
    recorded_at = datetime.now(timezone.utc).isoformat(timespec="microseconds")
    records: list[dict] = []
    for unit in proposal["units"]:
        record = {
            "schema_version": SCHEMA_VERSION,
            "unit_id": local_to_global[unit["unit_local_id"]],
            "unit_status": unit["unit_status"],
            "primary_msid": unit["primary_msid"],
            "canonical_claim": unit["canonical_claim"],
            "members": [
                {
                    "atom_key": member["atom_key"],
                    "effective_claim_sha256": store.corpus.by_key[member["atom_key"]].effective_claim_sha256,
                    "disposition": member["disposition"],
                }
                for member in unit["members"]
            ],
            "authority_basis_atom_keys": unit["authority_basis_atom_keys"],
            "related_unit_ids": [local_to_global[value] for value in unit["related_local_ids"]],
            "rationale": unit["rationale"],
            "decision_origin": "provider_reviewed",
            "evidence": {
                "packet_sha256": packet["packet_sha256"],
                "proposal_response_sha256": _sha256(proposal_path),
                "review_response_sha256": _sha256(review_path),
            },
            "recorded_by": f"{provider['name']}:{provider['model']}",
            "recorded_at": recorded_at,
        }
        store._validate_unit(record)
        records.append(record)
    existing = [*store.units, *records]
    unit_ids: set[str] = set()
    primary_members: set[str] = set()
    for record in existing:
        store._validate_unit(record)
        if record["unit_id"] in unit_ids:
            raise TriageError("reviewed proposal repeats a canonical unit ID")
        unit_ids.add(record["unit_id"])
        for member in record["members"]:
            if member["atom_key"] in primary_members:
                raise TriageError("reviewed proposal duplicates a canonical atom home")
            primary_members.add(member["atom_key"])
    content = b"".join(_canonical_bytes(record) + b"\n" for record in existing)
    descriptor, name = tempfile.mkstemp(dir=store.path.parent, prefix=f".{store.path.name}.")
    temporary = Path(name)
    try:
        with os.fdopen(descriptor, "wb") as handle:
            handle.write(content)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, store.path)
    except BaseException:
        temporary.unlink(missing_ok=True)
        raise


def run_provider_call(
    repo_root: Path,
    state: dict,
    corpus: ReconciliationCorpus,
    store: ReconciliationStore,
    *,
    role: str,
    api_key_file: Path,
    timeout: float,
) -> tuple[dict, dict]:
    tranche_id, prefix, selector = _target(state)
    packet = build_packet(
        corpus, store, tranche_id=tranche_id, msid_prefix=prefix, selector=selector
    )
    base_dir = repo_root / RUNS / tranche_id
    ledger = base_dir / "run_ledger.jsonl"
    attempt = _next_attempt(ledger, role)
    paths = _run_paths(repo_root, tranche_id, role, attempt)
    proposal = None
    proposal_path = None
    if role == "proposal":
        provider = state["reconciliation"]["provider"]
        request = build_proposer_request(packet, provider)
    elif role == "review":
        proposal, proposal_path = _latest_valid_proposal(repo_root, tranche_id)
        validate_proposal(packet, proposal, corpus)
        provider = state["reconciliation"]["provider"]
        request = build_reviewer_request(packet, proposal, provider)
    else:
        raise TriageError("provider role must be proposal or review")
    provider, ceiling = _provider_preflight(state, request)
    if paths["packet"].exists():
        existing_packet = json.loads(paths["packet"].read_text(encoding="utf-8"))
        if existing_packet != packet:
            raise TriageError("current packet differs from preserved tranche packet")
    else:
        _write_new_json(paths["packet"], packet)
    _write_new_json(paths["request"], request)
    try:
        http_status, raw_bytes = _send_anthropic(request, api_key_file, timeout)
    except (OSError, TimeoutError, urllib.error.URLError) as exc:
        _append_ledger(paths["ledger"], {
            "event_id": f"call_{uuid.uuid4().hex}", "role": role, "attempt": attempt,
            "result": "transport_failure", "error": str(exc),
            "conservative_ceiling_usd": format(ceiling, "f"),
            "recorded_at": datetime.now(timezone.utc).isoformat(timespec="microseconds"),
        })
        raise TriageError(f"provider transport failed; cost is unresolved: {exc}") from exc
    _write_new_bytes(paths["raw"], raw_bytes)
    try:
        raw = json.loads(raw_bytes)
    except json.JSONDecodeError as exc:
        _append_ledger(paths["ledger"], {
            "event_id": f"call_{uuid.uuid4().hex}", "role": role, "attempt": attempt,
            "result": "invalid_json", "http_status": http_status,
            "request": paths["request"].relative_to(repo_root).as_posix(),
            "raw_response": paths["raw"].relative_to(repo_root).as_posix(),
            "raw_response_sha256": _sha256(paths["raw"]),
            "recorded_at": datetime.now(timezone.utc).isoformat(timespec="microseconds"),
        })
        raise TriageError("preserved provider response is not JSON") from exc
    if not isinstance(raw, dict):
        raise TriageError("preserved provider response root is not an object")
    if http_status != 200:
        cost = None
        updated_state = state
        if isinstance(raw.get("usage"), dict):
            updated_state, cost = _debit_response(state, raw, provider)
            _atomic_write_json(repo_root / STATE, updated_state)
        _append_ledger(paths["ledger"], {
            "event_id": f"call_{uuid.uuid4().hex}", "role": role, "attempt": attempt,
            "result": "http_failure", "http_status": http_status,
            "request": paths["request"].relative_to(repo_root).as_posix(),
            "raw_response": paths["raw"].relative_to(repo_root).as_posix(),
            "raw_response_sha256": _sha256(paths["raw"]), "cost": cost,
            "recorded_at": datetime.now(timezone.utc).isoformat(timespec="microseconds"),
        })
        raise TriageError(f"provider returned HTTP {http_status}; raw response is preserved")
    updated_state, cost = _debit_response(state, raw, provider)
    try:
        structured = extract_anthropic_structured_response(raw)
        if role == "proposal":
            validate_proposal(packet, structured, corpus)
            result = "mechanically_valid"
        else:
            assert proposal is not None and proposal_path is not None
            validate_review(packet, proposal, structured)
            result = f"review_{structured['verdict']}"
    except (ContractError, TriageError) as exc:
        _atomic_write_json(repo_root / STATE, updated_state)
        _append_ledger(paths["ledger"], {
            "event_id": f"call_{uuid.uuid4().hex}", "role": role, "attempt": attempt,
            "result": "mechanical_failure", "error": str(exc), "http_status": http_status,
            "request": paths["request"].relative_to(repo_root).as_posix(),
            "raw_response": paths["raw"].relative_to(repo_root).as_posix(),
            "raw_response_sha256": _sha256(paths["raw"]), "cost": cost,
            "recorded_at": datetime.now(timezone.utc).isoformat(timespec="microseconds"),
        })
        raise TriageError(f"provider response failed mechanical validation: {exc}") from exc
    _write_new_json(paths["structured"], structured)
    if role == "review" and structured["verdict"] == "accept":
        assert proposal is not None and proposal_path is not None
        _promote_reviewed_proposal(
            store, packet, proposal, proposal_path=proposal_path,
            review_path=paths["structured"], provider=provider,
        )
    _atomic_write_json(repo_root / STATE, updated_state)
    event = {
        "event_id": f"call_{uuid.uuid4().hex}", "role": role, "attempt": attempt,
        "result": result, "http_status": http_status,
        "packet_sha256": packet["packet_sha256"],
        "request": paths["request"].relative_to(repo_root).as_posix(),
        "raw_response": paths["raw"].relative_to(repo_root).as_posix(),
        "raw_response_sha256": _sha256(paths["raw"]),
        "structured_response": paths["structured"].relative_to(repo_root).as_posix(),
        "structured_response_sha256": _sha256(paths["structured"]),
        "cost": cost,
        "recorded_at": datetime.now(timezone.utc).isoformat(timespec="microseconds"),
    }
    _append_ledger(paths["ledger"], event)
    return updated_state, {
        "role": role, "attempt": attempt, "result": result,
        "cost_usd": cost["total_usd"],
        "units_promoted": len(proposal["units"])
        if role == "review" and structured["verdict"] == "accept" else 0,
    }


def validate_proposal(packet: dict, proposal: dict, corpus: ReconciliationCorpus) -> None:
    required = {"schema_version", "packet_id", "packet_sha256", "units"}
    if not isinstance(proposal, dict) or set(proposal) != required:
        raise TriageError("reconciliation proposal shape is invalid")
    if (
        proposal.get("schema_version") != PROPOSAL_SCHEMA_VERSION
        or proposal.get("packet_id") != packet.get("packet_id")
        or proposal.get("packet_sha256") != packet.get("packet_sha256")
    ):
        raise TriageError("reconciliation proposal packet binding drifted")
    units = proposal.get("units")
    if not isinstance(units, list) or not units:
        raise TriageError("reconciliation proposal contains no units")
    local_ids: set[str] = set()
    covered: list[str] = []
    for unit in units:
        if not isinstance(unit, dict) or set(unit) != {
            "unit_local_id", "unit_status", "primary_msid", "canonical_claim",
            "members", "authority_basis_atom_keys", "related_local_ids",
            "rationale", "human_question",
        }:
            raise TriageError("reconciliation proposal unit shape is invalid")
        local_id = unit.get("unit_local_id")
        if not isinstance(local_id, str) or not local_id or local_id in local_ids:
            raise TriageError("reconciliation proposal local IDs are invalid")
        local_ids.add(local_id)
        status = unit.get("unit_status")
        if status not in {"reconciled", "human_required"}:
            raise TriageError("provider proposal may only reconcile or request human review")
        primary = unit.get("primary_msid")
        claim = unit.get("canonical_claim")
        if status == "reconciled":
            if not isinstance(primary, str) or corpus.vocabulary.classify(primary) not in {
                "settled", "candidate"
            }:
                raise TriageError("provider proposal invented or selected a non-current MSID")
            if not isinstance(claim, str) or not claim.strip():
                raise TriageError("provider proposal reconciled unit lacks a claim")
            if unit.get("human_question") is not None:
                raise TriageError("reconciled proposal cannot ask a human question")
        else:
            if claim is not None or not isinstance(unit.get("human_question"), str):
                raise TriageError("human-required proposal shape is invalid")
        members = unit.get("members")
        if not isinstance(members, list) or not members:
            raise TriageError("provider proposal unit has no members")
        for member in members:
            if not isinstance(member, dict) or set(member) != {"atom_key", "disposition"}:
                raise TriageError("provider proposal member shape is invalid")
            if member.get("disposition") not in MEMBER_DISPOSITIONS - {"deferred"}:
                raise TriageError("provider proposal member disposition is invalid")
            covered.append(member.get("atom_key"))
        basis = unit.get("authority_basis_atom_keys")
        packet_keys = {
            item["atom_key"] for item in (*packet.get("atoms", []), *packet.get("context_atoms", []))
        }
        if not isinstance(basis, list) or not set(basis) <= packet_keys:
            raise TriageError("provider proposal authority basis is invalid")
        related = unit.get("related_local_ids")
        if not isinstance(related, list) or len(related) != len(set(related)):
            raise TriageError("provider proposal related local IDs are invalid")
        rationale = unit.get("rationale")
        if not isinstance(rationale, str) or not rationale.strip():
            raise TriageError("provider proposal rationale is absent")
    if any(not isinstance(key, str) for key in covered):
        raise TriageError("provider proposal contains a non-string atom key")
    required_keys = packet.get("required_atom_keys", [])
    if len(covered) != len(set(covered)) or set(covered) != set(required_keys):
        raise TriageError("provider proposal does not cover each required atom exactly once")
    for unit in units:
        if not set(unit["related_local_ids"]) <= local_ids - {unit["unit_local_id"]}:
            raise TriageError("provider proposal relates to an absent or self unit")


def validate_review(packet: dict, proposal: dict, review: dict) -> None:
    required = {
        "schema_version", "packet_id", "packet_sha256", "proposal_sha256",
        "verdict", "defects",
    }
    if not isinstance(review, dict) or set(review) != required:
        raise TriageError("reconciliation semantic review shape is invalid")
    proposal_sha = hashlib.sha256(_canonical_bytes(proposal)).hexdigest()
    if (
        review.get("schema_version") != REVIEW_SCHEMA_VERSION
        or review.get("packet_id") != packet.get("packet_id")
        or review.get("packet_sha256") != packet.get("packet_sha256")
        or review.get("proposal_sha256") != proposal_sha
    ):
        raise TriageError("reconciliation semantic review binding drifted")
    if review.get("verdict") not in {"accept", "revise", "human_required"}:
        raise TriageError("reconciliation semantic review verdict is invalid")
    defects = review.get("defects")
    if not isinstance(defects, list) or any(not isinstance(item, str) for item in defects):
        raise TriageError("reconciliation semantic review defects are invalid")
    if review["verdict"] == "accept" and defects:
        raise TriageError("accepted semantic review cannot retain defects")
    if review["verdict"] != "accept" and not defects:
        raise TriageError("non-accepted semantic review must identify a defect")


def inventory(corpus: ReconciliationCorpus, store: ReconciliationStore, state: dict) -> dict:
    mapping_counts: dict[str, int] = {}
    for item in corpus.atoms:
        status = item.mapping["mapping_status"]
        mapping_counts[status] = mapping_counts.get(status, 0) + 1
    target = state.get("reconciliation", {}).get("target", {})
    prefix = target.get("msid_prefix") if isinstance(target, dict) else None
    selector = target.get("selector", "subtree") if isinstance(target, dict) else None
    target_count = (
        len(corpus.target_atoms(prefix, selector=selector))
        if isinstance(prefix, str) and isinstance(selector, str) else 0
    )
    return {
        "input_atoms": len(corpus.atoms),
        "mapping_counts": dict(sorted(mapping_counts.items())),
        "reconciliation_counts": store.counts(),
        "target": target,
        "target_atom_count": target_count,
        "provider": state.get("reconciliation", {}).get("provider"),
    }


def _replace_dashboard_fields(state: dict, fields: dict[str, str]) -> None:
    dashboard = state.setdefault("dashboard", {})
    updated_human = dashboard.get("updated_human")
    dashboard.clear()
    dashboard.update(fields)
    if isinstance(updated_human, str):
        dashboard["updated_human"] = updated_human


def _target(state: dict) -> tuple[str, str, str]:
    target = state.get("reconciliation", {}).get("target")
    if not isinstance(target, dict):
        raise TriageError("Stage 5 target is absent")
    tranche_id = target.get("tranche_id")
    prefix = target.get("msid_prefix")
    selector = target.get("selector")
    if (
        not isinstance(tranche_id, str) or not tranche_id
        or not isinstance(prefix, str) or not prefix
        or selector not in {"exact", "subtree"}
    ):
        raise TriageError("Stage 5 target is malformed")
    return tranche_id, prefix, selector


def _dashboard(state: dict, store: ReconciliationStore, *, active: bool) -> dict[str, str]:
    tranche_id, prefix, _selector = _target(state)
    counts = store.counts()
    status = "ACTIVE — Stage 5 reconciliation" if active else "READY — Stage 5 reconciliation"
    now = (
        f"{prefix} reconciliation is active within tranche {tranche_id}"
        if active
        else f"Stage 5 is installed at the {prefix} pilot boundary; the Compile Worker is Stopped Down"
    )
    next_text = (
        "Complete and review only the released semantic tranche, then Stopdown"
        if active
        else "Spark Up may grant the bounded pilot; Proceed is still required before execution"
    )
    return {
        "status": status,
        "phase": "Semantic reconciliation — reviewed proposition unification",
        "source": f"Unitary 5,382-atom corpus — current semantic boundary {prefix}",
        "progress": f"{counts['accounted_atoms']:,} / {counts['total_atoms']:,} atoms assigned to canonical semantic units",
        "now": now,
        "next": next_text,
    }


def _validate_lifecycle(state: dict) -> tuple[bool, bool]:
    status = state.get("status")
    lifecycle = RECONCILIATION_LIFECYCLE.get(status)
    if lifecycle is None or state.get("execution_state") != status:
        raise TriageError("canonical Stage 5 lifecycle is invalid")
    reconciliation_status, dashboard_status, active = lifecycle
    if state.get("reconciliation", {}).get("status") != reconciliation_status:
        raise TriageError("Stage 5 reconciliation status disagrees with lifecycle")
    authority = state.get("authority", {})
    for key in (
        "reconciliation_authorized", "semantic_acceptance_authorized",
        "repository_writes_authorized",
    ):
        if authority.get(key) is not active:
            raise TriageError("Stage 5 authority disagrees with lifecycle")
    if authority.get("source_work_authorized") is not False:
        raise TriageError("Stage 5 cannot activate source-work authority")
    if state.get("dashboard", {}).get("status") != dashboard_status:
        raise TriageError("Stage 5 dashboard status disagrees with lifecycle")
    provider_enabled = state.get("reconciliation", {}).get("provider", {}).get("enabled") is True
    if authority.get("provider_calls_authorized") is not (active and provider_enabled):
        raise TriageError("Stage 5 provider-call authority disagrees with lifecycle and configuration")
    if state.get("spend", {}).get("active") is not (active and provider_enabled):
        raise TriageError("Stage 5 spend activation disagrees with provider-call authority")
    return active, provider_enabled


def plan_lifecycle_transition(
    state: dict,
    corpus: ReconciliationCorpus,
    store: ReconciliationStore,
    transition: str,
    *,
    expected_tranche_id: str | None = None,
) -> tuple[dict, dict]:
    if transition not in TRANSITIONS:
        raise TriageError(f"unsupported Stage 5 lifecycle transition: {transition}")
    active, _provider_enabled = _validate_lifecycle(state)
    tranche_id, prefix, selector = _target(state)
    if transition == "prepare-spark-up":
        if active:
            raise TriageError("Spark Up assessment requires Stage 5 READY")
        packet = build_packet(
            corpus, store, tranche_id=tranche_id, msid_prefix=prefix, selector=selector
        )
        return copy.deepcopy(state), {
            "transition": transition,
            "tranche_id": tranche_id,
            "msid_prefix": prefix,
            "selector": selector,
            "required_atoms": len(packet["required_atom_keys"]),
            "context_atoms": len(packet["context_atoms"]),
            "packet_sha256": packet["packet_sha256"],
        }
    if transition == "activate-on-proceed":
        if active:
            raise TriageError("Stage 5 tranche is already active")
        build_packet(
            corpus, store, tranche_id=tranche_id, msid_prefix=prefix, selector=selector
        )
        if expected_tranche_id != tranche_id:
            raise TriageError("assessed tranche no longer matches the canonical Stage 5 boundary")
        result = copy.deepcopy(state)
        result["status"] = result["execution_state"] = "RECONCILIATION_ACTIVE"
        result["reconciliation"]["status"] = "ACTIVE"
        result["authority"]["reconciliation_authorized"] = True
        result["authority"]["semantic_acceptance_authorized"] = True
        result["authority"]["repository_writes_authorized"] = True
        provider_enabled = result["reconciliation"]["provider"]["enabled"] is True
        result["authority"]["provider_calls_authorized"] = provider_enabled
        result["spend"]["active"] = provider_enabled
        _replace_dashboard_fields(result, _dashboard(result, store, active=True))
        result["next_possible_transition"] = (
            f"Finish and semantically review tranche {tranche_id}, then formal Stopdown."
        )
        return result, {"transition": transition, "tranche_id": tranche_id, "activated": True}
    if not active:
        return copy.deepcopy(state), {"transition": transition, "already_stopped": True}
    target_keys = {
        item.key for item in corpus.target_atoms(prefix, selector=selector)
    }
    missing = target_keys - set(store.primary_members)
    if missing:
        raise TriageError(
            f"formal Stopdown requires complete tranche coverage; {len(missing)} target atoms remain"
        )
    result = copy.deepcopy(state)
    result["status"] = result["execution_state"] = "RECONCILIATION_READY"
    result["reconciliation"]["status"] = "READY"
    for key in (
        "reconciliation_authorized", "semantic_acceptance_authorized",
        "repository_writes_authorized", "provider_calls_authorized"
    ):
        result["authority"][key] = False
    result["spend"]["active"] = False
    completed = result["reconciliation"].setdefault("completed_tranche_ids", [])
    if tranche_id not in completed:
        completed.append(tranche_id)
    _replace_dashboard_fields(result, _dashboard(result, store, active=False))
    result["next_possible_transition"] = (
        "Stage 5 pilot is complete; halt for Supervisor/author quality adjudication and next boundary selection."
    )
    return result, {"transition": transition, "tranche_id": tranche_id, "stopped": True}


def _require_clean_synchronized_checkpoint(repo_root: Path, expected_head: str) -> None:
    def git(*args: str) -> str:
        result = subprocess.run(
            ["git", *args], cwd=repo_root, text=True, capture_output=True, check=False
        )
        if result.returncode:
            raise TriageError(result.stderr.strip() or "Git checkpoint verification failed")
        return result.stdout.strip()

    if git("status", "--porcelain"):
        raise TriageError("repository changed since the Spark Up assessment")
    head = git("rev-parse", "HEAD")
    if head != expected_head or git("rev-parse", "origin/main") != expected_head:
        raise TriageError("repository checkpoint changed since the Spark Up assessment")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--inventory", action="store_true")
    parser.add_argument("--transition", choices=sorted(TRANSITIONS))
    parser.add_argument("--expected-tranche-id")
    parser.add_argument("--expected-head")
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--provider-role", choices=("proposal", "review"))
    parser.add_argument("--api-key-file", type=Path)
    parser.add_argument("--timeout", type=float, default=360.0)
    args = parser.parse_args(argv)
    repo_root = Path(__file__).resolve().parents[2]
    try:
        state_path = repo_root / STATE
        state = json.loads(state_path.read_text(encoding="utf-8"))
        corpus = ReconciliationCorpus(repo_root)
        store = ReconciliationStore(repo_root / DEFAULT_RECONCILIATIONS, corpus)
        if args.provider_role:
            if args.transition or args.inventory or args.apply:
                raise TriageError("provider call cannot be combined with lifecycle or inventory flags")
            if args.api_key_file is None:
                raise TriageError("provider call requires --api-key-file")
            _updated, summary = run_provider_call(
                repo_root, state, corpus, store,
                role=args.provider_role,
                api_key_file=args.api_key_file.resolve(),
                timeout=args.timeout,
            )
            print(json.dumps(summary, indent=2, ensure_ascii=False))
            return 0
        if args.inventory:
            print(json.dumps(inventory(corpus, store, state), indent=2, ensure_ascii=False))
            return 0
        if not args.transition:
            parser.error("choose --inventory or --transition")
        if args.transition == "prepare-spark-up" and args.apply:
            raise TriageError("read-only Spark Up assessment rejects --apply")
        if args.transition == "activate-on-proceed":
            if not args.apply or not args.expected_tranche_id or not args.expected_head:
                raise TriageError(
                    "Proceed activation requires --apply, --expected-tranche-id, and --expected-head"
                )
            _require_clean_synchronized_checkpoint(repo_root, args.expected_head)
        replacement, report = plan_lifecycle_transition(
            state, corpus, store, args.transition,
            expected_tranche_id=args.expected_tranche_id,
        )
        if args.apply:
            _atomic_write_json(state_path, replacement)
        print(json.dumps(report, indent=2, ensure_ascii=False))
        return 0
    except (OSError, json.JSONDecodeError, TriageError) as exc:
        print(f"Stage 5 reconciliation error: {exc}")
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
