"""Unit tests for agent-cli headless mode."""

import argparse
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest
from agent_cli.interfaces import IAgentUI
from agent_cli.ui_headless import HeadlessOutput
from anthropic.types import TextBlock


class TestHeadlessOutput:
    """Tests for HeadlessOutput class."""

    @pytest.fixture(autouse=True)
    def setup(self) -> None:
        """Set up HeadlessOutput instance for each test."""
        self.output = HeadlessOutput()

    def test_implements_iagentui_protocol(self) -> None:
        """HeadlessOutput should satisfy the IAgentUI protocol."""
        assert isinstance(self.output, IAgentUI)

    def test_noop_methods_no_exception(self) -> None:
        """All no-op methods should execute without raising."""
        self.output.text("message")
        self.output.newline()
        self.output.clear()
        self.output.primary("msg")
        self.output.accent("msg")
        self.output.debug("msg")
        self.output.thinking("content", duration=1.0)
        self.output.response("text")
        self.output.tool_call("Bash", {"command": "echo"})
        self.output.tool_result("output")
        self.output.interrupted()
        self.output.status("status", spinning=True)
        self.output.banner("model", Path.cwd())

    def test_noop_methods_accept_none(self) -> None:
        """No-op methods should accept None values gracefully."""
        self.output.primary(None)
        self.output.accent(None)
        self.output.debug(None)
        self.output.thinking(None)
        self.output.response(None)
        self.output.tool_result(None)
        self.output.status(None)

    def test_error_prints_to_stderr(self, capsys: pytest.CaptureFixture[str]) -> None:
        """error() should print message to stderr."""
        self.output.error("test error message")
        captured = capsys.readouterr()
        assert captured.out == ""
        assert "test error message" in captured.err

    def test_error_none_is_silent(self, capsys: pytest.CaptureFixture[str]) -> None:
        """error(None) should not print anything."""
        self.output.error(None)
        captured = capsys.readouterr()
        assert captured.out == ""
        assert captured.err == ""


class TestHeadlessAppRun:
    """Tests for HeadlessApp.run() response extraction logic."""

    @patch("agent_cli.headless.Agent")
    @patch("agent_cli.headless.build_all_tools", return_value=[])
    @patch("agent_cli.headless.build_system_prompt", return_value="system")
    @patch("agent_cli.headless.AgentConfig.from_settings")
    def test_prints_final_text_response(
        self,
        mock_config_cls: MagicMock,
        mock_build_prompt: MagicMock,
        mock_build_tools: MagicMock,
        mock_agent_cls: MagicMock,
        capsys: pytest.CaptureFixture[str],
    ) -> None:
        """Should print the final TextBlock content to stdout."""
        mock_config = MagicMock()
        mock_config._config_error = None
        mock_config.workdir = Path.cwd()
        mock_config_cls.return_value = mock_config

        text_block = TextBlock(type="text", text="Final response")
        mock_agent = MagicMock()
        mock_agent.run.return_value = [
            {"role": "assistant", "content": [text_block]},
        ]
        mock_agent_cls.return_value = mock_agent

        from agent_cli.headless import HeadlessApp

        app = HeadlessApp()
        app.run("hello")

        captured = capsys.readouterr()
        assert "Final response" in captured.out

    @patch("agent_cli.headless.Agent")
    @patch("agent_cli.headless.build_all_tools", return_value=[])
    @patch("agent_cli.headless.build_system_prompt", return_value="system")
    @patch("agent_cli.headless.AgentConfig.from_settings")
    def test_only_prints_last_assistant_message(
        self,
        mock_config_cls: MagicMock,
        mock_build_prompt: MagicMock,
        mock_build_tools: MagicMock,
        mock_agent_cls: MagicMock,
        capsys: pytest.CaptureFixture[str],
    ) -> None:
        """Should only print text from the last assistant message, not intermediate ones."""
        mock_config = MagicMock()
        mock_config._config_error = None
        mock_config.workdir = Path.cwd()
        mock_config_cls.return_value = mock_config

        intermediate_block = TextBlock(type="text", text="Intermediate text")
        final_block = TextBlock(type="text", text="Final answer")
        mock_agent = MagicMock()
        mock_agent.run.return_value = [
            {"role": "assistant", "content": [intermediate_block]},
            {
                "role": "user",
                "content": [
                    {"type": "tool_result", "tool_use_id": "x", "content": "ok"}
                ],
            },
            {"role": "assistant", "content": [final_block]},
        ]
        mock_agent_cls.return_value = mock_agent

        from agent_cli.headless import HeadlessApp

        app = HeadlessApp()
        app.run("hello")

        captured = capsys.readouterr()
        assert "Final answer" in captured.out
        assert "Intermediate text" not in captured.out

    @patch("agent_cli.headless.Agent")
    @patch("agent_cli.headless.build_all_tools", return_value=[])
    @patch("agent_cli.headless.build_system_prompt", return_value="system")
    @patch("agent_cli.headless.AgentConfig.from_settings")
    def test_empty_messages_no_output(
        self,
        mock_config_cls: MagicMock,
        mock_build_prompt: MagicMock,
        mock_build_tools: MagicMock,
        mock_agent_cls: MagicMock,
        capsys: pytest.CaptureFixture[str],
    ) -> None:
        """Empty message list should produce no output."""
        mock_config = MagicMock()
        mock_config._config_error = None
        mock_config.workdir = Path.cwd()
        mock_config_cls.return_value = mock_config

        mock_agent = MagicMock()
        mock_agent.run.return_value = []
        mock_agent_cls.return_value = mock_agent

        from agent_cli.headless import HeadlessApp

        app = HeadlessApp()
        app.run("hello")

        captured = capsys.readouterr()
        assert captured.out == ""

    @patch("agent_cli.headless.Agent")
    @patch("agent_cli.headless.build_all_tools", return_value=[])
    @patch("agent_cli.headless.build_system_prompt", return_value="system")
    @patch("agent_cli.headless.AgentConfig.from_settings")
    def test_agent_error_prints_to_stderr(
        self,
        mock_config_cls: MagicMock,
        mock_build_prompt: MagicMock,
        mock_build_tools: MagicMock,
        mock_agent_cls: MagicMock,
        capsys: pytest.CaptureFixture[str],
    ) -> None:
        """Agent exceptions should be printed to stderr with sys.exit(1)."""
        mock_config = MagicMock()
        mock_config._config_error = None
        mock_config.workdir = Path.cwd()
        mock_config_cls.return_value = mock_config

        mock_agent = MagicMock()
        mock_agent.run.side_effect = RuntimeError("API connection failed")
        mock_agent_cls.return_value = mock_agent

        from agent_cli.headless import HeadlessApp

        app = HeadlessApp()
        with pytest.raises(SystemExit) as exc_info:
            app.run("hello")

        assert exc_info.value.code == 1
        captured = capsys.readouterr()
        assert "API connection failed" in captured.err


class TestCliArgumentParsing:
    """Tests for CLI argument parsing."""

    @staticmethod
    def _make_parser() -> argparse.ArgumentParser:
        parser = argparse.ArgumentParser()
        parser.add_argument("-p", "--print", dest="prompt", type=str, default=None)
        return parser

    def test_short_flag(self) -> None:
        """'-p' flag should parse the prompt."""
        args = self._make_parser().parse_args(["-p", "hello"])
        assert args.prompt == "hello"

    def test_long_flag(self) -> None:
        """'--print' flag should parse the prompt."""
        args = self._make_parser().parse_args(["--print", "hello world"])
        assert args.prompt == "hello world"

    def test_no_flag_defaults_none(self) -> None:
        """No flag should default to None."""
        args = self._make_parser().parse_args([])
        assert args.prompt is None

    def test_empty_string_prompt(self) -> None:
        """Empty string prompt should be preserved (not treated as None)."""
        args = self._make_parser().parse_args(["-p", ""])
        assert args.prompt is not None
        assert args.prompt == ""
