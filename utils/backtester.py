from utils.news_fetcher import fetch_news
from utils.sentiment import aggregate_sentiment
from utils.stock_fetcher import get_stock_price
from utils.trading import simple_trade_signal

import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

def fetch_historical_prices(ticker, days):
    data = yf.download(ticker, period=f"{days}d")
    return data['Close']

def backtest_stock(ticker, days=30, page_size=5, initial_cash=10000):
    """
    Backtest a sentiment-based trading strategy for the last `days` days.
    """
    print(f"Starting backtest for {ticker} over last {days} days...\n")

    # Fetch historical stock prices
    prices = fetch_historical_prices(ticker, days)  # make sure this returns a pd.Series with dates as index

    # Prepare DataFrame to store daily info
    df = pd.DataFrame(index=prices.index)
    df['close_price'] = prices
    df['sentiment'] = 0.0
    df['action'] = 'HOLD'
    df['cash'] = initial_cash
    df['shares'] = 0
    df['total_value'] = initial_cash

    cash = initial_cash
    shares = 0

    # Loop over each day
    for date in df.index:
        # Step 1: Fetch news for that day (currently will fetch latest, but works for demo)
        articles = fetch_news(ticker, page_size=page_size)
        daily_sentiment = aggregate_sentiment(articles)
        df.at[date, 'sentiment'] = daily_sentiment

        # Step 2: Determine action
        if daily_sentiment > 0.05:
            action = 'BUY'
            # Buy as many shares as possible
            shares_to_buy = cash // df.at[date, 'close_price']
            cash -= shares_to_buy * df.at[date, 'close_price']
            shares += shares_to_buy
        elif daily_sentiment < -0.05:
            action = 'SELL'
            # Sell all shares
            cash += shares * df.at[date, 'close_price']
            shares = 0
        else:
            action = 'HOLD'

        df.at[date, 'action'] = action
        df.at[date, 'cash'] = cash
        df.at[date, 'shares'] = shares
        df.at[date, 'total_value'] = cash + shares * df.at[date, 'close_price']

    # Show final summary
    print(df)
    final_value = df['total_value'].iloc[-1]
    profit = final_value - initial_cash
    print(f"\nInitial cash: ${initial_cash:.2f}")
    print(f"Final portfolio value: ${final_value:.2f}")
    print(f"Profit/Loss: ${profit:.2f}")

    # Step 3: Plot results
    plt.figure(figsize=(12,6))
    plt.plot(df.index, df['close_price'], label='Stock Price', color='blue')
    plt.plot(df.index, df['total_value'], label='Portfolio Value', color='green')
    plt.scatter(df.index[df['action']=='BUY'], df['close_price'][df['action']=='BUY'], marker='^', color='g', s=100, label='BUY')
    plt.scatter(df.index[df['action']=='SELL'], df['close_price'][df['action']=='SELL'], marker='v', color='r', s=100, label='SELL')
    plt.title(f'{ticker} Sentiment Backtest')
    plt.xlabel('Date')
    plt.ylabel('Price / Portfolio Value')
    plt.legend()
    plt.show()