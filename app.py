from flask import Flask, request, jsonify
from flask_cors import CORS

from utils.news_fetcher import fetch_news
from utils.sentiment import analyze_sentiment, aggregate_sentiment
from utils.trading import simple_trade_signal

app = Flask(__name__, static_folder="static", static_url_path="")
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

        articles = fetch_news(ticker, page_size=5)
        print("Fetched articles:", len(articles))

        headlines = []
        for a in articles:
            label, score = analyze_sentiment(a["title"])
            headlines.append({
                "title": a["title"],
                "sentiment": label,
                "score": score
            })

        daily_score = aggregate_sentiment(articles)
        action = simple_trade_signal(daily_score)

        return jsonify({
            "ticker": ticker,
            "daily_score": round(daily_score, 3),
            "action": action,
            "headlines": headlines
        })

    except Exception as e:
        print("ERROR:", e)
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
