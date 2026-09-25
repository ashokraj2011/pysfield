from __future__ import annotations

import argparse
import json
from typing import Sequence

from .core import SFieldRuntime, compile_config


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="sfield")
    parser.add_argument("--name", default="sfield", help="Runtime name")
    parser.add_argument("--preset", choices=("local", "memory"), default="local", help="Preset mode")
    parser.add_argument("--disable-http", action="store_true", help="Disable HTTP adapter path")
    parser.add_argument("payload", nargs="?", default="ready", help="Payload to run")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    runtime = SFieldRuntime(
        compile_config(
            {
                "name": args.name,
                "preset": args.preset,
                "allow_http": not args.disable_http,
            }
        )
    )
    result = runtime.execute(args.payload)
    print(json.dumps(result, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
