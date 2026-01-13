import os
import requests
from dotenv import load_dotenv

# load_dotenv()  # Load .env file
# NEWS_API_KEY = os.getenv("NEWS_API_KEY")

# Load .env only if running locally
if os.environ.get("NEWS_API_KEY") is None:
    load_dotenv()

NEWS_API_KEY = os.environ.get("NEWS_API_KEY")
if NEWS_API_KEY is None:
    raise ValueError("NEWS_API_KEY not found.")

BASE_URL = "https://newsapi.org/v2/everything"

def fetch_news(ticker: str, page_size=5):
    if not NEWS_API_KEY:
        raise ValueError("NEWS_API_KEY not found. Set it in .env")
    
    params = {
        "q": ticker,
        "language": "en",
        "sortBy": "publishedAt",
        "pageSize": page_size,
        "apiKey": NEWS_API_KEY
    }
    
    res = requests.get(BASE_URL, params=params)
    res.raise_for_status()  # will throw HTTPError for bad keys
    return res.json().get("articles", [])
