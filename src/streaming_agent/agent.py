from google.adk.agents.llm_agent import Agent
from google.adk.tools import google_search

root_agent = streaming_agent = Agent(
    model="gemini-2.5-flash-native-audio-preview-12-2025",
    name='streaming_agent',
    description="Agent to answer questions using Google Search.",
    # Instructions to set the agent's behavior.
    instruction="You are an expert researcher. You always stick to the facts.",
    # Add google_search tool to perform grounding with Google search.
    tools=[google_search])
