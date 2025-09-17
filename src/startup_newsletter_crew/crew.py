from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai_tools import WebsiteSearchTool
from typing import List


@CrewBase
class StartupNewsletterCrew():
    """StartupNewsletterCrew crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    website_tool = WebsiteSearchTool(website="https://www.deutsche-startups.de/taeglich/")

    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['researcher'], 
            tools=[self.website_tool],
            verbose=True
        )

    @agent
    def reporter(self) -> Agent:
        return Agent(
            config=self.agents_config['reporter'], 
            verbose=True
        )

    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_task'], 
        )

    @task
    def reporting_task(self) -> Task:
        return Task(
            config=self.tasks_config['reporting_task'], 
        )

    @crew
    def crew(self) -> Crew:
        """Creates the StartupNewsletterCrew crew"""

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
