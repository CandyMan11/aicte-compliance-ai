import os
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_DIR = os.path.join(BASE_DIR, "data")
POLICY_DIR = os.path.join(DATA_DIR, "policies")
IMAGE_DIR = os.path.join(DATA_DIR, "images")

LLM_API_KEY = os.getenv("OPENAI_API_KEY")

LLM_API_URL = "https://api.openai.com/v1/chat/completions"

MODEL_NAME = "gpt-4o"