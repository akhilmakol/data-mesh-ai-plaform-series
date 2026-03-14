import pandas as pd

customers = pd.read_csv("../../datasets/customers.csv")
loans = pd.read_csv("../../datasets/loans.csv")

features = customers.merge(loans,on="customer_id")

print(features.head())
