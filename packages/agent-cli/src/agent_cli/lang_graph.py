# pyright: reportMissingTypeStubs=none, reportUnknownVariableType=none, reportUnknownMemberType=none
import os
from typing import cast

from dotenv import find_dotenv, load_dotenv
from langchain.messages import AIMessage, HumanMessage, SystemMessage
from langchain.tools import tool
from langchain_openai import ChatOpenAI
from langgraph.graph import (
    END,
    START,
    MessagesState,
    StateGraph,
)
from langgraph.graph.state import (
    RunnableConfig,
)
from langgraph.prebuilt import ToolNode
from pydantic import SecretStr


@tool
def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"


def assistant(state: MessagesState, config: RunnableConfig):
    llm = config.get("configurable", {}).get("model")
    assert llm is not None
    system_prompt = "You are a helpful assistant that can check weather."
    all_messages = [SystemMessage(system_prompt)] + state["messages"]
    return {"messages": [llm.invoke(all_messages)]}


def should_continue(state: MessagesState):
    messages = state["messages"]
    last_message = cast(AIMessage, messages[-1])

    if last_message.tool_calls:
        return "continue"
    return "end"


def demo_state_graph() -> None:
    load_dotenv(find_dotenv())
    llm = ChatOpenAI(
        model="glm-5-turbo",
        temperature=0.7,
        base_url=os.getenv("OPENAI_BASE_URL"),
        api_key=cast(SecretStr, os.getenv("OPENAI_API_KEY")),
    )
    tools = [get_weather]
    tool_node = ToolNode(tools)
    model = llm.bind_tools(tools)

    workflow = StateGraph(MessagesState)
    workflow.add_node("assistant", assistant)
    workflow.add_node("tool", tool_node)
    workflow.add_edge(START, "assistant")
    workflow.add_conditional_edges(
        "assistant", should_continue, {"continue": "tool", "end": END}
    )
    workflow.add_edge("tool", "assistant")

    app = workflow.compile(name="app")
    response = app.invoke(
        {"messages": [HumanMessage(content="上海天气怎么样?")]},
        config={"configurable": {"model": model}},
    )

    for message in response["messages"]:
        message.pretty_print()


demo_state_graph()
