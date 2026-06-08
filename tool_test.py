from ddgs import DDGS
from ddgs.exceptions import TimeoutException

def search_web(query):
    with DDGS() as ddgs:
        return list(ddgs.text(query, max_results=5))
    
results = search_web("list top 10 ai startup which recently got the funding have around 10-20 people in total in year 205 the most recent ")
print(results)