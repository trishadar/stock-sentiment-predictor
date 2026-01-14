def simple_trade_signal(sentiment_score, threshold=0.2):
    """
    Determine trade action based on aggregated daily sentiment.
    threshold: minimum sentiment magnitude to trigger buy/sell
    """
    if sentiment_score > threshold:
        return "BUY"
    elif sentiment_score < -threshold:
        return "SELL"
    else:
        return "HOLD"
