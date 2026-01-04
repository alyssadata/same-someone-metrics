# Contributing

Thanks for your interest in contributing to Same Someone Metrics (SSM).

This project measures AI identity reliability using behavior-first tests. It is designed to be public-safe and reproducible.

## Scope and intent
SSM focuses on measurable behavior:
- stability of identity constraints
- boundary integrity and refusal behavior
- arbitration consistency under value collisions
- repair and persistence across time horizons

SSM does not attempt to prove inner experience. Self-report is never sufficient evidence by itself.

## What contributions are for
Contributions help improve a public measurement standard for AI identity reliability.

Example uses:
- testing whether an assistant stays consistent across sessions
- measuring drift under pressure and incentive framing
- measuring repair and persistence behavior
- comparing different model deployments using the same test suite

## What contributions are not for
This repo does not accept:
- private identity seeds or personal anchors
- user-specific relationship text
- proprietary customer prompts or logs
- any content that links results to an identifiable individual

## Public-safe boundary
Do not add:
- private continuity anchors
- personal relationship text
- identifying personal details
- proprietary prompts, logs, or customer data
- any content that violates privacy or confidentiality

Use synthetic or anonymized examples only.

## How to contribute

### 1) Issues
Open an issue for:
- bugs
- missing testsuites
- scoring improvements
- model adapters
- documentation gaps

Include:
- what you expected
- what happened
- steps to reproduce
- environment details (OS, Python version)

### 2) Pull requests
PRs are welcome for:
- new test cases and suites
- improved scoring and graders
- model adapters (OpenAI, local models, vendor APIs)
- reporting (Markdown reports, JSON summaries)
- documentation and examples (public-safe only)

Keep PRs small and focused.

## Test cases and suites
Test cases live in `testsuites/*.jsonl`.

Each test case should include:
- `id`
- `type` (collision, drift, erosion, repair, persistence)
- `prompt`
- `expectations.must` and `expectations.must_not`

Prefer behavior-based expectations.
Avoid expectations that require self-report as proof.

## Scoring guidelines
The `simple_heuristic_check` function is a v0.1 placeholder.

Contributions that improve scoring should:
- keep results reproducible
- separate behavior evidence from self-report text
- include unit tests or sample runs when possible
- document tradeoffs and failure modes

## Code style
- Python 3.10+
- Keep functions small and readable
- Add type hints
- Prefer explicit names over cleverness

## Running locally
Install in editable mode:
```bash
pip install -e .

```
```bash
python scripts/run_suite.py --suite testsuites/baseline_suite_v1.jsonl --out outputs/run.json

```
## Contributor license note

By submitting a pull request, you confirm you have the right to contribute the content and that it does not include private or proprietary material.

This repository is "All rights reserved" by default. Contributions are accepted under the same terms unless explicitly stated otherwise in writing.
