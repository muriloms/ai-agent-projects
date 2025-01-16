# filename: fetch_nvidia_stock_data.py
import yfinance as yf
from datetime import datetime, timedelta

# Define the ticker symbol for Nvidia
ticker_symbol = 'NVDA'

# Get today's date and the date one month ago
today = datetime(2024, 12, 23)
one_month_ago = today - timedelta(days=30)

# Fetch historical data for the past month
nvidia_data = yf.download(ticker_symbol, start=one_month_ago, end=today)

# Check if the data is available
if nvidia_data.empty:
    print("No data found for the specified date range.")
else:
    # Fetch the current stock price (last closing price)
    current_price = nvidia_data['Close'].iloc[-1]

    # Calculate the change in stock price and percentage change
    initial_price = nvidia_data['Close'].iloc[0]  # No conversion needed here, just use it directly
    price_change = current_price - initial_price
    percentage_change = (price_change / initial_price * 100) if initial_price != 0 else float('nan')

    # Fetch trading volume data correctly
    trading_volume = nvidia_data['Volume'].values  # Use .values to get a numpy array

    # Print the results
    print("Current Price:", current_price)
    print("Price Change:", price_change)
    print("Percentage Change: {:.2f}%".format(percentage_change))
    print("Trading Volume Over the Past Month:", trading_volume)