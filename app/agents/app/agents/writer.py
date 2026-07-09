from crewai import Agent
from langchain_openai import ChatOpenAI
from app.core.config import settings

def create_writer_agent():
    """Create the Writer agent responsible for producing the final report."""
    
    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0.3,
        api_key=settings.OPENAI_API_KEY
    )
    
    return Agent(
        role="Technical Writer",
        goal="Produce a well-structured, professional research report",
        backstory="""You are a skilled writer with experience in research communications. 
        You excel at making complex topics accessible without sacrificing accuracy.""",
        tools=[],
        llm=llm,
        verbose=True,
        allow_delegation=False,
    )