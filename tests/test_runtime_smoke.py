# @ac:MIGRATION:AC-002

from __future__ import annotations

from sfield.core import SFieldRuntime, compile_config


def test_runtime_compiles_config() -> None:
    config = compile_config({"name": "demo", "preset": "memory", "max_items": 7, "allow_http": False})
    assert config.name == "demo"
    assert config.preset == "memory"
    assert config.max_items == 7
    assert config.allow_http is False


def test_runtime_executes_payload() -> None:
    runtime = SFieldRuntime({"name": "demo", "preset": "local", "max_items": 4, "allow_http": True})
    outcome = runtime.execute("hello world")
    assert outcome["status"] == "ok"
    assert outcome["name"] == "demo"
    assert outcome["payload"] == "hello world"
    assert outcome["adapter"] == "http"
