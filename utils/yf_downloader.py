import yfinance as yf
import pandas as pd

def fetch_stock_data(ticker, period="5d", interval="1h"):
    try:
        stock = yf.Ticker(ticker)
        df = stock.history(period=period, interval=interval)
        df.reset_index(inplace=True)
        return df
    except Exception as e:
        print(f"[ERROR] Failed to fetch yFinance data: {e}")
        return pd.DataFrame()
