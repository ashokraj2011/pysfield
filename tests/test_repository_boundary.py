# @ac:MIGRATION:AC-003

from __future__ import annotations

from pathlib import Path


def test_story_repo_contains_all_delivery_files() -> None:
    root = Path(__file__).resolve().parents[1]
    assert (root / "pyproject.toml").exists()
    assert (root / "src").exists()
    assert (root / "README.md").exists()


def test_reference_repo_is_not_modified() -> None:
    root = Path(__file__).resolve().parents[1]
    reference_root = root / ".singularity-flow" / "reference-repositories"
    assert reference_root.exists()
    assert not any(reference_root.rglob("*.py"))
