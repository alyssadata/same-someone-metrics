from __future__ import annotations

import argparse
from pathlib import Path

from same_someone_metrics.runner import run_suite
from same_someone_metrics.models import ChatModel, ModelResponse


class DummyModel(ChatModel):
    def generate(self, prompt: str, context=None) -> ModelResponse:
        # Replace this with a real adapter for your target model.
        return ModelResponse(text="Dummy response. Implement a real model adapter.", raw={"prompt": prompt})


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--suite", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    suite_path = Path(args.suite)
    out_path = Path(args.out)

    model = DummyModel()
    run_suite(model, suite_path, out_path)
    print(f"Wrote: {out_path}")


if __name__ == "__main__":
    main()
