# @ac:MIGRATION:AC-001
# @ac:MIGRATION:AC-002
# @ac:MIGRATION:AC-003

from __future__ import annotations

import re
from pathlib import Path


def test_every_planned_test_exists() -> None:
    root = Path(__file__).resolve().parents[1]
    plan = root / "singularity" / "work-items" / "migration" / "artifacts" / "planning" / "plan.md"
    planned_tests = set(re.findall(r"`(tests/test_[^`]+\.py)`", plan.read_text(encoding="utf-8")))

    assert planned_tests
    assert not [path for path in sorted(planned_tests) if not (root / path).is_file()]