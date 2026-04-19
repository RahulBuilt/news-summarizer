from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
import os

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "AIzaSyA5N8o_BT3h_7Tt46XiWwQsqI6p5sB5VgQ")

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    google_api_key=GEMINI_API_KEY,
    temperature=0.3
)


def summarize_with_gemini(title, description):
    """Use Gemini to generate a smart 2-sentence summary"""

    if not description or description.strip() == "":
        return "No summary available for this article."

    prompt = f"""You are a news summarizer. Given the article title and description below, 
write a clear and concise 2-sentence summary that captures the key information.
Do not use phrases like 'This article' or 'The article'. Just summarize directly.

Title: {title}
Description: {description}

Summary:"""

    try:
        response = llm.invoke([HumanMessage(content=prompt)])
        return response.content.strip()
    except Exception as e:
        print(f"Gemini error: {e}")
        # fallback to basic summarizer if Gemini fails
        return description[:200] + "..." if len(description) > 200 else description


def summarize_articles(articles):
    """Summarize a list of articles using Gemini"""
    summarized = []

    for article in articles:
        summarized.append({
            "title": article["title"],
            "summary": summarize_with_gemini(article["title"], article["description"]),
            "url": article["url"],
            "source": article["source"]
        })

    return summarized


# --- Test it ---
if __name__ == "__main__":
    test = [{
        "title": "India wins cricket match against Australia",
        "description": "India defeated Australia by 6 wickets in Mumbai. Virat Kohli scored a century. The crowd was electric throughout.",
        "url": "https://example.com",
        "source": "ESPN"
    }]

    results = summarize_articles(test)
    for r in results:
        print(f"Title: {r['title']}")
        print(f"Summary: {r['summary']}")