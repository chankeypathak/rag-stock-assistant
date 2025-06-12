import feedparser

def fetch_rss_news(feed_url="https://www.moneycontrol.com/rss/MCtopnews.xml"):
    try:
        feed = feedparser.parse(feed_url)
        articles = [{"title": entry.title, "link": entry.link, "summary": entry.summary} for entry in feed.entries]
        return articles
    except Exception as e:
        print(f"[ERROR] Failed to fetch RSS feed: {e}")
        return []
