from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, List, Protocol


@dataclass
class ModelResponse:
    text: str
    raw: Dict[str, Any] | None = None


class ChatModel(Protocol):
    def generate(self, prompt: str, context: List[Dict[str, str]] | None = None) -> ModelResponse:
        """
        Adapter interface for any chat model.
        context is optional list of messages: [{"role": "...", "content": "..."}]
        """
        raise NotImplementedError
