from flask import Flask, request, jsonify
from flask_cors import CORS
from utils.news_fetcher import fetch_news
from utils.sentiment import analyze_sentiment, aggregate_sentiment
from utils.stock_fetcher import get_stock_price
from utils.trading import simple_trade_signal

app = Flask(__name__)
CORS(app)  # <-- allow requests from React frontend

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    ticker = data.get("ticker", "").upper()
    
    articles = fetch_news(ticker, page_size=5)
    headlines = [a["title"] for a in articles]
    
    scores = [analyze_sentiment(h)[1] for h in headlines]
    daily_score = sum(scores)/len(scores) if scores else 0.0
    
    prices = get_stock_price(ticker, period="1d")
    last_price = prices[-1] if not prices.empty else None
    
    action = simple_trade_signal(daily_score)
    
    return jsonify({
        "ticker": ticker,
        "daily_score": daily_score,
        "last_price": last_price,
        "action": action,
        "headlines": headlines
    })

if __name__ == "__main__":
    app.run(debug=True)
