from flask import Flask, render_template, request
from news_fetcher import fetch_news
from summarizer import summarize_articles
from database import get_cached_result, save_result, get_recent_searches

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    articles = []
    topic = ""
    error = ""
    from_cache = False
    recent_searches = get_recent_searches()

    if request.method == "POST":
        topic = request.form.get("topic", "").strip()

        if not topic:
            error = "Please enter a topic to search."
        else:
            # Check MongoDB cache first
            cached = get_cached_result(topic)

            if cached:
                # Return saved result instantly
                articles = cached["articles"]
                from_cache = True
            else:
                # Fetch fresh news + summarize with Gemini
                raw_articles = fetch_news(topic)

                if not raw_articles:
                    error = f"No articles found for '{topic}'. Try a different topic."
                else:
                    articles = summarize_articles(raw_articles)
                    # Save to MongoDB for future searches
                    save_result(topic, articles)

    return render_template("index.html",
                           articles=articles,
                           topic=topic,
                           error=error,
                           from_cache=from_cache,
                           recent_searches=recent_searches)


if __name__ == "__main__":
    app.run(debug=True)