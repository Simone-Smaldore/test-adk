from google.adk.agents.llm_agent import Agent

from src.const import SMART_MODEL_USED
from src.tools.greeting_tools import say_hello

greeting_agent  = Agent(
    model=SMART_MODEL_USED,
    name='greeting_agent',
    description=
    "Handles simple greetings and hellos using the 'say_hello' tool.",
    instruction=
    "You are the Greeting Agent. Your ONLY task is to provide a friendly greeting to the user. "
    "Use the 'say_hello' tool to generate the greeting. "
    "If the user provides their name, make sure to pass it to the tool. "
    "Do not engage in any other conversation or tasks.",
    tools=[say_hello],
    disallow_transfer_to_parent=True)
