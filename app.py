from flask import Flask, render_template, request
from utils.news_fetcher import fetch_news
from utils.sentiment import analyze_sentiment, aggregate_sentiment
from utils.trading import simple_trade_signal

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    recommendation = None
    headlines_with_sentiment = []

    if request.method == "POST":
        ticker = request.form.get("ticker").upper()
        articles = fetch_news(ticker, page_size=5)

        # Analyze sentiment for each headline
        for a in articles:
            label, score = analyze_sentiment(a["title"])
            headlines_with_sentiment.append((a["title"], label, score))

        # Aggregate sentiment and get trade action
        daily_score = aggregate_sentiment(articles)
        recommendation = simple_trade_signal(daily_score)

    return render_template(
        "index.html",
        headlines=headlines_with_sentiment,
        recommendation=recommendation
    )

if __name__ == "__main__":
    app.run(debug=True)