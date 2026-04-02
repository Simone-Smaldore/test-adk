import os
import uvicorn
from fastapi import FastAPI
from google.adk.cli.fast_api import get_fast_api_app
from dotenv import load_dotenv

load_dotenv()

# Directory dove si trova main.py (e la cartella del tuo agente)
AGENT_DIR = os.path.dirname(os.path.abspath(__file__)) + "/src"

# Stringa di connessione PostgreSQL — usa asyncpg come driver async
SESSION_DB_URL = os.getenv(
    "DATABASE_URL"
)

print(">>> DATABASE_URL:", SESSION_DB_URL)

ALLOWED_ORIGINS = ["*"]  # In produzione, restringi agli origins reali

app: FastAPI = get_fast_api_app(
    agents_dir=AGENT_DIR,
    session_service_uri=SESSION_DB_URL,
    allow_origins=ALLOWED_ORIGINS,
    web=True,  # Abilita la Dev UI su /dev-ui/
)

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    uvicorn.run("main_uvicorn:app", host="0.0.0.0", port=8000, reload=True)