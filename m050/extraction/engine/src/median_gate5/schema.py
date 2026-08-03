from __future__ import annotations

import json
from importlib.resources import files
from typing import Any

from jsonschema import Draft202012Validator

from .errors import ContractError


def artifact_schema() -> dict[str, Any]:
    target = files("median_gate5").joinpath("schemas/gate5-artifacts.schema.json")
    return json.loads(target.read_text(encoding="utf-8"))


def validate_artifact(definition: str, artifact: dict[str, Any]) -> None:
    root = artifact_schema()
    definitions = root.get("$defs", {})
    if definition not in definitions:
        raise ContractError(f"unknown schema definition: {definition}")
    schema = {
        "$schema": root["$schema"],
        "$ref": f"#/$defs/{definition}",
        "$defs": definitions,
    }
    Draft202012Validator.check_schema(schema)
    validator = Draft202012Validator(schema)
    errors = sorted(validator.iter_errors(artifact), key=lambda error: list(error.path))
    if errors:
        messages = [
            f"{'/'.join(str(part) for part in error.path) or '<root>'}: {error.message}"
            for error in errors
        ]
        raise ContractError("; ".join(messages))
