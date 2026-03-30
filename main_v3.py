import os
import asyncio
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm  # For multi-model support
from google.adk.sessions import InMemorySessionService
from google.adk.runners import Runner
from google.genai import types  # For creating message Content/Parts
from dotenv import load_dotenv

import warnings

from src.weather_agent_v3.agent import weather_agent_v3
# Ignore all warnings
warnings.filterwarnings("ignore")

import logging

logging.basicConfig(level=logging.ERROR)

APP_NAME = "weather_tutorial_app"
USER_ID = "user_1"
SESSION_ID = "session_001"

session_service_stateful = InMemorySessionService()
load_dotenv()


async def init_session(app_name: str, user_id: str,
                       session_id: str) -> InMemorySessionService:

    session = await session_service_stateful.create_session(
        app_name=app_name, user_id=user_id, session_id=session_id)
    print(
        f"Session created: App='{app_name}', User='{user_id}', Session='{session_id}'"
    )
    return session


async def call_agent_async(query: str, runner, user_id, session_id):
    """Sends a query to the agent and prints the final response."""
    print(f"\n>>> User Query: {query}")

    # Prepare the user's message in ADK format
    content = types.Content(role='user', parts=[types.Part(text=query)])

    final_response_text = "Agent did not produce a final response."  # Default

    # Key Concept: run_async executes the agent logic and yields Events.
    # We iterate through events to find the final answer.
    async for event in runner.run_async(user_id=user_id,
                                        session_id=session_id,
                                        new_message=content):
        # You can uncomment the line below to see *all* events during execution
        # print(
        #     f"  [Event] Author: {event.author}, Type: {type(event).__name__}, Final: {event.is_final_response()}, Content: {event.content}"
        # )

        # Key Concept: is_final_response() marks the concluding message for the turn.
        if event.is_final_response():
            if event.content and event.content.parts:
                # Assuming text response in the first part
                final_response_text = event.content.parts[0].text
            elif event.actions and event.actions.escalate:  # Handle potential errors/escalations
                final_response_text = f"Agent escalated: {event.error_message or 'No specific message.'}"
            # Add more checks here if needed (e.g., specific error codes)
            break  # Stop processing events once the final response is found

    print(f"<<< Agent Response: {final_response_text}")


def aggiorna_stato_interno():
    print("\n--- Manually Updating State: Setting unit to Fahrenheit ---")
    try:
        # Access the internal storage directly - THIS IS SPECIFIC TO InMemorySessionService for testing
        # NOTE: In production with persistent services (Database, VertexAI), you would
        # typically update state via agent actions or specific service APIs if available,
        # not by direct manipulation of internal storage.
        stored_session = session_service_stateful.sessions[APP_NAME][USER_ID][
            SESSION_ID]
        stored_session.state["user_preference_temperature_unit"] = "Fahrenheit"
        # Optional: You might want to update the timestamp as well if any logic depends on it
        # import time
        # stored_session.last_update_time = time.time()
        print(
            f"--- Stored session state updated. Current 'user_preference_temperature_unit': {stored_session.state.get('user_preference_temperature_unit', 'Not Set')} ---"
        )  # Added .get for safety
    except KeyError:
        print(
            f"--- Error: Could not retrieve session '{SESSION_ID}' from internal storage for user '{USER_ID}' in app '{APP_NAME}' to update state. Check IDs and if session was created. ---"
        )
    except Exception as e:
        print(f"--- Error updating internal session state: {e} ---")


async def run_conversation(runner: Runner):
    await call_agent_async(query="What is the weather in London?",
                           runner=runner,
                           user_id=USER_ID,
                           session_id=SESSION_ID)
    aggiorna_stato_interno()
    await call_agent_async(query="What is the weather in New York?",
                           runner=runner,
                           user_id=USER_ID,
                           session_id=SESSION_ID)


def main():
    print("Hello from test-adk!")

    session = asyncio.run(init_session(APP_NAME, USER_ID, SESSION_ID))
    print(
        f"Session created: App='{APP_NAME}', User='{USER_ID}', Session='{SESSION_ID}'"
    )

    # --- Runner ---
    # Key Concept: Runner orchestrates the agent execution loop.
    runner = Runner(
        agent=weather_agent_v3,  # The agent we want to run
        app_name=APP_NAME,  # Associates runs with our app
        session_service=session_service_stateful  # Uses our session manager
    )
    print(f"Runner created for agent '{runner.agent.name}'.")
    asyncio.run(run_conversation(runner=runner))

    print("\n--- Inspecting Final Session State ---")
    final_session = asyncio.run(
        session_service_stateful.get_session(app_name=APP_NAME,
                                             user_id=USER_ID,
                                             session_id=SESSION_ID))
    if final_session:
        # Use .get() for safer access to potentially missing keys
        print(
            f"Final Preference: {final_session.state.get('user_preference_temperature_unit', 'Not Set')}"
        )
        print(
            f"Final Last Weather Report (from output_key): {final_session.state.get('last_weather_report', 'Not Set')}"
        )
        print(
            f"Final Last City Checked (by tool): {final_session.state.get('last_city_checked_stateful', 'Not Set')}"
        )
        # Print full state for detailed view
        # print(f"Full State Dict: {final_session.state}") # For detailed view
    else:
        print("\n❌ Error: Could not retrieve final session state.")


if __name__ == "__main__":
    main()
