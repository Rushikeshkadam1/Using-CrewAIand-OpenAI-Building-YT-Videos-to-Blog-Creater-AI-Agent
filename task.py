from crewai import Task
from tools import yt_tool
from agents import blog_researcher, blog_writer

# researcher task
research_task = Task(
    description=(
        "Identify the video {topic}."
        "Get detailed information about the video from the channel."
    ),
    expected_output= "a comprehensive 3 paragraphs long report based on the {topic} of the video content.",
    tools=[yt_tool],
    agent=blog_researcher
)

# Writting task with language model configuration
write_task = Task(
    description = (
        "get the info from the the youtube channel on the topic {topic}."
    ),
    expected_output = 'Summerize the info from the youtube channel video on the topic {topic} and create the content for blog',
    tools= [yt_tool],
    agent=blog_writer,
    async_execution=False,
    output_file='new-blog-post.md'
)