from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Mapping


# @clause:MIGRATION:REQ-002
@dataclass(frozen=True)
class RuntimeConfig:
    """Validated runtime settings used by the Python execution path."""

    name: str = "sfield"
    preset: str = "local"
    max_items: int = 10
    allow_http: bool = True
    debug: bool = False

    def as_dict(self) -> dict[str, Any]:
        """Return a mutable representation suitable for recompilation."""

        return {
            "name": self.name,
            "preset": self.preset,
            "max_items": self.max_items,
            "allow_http": self.allow_http,
            "debug": self.debug,
        }


# @clause:MIGRATION:REQ-002
def compile_config(raw: Mapping[str, Any] | None = None) -> RuntimeConfig:
    """Validate and compile user settings without coercing invalid types."""

    data = dict(raw or {})
    unknown_keys = sorted(data.keys() - {"name", "preset", "max_items", "allow_http", "debug"})
    if unknown_keys:
        raise ValueError(f"Unknown configuration key: {unknown_keys[0]}")

    name_value = data.get("name", "sfield")
    preset_value = data.get("preset", "local")
    max_items = data.get("max_items", 10)
    allow_http = data.get("allow_http", True)
    debug = data.get("debug", False)
    if not isinstance(name_value, str):
        raise ValueError("name must be a string")
    if not isinstance(preset_value, str):
        raise ValueError("preset must be a string")
    if isinstance(max_items, bool) or not isinstance(max_items, int):
        raise ValueError("max_items must be an integer")
    if not isinstance(allow_http, bool):
        raise ValueError("allow_http must be a boolean")
    if not isinstance(debug, bool):
        raise ValueError("debug must be a boolean")

    name = name_value.strip() or "sfield"
    preset = preset_value.strip().lower()
    if preset not in {"local", "memory"}:
        raise ValueError(f"Unsupported preset: {preset!r}")
    return RuntimeConfig(
        name=name,
        preset=preset,
        max_items=max_items,
        allow_http=allow_http,
        debug=debug,
    )


def validate_runtime(config: RuntimeConfig) -> bool:
    """Reject runtime settings that cannot execute safely."""

    if not config.name.strip():
        raise ValueError("Runtime name cannot be empty")
    if config.preset not in {"local", "memory"}:
        raise ValueError(f"Unsupported preset: {config.preset!r}")
    if config.max_items <= 0:
        raise ValueError("max_items must be positive")
    return True


# @clause:MIGRATION:REQ-002
class SFieldRuntime:
    """Execute payloads using a validated SField runtime configuration."""

    def __init__(self, config: Mapping[str, Any] | RuntimeConfig | None = None) -> None:
        self.config = compile_config(config if isinstance(config, Mapping) else getattr(config, "as_dict", lambda: {})()) if not isinstance(config, RuntimeConfig) else config
        validate_runtime(self.config)

    def execute(self, payload: str) -> dict[str, Any]:
        """Execute one non-empty payload and return its observable result."""

        if not isinstance(payload, str) or not payload.strip():
            raise ValueError("Payload must be a non-empty string")
        result = {
            "status": "ok",
            "name": self.config.name,
            "preset": self.config.preset,
            "payload": payload.strip(),
            "items": min(len(payload.strip()), self.config.max_items),
        }
        if self.config.allow_http:
            result["adapter"] = "http"
        else:
            result["adapter"] = "local"
        return result
