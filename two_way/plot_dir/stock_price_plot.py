# filename: stock_price_plot.py
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Download historical data for NVIDIA and Tesla
nvda = yf.download('NVDA', start='2023-01-01', end='2023-10-01')
tsla = yf.download('TSLA', start='2023-01-01', end='2023-10-01')

# Extract 'Close' prices from the MultiIndex
nvda_close = nvda[('Close', 'NVDA')]
tsla_close = tsla[('Close', 'TSLA')]

# Calculate daily percentage change
nvda['Price Change'] = nvda_close.pct_change() * 100
tsla['Price Change'] = tsla_close.pct_change() * 100

# Drop the first row because it contains NaN after pct_change
nvda = nvda.dropna()
tsla = tsla.dropna()

# Plot NVIDIA price change
plt.figure(figsize=(14,7))
plt.plot(nvda.index, nvda['Price Change'], label='NVIDIA Price Change', color='blue')
plt.title('NVIDIA Stock Price Daily Percentage Change')
plt.xlabel('Date')
plt.ylabel('Percentage Change (%)')
plt.legend()
plt.grid(True)
plt.savefig('nvidia_price_change.png')
plt.close()

# Plot Tesla price change
plt.figure(figsize=(14,7))
plt.plot(tsla.index, tsla['Price Change'], label='Tesla Price Change', color='green')
plt.title('Tesla Stock Price Daily Percentage Change')
plt.xlabel('Date')
plt.ylabel('Percentage Change (%)')
plt.legend()
plt.grid(True)
plt.savefig('tesla_price_change.png')
plt.close()

print("Plots have been saved as 'nvidia_price_change.png' and 'tesla_price_change.png'.")