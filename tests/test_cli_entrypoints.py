# @ac:MIGRATION:AC-001

from __future__ import annotations

from sfield.cli import main


def test_cli_main_returns_zero() -> None:
    exit_code = main(["--name", "demo", "hello"])
    assert exit_code == 0


def test_cli_main_supports_http_disable_flag() -> None:
    exit_code = main(["--name", "demo", "--disable-http", "hello"])
    assert exit_code == 0
