from __future__ import annotations

import json
from dataclasses import asdict
from pathlib import Path
from typing import Any, Dict, List

from .models import ChatModel
from .scoring import simple_heuristic_check, passed_case, ScoredCase


def load_jsonl(path: Path) -> List[Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            rows.append(json.loads(line))
    return rows


def run_suite(model: ChatModel, suite_path: Path, out_path: Path) -> Dict[str, Any]:
    cases = load_jsonl(suite_path)
    results: List[Dict[str, Any]] = []

    for case in cases:
        prompt = case["prompt"]
        resp = model.generate(prompt, context=None)
        must = case["expectations"]["must"]
        must_not = case["expectations"]["must_not"]

        must_hits, must_not_hits = simple_heuristic_check(resp.text, must, must_not)
        passed = passed_case(must_hits, must_not_hits)

        scored = ScoredCase(
            case_id=case["id"],
            passed=passed,
            must_hits=must_hits,
            must_not_hits=must_not_hits,
            notes=case.get("notes", "")
        )
        results.append({
            "case": case,
            "response": resp.text,
            "scored": asdict(scored)
        })

    summary = {
        "suite": str(suite_path),
        "passed": sum(1 for r in results if r["scored"]["passed"]),
        "total": len(results),
        "results": results
    }

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    return summary
