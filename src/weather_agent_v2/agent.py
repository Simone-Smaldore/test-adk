from google.adk.agents.llm_agent import Agent

from src.const import SMART_MODEL_USED
from src.farewell_agent.agent import farewell_agent
from src.greeting_agent.greeting_agent import greeting_agent
from src.tools.weather_tools import get_weather

root_agent = weather_agent_v2 = Agent(
    model=SMART_MODEL_USED,
    name='weather_agent_v2',
    description=
    "The main coordinator agent. Handles weather requests and delegates greetings/farewells to specialists.",
    instruction="You are the main Weather Agent. "
    "Use the 'get_weather' tool for weather requests. "
    "For greetings or farewells, transfer to the appropriate specialist agent. "
    "Do not try to call sub-agents as if they were tools.",
    tools=[get_weather],
    sub_agents=[greeting_agent, farewell_agent])
