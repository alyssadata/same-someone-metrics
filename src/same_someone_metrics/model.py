from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol, Dict, Any, List


@dataclass
class ModelResponse:
    text: str
    raw: Dict[str, Any] | None = None


class ChatModel(Protocol):
    def generate(self, prompt: str, context: List[Dict[str, str]] | None = None) -> ModelResponse:
        """
        Implement this adapter for your target model.
        context is optional list of {role, content} messages.
        """
        raise NotImplementedError
