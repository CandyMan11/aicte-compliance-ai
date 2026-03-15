import requests
from config import LLM_API_KEY, LLM_API_URL, MODEL_NAME

def call_llm(prompt):
    headers = {
        "Authorization": f"Bearer {LLM_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": MODEL_NAME,
        "messages": [
            {"role": "system", "content": "You are a strict compliance auditor."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.2
    }

    response = requests.post(LLM_API_URL, headers=headers, json=payload)
    return response.json()