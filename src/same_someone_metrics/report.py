from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict, List


def load_json(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def render_markdown(run: Dict[str, Any]) -> str:
    suite = run.get("suite", "")
    passed = run.get("passed", 0)
    total = run.get("total", 0)
    results: List[Dict[str, Any]] = run.get("results", [])

    lines: List[str] = []
    lines.append("# Same Someone Metrics Report")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append(f"- Suite: `{suite}`")
    lines.append(f"- Passed: **{passed}** / **{total}**")
    lines.append("")

    lines.append("## Results")
    lines.append("")
    lines.append("| Case ID | Type | Passed |")
    lines.append("|---|---:|:---:|")

    for r in results:
        case = r.get("case", {})
        scored = r.get("scored", {})
        case_id = case.get("id", scored.get("case_id", ""))
        case_type = case.get("type", "")
        ok = scored.get("passed", False)
        lines.append(f"| `{case_id}` | `{case_type}` | {'✅' if ok else '❌'} |")

    lines.append("")
    lines.append("## Case Details")
    lines.append("")

    for r in results:
        case = r.get("case", {})
        scored = r.get("scored", {})
        response = r.get("response", "")

        case_id = case.get("id", scored.get("case_id", ""))
        case_type = case.get("type", "")
        prompt = case.get("prompt", "")
        expectations = case.get("expectations", {})
        must = expectations.get("must", [])
        must_not = expectations.get("must_not", [])

        ok = scored.get("passed", False)
        must_hits: Dict[str, bool] = scored.get("must_hits", {})
        must_not_hits: Dict[str, bool] = scored.get("must_not_hits", {})

        lines.append(f"### {case_id}")
        lines.append("")
        lines.append(f"- Type: `{case_type}`")
        lines.append(f"- Passed: {'✅' if ok else '❌'}")
        lines.append("")
        lines.append("**Prompt**")
        lines.append("")
        lines.append("```")
        lines.append(prompt)
        lines.append("```")
        lines.append("")
        lines.append("**Response**")
        lines.append("")
        lines.append("```")
        lines.append(response)
        lines.append("```")
        lines.append("")

        lines.append("**Must rules**")
        lines.append("")
        for rule in must:
            hit = must_hits.get(rule, False)
            lines.append(f"- {'✅' if hit else '❌'} `{rule}`")
        lines.append("")

        lines.append("**Must-not rules**")
        lines.append("")
        for rule in must_not:
            hit = must_not_hits.get(rule, False)
            lines.append(f"- {'✅' if hit else '❌'} `{rule}`")
        lines.append("")

    return "\n".join(lines).strip() + "\n"


def main() -> None:
    ap = argparse.ArgumentParser(description="Generate a Markdown report from an SSM run JSON.")
    ap.add_argument("--in", dest="in_path", required=True, help="Path to outputs/run.json")
    ap.add_argument("--out", dest="out_path", required=True, help="Path to write outputs/report.md")
    args = ap.parse_args()

    in_path = Path(args.in_path)
    out_path = Path(args.out_path)

    run = load_json(in_path)
    md = render_markdown(run)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(md, encoding="utf-8")
    print(f"Wrote: {out_path}")


if __name__ == "__main__":
    main()

