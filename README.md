# Blog Content Creation Agents with YouTube Integration

## Aim
The primary aim of this project is to develop and execute a crew of agents tasked with researching content from a YouTube channel and generating well-crafted blog posts. These agents work in tandem to gather video content and transform it into structured, engaging blog articles.

## Methodology
1. **Agents Setup:**
   - Two agents are created: 
     - **Blog Researcher Agent**: Extracts relevant video content from a specified YouTube channel based on a provided topic.
     - **Blog Writer Agent**: Generates a blog post based on the video content researched by the Blog Researcher.

2. **YouTube Search Tool:**
   - The project integrates a `YoutubeChannelSearchTool`, allowing the agents to search and retrieve videos from the specified YouTube channel (`@Badminton Insight`) based on the given topic.

3. **LLM Integration:**
   - Both agents are powered by GPT-4 through OpenAI's API. The large language model (LLM) is used to process and generate human-like content based on the video inputs.

4. **Tasks Execution:**
   - Two tasks are defined:
     1. **Research Task**: The Blog Researcher Agent is responsible for gathering and analyzing video content related to a given topic.
     2. **Writing Task**: The Blog Writer Agent summarizes the research findings into a well-structured blog post.
   
   - The tasks are executed in sequence using a `Crew` that manages the coordination between the agents and the tasks.

## Components
### Requirements
The following libraries are required for the project:
- `crewai`
- `crewai_tools`
- `load_dotenv`
- `langchain-huggingface`

crewai and crewai_tools: Handle agent-based task delegation and provide tools (like YouTube search) for external data retrieval.

load_dotenv: Ensures secure and easy access to environment variables, such as API keys.

langchain-huggingface: Enables integration and efficient usage of large language models (like GPT-4) to process and generate text-based outputs, which is key to the blog writing and research functionality of the agents.

### Agent Definitions
- **Blog Researcher Agent:**
   - **Role**: Blog researcher from YouTube videos.
   - **Goal**: Retrieve relevant video content from a YouTube channel based on a specific topic.
   - **Backstory**: Expert in understanding videos related to badminton coaching, gameplay, and tips to improve player performance.
   - **Tools**: YouTube search tool.
   - **LLM**: GPT-4 model.

- **Blog Writer Agent:**
   - **Role**: Blog writer.
   - **Goal**: Create compelling blog content based on YouTube video summaries.
   - **Backstory**: Skilled at simplifying complex information and crafting engaging narratives.
   - **Tools**: YouTube search tool.
   - **LLM**: GPT-4 model.

### Tools Definition
- **YouTube Channel Search Tool**: 
   - Utilized by both agents to search the YouTube channel `@Badminton Insight` for relevant videos.

### Task Definitions
- **Research Task**: 
   - **Description**: Identify and research video content based on the topic.
   - **Expected Output**: A 3-paragraph comprehensive report summarizing the video content.
   - **Agent**: Blog Researcher.
   
- **Writing Task**: 
   - **Description**: Summarize video content and create blog content based on the topic.
   - **Expected Output**: Blog content in markdown format (`new-blog-post.md`).
   - **Agent**: Blog Writer.

### Crew Process
The `Crew` orchestrates the agents and tasks:
- **Process**: Sequential execution of tasks.
- **Memory & Cache**: Used to store intermediate results and reuse past data.
- **Max RPM**: 100 requests per minute to avoid API overload.
- **Task Execution**: The crew kicks off by processing the input topic: _"How To Defend A Powerful Smash In Badminton (6 Steps)"_.

## Evaluation Metrics
- **Relevance of Video Content**: Accuracy in retrieving and analyzing video content based on the provided topic.
- **Coherence of Blog Content**: How well the generated blog post aligns with the research and video content.
- **User Feedback**: Effectiveness of the generated blog post in engaging readers and providing valuable insights.

## Results
Upon executing the `crew.kickoff()` method with the topic _"How To Defend A Powerful Smash In Badminton (6 Steps)"_, the following outcomes are expected:
- A detailed research report summarizing the video content.
- A well-structured blog post providing insights into defending a powerful smash in badminton.

## Conclusion
This project demonstrates an effective workflow for automating blog content creation from YouTube videos. The integration of agents, powered by large language models (LLMs) and the YouTube search tool, enables seamless research and writing tasks.

## Future Work
- **Enhanced Video Analysis**: Incorporating video transcript analysis to provide deeper insights into video content.
- **Topic Diversification**: Expanding the tool's scope to support a wider range of YouTube channels and topics.
- **Multilingual Support**: Adding support for generating blog content in multiple languages.
- **Content Personalization**: Using AI to personalize blog content based on user preferences or reading habits.

## How to Run
1. Clone the repository.
2. Install the dependencies using `pip install -r requirements.txt`.
3. Configure your OpenAI API key in the `.env` file.
4. Run the script `crew.py` to kick off the process.
