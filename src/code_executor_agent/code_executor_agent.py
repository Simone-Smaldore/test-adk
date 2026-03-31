from google.adk.agents.llm_agent import  LlmAgent
from google.adk.code_executors import BuiltInCodeExecutor

from src.const import SMART_MODEL_USED

code_executor_agent = LlmAgent(
    name="code_executor_agent",
    model=SMART_MODEL_USED,
    code_executor=BuiltInCodeExecutor(),
    instruction="""You are a calculator agent.
    When given a mathematical expression, write and execute Python code to calculate the result.
    Return only the final numerical result as plain text, without markdown or code blocks.
    """,
    description="Executes Python code to perform calculations.",
)
