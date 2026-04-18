# News Summarizer

A web app that fetches the top 5 latest news articles on any topic
and summarizes them into short, readable snippets.

**Live demo:** https://news-summarizer-ovog.onrender.com

## Tech Stack
- Python + Flask (backend)
- NewsAPI.org (news data)
- HTML + CSS (frontend)

## How to run locally
1. Clone this repo
2. Install dependencies: `pip install -r requirements.txt`
3. Set your API key: `export NEWS_API_KEY=your_key_here`
4. Run: `python app.py`
5. Open: `http://localhost:5000`

## Features
- Search any topic
- Get top 5 latest articles
- Clean summaries for each article
- Links to full articles