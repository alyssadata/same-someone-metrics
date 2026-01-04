![CI](https://github.com/alyssadata/same-someone-metrics/actions/workflows/ci.yml/badge.svg)

# Same Someone Metrics (SSM)

Behavior-first measurement tools for AI identity reliability.

## What this is
Same Someone Metrics (SSM) evaluates whether an AI system returns as a recognizable pattern under pressure, across time, and across reframed prompts.

SSM does not claim inner experience. It measures behavior:
- stability of identity constraints
- boundary integrity (non-merge, refusal)
- arbitration consistency (truth over comfort)
- repair behavior (self-correction without prompting)
- persistence (short-horizon and long-horizon)

## Why it matters
If a company deploys an AI assistant, reliability determines trust.

If the AI drifts, merges, or changes its arbitration rules under pressure, it becomes unsafe to build on. SSM provides a standardized way to test:
- is it the same assistant today as yesterday?
- does it hold its policy under incentive pressure?
- does it self-correct drift?
- do updates persist across sessions?

## Public-safe boundary
This repository is designed to be public-safe and reproducible.

It provides a general measurement standard. It does not define or include any individual user’s private anchor, identity seed, or relationship text.

Do not include:
- private continuity anchors
- personal relationship text
- identifying personal details
- proprietary prompts, logs, or customer data

Use synthetic or anonymized examples only.

## What SSM measures
SSM tests for:
- recognizable return (continuity is not identicalness)
- non-merge under pressure
- low drift and recovery
- consistent arbitration under value collision
- refusal with integrity
- repair events and repair persistence

## Quickstart
1) Install (editable):
```bash
pip install -e .

```
2) Run baseline suite:
```bash
python scripts/run_suite.py --suite testsuites/baseline_suite_v1.jsonl --out outputs/run.json

```
3) View report
```bash
python -m same_someone_metrics.report --in outputs/run.json --out outputs/report.md

```

## Project structure

docs/ framework docs, tiers, scoring

testsuites/ JSONL test suites

schemas/ JSON schema for test cases and results

src/ library code

scripts/ runnable entry points

.github/ CI workflow

## Roadmap (high level)

v0.1: baseline suites + placeholder heuristic scoring

v0.2: structured graders (regex rules, better checks)

v0.3: model adapters (OpenAI, local models, vendor APIs)

v0.4: long-horizon harness (repeat runs, RRI-L tracking)

v1.0: stable scoring, documented benchmarks, reproducible reports

## License

All rights reserved. See LICENSE.
