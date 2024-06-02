from crewai import Task



class BlogPosterTask():
    
    def __init__(self):
        pass

        
    def plan_task(self, agent):
        return Task(
           description = ("""1. Prioritize the latest trends, key players, and noteworthy news on {topic}.
                            2. Identify the target audience, considering their interests and pain points.
                            3. Develop a detailed content outline including an introduction, key points, and a call to action.
                            4. Include SEO keywords and relevant data or sources."""),
           expected_output = """
                            A comprehensive content plan document
                            with an outline, audience analysis,
                            SEO keywords, and resources.
           """,
           agent = agent,
        )
        
    def writer_task(self, agent):
        return Task(
           description = ("""1. Use the content plan to craft a compelling blog post on {topic}.
                             2. Incorporate SEO keywords naturally.
                             3. Sections/Subtitles are properly named in an engaging manner.
                             4. Ensure the post is structured with an engaging introduction, insightful body, and a summarizing conclusion.
                             5. Proofread for grammatical errors and alignment with the brand's voice."""),
           expected_output = """A well-written blog post
                                in markdown format, ready for publication,
                                each section should have 2 or 3 paragraphs.""",
           agent = agent,
        )
        
    
    def editor_task(self, agent):
        return Task(
           description = ("""Proofread the given blog post for
                          grammatical errors and 
                          alignment with the brand's voice."""),
           expected_output = """
                       A well-written blog post in markdown format,
                      ready for publication,
                      each section should have 2 or 3 paragraphs.
           """,
           agent = agent
        )
    def prompt_task(self, agent):
        return Task(
           description =("""Generate prompts for the most amazing photo ever for an Instagram post.{topic}"""),
           expected_output = """ Craft a compelling visual narrative capturing various scenes and messages
                                through a series of captivating images. Each image should vividly depict a unique
                                aspect of the story, engaging the audience and evoking curiosity..""",
           agent = agent,
        )
        
    