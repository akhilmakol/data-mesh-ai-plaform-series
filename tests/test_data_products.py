import pytest
from src.data_products import get_data_products

def test_data_products_exist():
    products = get_data_products()

    assert isinstance(products, list)
    assert len(products) > 0


def test_expected_domains_present():
    products = get_data_products()

    domains = [p["domain"] for p in products]

    assert "payments" in domains
    assert "risk" in domains
    assert "customer" in domains


def test_data_product_schema():
    products = get_data_products()

    product = products[0]

    assert "name" in product
    assert "domain" in product
    assert "owner" in product