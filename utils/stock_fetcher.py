import yfinance as yf

def get_stock_price(ticker: str, period="5d", interval="1d"):
    """
    Fetch historical stock price data.
    period: how far back (e.g., "5d", "1mo")
    interval: time granularity ("1d", "1h")
    """
    stock = yf.Ticker(ticker)
    hist = stock.history(period=period, interval=interval)
    # Only keep date and closing price
    return hist['Close']
