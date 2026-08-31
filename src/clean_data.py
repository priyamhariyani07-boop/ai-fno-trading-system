import pandas as pd

data = pd.read_csv(
    "../data/raw/nifty50.csv",
    skiprows=[1, 2]
)

data = data.rename(columns={"Price": "Date"})

data["Date"] = pd.to_datetime(data["Date"])

data = data[["Date", "Open", "High", "Low", "Close", "Volume"]]

print("Shape:", data.shape)

print("\nFirst 5 rows:")
print(data.head())

print("\nColumn names:")
print(data.columns)

print("\nData types:")
print(data.dtypes)

print("\nMissing values:")
print(data.isnull().sum())

print("\nDuplicate dates:")
print(data["Date"].duplicated().sum())

print("\nDates sorted:")
print(data["Date"].is_monotonic_increasing)

print("\nInvalid OHLC rows:")

invalid_ohlc = (
    (data["High"] < data["Open"]) |
    (data["High"] < data["Close"]) |
    (data["Low"] > data["Open"]) |
    (data["Low"] > data["Close"])
)

print(invalid_ohlc.sum())


data = data.set_index("Date")

data = data.sort_index()

data.to_csv("../data/processed/nifty50_clean.csv")

print("\nCleaned data saved successfully.")
print("Final shape:", data.shape)
print("\nFinal data:")
print(data.head())