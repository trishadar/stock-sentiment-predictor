# utils/news_fetcher_nyt.py
import requests

NYT_API_KEY = os.getenv("NYT_NEWS_API_KEY")

def fetch_nyt_news(ticker, from_date, to_date, page=0):
    """
    Fetches historical NYT headlines for a stock ticker between two dates.
    Dates should be strings in YYYYMMDD format.
    """
    url = "https://api.nytimes.com/svc/search/v2/articlesearch.json"
    query = f"{ticker}"  # NYT article search query
    params = {
        "q": query,
        "begin_date": from_date,
        "end_date": to_date,
        "sort": "newest",
        "page": page,
        "api-key": NYT_API_KEY
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()
    articles = []

    for doc in data.get("response", {}).get("docs", []):
        headline = doc.get("headline", {}).get("main")
        if headline:
            articles.append(headline)

    return articles
