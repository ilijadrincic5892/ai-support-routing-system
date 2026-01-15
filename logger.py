def route_decision(category: str):
    ai_allowed = ["informational", "account"]

    if category in ai_allowed:
        return "AI_CAN_HANDLE"
    else:
        return "HUMAN_REQUIRED"
