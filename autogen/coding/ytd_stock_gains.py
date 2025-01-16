# filename: ytd_stock_gains.py
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

# Define the stock symbols and the date range
stocks = ['NVDA', 'TSLA']
start_date = '2025-01-01'
end_date = '2025-01-16'

# Fetch historical stock data
data = {}
for stock in stocks:
    data[stock] = yf.download(stock, start=start_date, end=end_date)
    print(f"Data for {stock}:\n{data[stock]}\n")  # Print stock data

# Check if we have data for calculating YTD gains
for stock in stocks:
    if not data[stock].empty:
        ytd_gain = (data[stock]['Close'][-1] - data[stock]['Close'][0]) / data[stock]['Close'][0] * 100  # in percentage
        ytd_gains[stock] = ytd_gain
    else:
        ytd_gains[stock] = None  # No data available

# Plotting
ytd_gains_cleaned = {stock: gain for stock, gain in ytd_gains.items() if gain is not None}

plt.bar(ytd_gains_cleaned.keys(), ytd_gains_cleaned.values(), color=['blue', 'orange'])
plt.title('YTD Stock Gains for NVDA and TSLA (2025)')
plt.xlabel('Stocks')
plt.ylabel('YTD Gain (%)')
plt.ylim(-10, max(ytd_gains_cleaned.values()) + 10 if ytd_gains_cleaned else 10)
plt.axhline(0, color='grey', linewidth=0.8, linestyle='--')

# Save the figure
plt.savefig('ytd_stock_gains.png')
plt.show()