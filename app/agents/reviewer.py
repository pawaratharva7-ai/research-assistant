from crewai import Agent
from app.core.config import settings

def create_reviewer_agent():
    return Agent(
        role='Quality Reviewer',
        goal='Verify every claim is supported and correctly cited',
        backstory='You are a skeptical fact-checker.',
        tools=[],
        llm='gpt-4o-mini',
        verbose=True,
        allow_delegation=False,
    )
