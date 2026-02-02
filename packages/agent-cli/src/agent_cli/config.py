"""Agent configuration management.

Configuration priority:
1. CONFIG_FILE (~/.claude/settings.json) env field
2. Environment variables (os.getenv)
3. Default constants
"""

import json
import os
from dataclasses import dataclass
from pathlib import Path
from typing import TYPE_CHECKING, Literal, TypedDict

from anthropic import Anthropic
from dotenv import load_dotenv

if TYPE_CHECKING:
    from .interfaces import IAgentUI

load_dotenv(override=True)


CONFIG_FILE = Path.home() / ".claude" / "settings.json"

EnvConfigKey = Literal[
    "ANTHROPIC_AUTH_TOKEN",
    "ANTHROPIC_BASE_URL",
    "ANTHROPIC_MODEL",
    "MAX_THINKING_TOKENS",
]


class EnvConfig(TypedDict, total=False):
    ANTHROPIC_AUTH_TOKEN: str
    ANTHROPIC_BASE_URL: str
    ANTHROPIC_MODEL: str
    MAX_THINKING_TOKENS: str


class Config(TypedDict, total=False):
    env: EnvConfig


def _parse_config(config_file: Path) -> tuple[EnvConfig, str | None]:
    """Parse config file and return (config, error_message)."""
    try:
        if config_file.exists():
            with open(config_file, encoding="utf-8") as f:
                config: Config = json.load(f)
                return config.get("env", {}), None
    except (json.JSONDecodeError, OSError) as e:
        return {}, f"Error parsing config file at {config_file}: {e}"
    return {}, None


def _get_config_value(
    env_config: EnvConfig, key: EnvConfigKey, default: str = ""
) -> str:
    """Get config value with priority: env_config > os.getenv > default."""
    value = env_config.get(key)
    if value is not None:
        return value
    return os.getenv(key, default)


def _get_config_int_value(
    env_config: EnvConfig,
    key: EnvConfigKey,
    default: int,
    min_value: int | None = None,
) -> int:
    """Get config value as integer with optional minimum validation."""
    str_value = _get_config_value(env_config, key, "")
    if not str_value:
        return default
    try:
        value = int(str_value)
        if min_value is not None and value < min_value:
            return min_value
        return value
    except ValueError:
        return default


@dataclass
class AgentConfig:
    """Agent configuration class encapsulating all config items."""

    model: str
    max_thinking_tokens: int
    api_key: str
    base_url: str
    workdir: Path
    _config_error: str | None = None

    @classmethod
    def from_settings(cls, workdir: Path | None = None) -> AgentConfig:
        """Load configuration from settings file and environment variables.

        Args:
            workdir: Working directory. Defaults to current working directory.

        Returns:
            AgentConfig instance with loaded configuration.
        """
        if workdir is None:
            workdir = Path.cwd()

        env_config, config_error = _parse_config(CONFIG_FILE)

        return cls(
            model=_get_config_value(
                env_config, "ANTHROPIC_MODEL", "claude-opus-4-5-20251101"
            ),
            max_thinking_tokens=_get_config_int_value(
                env_config, "MAX_THINKING_TOKENS", 31999, min_value=1024
            ),
            api_key=_get_config_value(env_config, "ANTHROPIC_AUTH_TOKEN"),
            base_url=_get_config_value(env_config, "ANTHROPIC_BASE_URL"),
            workdir=workdir,
            _config_error=config_error,
        )

    def create_client(self) -> Anthropic:
        """Create an Anthropic client with the configured settings."""
        return Anthropic(api_key=self.api_key, base_url=self.base_url)

    def report_errors(self, ui: IAgentUI) -> None:
        """Report any configuration loading errors to the UI.

        Call this after the UI is ready to display messages.
        """
        if self._config_error:
            ui.error(self._config_error)
