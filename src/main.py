from src.instabot.agents import BlogPosterAgenst
from src.instabot.task import BlogPosterTask
from crewai import Crew, Process
from langchain_groq import ChatGroq


agents = BlogPosterAgenst()
task = BlogPosterTask()


# settingup agents
contant_planer = agents.contant_planer()
contant_writer = agents.contant_writer()
contant_editor = agents.contant_editor()
prompt_writer = agents.prompt_writer()

# setting up task 
plan_task = task.plan_task(agent=contant_planer)
write_task = task.writer_task(agent=contant_writer)
editor_task = task.editor_task(agent= contant_editor)
prompt_task = task.prompt_task(agent=prompt_writer)

crew = Crew(
    agents=[contant_planer,contant_writer,contant_editor],
    tasks= [plan_task, write_task,editor_task],
)

crew2 = Crew(
    agents=[prompt_writer],
    tasks= [prompt_task],
)


# aa = {"topic": "Artificial Intelligence"}
# #result = crew.kickoff(inputs=aa)
# result2 = crew2.kickoff(inputs=aa)

# #print(result)
# print(result2)