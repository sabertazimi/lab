"""Unit tests for agent-cli Agent core logic."""

import threading
from pathlib import Path
from typing import cast
from unittest.mock import MagicMock, patch

import pytest
from agent_cli.agent import Agent
from anthropic.types import MessageParam, TextBlock, TextBlockParam


@pytest.fixture
def mock_config() -> MagicMock:
    """Create a mock AgentConfig."""
    config = MagicMock()
    config.model = "test-model"
    config.workdir = Path("/tmp/test")
    config.max_thinking_tokens = 1024
    config.create_client.return_value = MagicMock()
    return config


@pytest.fixture
def agent(
    mock_ui: MagicMock,
    mock_config: MagicMock,
    mock_skill_loader: MagicMock,
    mock_task_manager: MagicMock,
) -> Agent:
    """Create an Agent instance with mocked dependencies."""
    return Agent(
        ui=mock_ui,
        config=mock_config,
        system_prompt="You are a test agent.",
        tools=[],
        skill_loader=mock_skill_loader,
        task_manager=mock_task_manager,
    )


@pytest.fixture
def subagent(
    mock_ui: MagicMock,
    mock_config: MagicMock,
    mock_skill_loader: MagicMock,
    mock_task_manager: MagicMock,
) -> Agent:
    """Create a subagent (is_subagent=True) with mocked dependencies."""
    return Agent(
        ui=mock_ui,
        config=mock_config,
        system_prompt="You are a test subagent.",
        tools=[],
        skill_loader=mock_skill_loader,
        task_manager=mock_task_manager,
        is_subagent=True,
    )


def _get_text_blocks(msg: MessageParam) -> list[TextBlockParam]:
    """Extract content as list of TextBlockParam from a message.

    Helper to safely cast the complex union type in tests.
    """
    return cast(list[TextBlockParam], msg["content"])


class TestAgentInit:
    """Tests for Agent.__init__."""

    def test_attributes_set(self, agent: Agent, mock_config: MagicMock) -> None:
        """All attributes should be initialized correctly."""
        assert agent.system_prompt == "You are a test agent."
        assert agent.tools == []
        assert agent.config is mock_config
        assert agent.is_subagent is False

    def test_initial_state(self, agent: Agent) -> None:
        """Agent should start with empty messages and first_turn=True."""
        assert agent.messages == []
        assert agent.first_turn is True

    def test_subagent_flag(self, subagent: Agent) -> None:
        """Subagent should have is_subagent=True."""
        assert subagent.is_subagent is True

    def test_client_created_from_config(
        self, mock_config: MagicMock, agent: Agent
    ) -> None:
        """Agent should create client via config.create_client()."""
        mock_config.create_client.assert_called_once()


class TestBuildMessage:
    """Tests for Agent._build_message."""

    @patch("agent_cli.context.load_system_reminder", return_value=None)
    def test_first_turn_includes_task_reminder(
        self,
        mock_load: MagicMock,
        agent: Agent,
        mock_task_manager: MagicMock,
    ) -> None:
        """First turn should include INITIAL_REMINDER and user input."""
        agent._build_message("hello")  # pyright: ignore[reportPrivateUsage]

        assert len(agent.messages) == 1
        msg = agent.messages[0]
        assert msg["role"] == "user"

        content = _get_text_blocks(msg)
        # Should have task reminder + user input (no system reminder since CLAUDE.md absent)
        texts = [block["text"] for block in content]
        assert mock_task_manager.INITIAL_REMINDER in texts
        assert "hello" in texts

    @patch(
        "agent_cli.context.load_system_reminder",
        return_value="<system-reminder>test rules</system-reminder>",
    )
    def test_first_turn_includes_system_reminder(
        self,
        mock_load: MagicMock,
        agent: Agent,
    ) -> None:
        """First turn with CLAUDE.md should include system reminder."""
        agent._build_message("hello")  # pyright: ignore[reportPrivateUsage]

        content = _get_text_blocks(agent.messages[0])
        texts = [block["text"] for block in content]
        assert any("system-reminder" in t for t in texts)

    @patch("agent_cli.context.load_system_reminder", return_value=None)
    def test_first_turn_sets_first_turn_false(
        self,
        mock_load: MagicMock,
        agent: Agent,
    ) -> None:
        """After first _build_message, first_turn should be False."""
        assert agent.first_turn is True
        agent._build_message("hello")  # pyright: ignore[reportPrivateUsage]
        assert agent.first_turn is False

    @patch("agent_cli.context.load_system_reminder", return_value=None)
    def test_second_turn_only_user_input(
        self,
        mock_load: MagicMock,
        agent: Agent,
    ) -> None:
        """Second turn should only contain user input (no reminders)."""
        agent._build_message("first")  # pyright: ignore[reportPrivateUsage]
        agent._build_message("second")  # pyright: ignore[reportPrivateUsage]

        assert len(agent.messages) == 2
        content = _get_text_blocks(agent.messages[1])
        # Only the user input text
        assert len(content) == 1
        assert content[0]["text"] == "second"

    @patch("agent_cli.context.load_system_reminder", return_value=None)
    def test_subagent_skips_reminders(
        self,
        mock_load: MagicMock,
        subagent: Agent,
    ) -> None:
        """Subagent should skip system reminder and task reminder on first turn."""
        subagent._build_message("do something")  # pyright: ignore[reportPrivateUsage]

        content = _get_text_blocks(subagent.messages[0])
        # Only user input, no reminders
        assert len(content) == 1
        assert content[0]["text"] == "do something"


class TestInterrupt:
    """Tests for Agent interrupt mechanism."""

    def test_initial_state_not_interrupted(self, agent: Agent) -> None:
        """Interrupt should not be requested initially."""
        assert agent._is_interrupt_requested() is False  # pyright: ignore[reportPrivateUsage]

    def test_request_interrupt(self, agent: Agent) -> None:
        """request_interrupt should set the flag."""
        agent.request_interrupt()
        assert agent._is_interrupt_requested() is True  # pyright: ignore[reportPrivateUsage]

    def test_clear_interrupt(self, agent: Agent) -> None:
        """_clear_interrupt should reset the flag."""
        agent.request_interrupt()
        agent._clear_interrupt()  # pyright: ignore[reportPrivateUsage]
        assert agent._is_interrupt_requested() is False  # pyright: ignore[reportPrivateUsage]

    def test_thread_safety(self, agent: Agent) -> None:
        """Interrupt mechanism should be thread-safe under concurrent access."""
        results: list[bool] = []

        def reader() -> None:
            for _ in range(100):
                results.append(agent._is_interrupt_requested())  # pyright: ignore[reportPrivateUsage]

        def writer() -> None:
            for _ in range(50):
                agent.request_interrupt()
                agent._clear_interrupt()  # pyright: ignore[reportPrivateUsage]

        t1 = threading.Thread(target=reader)
        t2 = threading.Thread(target=writer)
        t1.start()
        t2.start()
        t1.join()
        t2.join()

        # Should not raise; all results should be bool
        assert all(isinstance(r, bool) for r in results)
        assert len(results) == 100


class TestAppendInterruptMessage:
    """Tests for Agent._append_interrupt_message."""

    def test_appends_user_message(self, agent: Agent) -> None:
        """Should append a user-role message to history."""
        agent._append_interrupt_message()  # pyright: ignore[reportPrivateUsage]

        assert len(agent.messages) == 1
        msg = agent.messages[0]
        assert msg["role"] == "user"

    def test_contains_interrupt_notification(self, agent: Agent) -> None:
        """Message should contain task_interrupted notification."""
        agent._append_interrupt_message()  # pyright: ignore[reportPrivateUsage]

        content = agent.messages[0]["content"]
        assert isinstance(content, str)
        assert "task_interrupted" in content
        assert "ctrl+c" in content


class TestAgentLoopInterrupt:
    """Tests for Agent._agent_loop interrupt handling."""

    @patch("agent_cli.context.load_system_reminder", return_value=None)
    def test_interrupt_before_api_call(
        self,
        mock_load: MagicMock,
        agent: Agent,
        mock_ui: MagicMock,
    ) -> None:
        """If interrupt is requested before API call, should return early."""
        agent._build_message("hello")  # pyright: ignore[reportPrivateUsage]
        agent.request_interrupt()

        messages = agent._agent_loop()  # pyright: ignore[reportPrivateUsage]

        mock_ui.interrupted.assert_called_once()
        # Should have the user message + interrupt notification
        has_interrupt = False
        for m in messages:
            msg_content = m.get("content")
            if isinstance(msg_content, str) and "task_interrupted" in msg_content:
                has_interrupt = True
        assert has_interrupt


class TestSpawnSubagentValidation:
    """Tests for Agent.spawn_subagent input validation."""

    def test_unknown_agent_type(self, agent: Agent) -> None:
        """Unknown agent type should return an error string."""
        result = agent.spawn_subagent("UnknownType", "do something", "test")
        assert "Error" in result
        assert "UnknownType" in result

    @patch("agent_cli.subagent.AGENTS", {"Explore": {"prompt": "explore"}})
    @patch("agent_cli.subagent.get_tools_for_agent", return_value=[])
    def test_known_agent_type_does_not_error(
        self,
        mock_tools: MagicMock,
        agent: Agent,
    ) -> None:
        """Known agent type should not return the 'unknown' error.

        The actual API call will fail (mocked client), but it should
        proceed past the validation check.
        """
        # Mock the API response for the subagent
        mock_response = MagicMock()
        mock_response.stop_reason = "end_turn"
        mock_response.content = [TextBlock(type="text", text="Subagent result")]
        mock_client = cast(MagicMock, agent.client)
        mock_client.messages.create.return_value = mock_response

        result = agent.spawn_subagent("Explore", "find files", "test")
        assert "Error" not in result or "Unknown" not in result
        assert result == "Subagent result"
