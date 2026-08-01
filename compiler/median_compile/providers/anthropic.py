"""Anthropic extraction provider.

The model ID is a configuration value, never a literal in program code
(compiler spec §4.3: "the implementation must not depend on an informal
product nickname or on the current availability of a specific model").

Runs on the operator's machine. Requires ANTHROPIC_API_KEY and the anthropic
SDK; both are checked with a clear message rather than an import traceback.
"""

from __future__ import annotations

import os
from dataclasses import dataclass


class ProviderUnavailable(RuntimeError):
    pass


@dataclass
class AnthropicProvider:
    model: str
    name: str = "anthropic"
    api_key_env: str = "ANTHROPIC_API_KEY"
    _client: object | None = None

    def __post_init__(self) -> None:
        key = os.environ.get(self.api_key_env)
        if not key:
            raise ProviderUnavailable(
                f"{self.api_key_env} is not set. Extraction makes real API calls and "
                "must run where that key is available."
            )
        try:
            import anthropic  # noqa: PLC0415
        except ImportError as exc:
            raise ProviderUnavailable(
                "the anthropic SDK is not installed — `pip install anthropic`"
            ) from exc
        self._client = anthropic.Anthropic(api_key=key)

    def complete(self, system: str, user: str, max_tokens: int) -> tuple[str, dict]:
        resp = self._client.messages.create(  # type: ignore[union-attr]
            model=self.model,
            max_tokens=max_tokens,
            system=system,
            messages=[{"role": "user", "content": user}],
        )
        text = "".join(
            block.text for block in resp.content if getattr(block, "type", "") == "text"
        )
        return text, {
            "input_tokens": resp.usage.input_tokens,
            "output_tokens": resp.usage.output_tokens,
        }
