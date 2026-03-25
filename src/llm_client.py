import requests
from src.config import LLM_API_KEY, LLM_API_URL, MODEL_NAME


# def call_llm(prompt: str):

#     headers = {
#         "Authorization": f"Bearer {LLM_API_KEY}",
#         "Content-Type": "application/json"
#     }

#     payload = {
#         "model": MODEL_NAME,
#         "messages": [
#             {"role": "system", "content": "You are a strict compliance auditor."},
#             {"role": "user", "content": prompt}
#         ],
#         "temperature": 0.2
#     }

#     response = requests.post(
#         LLM_API_URL,
#         headers=headers,
#         json=payload,
#         timeout=60
#     )

#     return response.json()

def call_llm(prompt: str):

    # TEMP MOCK RESPONSE (for development without API)
    mock_response = {
        "decision": "ACCEPTED",
        "confidence_score": 78,
        "reasoning": "The provided documents indicate compliance with the requirement.",
        "suggestions": "Include more supporting evidence for stronger validation."
    }

    return mock_response