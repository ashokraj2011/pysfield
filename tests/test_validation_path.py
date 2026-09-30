# @ac:MIGRATION:AC-001
# @ac:MIGRATION:AC-002

from __future__ import annotations

import importlib.util

from sfield.cli import main


def test_package_and_cli_are_executable(capsys: object) -> None:
    assert importlib.util.find_spec("sfield") is not None
    assert main(["--disable-http", "validation"]) == 0

    output = capsys.readouterr().out  # type: ignore[attr-defined]
    assert '"status": "ok"' in output
    assert '"adapter": "local"' in output