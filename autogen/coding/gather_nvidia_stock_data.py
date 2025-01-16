# filename: gather_nvidia_stock_data.py
import yfinance as yf
from datetime import datetime, timedelta

# Define the stock ticker symbol and date range
ticker_symbol = "NVDA"
end_date = datetime.now()
start_date = end_date - timedelta(days=30)

# Fetch current stock price
current_stock = yf.Ticker(ticker_symbol)
current_price = current_stock.history(period='1d')['Close'][-1]

# Fetch historical stock prices for the last month
historical_data = current_stock.history(start=start_date, end=end_date)

# Calculate key metrics
highest_price = historical_data['High'].max()
lowest_price = historical_data['Low'].min()
percentage_change = ((current_price - historical_data['Close'][0]) / historical_data['Close'][0]) * 100

# Print the results
print(f"Current Price: ${current_price:.2f}")
print(f"Highest Price in the last month: ${highest_price:.2f}")
print(f"Lowest Price in the last month: ${lowest_price:.2f}")
print(f"Percentage Change over the month: {percentage_change:.2f}%")