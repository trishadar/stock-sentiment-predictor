from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

def analyze_sentiment(text):
    scores = analyzer.polarity_scores(text)
    compound = scores["compound"]

    if compound >= 0.05:
        return "positive", compound
    elif compound <= -0.05:
        return "negative", compound
    else:
        return "neutral", compound


def aggregate_sentiment(headlines):
    if not headlines:
        return 0.0

    total = 0
    for h in headlines:
        _, score = analyze_sentiment(h)
        total += score

    return total / len(headlines)
