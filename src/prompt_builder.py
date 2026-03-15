def build_prompt(question: str, evidence: str):

    prompt = f"""
You are an AICTE compliance auditor.

Your task is to evaluate whether the institution satisfies
the compliance question using the provided evidence.

Question:
{question}

Evidence:
{evidence}

Return ONLY valid JSON in the format:

{{
  "decision": "ACCEPTED or DECLINED",
  "confidence_score": 0-100,
  "reasoning": "explain decision",
  "suggestions": "improvements if needed"
}}

Do not return anything outside JSON.
"""

    return prompt