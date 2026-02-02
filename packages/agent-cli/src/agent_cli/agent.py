"""Agent core implementation.

This module contains the Agent class that manages conversation and tool execution.
It consolidates the logic from workflow.py into an object-oriented design.
"""

from __future__ import annotations

import threading
import time
from collections.abc import Callable
from typing import TYPE_CHECKING

from anthropic import Anthropic
from anthropic.types import (
    MessageParam,
    TextBlock,
    TextBlockParam,
    ThinkingBlock,
    ToolParam,
    ToolResultBlockParam,
    ToolUseBlock,
)

if TYPE_CHECKING:
    from .config import AgentConfig
    from .interfaces import IAgentUI
    from .skill import SkillLoader
    from .task import TaskManager

SpawnSubagentFn = Callable[[str, str, str], str]


class Agent:
    """Agent core class managing conversation and tool execution.

    This class encapsulates the agent loop pattern:
        while True:
            response = model(messages, tools)
            if no tool calls: return
            execute tools, append results, continue

    Attributes:
        ui: The UI interface for output.
        config: Agent configuration.
        client: Anthropic API client.
        system_prompt: System prompt for the agent.
        tools: Available tools for the agent.
        skill_loader: Skill loader instance.
        task_manager: Task manager instance.
        is_subagent: Whether this is a subagent.
        messages: Conversation message history.
        first_turn: Whether this is the first turn (for initial reminders).
    """

    def __init__(
        self,
        ui: IAgentUI,
        config: AgentConfig,
        *,
        system_prompt: str,
        tools: list[ToolParam],
        skill_loader: SkillLoader,
        task_manager: TaskManager,
        is_subagent: bool = False,
    ) -> None:
        """Initialize the Agent.

        Args:
            ui: UI interface for output.
            config: Agent configuration.
            system_prompt: System prompt for the agent.
            tools: Available tools.
            skill_loader: Skill loader instance.
            task_manager: Task manager instance.
            is_subagent: Whether this is a subagent (default: False).
        """
        self.ui = ui
        self.config = config
        self.client: Anthropic = config.create_client()
        self.system_prompt = system_prompt
        self.tools = tools
        self.skill_loader = skill_loader
        self.task_manager = task_manager
        self.is_subagent = is_subagent

        self.messages: list[MessageParam] = []
        self.first_turn = True

        # Thread-safe interrupt flag
        self._interrupt_lock = threading.Lock()
        self._interrupt_requested = False

    def run(self, user_input: str) -> list[MessageParam]:
        """Execute a conversation turn with the given user input.

        Args:
            user_input: The user's input message.

        Returns:
            Updated message history after the conversation turn.
        """
        self._clear_interrupt()
        self._build_message(user_input)
        return self._agent_loop()

    def request_interrupt(self) -> None:
        """Request interruption of the agent loop (thread-safe)."""
        with self._interrupt_lock:
            self._interrupt_requested = True

    def _clear_interrupt(self) -> None:
        """Clear the interrupt flag."""
        with self._interrupt_lock:
            self._interrupt_requested = False

    def _is_interrupt_requested(self) -> bool:
        """Check if interrupt has been requested."""
        with self._interrupt_lock:
            return self._interrupt_requested

    def _build_message(self, user_input: str) -> None:
        """Build and append user message to history.

        On first turn, includes system reminder and task reminder.
        """
        from .context import load_system_reminder

        content: list[TextBlockParam] = []

        if self.first_turn and not self.is_subagent:
            system_reminder = load_system_reminder(self.config.workdir)
            if system_reminder:
                content.append({"type": "text", "text": system_reminder})
            content.append({"type": "text", "text": self.task_manager.INITIAL_REMINDER})
            self.first_turn = False

        content.append({"type": "text", "text": user_input})
        self.messages.append({"role": "user", "content": content})

    def _agent_loop(self) -> list[MessageParam]:
        """Core agent loop: call model -> execute tools -> continue.

        Returns:
            Updated message history.
        """
        from .tools import execute_tool

        try:
            while True:
                # Check for interrupt request
                if self._is_interrupt_requested():
                    raise KeyboardInterrupt

                # Step 1: Call the model
                start_time = time.time()
                response = self.client.messages.create(
                    model=self.config.model,
                    system=self.system_prompt,
                    messages=self.messages,
                    tools=self.tools,
                    max_tokens=8000,
                    thinking={
                        "type": "enabled",
                        "budget_tokens": self.config.max_thinking_tokens,
                    },
                )
                elapsed_time = time.time() - start_time

                # Check for interrupt after API call
                if self._is_interrupt_requested():
                    raise KeyboardInterrupt

                # Step 2: Collect any tool calls and print text output
                tool_calls: list[ToolUseBlock] = []
                for block in response.content:
                    if isinstance(block, ThinkingBlock):
                        self.ui.thinking(block.thinking, duration=elapsed_time)
                    elif isinstance(block, TextBlock):
                        self.ui.response(block.text)
                    elif isinstance(block, ToolUseBlock):
                        tool_calls.append(block)

                # Step 3: If no tool calls, task is complete
                if response.stop_reason != "tool_use":
                    self.messages.append(
                        {"role": "assistant", "content": response.content}
                    )
                    return self.messages

                # Step 4: Execute each tool and collect results
                results: list[ToolResultBlockParam | TextBlockParam] = []
                used_task = False

                for tool_call in tool_calls:
                    # Check for interrupt before each tool execution
                    if self._is_interrupt_requested():
                        raise KeyboardInterrupt

                    self.ui.tool_call(tool_call.name, tool_call.input)
                    output = execute_tool(
                        ui=self.ui,
                        name=tool_call.name,
                        args=tool_call.input,
                        workdir=self.config.workdir,
                        skill_loader=self.skill_loader,
                        spawn_subagent=self.spawn_subagent,
                        task_manager=self.task_manager,
                    )
                    self.ui.tool_result(output)

                    results.append(
                        {
                            "type": "tool_result",
                            "tool_use_id": tool_call.id,
                            "content": output,
                        }
                    )

                    if tool_call.name == "TaskUpdate":
                        used_task = True

                if used_task:
                    self.task_manager.reset()
                else:
                    self.task_manager.increment()

                # Step 5: Append to conversation and continue
                self.messages.append({"role": "assistant", "content": response.content})
                if self.task_manager.too_long_without_task():
                    results.insert(
                        0, {"type": "text", "text": self.task_manager.NAG_REMINDER}
                    )
                self.messages.append({"role": "user", "content": results})

        except KeyboardInterrupt:
            self.ui.interrupted()
            self._append_interrupt_message()
            return self.messages

    def _append_interrupt_message(self) -> None:
        """Append interruption notification to message history."""
        self.messages.append(
            {
                "role": "user",
                "content": """<system_notification type="task_interrupted">
User has pressed ctrl+c to interrupt the current task.
Please acknowledge the interruption and summarize what was completed.
</system_notification>""",
            }
        )

    def spawn_subagent(self, agent_type: str, prompt: str, description: str) -> str:
        """Create and run a subagent, returning the result text.

        Subagents share the same UI but have isolated message history.
        They display progress through the shared UI but only return
        the final text result to keep the parent's context clean.

        Args:
            agent_type: Type of agent (Explore, Plan, Code).
            prompt: Detailed instructions for the subagent.
            description: Short task name for progress display.

        Returns:
            Final text result from the subagent.
        """
        from .output import get_tool_call_detail
        from .subagent import AGENTS, get_tools_for_agent
        from .tools import execute_tool

        if agent_type not in AGENTS:
            return f"Error: Unknown agent type '{agent_type}'"

        agent_config = AGENTS[agent_type]
        system_prompt = f"""You are a {agent_type} subagent at {self.config.workdir}.

{agent_config["prompt"]}

Complete the task and return a clear, concise summary."""

        tools = get_tools_for_agent(agent_type)
        messages: list[MessageParam] = [
            {"role": "user", "content": prompt},
        ]

        tool_count = 0
        interrupted = False
        response = None

        try:
            self.ui.status(f"Preparing {agent_type} agent...")
            while True:
                response = self.client.messages.create(
                    model=self.config.model,
                    system=system_prompt,
                    messages=messages,
                    tools=tools,
                    max_tokens=8000,
                    thinking={
                        "type": "enabled",
                        "budget_tokens": self.config.max_thinking_tokens,
                    },
                )

                if response.stop_reason != "tool_use":
                    break

                tool_calls: list[ToolUseBlock] = [
                    block
                    for block in response.content
                    if isinstance(block, ToolUseBlock)
                ]
                results: list[ToolResultBlockParam] = []

                for tool_call in tool_calls:
                    tool_count += 1
                    # Subagent cannot spawn further subagents (no spawn_subagent)
                    output = execute_tool(
                        ui=self.ui,
                        name=tool_call.name,
                        args=tool_call.input,
                        workdir=self.config.workdir,
                        skill_loader=self.skill_loader,
                        spawn_subagent=None,  # No recursive subagents
                    )
                    results.append(
                        {
                            "type": "tool_result",
                            "tool_use_id": tool_call.id,
                            "content": output,
                        }
                    )
                    self.ui.status(
                        f"{get_tool_call_detail(tool_call.name, tool_call.input)}"
                    )

                messages.append({"role": "assistant", "content": response.content})
                messages.append({"role": "user", "content": results})

        except KeyboardInterrupt:
            interrupted = True
            self.ui.interrupted()

        self.ui.accent(f"  {tool_count} tools used")

        if interrupted:
            return f"(subagent interrupted by user after {tool_count} tool calls)"

        if response is not None:
            for block in response.content:
                if isinstance(block, TextBlock):
                    return block.text

        return "(subagent returned no text)"
