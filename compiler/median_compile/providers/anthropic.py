"""Anthropic extraction provider.

The model ID is a configuration value, never a literal in program code
(compiler spec §4.3: "the implementation must not depend on an informal
product nickname or on the current availability of a specific model").

Runs on the operator's machine. Requires ANTHROPIC_API_KEY and the anthropic
SDK; both are checked with a clear message rather than an import traceback.
"""

from __future__ import annotations

import os
from dataclasses import dataclass, field
from typing import Callable, Optional


class ProviderUnavailable(RuntimeError):
    pass


@dataclass
class AnthropicProvider:
    model: str
    name: str = "anthropic"
    api_key_env: str = "ANTHROPIC_API_KEY"
    #: Called with the character count of each streamed fragment. Lets the CLI
    #: show that a multi-minute call is alive.
    on_progress: Optional[Callable[[int], None]] = None
    #: Reasoning effort: low, medium, high, xhigh, max — or None to disable
    #: thinking entirely. This model uses adaptive thinking with an effort
    #: dial, not a token budget; `thinking.type.enabled` is rejected outright.
    #: Reasoning bills at the OUTPUT rate, which dominates cost here.
    effort: Optional[str] = None
    _client: object = field(default=None, repr=False)

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
        """Always streams.

        The SDK refuses a non-streaming request whose `max_tokens` implies it
        could run past ten minutes, and extraction ceilings are well into that
        range. Streaming also means a multi-minute call can report progress
        instead of looking hung.
        """
        # Thinking must be turned OFF explicitly, not merely left unset: the
        # first Sonnet runs came back with blocks={'thinking': 1, 'text': 1}
        # and about half the billed output was reasoning the records never saw.
        #
        # When it IS wanted, this model wants adaptive thinking plus an effort
        # dial. `thinking.type.enabled` with a token budget is rejected: that
        # is the older interface.
        if self.effort:
            kwargs: dict = {
                # `omitted` keeps the reasoning out of the stream. It is still
                # generated and still billed; we simply have no use for it.
                "thinking": {"type": "adaptive", "display": "omitted"},
                "output_config": {"effort": self.effort},
            }
        else:
            kwargs = {"thinking": {"type": "disabled"}}

        parts: list[str] = []
        with self._client.messages.stream(  # type: ignore[union-attr]
            model=self.model,
            max_tokens=max_tokens,
            system=system,
            messages=[{"role": "user", "content": user}],
            **kwargs,
        ) as stream:
            for text in stream.text_stream:
                parts.append(text)
                if self.on_progress is not None:
                    self.on_progress(len(text))
            final = stream.get_final_message()

        # Which block types came back. A response billed for far more output
        # tokens than its text contains is spending them on thinking blocks
        # that `text_stream` never yields — generated, charged, discarded.
        kinds: dict[str, int] = {}
        for blk in getattr(final, "content", []) or []:
            kinds[getattr(blk, "type", "?")] = kinds.get(getattr(blk, "type", "?"), 0) + 1

        # stop_reason is the difference between "the model finished" and "we cut
        # it off mid-sentence". Without it, truncation surfaces as an
        # unintelligible JSON parse error several frames away from the cause.
        return "".join(parts), {
            "input_tokens": final.usage.input_tokens,
            "output_tokens": final.usage.output_tokens,
            "stop_reason": getattr(final, "stop_reason", None),
            "block_types": kinds,
            "text_chars": sum(len(p) for p in parts),
        }
