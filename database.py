from pymongo import MongoClient
from datetime import datetime, timedelta
import os

MONGO_URI = os.environ.get("MONGO_URI", "mongodb+srv://chatbot_user:Rahul1234@cluster0.g6scf2n.mongodb.net/?appName=Cluster0")

client = MongoClient(MONGO_URI)
db = client["news_summarizer"]
collection = db["searches"]


def get_cached_result(topic):
    """Check if we already have results for this topic from last 6 hours"""
    six_hours_ago = datetime.utcnow() - timedelta(hours=6)

    result = collection.find_one({
        "topic": topic.lower(),
        "created_at": {"$gte": six_hours_ago}
    })

    return result


def save_result(topic, articles):
    """Save search results to MongoDB"""
    collection.insert_one({
        "topic": topic.lower(),
        "articles": articles,
        "created_at": datetime.utcnow()
    })


def get_recent_searches(limit=5):
    """Get the last 5 unique topics searched"""
    pipeline = [
        {"$group": {"_id": "$topic", "last_searched": {"$max": "$created_at"}}},
        {"$sort": {"last_searched": -1}},
        {"$limit": limit}
    ]
    results = list(collection.aggregate(pipeline))
    return [r["_id"] for r in results]