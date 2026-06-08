import os 
from langgraph.graph import (
    StateGraph, START, END
)
from state import AgentState
from nodes import ( agent, search,)

def router(state):
    if state["final_answer"]:
        return "end"
    return "search"

builder = StateGraph(
    AgentState
)
 
builder.add_node("agent", agent)
builder.add_node("search", search)
 
builder.add_edge(START, "agent")
builder.add_conditional_edges(
    "agent",
    router,
    {
        "search": "search",
        "end": END
    }
)
builder.add_edge("search","agent")
graph =  builder.compile()

