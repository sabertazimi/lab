"""LLM client configuration and initialization.

Configuration priority:
1. CONFIG_FILE (~/.claude/settings.json) env field
2. Environment variables (os.getenv)
3. Default constants
"""

import json
import os
from pathlib import Path
from typing import Literal, TypedDict

from anthropic import Anthropic
from dotenv import load_dotenv

from .console import console

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


def _parse_config() -> EnvConfig:
    try:
        if CONFIG_FILE.exists():
            with open(CONFIG_FILE, encoding="utf-8") as f:
                config: Config = json.load(f)
                return config.get("env", {})
    except (json.JSONDecodeError, OSError):
        console.print(f"Error: parsing config file at {CONFIG_FILE}", style="error")
    return {}


def _get_config_value(key: EnvConfigKey, default: str = "") -> str:
    value = _ENV_CONFIG.get(key)
    if value is not None:
        return value
    return os.getenv(key, default)


_ENV_CONFIG: EnvConfig = _parse_config()

MODEL = _get_config_value("ANTHROPIC_MODEL", "glm-4.7")

client = Anthropic(
    api_key=_get_config_value("ANTHROPIC_AUTH_TOKEN"),
    base_url=_get_config_value("ANTHROPIC_BASE_URL"),
)
