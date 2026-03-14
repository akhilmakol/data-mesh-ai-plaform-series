import pandas as pd
from src.feature_pipeline import generate_features


def test_feature_generation_returns_dataframe():
    input_data = pd.DataFrame({
        "amount": [100, 200, 300],
        "transactions": [1, 2, 3]
    })

    result = generate_features(input_data)

    assert isinstance(result, pd.DataFrame)


def test_feature_columns_created():
    input_data = pd.DataFrame({
        "amount": [100, 200],
        "transactions": [1, 2]
    })

    result = generate_features(input_data)

    assert "avg_transaction_value" in result.columns


def test_no_null_values_in_features():
    input_data = pd.DataFrame({
        "amount": [100, 200],
        "transactions": [1, 2]
    })

    result = generate_features(input_data)

    assert result.isnull().sum().sum() == 0


def test_generate_features_missing_columns():
    df = pd.DataFrame({
        "amount": [100, 200]
    })

    result = generate_features(df)

    assert "avg_transaction_value" not in result.columns