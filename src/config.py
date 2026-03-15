import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_DIR = os.path.join(BASE_DIR, "data")
POLICY_DIR = os.path.join(DATA_DIR, "policies")

LLM_API_KEY = "YOUR_API_KEY"
LLM_API_URL = "https://api.openai.com/v1/chat/completions"
MODEL_NAME = "gpt-4o"