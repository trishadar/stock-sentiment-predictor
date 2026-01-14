from flask import Flask, request, jsonify
from flask_cors import CORS

from utils.news_fetcher import fetch_news
from utils.sentiment import analyze_sentiment, aggregate_sentiment
from utils.trading import simple_trade_signal
from utils.stock_fetcher import get_stock_price

import os

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return app.send_static_file("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    try:
        data = request.get_json()
        ticker = data.get("ticker", "").upper()
        print("Received ticker:", ticker)

        articles = fetch_news(ticker, page_size=10)
        print("Fetched articles:", len(articles))

        scored_headlines = []
        for a in articles:
            text = f"{a.get('title','')} {a.get('description','')} {a.get('content','')}"
            label, score = analyze_sentiment(text)
            scored_headlines.append({
                "title": a["title"],
                "sentiment": label,
                "score": score,
                "url": a["url"]
            })

        daily_score = aggregate_sentiment(scored_headlines)
        print("RAW SENTIMENT:", daily_score)
        action = simple_trade_signal(daily_score)
        stock_price = get_stock_price(ticker)
        print("stock_price:", stock_price)

        return jsonify({
            "ticker": ticker,
            "daily_score": round(daily_score, 3),
            "action": action,
            "headlines": scored_headlines,
            "price": stock_price
        })

    except Exception as e:
        print("ERROR:", e)
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    #app.run(debug=True)
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
