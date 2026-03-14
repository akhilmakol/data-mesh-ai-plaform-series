def interpret_query(query: str):

    query = query.lower()

    if "payment" in query:
        return {"domain": "payments", "action": "fetch_transactions"}

    if "risk" in query:
        return {"domain": "risk", "action": "fetch_risk_score"}

    if "customer" in query:
        return {"domain": "customer", "action": "fetch_customer_profile"}

    return {"domain": "unknown", "action": "none"}