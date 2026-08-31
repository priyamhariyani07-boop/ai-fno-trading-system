import yfinance as yf

# Download NIFTY 50 historical data
data = yf.download(
    "^NSEI",
    start="2020-01-01",
    end="2026-01-01",
    auto_adjust=False
)

# Save the raw downloaded data
data.to_csv("../data/raw/nifty50.csv")

print("NIFTY 50 data downloaded successfully.")
print("Rows and columns:", data.shape)
print("\nFirst 5 rows:")
print(data.head())