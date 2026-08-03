from __future__ import annotations

import hashlib
import math
from typing import Any


def select_tier3_sample(
    chunks: list[dict[str, Any]], *, seed: str, rate: float = 0.05
) -> list[int]:
    if not chunks:
        return []
    if not 0 < rate <= 1:
        raise ValueError("sample rate must be in (0, 1]")
    target = min(len(chunks), max(min(3, len(chunks)), math.ceil(len(chunks) * rate)))
    selected: set[int] = set()
    dense = max(chunks, key=lambda item: (item.get("claim_bearing_blocks", 0), -item["ordinal"]))
    risky = max(chunks, key=lambda item: (item.get("review_risk", 0), -item["ordinal"]))
    selected.update({dense["ordinal"], risky["ordinal"]})
    ranked = sorted(
        chunks,
        key=lambda item: hashlib.sha256(f"{seed}:{item['ordinal']}".encode()).hexdigest(),
    )
    for chunk in ranked:
        if len(selected) >= target:
            break
        selected.add(chunk["ordinal"])
    return sorted(selected)
