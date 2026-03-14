from src.agent_logic import Agent, interpret_query


def test_interpret_query_high_risk():
    assert interpret_query("check risk transaction") == "high_risk_transaction"


def test_interpret_query_low_risk():
    assert interpret_query("normal payment") == "low_risk_transaction"


def test_interpret_query_unknown():
    assert interpret_query("something random") == "unknown"


def test_agent_review():
    agent = Agent()
    assert agent.decide("high_risk_transaction") == "review"


def test_agent_approve():
    agent = Agent()
    assert agent.decide("low_risk_transaction") == "approve"


def test_agent_reject():
    agent = Agent()
    assert agent.decide("unknown") == "reject"