import os 
from graph import graph
initial_state={
    "user_query": "Who founded Anthropic?",
    "search_query": "",
    "search_results": "",
    "final_answer": "",
}
result = graph.invoke(initial_state)
print(
    result["final_answer"]
)
