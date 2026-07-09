from crewai import Crew, Task, Process
from app.agents.researcher import create_researcher_agent
from app.agents.analyst import create_analyst_agent
from app.agents.writer import create_writer_agent
from app.agents.reviewer import create_reviewer_agent

def build_research_crew(topic: str):
    """Build and return a Crew with all agents and tasks."""
    
    researcher = create_researcher_agent()
    analyst = create_analyst_agent()
    writer = create_writer_agent()
    reviewer = create_reviewer_agent()
    
    research_task = Task(
        description=f"Research the topic: '{topic}'. Gather at least 5 key findings.",
        expected_output="A list of findings with supporting evidence.",
        agent=researcher,
    )
    
    analysis_task = Task(
        description="Synthesise the research findings into 3-5 key themes.",
        expected_output="Themes with supporting evidence.",
        agent=analyst,
        context=[research_task],
    )
    
    writing_task = Task(
        description="Write a structured research report with executive summary, themed sections, and references.",
        expected_output="A well-formatted markdown report.",
        agent=writer,
        context=[analysis_task],
    )
    
    review_task = Task(
        description="Review the draft against the research findings. Flag any unsupported claims.",
        expected_output="The final report with review notes.",
        agent=reviewer,
        context=[research_task, writing_task],
    )
    
    return Crew(
        agents=[researcher, analyst, writer, reviewer],
        tasks=[research_task, analysis_task, writing_task, review_task],
        process=Process.sequential,
        verbose=True,
    )