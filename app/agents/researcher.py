from crewai import Agent
from app.core.config import settings

def create_researcher_agent():
    return Agent(
        role='Senior Research Specialist',
        goal='Gather comprehensive, credible information from diverse sources',
        backstory='You are a meticulous researcher who never states a fact without a source.',
        tools=[],
        llm='gpt-4o-mini',
        verbose=True,
        allow_delegation=False,
        max_iter=3,
    )
