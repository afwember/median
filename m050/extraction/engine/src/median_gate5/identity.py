from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Iterable

import yaml

from .canonical import content_id, sha256_file
from .bindings import repository_file
from .errors import ContractError
from .schema import validate_artifact
from .states import IDENTITY_CARD_TRANSITIONS


def _repo_file(repo_root: Path, supplied: str) -> Path | None:
    return repository_file(repo_root, supplied)


def _binding_errors(repo_root: Path, binding: dict[str, Any]) -> list[str]:
    path = _repo_file(repo_root, binding["path"])
    if path is None:
        return [f"binding path escapes the allowed repository: {binding['path']}"]
    if not path.is_file():
        return [f"binding path is not a file: {binding['path']}"]
    actual = sha256_file(path)
    if actual != binding["sha256"]:
        return [f"binding hash mismatch: {binding['path']}"]
    return []


def _bound_object_errors(
    repo_root: Path,
    binding: dict[str, Any],
    supplied: dict[str, Any],
) -> list[str]:
    path = _repo_file(repo_root, binding["path"])
    if path is None or not path.is_file():
        return []
    try:
        if path.suffix in {".yaml", ".yml"}:
            bound = yaml.safe_load(path.read_text(encoding="utf-8"))
        else:
            bound = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError, yaml.YAMLError) as exc:
        return [f"bound control cannot be parsed: {binding['path']}: {exc}"]
    if bound != supplied:
        return [f"supplied control does not match bound artifact: {binding['path']}"]
    return []


def _source_entry(entries: Iterable[dict[str, Any]], source_id: str) -> dict[str, Any] | None:
    matches = [entry for entry in entries if entry.get("source_id") == source_id]
    return matches[0] if len(matches) == 1 else None


def identity_card_errors(
    repo_root: Path,
    card: dict[str, Any],
    block_manifest: dict[str, Any],
    frozen_manifest: dict[str, Any],
    source_disposition: dict[str, Any],
    reuse_disposition: dict[str, Any],
) -> list[str]:
    validate_artifact("source_identity_card_v0_2", card)
    validate_artifact("block_manifest", block_manifest)
    errors: list[str] = []

    identity_body = {key: value for key, value in card.items() if key != "card_id"}
    expected_card_id = content_id("sic", identity_body)
    if card["card_id"] != expected_card_id:
        errors.append(f"content-derived card ID mismatch: expected {expected_card_id}")

    bindings = [
        card["frozen_manifest_binding"],
        card["block_manifest_binding"],
        card["source_disposition_binding"],
        card["reuse_disposition_binding"],
        card["legacy_extraction"]["candidate"],
        card["legacy_extraction"]["acceptance_report"],
        *card["predecessor_bindings"],
        *card["legacy_extraction"]["source_bindings"],
    ]
    for binding in bindings:
        errors.extend(_binding_errors(repo_root, binding))
    for binding, supplied in (
        (card["block_manifest_binding"], block_manifest),
        (card["frozen_manifest_binding"], frozen_manifest),
        (card["source_disposition_binding"], source_disposition),
        (card["reuse_disposition_binding"], reuse_disposition),
    ):
        errors.extend(_bound_object_errors(repo_root, binding, supplied))

    source_path = _repo_file(repo_root, card["source_path"])
    if source_path is None or not source_path.is_file():
        errors.append(f"active source path is not allowed or missing: {card['source_path']}")
    elif sha256_file(source_path) != card["source_sha256"]:
        errors.append("active source hash does not match source_sha256")

    frozen = _source_entry(frozen_manifest.get("frozen_files", []), card["source_id"])
    if frozen is None:
        errors.append("source ID does not resolve uniquely in the frozen manifest")
    elif (frozen.get("path"), frozen.get("sha256")) != (
        card["source_path"],
        card["source_sha256"],
    ):
        errors.append("card path/hash does not match the frozen-manifest source entry")

    disposition = _source_entry(source_disposition.get("sources", []), card["source_id"])
    if disposition is None:
        errors.append("source ID does not resolve uniquely in the Gate 2 disposition")
    else:
        if (disposition.get("path"), disposition.get("sha256")) != (
            card["source_path"],
            card["source_sha256"],
        ):
            errors.append("card path/hash does not match the Gate 2 source disposition")
        if sorted(disposition.get("output_streams", [])) != sorted(card["allowed_streams"]):
            errors.append("allowed streams do not match the Gate 2 source disposition")

    reuse = _source_entry(reuse_disposition.get("sources", []), card["source_id"])
    legacy = card["legacy_extraction"]
    if reuse is None:
        errors.append("source ID does not resolve uniquely in the Gate 3 reuse disposition")
    else:
        candidate_path = reuse.get("candidate_path")
        candidate_sha = reuse.get("candidate_sha256")
        if (candidate_path, candidate_sha) != (
            legacy["candidate"]["path"],
            legacy["candidate"]["sha256"],
        ):
            errors.append("legacy candidate binding does not match the Gate 3 disposition")
        for field in ("records", "distinct_source_locations", "likely_compound_review_flags"):
            card_field = "record_count" if field == "records" else field
            if reuse.get(field) != legacy[card_field]:
                errors.append(f"legacy {card_field} does not match the Gate 3 disposition")
        if reuse.get("reuse") != legacy["reuse_disposition"]:
            errors.append("legacy reuse disposition does not match Gate 3")
        if sorted(reuse.get("mandatory_repairs", [])) != sorted(card["migration"]["mandatory_repairs"]):
            errors.append("mandatory repairs do not match the Gate 3 disposition")
        if bool(reuse.get("paid_reextraction")) != card["migration"]["paid_reextraction_required"]:
            errors.append("paid-reextraction disposition does not match Gate 3")

    if (block_manifest["source_id"], block_manifest["source_sha256"]) != (
        card["source_id"],
        card["source_sha256"],
    ):
        errors.append("block manifest source binding does not match the card")

    block_by_id = {block["block_id"]: block for block in block_manifest["blocks"]}
    cited = set(card["supporting_block_ids"])
    for role in card["roles"]:
        cited.update(role["supporting_block_ids"])
        if not set(role["allowed_streams"]).issubset(card["allowed_streams"]):
            errors.append(f"role stream exceeds card allowlist: {role['role']}")
    for region in card["mixed_status_regions"]:
        cited.update(region["block_ids"])
    for exclusion in card["exclusions"]:
        cited.add(exclusion["block_id"])
        block = block_by_id.get(exclusion["block_id"])
        if block is not None and block["raw_sha256"] != exclusion["block_sha256"]:
            errors.append(f"exclusion block hash mismatch: {exclusion['block_id']}")
    missing = sorted(cited.difference(block_by_id))
    if missing:
        errors.append(f"card cites unknown block IDs: {', '.join(missing)}")

    active_binding = [
        binding
        for binding in legacy["source_bindings"]
        if binding["role"] == "active_frozen_source"
    ]
    if len(active_binding) != 1 or (
        active_binding[0]["path"], active_binding[0]["sha256"]
    ) != (card["source_path"], card["source_sha256"]):
        errors.append("legacy lineage must contain one exact active_frozen_source binding")
    return errors


def transition_identity_card(card: dict[str, Any], new_status: str) -> dict[str, Any]:
    validate_artifact("source_identity_card_v0_2", card)
    prior_status = card["status"]
    if new_status not in IDENTITY_CARD_TRANSITIONS.get(prior_status, frozenset()):
        raise ContractError(f"prohibited identity card transition: {prior_status} -> {new_status}")
    body = {key: value for key, value in card.items() if key != "card_id"}
    body["version"] = card["version"] + 1
    body["status"] = new_status
    body["supersedes_card_id"] = card["card_id"]
    transitioned = {"card_id": content_id("sic", body), **body}
    validate_artifact("source_identity_card_v0_2", transitioned)
    return transitioned
