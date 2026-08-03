from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .canonical import sha256_bytes, write_new_bytes
from .errors import ContractError


def capture_raw_bytes(path: Path, raw: bytes) -> str:
    if not raw:
        raise ContractError("raw response is empty")
    write_new_bytes(path, raw)
    return sha256_bytes(raw)


def parse_json_response(raw: bytes) -> dict[str, Any]:
    try:
        text = raw.decode("utf-8", errors="strict")
    except UnicodeDecodeError as exc:
        raise ContractError(f"response is not valid UTF-8: {exc}") from exc
    try:
        value = json.loads(text)
    except json.JSONDecodeError as exc:
        near_end = exc.pos >= max(0, len(text) - 16)
        kind = "possibly truncated" if near_end else "malformed"
        raise ContractError(f"{kind} JSON response at character {exc.pos}: {exc.msg}") from exc
    if not isinstance(value, dict):
        raise ContractError("response root must be an object")
    return value
