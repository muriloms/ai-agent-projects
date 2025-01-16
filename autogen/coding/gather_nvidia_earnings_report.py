# filename: gather_nvidia_earnings_report.py
import yfinance as yf

# Define the stock ticker symbol
ticker_symbol = "NVDA"

# Fetch Nvidia stock data
nvidia = yf.Ticker(ticker_symbol)

# Get earnings data
earnings = nvidia.earnings
latest_earnings = earnings.iloc[0]  # latest earnings data
print("Latest Earnings Report:")
print(f"Revenue: ${latest_earnings['Revenue']:,.2f}")
print(f"Net Income: ${latest_earnings['Net Income']:,.2f}")
print(f"Guidance: {nvidia.info['forwardPE']} (Forward P/E Ratio)")