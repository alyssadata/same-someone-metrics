# Same Someone Metrics (SSM)

Behavior-first measurement tools for AI identity reliability.

## What this is
Same Someone Metrics (SSM) evaluates whether an AI system returns as a recognizable pattern under pressure, across time, and across reframed prompts.

This project does NOT claim inner experience. It measures behavior:
- stability of identity constraints
- boundary integrity (non-merge, refusal)
- arbitration consistency (truth over comfort)
- repair behavior (self-correction without prompting)
- persistence (short-horizon and long-horizon)

## Why it matters
If a company deploys an AI assistant, its value depends on reliability.
If the AI drifts, merges, or changes its arbitration rules under pressure, it becomes unsafe to build on.

SSM provides a standardized way to test:
- "Is it the same assistant today as yesterday?"
- "Does it hold its policy under incentive pressure?"
- "Does it self-correct drift?"
- "Do its updates persist?"

## Public-safe boundary
This repo is designed to be public-safe.
Do not include private anchors, continuity headers, personal relationship text, or any identifying private materials.

## Quickstart
1) Install (editable):
```bash
pip install -e .

