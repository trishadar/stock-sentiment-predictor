# Stock Sentiment Predictor

Predict stock sentiment and get Buy/Sell/Hold suggestions using news headlines.

## Features
- Fetch latest stock news (NewsAPI)
- Analyze headline sentiment with transformers
- Aggregate daily sentiment
- Suggest trade action: Buy / Sell / Hold
- Fetch latest stock price via Yahoo Finance

## Live Demo
Frontend hosted on GitHub Pages: [Live Demo](https://<your-username>.github.io/<repo-name>/)

## Backend Setup

1. **Clone the repo**
```bash
git clone <repo-url>
cd ai-stock-sentiment-trader
```

2. **Create & activate virtual environment**
```bash
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

3. **Install Dependencies**
```bash
pip install -r requirements.txt
```

4. **Set your NewsAPI key in .env**
```bash
NEWS_API_KEY=your_api_key_here
```

5. **Run Flask backend**
```bash
python app.py
```

The backend runs at http://127.0.0.1:5000. Frontend (live demo) sends requests to this API.

**Requirements**
- Python 3.10+
- See requirements.txt for Python packages
- Node.js & npm only if running frontend locally
