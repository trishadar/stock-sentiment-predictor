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
    total = 0.0
    for h in headlines:
        # text = f"{h.get('title','')} {h.get('content','')}"
        # label, s = analyze_sentiment(text)
        print(h)
        print("label:", h["sentiment"], "compound:", h["score"])
        total += h["score"]   # use real compound score

    return total / len(headlines)


