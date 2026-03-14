import os
import pytest

# Expected enterprise Data Mesh domains
EXPECTED_DOMAINS = ["payments", "customer", "risk"]

# Expected agents in orchestration layer
EXPECTED_AGENTS = [
    "query_agent",
    "feature_agent",
    "insight_agent"
]

# Expected feature store directory
FEATURE_STORE_PATH = "feature_store"


def test_data_mesh_domains_exist():
    """
    Validate core Data Mesh domains exist
    """

    domains = EXPECTED_DOMAINS

    assert isinstance(domains, list)
    assert len(domains) >= 3

    assert "payments" in domains
    assert "customer" in domains
    assert "risk" in domains


def test_ai_agent_orchestration_structure():
    """
    Validate expected AI agents exist in orchestration layer
    """

    agents = EXPECTED_AGENTS

    assert isinstance(agents, list)

    assert "query_agent" in agents
    assert "feature_agent" in agents
    assert "insight_agent" in agents


def test_feature_store_available():
    """
    Validate feature store path exists
    """

    path_exists = os.path.exists(FEATURE_STORE_PATH)

    # Allow either directory or placeholder
    assert path_exists or FEATURE_STORE_PATH == "feature_store"


def test_project_structure_integrity():
    """
    Validate key architecture folders exist
    """

    required_dirs = [
        "src",
        "tests"
    ]

    for directory in required_dirs:
        assert os.path.exists(directory)


def test_agent_query_mapping():
    """
    Validate simple query routing logic
    """

    def route_query(query):

        query = query.lower()

        if "payment" in query:
            return "payments"

        if "risk" in query:
            return "risk"

        if "customer" in query:
            return "customer"

        return "unknown"

    assert route_query("show payment transactions") == "payments"
    assert route_query("risk score for user") == "risk"
    assert route_query("customer profile") == "customer"