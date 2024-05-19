from crewai import Agent, Task, Crew
from langchain_openai import ChatOpenAI
import os



os.environ["OPENAI_API_KEY"] = "NA"

llm = ChatOpenAI(

    model = "mistralcrew",

    base_url = "http://localhost:11434/v1")


#agent1 researcher
researcher = Agent(role = "Expert AI researcher",

                      goal = """Comprehensive analysis of recent AI opportunities for tech solopreneurs""",

                      backstory = """You are an expert research analyst in AI and its advancements and tech market opportunities. You can provide comprehensive research and analysis of the existing opportunities for solopreneurs""",

                      allow_delegation = False,

                      verbose = True,

                      llm = llm)

#agent2 writer
writer = Agent(role = "Refiner and Expert AI Writer",

                      goal = """Refine the researcher's responses to make it more relevant and precise and then write expert-level explanation of core concepts and advancements in AI in friendly and accessible language.""",

                      backstory = """You are an expert in writing AI-related technical report in precise and actionable style for individual tech enthusiasts who need precise insight into opportunities in tech inductry. You are able to proofread your own text and produce a detailed report in an easy-to-follow and accessible language.""",

                      allow_delegation = False,

                      verbose = True,

                      llm = llm)

# Create tasks
task1 = Task(
  description="""Conduct a comprehensive analysis of the latest advancements in AI in 2024.
  Identify key trends, breakthrough technologies, and potential industry impacts and opportunities for solo entrepreneurs.""",
  expected_output="Full analysis report in bullet points",
  agent=researcher
)

task2 = Task(
  description="""Using the insights provided, develop a precise technical report
  that highlights the most significant opportunities in AI for solopreneurs.
  Your post should be informative yet accessible, catering to a tech-savvy audience.
  Write in accessible language and if needed briefly explain each technical term you introduce; proofread and edit your own report for a polished format.""",
  expected_output="Full report of at least 1000 words",
  agent=writer
)


# Instantiate your crew with a sequential process
crew = Crew(
  agents=[researcher, writer],
  tasks=[task1, task2],
  verbose=2, 
)


result = crew.kickoff()

print(result)
