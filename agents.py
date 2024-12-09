from crewai import Agent
from tools import yt_tool

from dotenv import load_dotenv
load_dotenv()

import os
os.environ["OPENAI_API_KEY"]= os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_MODEL_NAME"]="gpt-4-0125-preview"



## Create a blog content researcher

blog_researcher = Agent(
    role='Blog researcher from youtube videos',
    goal = 'Get the relavent video content for the topic{topic} from Yt channel',
    verbose=True,
    memory=True,
    backstory=(
        "Expert in understanding videos related badminton coaching, gameplay, tricks and tips to improve performance of players and providing suggestions."
    ),
    tools=[yt_tool],
    llm = llm,
    allow_delegation=True
)


# Creating a senior blog writer agent with YT tool

blog_writer=Agent(
    role='Blog writer',
    goal= 'Narret compelling stories about the video {topic} from YT channel',
    verbose=True,
    memory=True,
    backstory=(
        "With a flair for simplifying information, you craft"
        "engaging narratives that captivate and educate, bringing new"
        "discoveries to light in an accessible mannner."
    ),
    tools=[yt_tool],
    llm = llm,
    allow_delegation=False
)