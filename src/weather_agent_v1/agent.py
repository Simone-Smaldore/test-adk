from google.adk.agents.llm_agent import Agent

from src.const import CHEAP_MODEL_USED
from src.tools.weather_tools import get_weather

# Example tool usage (optional test)

root_agent = weather_agent_v1 = Agent(
    model=CHEAP_MODEL_USED,
    name='weather_agent_v1',
    description='You are a helpful weather assistant. ',
    instruction="You are a helpful weather assistant. "
    "When the user asks for the weather in a specific city, "
    "use the 'get_weather' tool to find the information. "
    "If the tool returns an error, inform the user politely. "
    "If the tool is successful, present the weather report clearly.",
    tools=[get_weather])
