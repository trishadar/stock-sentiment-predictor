import yfinance as yf

def get_stock_price(ticker: str):
    try:
        stock = yf.Ticker(ticker)
        hist = stock.history(period="1d")

        if hist.empty:
            return None

        return round(float(hist["Close"].iloc[-1]), 2)

    except Exception as e:
        print("Stock price error:", e)
        return None
