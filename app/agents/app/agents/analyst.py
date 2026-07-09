from crewai import Agent
from langchain_openai import ChatOpenAI
from app.core.config import settings

def create_analyst_agent():
    """Create the Analyst agent responsible for synthesis."""
    
    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0.2,
        api_key=settings.OPENAI_API_KEY
    )
    
    return Agent(
        role="Senior Data Analyst",
        goal="Synthesise findings into clear, coherent themes",
        backstory="""You are a seasoned analyst who excels at pattern recognition. 
        You never invent data; you only work with what the Researcher provides.""",
        tools=[],
        llm=llm,
        verbose=True,
        allow_delegation=False,
    )