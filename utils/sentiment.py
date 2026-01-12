from transformers import pipeline

sentiment_pipeline = pipeline(
    "sentiment-analysis",
    model="ProsusAI/finbert",
    framework="pt"
)

def analyze_sentiment(text: str):
    result = sentiment_pipeline(text[:512])[0]
    return result["label"], result["score"]

# Convert label to numeric score
def label_to_score(label: str):
    if label.lower() == "positive":
        return 1
    if label.lower() == "negative":
        return -1
    return 0  # neutral

# Aggregate a list of articles
def aggregate_sentiment(articles):
    scores = []
    for article in articles:
        title = article.get("title")
        if not title:
            continue
        label, confidence = analyze_sentiment(title)
        scores.append(label_to_score(label) * confidence)
    if not scores:
        return 0
    return sum(scores) / len(scores)