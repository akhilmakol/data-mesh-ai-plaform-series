import pandas as pd


def generate_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Generate simple feature engineering outputs
    for the Data Mesh AI platform demo.
    """

    df = df.copy()

    if "amount" in df.columns and "transactions" in df.columns:
        df["avg_transaction_value"] = df["amount"] / df["transactions"]

    return df