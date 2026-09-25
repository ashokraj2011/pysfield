from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Mapping


@dataclass(frozen=True)
class RuntimeConfig:
    name: str = "sfield"
    preset: str = "local"
    max_items: int = 10
    allow_http: bool = True
    debug: bool = False

    def as_dict(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "preset": self.preset,
            "max_items": self.max_items,
            "allow_http": self.allow_http,
            "debug": self.debug,
        }


def compile_config(raw: Mapping[str, Any] | None = None) -> RuntimeConfig:
    data = dict(raw or {})
    name = str(data.get("name", "sfield")).strip() or "sfield"
    preset = str(data.get("preset", "local")).strip().lower()
    if preset not in {"local", "memory"}:
        raise ValueError(f"Unsupported preset: {preset!r}")
    max_items = int(data.get("max_items", 10))
    allow_http = bool(data.get("allow_http", True))
    debug = bool(data.get("debug", False))
    return RuntimeConfig(
        name=name,
        preset=preset,
        max_items=max_items,
        allow_http=allow_http,
        debug=debug,
    )


def validate_runtime(config: RuntimeConfig) -> bool:
    if not config.name.strip():
        raise ValueError("Runtime name cannot be empty")
    if config.preset not in {"local", "memory"}:
        raise ValueError(f"Unsupported preset: {config.preset!r}")
    if config.max_items <= 0:
        raise ValueError("max_items must be positive")
    return True


class SFieldRuntime:
    def __init__(self, config: Mapping[str, Any] | RuntimeConfig | None = None) -> None:
        self.config = compile_config(config if isinstance(config, Mapping) else getattr(config, "as_dict", lambda: {})()) if not isinstance(config, RuntimeConfig) else config
        validate_runtime(self.config)

    def execute(self, payload: str) -> dict[str, Any]:
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
