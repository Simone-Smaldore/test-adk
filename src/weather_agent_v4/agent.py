from google.adk.agents.llm_agent import Agent

from src.callback_guardrails.callback_tool import block_paris_tool_guardrail
from src.farewell_agent.agent import farewell_agent
from src.greeting_agent.agent import greeting_agent
from src.callback_guardrails.callback_model import block_keyword_guardrail
from src.const import SMART_MODEL_USED
from src.tools.weather_tools import get_weather_stateful

root_agent = weather_agent_v4 = Agent(
    model=SMART_MODEL_USED,
    name='weather_agent_v4',
    description=
    "Main agent: Handles weather, delegates greetings/farewells, includes input keyword guardrail.",
    instruction=
    "You are the main Weather Agent. Provide weather using 'get_weather_stateful'. "
    "Delegate simple greetings to 'greeting_agent' and farewells to 'farewell_agent'. "
    "Handle only weather requests, greetings, and farewells.",
    tools=[get_weather_stateful],
    sub_agents=[greeting_agent,
                farewell_agent],  # Reference the redefined sub-agents
    output_key="last_weather_report",  # Keep output_key from Step 4
    before_model_callback=block_keyword_guardrail,
    before_tool_callback=block_paris_tool_guardrail)
