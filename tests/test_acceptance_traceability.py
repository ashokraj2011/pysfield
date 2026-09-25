# @ac:MIGRATION:AC-001
# @ac:MIGRATION:AC-002
# @ac:MIGRATION:AC-003

from __future__ import annotations

from pathlib import Path


def test_story_requirements_and_tests_are_present() -> None:
    root = Path(__file__).resolve().parents[1]
    spec = root / "singularity" / "work-items" / "migration" / "artifacts" / "specification" / "spec.md"
    plan = root / "singularity" / "work-items" / "migration" / "artifacts" / "planning" / "plan.md"
    assert spec.exists()
    assert plan.exists()
    assert "[migration:REQ-001]" in spec.read_text(encoding="utf-8")
    assert "[migration:AC-001]" in plan.read_text(encoding="utf-8")
