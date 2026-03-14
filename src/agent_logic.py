class Agent:

    def decide(self, input_signal):

        if input_signal == "high_risk_transaction":
            return "review"

        elif input_signal == "low_risk_transaction":
            return "approve"

        else:
            return "reject"


def interpret_query(query: str) -> str:
    """
    Simple AI agent query interpreter
    """

    query = query.lower()

    if "risk" in query:
        return "high_risk_transaction"

    elif "normal" in query:
        return "low_risk_transaction"

    return "unknown"