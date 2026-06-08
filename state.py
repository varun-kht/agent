import os
#state defining -single source of truth for state
from typing import TypedDict

class AgentState(TypedDict):
    user_query: str
    search_query: str
    search_results: str
    final_answer: str

