def build_prompt(question, evidence):
    return f"""
You are an AICTE compliance auditor.

Question:
{question}

Evidence:
{evidence}

Return JSON:
{{
  "decision": "ACCEPTED or DECLINED",
  "confidence_score": 0-100,
  "reasoning": "...",
  "suggestions": "..."
}}
"""