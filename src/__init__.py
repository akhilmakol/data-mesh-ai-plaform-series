"""
Data Mesh AI Platform Series package
"""

from .data_products import get_data_products
from .feature_pipeline import generate_features
from .agent_logic import interpret_query

__all__ = [
    "get_data_products",
    "generate_features",
    "interpret_query"
]

__version__ = "0.1.0"
__author__ = "Akhil Makol"
__description__ = "Reference architecture for Data Mesh + Agentic AI platforms"