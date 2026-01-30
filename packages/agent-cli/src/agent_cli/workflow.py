from anthropic.types import (
    MessageParam,
    TextBlock,
    TextBlockParam,
    ToolResultBlockParam,
    ToolUseBlock,
)

from .llm import MODEL, client
from .output import (
    print_interrupted,
    print_response,
    print_tool_call,
    print_tool_result,
)
from .system import SYSTEM
from .task import task_manager
from .tools import ALL_TOOLS, execute_tool


def agent_loop(messages: list[MessageParam]) -> list[MessageParam]:
    """
    This is the pattern that ALL coding agents share:

        while True:
            response = model(messages, tools)
            if no tool calls: return
            execute tools, append results, continue

    Handles Ctrl+C to gracefully interrupt the loop.
    """
    try:
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
                    print_response(block.text)
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

    except KeyboardInterrupt:
        print_interrupted()
        messages.append(
            {
                "role": "user",
                "content": """<system_notification type="task_interrupted">
User has pressed Ctrl+C to interrupt the current task.
Please acknowledge the interruption and summarize what was completed.
</system_notification>""",
            }
        )
        return messages
