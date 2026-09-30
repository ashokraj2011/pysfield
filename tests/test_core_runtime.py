# @ac:MIGRATION:AC-001
# @ac:MIGRATION:AC-002

from __future__ import annotations

import pytest

from sfield.core import RuntimeConfig, SFieldRuntime, compile_config, validate_runtime


def test_compile_config_uses_runtime_defaults() -> None:
    assert compile_config() == RuntimeConfig()


def test_runtime_rejects_invalid_configuration_and_payload() -> None:
    with pytest.raises(ValueError, match="Unsupported preset"):
        compile_config({"preset": "remote"})

    with pytest.raises(ValueError, match="max_items must be positive"):
        validate_runtime(RuntimeConfig(max_items=0))

    with pytest.raises(ValueError, match="Payload must be a non-empty string"):
        SFieldRuntime().execute("  ")


def test_compile_config_rejects_schema_type_coercion() -> None:
    with pytest.raises(ValueError, match="max_items must be an integer"):
        compile_config({"max_items": "10"})

    with pytest.raises(ValueError, match="allow_http must be a boolean"):
        compile_config({"allow_http": "false"})

    with pytest.raises(ValueError, match="Unknown configuration key: timeout"):
        compile_config({"timeout": 10})