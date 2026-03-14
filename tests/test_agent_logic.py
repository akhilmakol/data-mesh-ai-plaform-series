from src.agent_logic import Agent, interpret_query

def test_agent_initialization():
    agent = Agent()
    assert agent is not None


def test_agent_decision_output():
    agent = Agent()
    result = agent.decide("high_risk_transaction")
    assert result in ["approve", "review", "reject"]


def test_interpret_query_high_risk():
    assert interpret_query("check risk transaction") == "high_risk_transaction"


def test_agent_review():
    agent = Agent()
    assert agent.decide("high_risk_transaction") == "review"    