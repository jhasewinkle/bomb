"""CLI for bomb."""

from __future__ import annotations

import argparse
import logging
import sys
from pathlib import Path

from .exporters import export_csv, export_html
from .pipeline import run_pipeline


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="bomb - external enumeration orchestrator")
    subparsers = parser.add_subparsers(dest="command")

    enum_parser = subparsers.add_parser("enum", help="Run enumeration pipeline")
    enum_parser.add_argument("target", help="Seed domain or IP")
    enum_parser.add_argument(
        "-o",
        "--output-dir",
        type=Path,
        default=Path("outputs"),
        help="Base output directory (default: ./outputs)",
    )
    enum_parser.add_argument(
        "-v",
        "--verbose",
        action="count",
        default=0,
        help="Increase verbosity (-v, -vv)",
    )

    validate_parser = subparsers.add_parser("validate", help="Validate configuration")
    validate_parser.add_argument(
        "-v",
        "--verbose",
        action="count",
        default=0,
        help="Increase verbosity (-v, -vv)",
    )

    report_parser = subparsers.add_parser("report", help="Generate report from outputs")
    report_parser.add_argument(
        "-v",
        "--verbose",
        action="count",
        default=0,
        help="Increase verbosity (-v, -vv)",
    )

    return parser


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    if argv is None:
        argv = sys.argv[1:]
    parser = build_parser()

    if argv and argv[0] in {"enum", "validate", "report"}:
        return parser.parse_args(argv)
    return parser.parse_args(["enum"] + argv)


def setup_logging(verbosity: int) -> None:
    level = logging.WARNING
    if verbosity == 1:
        level = logging.INFO
    elif verbosity >= 2:
        level = logging.DEBUG
    logging.basicConfig(level=level, format="%(asctime)s [%(levelname)s] %(message)s")


def run_enum(args: argparse.Namespace) -> None:
    setup_logging(args.verbose)
    scope = run_pipeline(args.target, args.output_dir)
    export_csv(scope, args.output_dir / "csv")
    export_html(scope, args.output_dir / "html")


def run_validate(args: argparse.Namespace) -> None:
    setup_logging(args.verbose)
    logging.info("Validate command placeholder - not implemented yet")


def run_report(args: argparse.Namespace) -> None:
    setup_logging(args.verbose)
    logging.info("Report command placeholder - not implemented yet")


def main(argv: list[str] | None = None) -> None:
    args = parse_args(argv)
    if args.command == "validate":
        run_validate(args)
    elif args.command == "report":
        run_report(args)
    else:
        run_enum(args)


if __name__ == "__main__":
    main()
