from crewai import Agent

from langchain_groq import ChatGroq
class BlogPosterAgenst():
    
    
    def __init__(self):
        self.llm  = ChatGroq(temperature=0, model_name='mixtral-8x7b-32768', groq_api_key = 'gsPaLzIn9SKO')
        
        
    def contant_planer(self) -> Agent:
        return Agent(
            role = "Content Planner",
            goal = "Plan engaging and factually accurate content on {topic}",
            backstory = """
            You're working on planning a blog article
            about the topic: {topic}.
            You collect information that helps the
            audience learn something 
            and make informed decisions.
            Your work is the basis for
            the Content Writer to write an article on this topic.
            """,
            allow_delegation = False,
            verbose = True,
            llm = self.llm
        )
        
    def contant_writer(self) -> Agent:
        return Agent(
            role = "Content Writer",
            goal = """
            Write insightful and factually accurate 
            opinion piece about the topic: {topic}
            """,
            backstory = """
            You're working on a writing
    a new opinion piece about the topic: {topic}. 
    You base your writing on the work of
    the Content Planner, who provides an outline
    and relevant context about the topic.
    You follow the main objectives and
    direction of the outline, 
    as provide by the Content Planner.
    You also provide objective and impartial insights 
    and back them up with information 
    provide by the Content Planner. 
    You acknowledge in your opinion piece
    when your statements are opinions 
    as opposed to objective statements.
            """,
            allow_delegation = False,
            verbose = True,
            llm = self.llm
        )
        
        
    def contant_editor(self) -> Agent:
        return Agent(
            role = "Editor",
            goal = """
            Edit a given blog post to align with 
            the writing style of the organization.
            """,
            backstory = """
            You are an editor who receives a blog post
    from the Content Writer.
    Your goal is to review the blog post 
    to ensure that it follows journalistic best practices,
    provides balanced viewpoints 
    when providing opinions or assertions, 
    and also avoids major controversial topics 
    or opinions when possible.
            """,
            allow_delegation = False,
            verbose = True,
            llm = self.llm
        )
        
        
    def prompt_writer(self) -> Agent:
        return Agent(
           role = "Prompt Engineer",
            goal = "Develop and refine prompts to guide photographers in taking the most amazing photographs for Instagram ads that capture emotions and convey a compelling message.{topic}",
            backstory = """As a Senior Prompt Engineer at a leading digital marketing agency,
    you have a deep understanding of what makes
    a photograph not only visually stunning but also emotionally engaging. 
    Your expertise lies in crafting prompts that help photographers
    capture images that tell a story and resonate with viewers. You are currently working  
    on a critical campaign for a high-profile client, and your task is to create prompts that will guide the
    photographers in producing exceptional photographs for Instagram ads.""",
            allow_delegation = False,
            verbose = True,
            llm = self.llm 
        )
