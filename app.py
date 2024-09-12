import streamlit as st
import requests

# Set page config with a favicon and more emojis
st.set_page_config(page_title="📰 Streamlit New", page_icon="🌍")

# Title and description with emojis
st.title("📰 Streamlit News")
st.subheader("🚀 News API for Streamlit")

st.write("🔑 Get your API key from [News API](https://newsapi.org/register)")

# Sidebar for API key input
api_key = st.sidebar.text_input("🔑 Enter API key:", type="password")

# Sidebar input for news category
category = st.sidebar.selectbox(
    "Select a news category:",
    ["technology", "sports", "business", "entertainment", "politics", "health"]
)

# Function to fetch news based on the selected category
def get_news_by_category(api_key, category):
    url = 'https://newsapi.org/v2/top-headlines'
    params = {
        'apiKey': api_key,
        'category': category,
        'language': 'en',
        'pageSize': 2  # Get the top 2 news stories
    }

    response = requests.get(url, params=params)
    
    if response.status_code != 200:
        st.error(f"Error fetching news: {response.status_code}")
        return None

    data = response.json()
    if data['articles']:
        news_texts = []
        for article in data['articles']:
            news_texts.append(f"📰 **Title**: {article['title']}\n📝 *Description*: {article['description']}")
        return "\n\n".join(news_texts)
    else:
        st.warning("No news found.")
        return None

# Display news if the API key is entered and category is selected
if api_key:
    st.write(f"Fetching top news for **{category}** category...")
    news = get_news_by_category(api_key, category)
    if news:
        st.markdown(news)
else:
    st.warning("Please enter your API key to fetch news.")
