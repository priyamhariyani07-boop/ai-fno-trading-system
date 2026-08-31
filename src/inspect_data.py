import pandas as pd

# Load the raw NIFTY 50 data
data = pd.read_csv("../data/raw/nifty50.csv")

print("Shape:")
print(data.shape)

print("\nFirst 5 rows:")
print(data.head())

print("\nColumn names:")
print(data.columns)

print("\nData types:")
print(data.dtypes)

print("\nMissing values:")
print(data.isnull().sum())