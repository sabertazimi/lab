from anthropic.types import (
    MessageParam,
    TextBlock,
    TextBlockParam,
    ToolResultBlockParam,
    ToolUseBlock,
)

from .agent import get_agent_description
from .llm import MODEL, WORKDIR, client
from .output import print_text, print_tool_call, print_tool_result
from .skill import skill_loader
from .task import task_manager
from .tools import ALL_TOOLS, execute_tool

SYSTEM = f"""You are Cyber Code, a world-class coding agent at {WORKDIR}.

Loop: plan -> act with tools -> report.

<available_skills>
Invoke with Skill tool when task matches:
{skill_loader.get_descriptions()}
</available_skills>


<available_subagents>
Invoke with Task tool for focused subtasks:
{get_agent_description()}
</available_subagents>

Rules:
- Use Skill tool IMMEDIATELY when a task matches a skill description.
- Use Task tool for subtasks needing focused exploration or implementation.
- Use TaskUpdate to track multi-step work.
- Prefer tools over prose. Act, don't just explain.
- After finishing, summarize what changed.

Commit footer: When you make changes that get committed, add this footer:
Co-authored-by: Cyber Code"""


def agent_loop(messages: list[MessageParam]) -> list[MessageParam]:
    """
    This is the pattern that ALL coding agents share:

        while True:
            response = model(messages, tools)
            if no tool calls: return
            execute tools, append results, continue
    """
    while True:
        # Step 1: Call the model
        response = client.messages.create(
            model=MODEL,
            system=SYSTEM,
            messages=messages,
            tools=ALL_TOOLS,
            max_tokens=8000,
        )

        # Step 2: Collect any tool calls and print text output
        tool_calls: list[ToolUseBlock] = []
        for block in response.content:
            if isinstance(block, TextBlock):
                print_text(block.text)
            if isinstance(block, ToolUseBlock):
                tool_calls.append(block)

        # Step 3: If not tool calls, task is complete
        if response.stop_reason != "tool_use":
            messages.append({"role": "assistant", "content": response.content})
            return messages

        # Step 4: Execute each tool and collect results
        results: list[ToolResultBlockParam | TextBlockParam] = []
        used_task = False

        for tool_call in tool_calls:
            print_tool_call(tool_call.name, tool_call.input)
            output = execute_tool(tool_call.name, tool_call.input)
            print_tool_result(output)

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
            task_manager.reset()
        else:
            task_manager.increment()

        # Step 5: Append to conversation and continue
        messages.append({"role": "assistant", "content": response.content})
        if task_manager.too_long_without_task():
            results.insert(0, {"type": "text", "text": task_manager.NAG_REMINDER})
        messages.append({"role": "user", "content": results})
