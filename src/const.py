from google.adk.models import Gemini

MODEL_GEMINI = 'gemini-3.1-flash-lite-preview'
MODEL_GEMMA = Gemini(model="gemma-4-31b-it")
# Un modello piu semplice per evitare di spendere troppo
CHEAP_MODEL_USED = MODEL_GEMMA
# Un modello piu complicato per evitare un loop di chiamate
SMART_MODEL_USED = MODEL_GEMMA
