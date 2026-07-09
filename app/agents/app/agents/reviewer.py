from crewai import Agent
from langchain_openai import ChatOpenAI
from app.core.config import settings

def create_reviewer_agent():
    """Create the Reviewer agent responsible for quality control."""
    
    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0.1,
        api_key=settings.OPENAI_API_KEY
    )
    
    return Agent(
        role="Quality & Citation Reviewer",
        goal="Verify every claim is supported and correctly cited",
        backstory="""You are a skeptical fact-checker. You have no tools and cannot browse – 
        you only compare the draft against the supplied research notes.""",
        tools=[],
        llm=llm,
        verbose=True,
        allow_delegation=False,
    )