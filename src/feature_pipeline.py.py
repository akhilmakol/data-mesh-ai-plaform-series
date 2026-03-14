from src.agent_logic import interpret_query


def test_agent_understands_payment_query():

    query = "show payment transactions"

    result = interpret_query(query)

    assert result["domain"] == "payments"


def test_agent_understands_risk_query():

    query = "get risk score for customer"

    result = interpret_query(query)

    assert result["domain"] == "risk"


def test_agent_returns_action():

    query = "customer profile"

    result = interpret_query(query)

    assert "action" in result