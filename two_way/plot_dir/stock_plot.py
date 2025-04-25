# filename: stock_plot.py
import yfinance as yf
import matplotlib.pyplot as plt

# Define the tickers
tickers = ['NVDA', 'TSLA']

# Download historical data for NVIDIA and Tesla
data = yf.download(tickers, start="2022-01-01", end="2023-01-01")

# Print the columns of the downloaded data to inspect structure
print("Data Columns:", data.columns)

# Ensure we select the correct column (likely 'Close' instead of 'Adj Close')
if 'Adj Close' in data.columns.get_level_values(1):
    price_data = data['Adj Close']
else:
    price_data = data['Close']

# Calculate daily percentage change
daily_returns = price_data.pct_change()

# Plot the stock price changes
plt.figure(figsize=(14, 7))
for ticker in tickers:
    plt.plot(daily_returns.index, daily_returns[ticker], label=ticker)

plt.title('NVIDIA vs Tesla Stock Price Changes')
plt.xlabel('Date')
plt.ylabel('Daily Percentage Change')
plt.legend()
plt.grid(True)
plt.savefig("hi.png")
plt.close()