from utils.news_fetcher import fetch_news
from utils.sentiment import analyze_sentiment, aggregate_sentiment

def main():
    ticker = "AAPL"  # Change to any stock symbol
    print(f"Fetching news for {ticker}...")
    
    articles = fetch_news(ticker, page_size=5)
    
    print("\n--- Headlines + Sentiment ---")
    for a in articles:
        label, score = analyze_sentiment(a["title"])
        print(a["title"], "→", label, f"{score:.2f}")
    
    daily_score = aggregate_sentiment(articles)
    print("\n--- Aggregated Daily Sentiment ---")
    print(f"{ticker}: {daily_score:.3f}")

if __name__ == "__main__":
    main()