import os
from utils.yf_downloader import fetch_stock_data
from utils.rss_fetcher import fetch_rss_news
from utils.sec_downloader import fetch_sec_filings

def main():
    ticker = "AAPL"
    print(f"[INFO] Fetching stock data for {ticker}...")
    prices = fetch_stock_data(ticker)
    print(prices.head())

    print("[INFO] Fetching latest news...")
    news_items = fetch_rss_news()
    for item in news_items[:3]:
        print(f"- {item['title']}")

    print("[INFO] Fetching SEC filings...")
    filings = fetch_sec_filings(ticker)
    for form, date, acc_num in filings:
        print(f"- {form} filed on {date}")


if __name__ == "__main__":
    main()
