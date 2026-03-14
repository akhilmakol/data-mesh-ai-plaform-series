from src.agent_logic import Agent

def test_agent_initialization():
    agent = Agent()
    assert agent is not None


def test_agent_decision_output():
    agent = Agent()
    result = agent.decide("high_risk_transaction")
    assert result in ["approve", "review", "reject"]