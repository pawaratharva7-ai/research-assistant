from crewai import Agent
from app.core.config import settings

def create_writer_agent():
    return Agent(
        role='Technical Writer',
        goal='Produce a professional research report',
        backstory='You are a skilled writer with experience in research communications.',
        tools=[],
        llm='gpt-4o-mini',
        verbose=True,
        allow_delegation=False,
    )
