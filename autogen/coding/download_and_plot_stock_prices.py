# filename: download_and_plot_stock_prices.py
import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

# Define the stock symbols and the date range
tickers = ['NVDA', 'TSLA']
start_date = '2025-01-01'
end_date = '2025-01-16'

# Download the stock price data
data = yf.download(tickers, start=start_date, end=end_date)

# Plot the adjusted close prices
plt.figure(figsize=(10, 5))
for ticker in tickers:
    plt.plot(data['Adj Close'][ticker], label=ticker)

plt.title('Stock Prices YTD for NVDA and TSLA')
plt.xlabel('Date')
plt.ylabel('Adjusted Close Price (USD)')
plt.legend()
plt.grid(True)

# Save the plot to a file
plt.savefig('stock_prices_YTD_plot.png')
plt.close()