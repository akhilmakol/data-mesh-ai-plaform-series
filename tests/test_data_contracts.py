import pytest

# Example Data Mesh data contracts
DATA_CONTRACTS = [
    {
        "name": "payments_transactions",
        "domain": "payments",
        "owner": "payments_team",
        "schema": ["transaction_id", "amount", "timestamp"]
    },
    {
        "name": "customer_profile",
        "domain": "customer",
        "owner": "customer_team",
        "schema": ["customer_id", "name", "email"]
    },
    {
        "name": "risk_scores",
        "domain": "risk",
        "owner": "risk_team",
        "schema": ["customer_id", "risk_score", "model_version"]
    }
]


def test_data_contracts_exist():
    """
    Ensure at least one data product contract exists
    """
    assert isinstance(DATA_CONTRACTS, list)
    assert len(DATA_CONTRACTS) > 0


def test_contract_required_fields():
    """
    Validate required metadata fields for data products
    """
    required_fields = ["name", "domain", "owner", "schema"]

    for contract in DATA_CONTRACTS:
        for field in required_fields:
            assert field in contract


def test_schema_is_defined():
    """
    Validate schema definition exists for each contract
    """
    for contract in DATA_CONTRACTS:
        schema = contract["schema"]

        assert isinstance(schema, list)
        assert len(schema) > 0


def test_domain_validity():
    """
    Validate domain ownership aligns with Data Mesh domains
    """
    valid_domains = ["payments", "customer", "risk"]

    for contract in DATA_CONTRACTS:
        assert contract["domain"] in valid_domains


def test_unique_data_product_names():
    """
    Ensure no duplicate data product names exist
    """
    names = [contract["name"] for contract in DATA_CONTRACTS]

    assert len(names) == len(set(names))