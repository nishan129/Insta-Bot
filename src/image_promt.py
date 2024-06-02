from crewai import Agent, Crew, Task, Process
from crewai.project import CrewBase, agent, crew , task
from langchain_groq import ChatGroq

@CrewBase
class ImagePrompt():
    """Image Prompt Generator"""
    agents_config = "instabot/config/agents.yaml"
    tasks_config = "instabot/config/task.yaml"
    
    def __init__(self) -> None:
        self.llm = ChatGroq(temperature=0, model_name='mixtral-8x7b-32768', groq_api_key = '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')
        
    @agent
    def prompt_engg(self) -> Agent:
        return Agent(
            config = self.agents_config['prompt'],
            llm = self.llm
        )
    
    @task
    def prompt_task(self) -> Task:
        return Task(
           config = self.tasks_config['prompt'],
           agent = self.prompt_engg()
        )
        
    @crew
    def crew(self) -> Crew:
        """Create the Prompt crew"""
        return Crew(
            agents = self.agents,
            tasks = self.tasks,
            process = Process.sequential,
            verbose = 2
        )