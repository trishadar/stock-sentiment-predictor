from utils.news_fetcher import fetch_news
from utils.sentiment import analyze_sentiment, aggregate_sentiment
from utils.stock_fetcher import get_stock_price
from utils.trading import simple_trade_signal
from utils.backtester import backtest_stock

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

    # Fetch latest stock price
    prices = get_stock_price(ticker, period="1d")
    last_price = prices[-1] if not prices.empty else None
    print("\n--- Latest Stock Price ---")
    print(f"{ticker}: ${last_price:.2f}" if last_price else "Price not found")

    # Determine trade action
    action = simple_trade_signal(daily_score)
    print("\n--- Suggested Trade ---")
    print(f"Sentiment-based action: {action}")

if __name__ == "__main__":
    main()

    # Run backtest for last 30 days
    backtest_stock("AAPL", days=30, page_size=5)