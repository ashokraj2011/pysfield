# @ac:MIGRATION:AC-003

from __future__ import annotations

from pathlib import Path


def test_reference_source_remains_outside_delivery_paths() -> None:
    root = Path(__file__).resolve().parents[1]
    reference_root = root / ".singularity-flow" / "reference-repositories"

    assert reference_root.is_dir()
    assert not any(path.is_relative_to(reference_root) for path in (root / "src").rglob("*.py"))