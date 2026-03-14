class Agent:

    def decide(self, input_signal):

        if input_signal == "high_risk_transaction":
            return "review"

        elif input_signal == "low_risk_transaction":
            return "approve"

        else:
            return "reject"