from flask import Flask, render_template, request
from news_fetcher import fetch_news
from summarizer import summarize_articles

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    articles = []
    topic = ""
    error = ""

    if request.method == "POST":
        topic = request.form.get("topic", "").strip()

        if not topic:
            error = "Please enter a topic to search."
        else:
            raw_articles = fetch_news(topic)

            if not raw_articles:
                error = f"No articles found for '{topic}'. Try a different topic."
            else:
                articles = summarize_articles(raw_articles)

    return render_template("index.html",
                           articles=articles,
                           topic=topic,
                           error=error)

if __name__ == "__main__":
    app.run(debug=True)