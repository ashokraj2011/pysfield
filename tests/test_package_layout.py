# @ac:MIGRATION:AC-001

from __future__ import annotations

from pathlib import Path


def test_python_project_layout_exists() -> None:
    root = Path(__file__).resolve().parents[1]
    assert (root / "pyproject.toml").exists()
    assert (root / "src" / "sfield" / "__init__.py").exists()
    assert (root / "src" / "sfield" / "core.py").exists()
    assert (root / "src" / "sfield" / "cli.py").exists()


def test_package_metadata_matches_project_identity() -> None:
    root = Path(__file__).resolve().parents[1]
    text = (root / "pyproject.toml").read_text(encoding="utf-8")
    assert 'name = "pysfield"' in text
    assert 'requires-python = ">=3.11"' in text
