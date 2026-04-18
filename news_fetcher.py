import requests
import os

API_KEY = os.environ.get("NEWS_API_KEY", "6087c90800784a44b23eed2e2c40ab62")

def fetch_news(topic):
    url = "https://newsapi.org/v2/everything"
    
    params = {
        "q": topic,           # the search topic
        "pageSize": 5,        # only get 5 articles
        "language": "en",     # english articles only
        "sortBy": "publishedAt",  # latest first
        "apiKey": API_KEY
    }
    
    response = requests.get(url, params=params, timeout=10)
    data = response.json()
    
    if data["status"] != "ok":
        print("Error fetching news:", data.get("message"))
        return []
    
    articles = []
    for article in data["articles"]:
        articles.append({
            "title": article["title"],
            "description": article["description"] or "No description available",
            "url": article["url"],
            "source": article["source"]["name"]
        })
    
    return articles


# --- Test it right here ---
# --- Test with real API ---
if __name__ == "__main__":
    from summarizer import summarize_articles   # import your summarizer

    topic = input("Enter a news topic: ")
    results = fetch_news(topic)
    summarized = summarize_articles(results)    # run summarizer on results

    for i, article in enumerate(summarized, 1):
        print(f"\n--- Article {i} ---")
        print(f"Title  : {article['title']}")
        print(f"Source : {article['source']}")
        print(f"Summary: {article['summary']}")
        print(f"Link   : {article['url']}")