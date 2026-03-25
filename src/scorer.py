def score_response(parsed_response):
    """
    Applies rule-based scoring on LLM output
    """

    confidence = parsed_response.get("confidence_score", 0)
    decision = parsed_response.get("decision", "UNKNOWN")

    # Rule 1: Strong confidence → ACCEPT
    if confidence >= 75:
        final_decision = "ACCEPTED"

    # Rule 2: Medium confidence → CONDITIONAL
    elif 50 <= confidence < 75:
        final_decision = "PARTIALLY ACCEPTED"

    # Rule 3: Low confidence → DECLINE
    else:
        final_decision = "DECLINED"

    return {
        "final_decision": final_decision,
        "confidence_score": confidence,
        "reasoning": parsed_response.get("reasoning", ""),
        "suggestions": parsed_response.get("suggestions", "")
    }