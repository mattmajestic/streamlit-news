import requests
from config import settings

def get_news_by_category(category):
    url = 'https://newsapi.org/v2/top-headlines'
    params = {
        'apiKey': settings.NEWS_API_KEY,
        'category': category,
        'language': 'en',
        'pageSize': 4  # Get the top 4 news stories
    }

    response = requests.get(url, params=params)
    
    if response.status_code != 200:
        print(f"Error fetching news: {response.status_code}")
        print(response.text)
        return None

    data = response.json()
    if data['articles']:
        news_texts = []
        for article in data['articles']:
            news_texts.append(f"📰 **Title**: {article['title']}\n📝 *Description*: {article['description']}")
        return "\n\n".join(news_texts)
    else:
        print("No news found.")
        return None
