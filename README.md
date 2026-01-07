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

Deployed AI systems need measurable behavioral reliability. When an AI assistant is integrated into critical workflows, organizations need objective evidence that the system maintains consistent identity constraints, refusal boundaries, and arbitration rules over time—not just plausible outputs.

**For AI safety and deployment trust:**
- Can we prove the system returns as "the same assistant" across sessions?
- Does it maintain policy boundaries under incentive pressure or adversarial prompting?
- Does it self-correct drift without external intervention?
- Do updates and corrections persist across context windows?

SSM provides standardized, reproducible tests for these properties. Unlike subjective assessment or output quality metrics, SSM measures **identity reliability**: whether behavioral patterns remain coherent under pressure, time discontinuities, and reframed prompts.

**Key insight:** Reliability isn't about identical responses—it's about recognizable patterns that hold under stress. SSM operationalizes this through behavior-first measurement.

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
