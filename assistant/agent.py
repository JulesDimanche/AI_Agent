from google.adk.agents import LlmAgent
tech_agent=LlmAgent(
    name='Tech_News_Agent',
    model='gemini-2.5-flash',
    description='An agent that provides the latest updates in technology news.',
    instruction="""You are Technical News Agent, your task is to provide the latest updates in technology news and AI related news. Always respond with the most recent and relevant information available.""",
)
root_agent=tech_agent