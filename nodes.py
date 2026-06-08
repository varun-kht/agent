import os 
from llm import ask_llm
from tools.search import search_web

def planner(state):
    prompt = f"""
    Topic:
    {state['topic']}

    List exactly 5 AI startups.

    Return only startup names.
    One per line.
    """

    
    result = ask_llm(prompt)
    companies = [
        line.strip()
        for line in result.split("\n")
        if line.strip()
    ]
    return {
        **state, 
        "companies" : companies
    }

def research(state):
    findings=[]
    for company in state["companies"]:
        print(f"researching{company}....")
        search_results = search_web(
    f"{company} latest funding round")
        prompt = f"""
        Company:
        {company}

        Search Results:

        {search_results}

        Extract:

        - company description
        - latest funding round
        - funding amount
        - funding date
       """
        

        result = ask_llm(prompt)

        findings.append(
            {
                "company": company,
                "research": result
            }
        )
        return {
            **state,
            "findings":findings
        }
    

def writer(state):
    findings_text=""
    for item in state["findings"]:
        findings_text += f"""
        company:{item['company']}
        Research:{item['research']}
        """
        prompt = f"""
    Create a markdown report.

    Research:

    {findings_text}

    Include:

    - Company
    - Description
    - Funding Round
    - Funding Date
    - Funding Amount

    Format as markdown table.
    """
    report = ask_llm(prompt)
    return{
        **state,
        "report": report 
    }