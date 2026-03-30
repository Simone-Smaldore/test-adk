import os
import uvicorn
from google.adk.cli.fast_api import get_fast_api_app

BASE_DIR = os.path.abspath(os.path.dirname(__file__)) + "/src"

app = get_fast_api_app(
    agents_dir=BASE_DIR,
    allow_origins=["*"],  # permette tutte le origini (Codespaces incluso)
    web=True,
)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)