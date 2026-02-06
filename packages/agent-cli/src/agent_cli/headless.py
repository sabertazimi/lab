"""Headless mode for agent-cli.

This module provides the HeadlessApp that runs the agent non-interactively.
Used with `-p/--print` flag to execute a prompt and print the response to stdout.
"""

import sys

from anthropic.types import TextBlock

from .agent import Agent
from .config import AgentConfig
from .skill import SkillLoader
from .system import build_system_prompt
from .task import TaskManager
from .tools import build_all_tools
from .ui_headless import HeadlessOutput


class HeadlessApp:
    """Headless application for non-interactive agent execution.

    Mirrors the pattern of tui.AgentApp but without any UI framework.
    Runs the agent with a single prompt and prints the final response to stdout.
    """

    def __init__(self) -> None:
        self.config = AgentConfig.from_settings()
        self.skill_loader = SkillLoader(self.config.workdir)
        self.task_manager = TaskManager()
        self.ui = HeadlessOutput()

    def run(self, prompt: str) -> None:
        """Execute the agent with the given prompt and print the response.

        Args:
            prompt: The user prompt to execute.
        """
        self.config.report_errors(self.ui)

        system_prompt = build_system_prompt(self.config.workdir, self.skill_loader)
        agent = Agent(
            ui=self.ui,
            config=self.config,
            system_prompt=system_prompt,
            tools=build_all_tools(self.skill_loader),
            skill_loader=self.skill_loader,
            task_manager=self.task_manager,
        )

        try:
            messages = agent.run(prompt)
        except Exception as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)

        # Extract the final response text from the last assistant message
        if messages:
            last_msg = messages[-1]
            if last_msg.get("role") == "assistant":
                for block in last_msg.get("content", []):
                    if isinstance(block, TextBlock):
                        print(block.text)
