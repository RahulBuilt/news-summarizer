import re

def summarize(text, max_sentences=2):
    # If no text, return a default message
    if not text or text.strip() == "":
        return "No summary available."

    # Clean up extra spaces and newlines
    text = text.strip()
    text = re.sub(r'\s+', ' ', text)  # replace multiple spaces with one

    # Split into sentences
    # This splits at . ! ? followed by a space and capital letter
    sentences = re.split(r'(?<=[.!?])\s+(?=[A-Z])', text)

    # Remove very short sentences (less than 5 words) - they're usually noise
    sentences = [s for s in sentences if len(s.split()) >= 5]

    # Take only the first max_sentences
    summary = ' '.join(sentences[:max_sentences])

    # If summary is still empty after filtering, return original text trimmed
    if not summary:
        return text[:200] + "..." if len(text) > 200 else text

    return summary


def summarize_articles(articles):
    summarized = []

    for article in articles:
        summarized.append({
            "title": article["title"],
            "summary": summarize(article["description"]),
            "url": article["url"],
            "source": article["source"]
        })

    return summarized


# --- Test it right here ---
if __name__ == "__main__":
    # Fake test data so you can test without calling the API
    test_articles = [
        {
            "title": "India wins cricket match against Australia",
            "description": "India defeated Australia by 6 wickets in a thrilling match. The match was played in Mumbai. Virat Kohli scored a brilliant century. The crowd was absolutely electric throughout the game. Australia fought hard but could not defend their total.",
            "url": "https://example.com/article1",
            "source": "ESPN"
        },
        {
            "title": "New AI model released by Google",
            "description": "Google has released a new AI model that can understand images and text together. This is a significant step forward. The model was trained on billions of data points. Experts say it could change how we search the internet.",
            "url": "https://example.com/article2",
            "source": "TechCrunch"
        },
        {
            "title": "No description article",
            "description": "",
            "url": "https://example.com/article3",
            "source": "BBC"
        }
    ]

    results = summarize_articles(test_articles)

    for i, article in enumerate(results, 1):
        print(f"\n--- Article {i} ---")
        print(f"Title  : {article['title']}")
        print(f"Source : {article['source']}")
        print(f"Summary: {article['summary']}")
        print(f"Link   : {article['url']}")