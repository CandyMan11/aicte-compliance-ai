import json


def parse_llm_response(response):
    """
    Converts LLM response into structured dictionary.
    Handles both dict and string responses.
    """

    # Case 1: Already a dictionary (mock response)
    if isinstance(response, dict):

        # if API error present
        if "error" in response:
            return {
                "decision": "DECLINED",
                "confidence_score": 0,
                "reasoning": response["error"]["message"],
                "suggestions": "Fix API issue"
            }

        return {
            "decision": response.get("decision", "UNKNOWN"),
            "confidence_score": response.get("confidence_score", 0),
            "reasoning": response.get("reasoning", ""),
            "suggestions": response.get("suggestions", "")
        }

    # Case 2: Response is string (real LLM)
    try:
        parsed = json.loads(response)

        return {
            "decision": parsed.get("decision", "UNKNOWN"),
            "confidence_score": parsed.get("confidence_score", 0),
            "reasoning": parsed.get("reasoning", ""),
            "suggestions": parsed.get("suggestions", "")
        }

    except Exception:

        # fallback if parsing fails
        return {
            "decision": "UNKNOWN",
            "confidence_score": 0,
            "reasoning": str(response),
            "suggestions": "LLM output parsing failed"
        }