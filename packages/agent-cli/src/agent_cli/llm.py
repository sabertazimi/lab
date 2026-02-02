"""LLM client configuration and initialization.

Configuration priority:
1. CONFIG_FILE (~/.claude/settings.json) env field
2. Environment variables (os.getenv)
3. Default constants
"""

import json
import os
from pathlib import Path
from typing import TYPE_CHECKING, Literal, TypedDict

from anthropic import Anthropic
from dotenv import load_dotenv

if TYPE_CHECKING:
    from .tui import AgentApp

load_dotenv(override=True)


WORKDIR = Path.cwd()
CONFIG_FILE = Path.home() / ".claude" / "settings.json"

EnvConfigKey = Literal["ANTHROPIC_AUTH_TOKEN", "ANTHROPIC_BASE_URL", "ANTHROPIC_MODEL"]


class EnvConfig(TypedDict, total=False):
    ANTHROPIC_AUTH_TOKEN: str
    ANTHROPIC_BASE_URL: str
    ANTHROPIC_MODEL: str


class Config(TypedDict, total=False):
    env: EnvConfig


# Deferred initialization state
_env_config: EnvConfig | None = None
_config_error: str | None = None


def _parse_config() -> tuple[EnvConfig, str | None]:
    """Parse config file and return (config, error_message)."""
    try:
        if CONFIG_FILE.exists():
            with open(CONFIG_FILE, encoding="utf-8") as f:
                config: Config = json.load(f)
                return config.get("env", {}), None
    except (json.JSONDecodeError, OSError) as e:
        return {}, f"Error parsing config file at {CONFIG_FILE}: {e}"
    return {}, None


def _get_config_value(key: EnvConfigKey, default: str = "") -> str:
    global _env_config
    if _env_config is None:
        _load_config()
    assert _env_config is not None
    value = _env_config.get(key)
    if value is not None:
        return value
    return os.getenv(key, default)


def _load_config() -> None:
    """Load config (called on first access)."""
    global _env_config, _config_error
    _env_config, _config_error = _parse_config()


def report_config_errors(ctx: AgentApp) -> None:
    """Report any config errors to the UI. Call after app is mounted."""
    if _config_error:
        ctx.output.error(_config_error)


_load_config()
MODEL = _get_config_value("ANTHROPIC_MODEL", "glm-4.7")

client = Anthropic(
    api_key=_get_config_value("ANTHROPIC_AUTH_TOKEN"),
    base_url=_get_config_value("ANTHROPIC_BASE_URL"),
)
