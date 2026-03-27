from google.adk.agents.llm_agent import Agent

from src.const import SMART_MODEL_USED
from src.tools.greeting_tools import say_goodbye

farewell_agent = root_agent = Agent(
    model=SMART_MODEL_USED,
    name="farewell_agent",
    instruction=
    "You are the Farewell Agent. Your ONLY task is to provide a polite goodbye message. "
    "Use the 'say_goodbye' tool when the user indicates they are leaving or ending the conversation "
    "(e.g., using words like 'bye', 'goodbye', 'thanks bye', 'see you'). "
    "Do not perform any other actions.",
    description=
    "Handles simple farewells and goodbyes using the 'say_goodbye' tool.",
    tools=[say_goodbye],
    disallow_transfer_to_parent=True)
