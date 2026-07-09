from crewai import Agent
from app.core.config import settings

def create_analyst_agent():
    return Agent(
        role='Senior Data Analyst',
        goal='Synthesise findings into clear, coherent themes',
        backstory='You are a seasoned analyst who excels at pattern recognition.',
        tools=[],
        llm='gpt-4o-mini',
        verbose=True,
        allow_delegation=False,
    )
