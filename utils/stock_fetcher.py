import yfinance as yf

def get_stock_price(ticker: str):
    try:
        stock = yf.Ticker(ticker)
        hist = stock.history(period="1d")

        if hist.empty:
            return None
        price = hist["Close"].iloc[-1]
        return round(float(price), 2)

    except Exception as e:
        print("Stock price error:", e)
        return None
