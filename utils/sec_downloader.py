import requests

def fetch_sec_filings(ticker="AAPL", count=5):
    headers = {
        "User-Agent": "rag-assistant (chankey@example.com)"
    }
    try:
        url = f"https://data.sec.gov/submissions/CIK0000320193.json"
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        recent = data["filings"]["recent"]
        items = list(
            zip(recent["form"], recent["filingDate"], recent["accessionNumber"])
        )
        return items[:count]
    except Exception as e:
        print("[ERROR] Failed to fetch SEC filings:", e)
        return []
