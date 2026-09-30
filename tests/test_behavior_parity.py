# @ac:MIGRATION:AC-002

from __future__ import annotations

from sfield.core import SFieldRuntime


def test_runtime_normalizes_input_and_applies_item_limit() -> None:
    outcome = SFieldRuntime(
        {"name": " parity ", "preset": "MEMORY", "max_items": 3, "allow_http": False}
    ).execute("  payload  ")

    assert outcome == {
        "status": "ok",
        "name": "parity",
        "preset": "memory",
        "payload": "payload",
        "items": 3,
        "adapter": "local",
    }