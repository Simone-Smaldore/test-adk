from google.adk.agents.llm_agent import Agent

from src.const import SMART_MODEL_USED
from src.greeting_agent.greeting_agent import greeting_agent
from src.farewell_agent.agent import farewell_agent
from src.tools.weather_tools import get_weather_stateful

root_agent = weather_agent_v3 = Agent(
    model=SMART_MODEL_USED,
    name='weather_agent_v3',
    description=
    "Main agent: Provides weather (state-aware unit), delegates greetings/farewells, saves report to state.",
    instruction=
    "You are the main Weather Agent. Your job is to provide weather using 'get_weather_stateful'. "
    "The tool will format the temperature based on user preference stored in state. "
    "Delegate simple greetings to 'greeting_agent' and farewells to 'farewell_agent'. "
    "Handle only weather requests, greetings, and farewells.",
    tools=[get_weather_stateful],  # Use the state-aware tool
    sub_agents=[greeting_agent, farewell_agent],  # Include sub-agents
    output_key="last_weather_report")
