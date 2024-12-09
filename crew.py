from crewai import Crew, Process
from agents import blog_researcher, blog_writer
from tasks import research_task, write_task

# forming tthe crew with some enhanced configuration
crew = Crew(
    agents= [blog_researcher, blog_writer],
    tasks= [research_task, write_task],
    process=Process.sequential,
    memory=True,
    cache=True,
    max_rpm=100,
    share_crew=True
)


# satrt the task execution process with enhanced feedback
result=crew.kickoff(inputs={'topic':'How To Defend A Powerful Smash In Badminton (6 Steps)'})
print(result)