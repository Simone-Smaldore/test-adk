# tests/test_all_agents.py
import sys
import pytest
from pathlib import Path
from google.adk.evaluation.agent_evaluator import AgentEvaluator

# Aggiungi src al Python path così i moduli agente sono importabili per nome
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

SRC_DIR = Path(__file__).parent.parent / "src"

@pytest.mark.asyncio
@pytest.mark.parametrize("agent,evalset", [
    ("greeting_agent", "greeting_agent/evalset_test_greeting.evalset.json"),
])
async def test_agent(agent, evalset):
    await AgentEvaluator.evaluate(
        agent,                           # nome modulo, non path assoluto
        str(SRC_DIR / evalset),          # path assoluto solo per l'evalset
        num_runs=1
    )