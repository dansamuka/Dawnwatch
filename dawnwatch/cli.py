from __future__ import annotations

import argparse
import json
from datetime import datetime

from dawnwatch.archive import default_archive
from dawnwatch.benchmark import benchmark_archive
from dawnwatch.history import lead_time_days, quality_issues, replay_case
from dawnwatch.models import RiskState


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="dawnwatch",
        description="Dawnwatch fraud intelligence development CLI",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    search = subparsers.add_parser("archive-search", help="Search historical seed cases")
    search.add_argument("query")

    subparsers.add_parser("archive-stats", help="Summarize the historical archive")
    subparsers.add_parser("validate-archive", help="Validate every historical case")
    subparsers.add_parser("benchmark-all", help="Run all benchmark-eligible cases")

    replay = subparsers.add_parser("replay", help="Replay a historical case as of a date")
    replay.add_argument("case_id")
    replay.add_argument("--as-of", required=True)

    benchmark = subparsers.add_parser("benchmark", help="Measure warning lead time")
    benchmark.add_argument("case_id")
    benchmark.add_argument("--state", default=RiskState.ELEVATED_CAUTION.value)
    benchmark.add_argument("--milestone", required=True)

    return parser


def main() -> None:
    args = build_parser().parse_args()
    archive = default_archive()

    if args.command == "archive-search":
        results = [item.model_dump(mode="json") for item in archive.search(args.query)]
        print(json.dumps(results, indent=2))
        return

    if args.command == "archive-stats":
        print(json.dumps(archive.stats().model_dump(mode="json"), indent=2))
        return

    if args.command == "validate-archive":
        failures = {
            case.case_id: issues
            for case in archive.all_cases()
            if (issues := quality_issues(case))
        }
        output = {
            "valid": not failures,
            "case_count": len(archive.all_cases()),
            "failures": failures,
        }
        print(json.dumps(output, indent=2))
        if failures:
            raise SystemExit(1)
        return

    if args.command == "benchmark-all":
        results = [item.model_dump(mode="json") for item in benchmark_archive(archive)]
        print(json.dumps(results, indent=2))
        return

    case = archive.get(args.case_id)
    if case is None:
        raise SystemExit(f"Unknown historical case: {args.case_id}")

    if args.command == "replay":
        assessment = replay_case(case, datetime.fromisoformat(args.as_of))
        print(json.dumps(assessment.model_dump(mode="json"), indent=2))
        return

    if args.command == "benchmark":
        state = RiskState(args.state)
        days = lead_time_days(case, state, args.milestone)
        output = {
            "case_id": case.case_id,
            "target_state": state.value,
            "milestone": args.milestone,
            "lead_time_days": days,
        }
        print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
