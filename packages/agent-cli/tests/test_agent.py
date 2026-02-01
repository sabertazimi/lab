"""Unit tests for agent-cli agent module."""

from agent_cli.agent import AGENTS, get_agent_description


class TestGetAgentDescription:
    """Tests for get_agent_description() function."""

    def test_returns_all_agents(self) -> None:
        """Should include description for each agent in AGENTS."""
        result = get_agent_description()

        for name in AGENTS:
            assert name in result

    def test_format(self) -> None:
        """Each line should follow '- Name: description' format."""
        result = get_agent_description()
        lines = result.strip().split("\n")

        assert len(lines) == len(AGENTS)
        for line in lines:
            assert line.startswith("- ")
            assert ": " in line

    def test_includes_descriptions(self) -> None:
        """Should include actual descriptions from AGENTS dict."""
        result = get_agent_description()

        for config in AGENTS.values():
            desc = config["description"]
            assert isinstance(desc, str) and desc in result
