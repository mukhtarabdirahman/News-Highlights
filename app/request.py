from app import app
import urllib.request
import json
from .models import news, articles

News = news.News
Articles = articles.Articles
# Getting api key
apikey = app.config['NEWS_API_KEY']

# Getting the news base url
base_url = app.config['NEWS_API_BASE_URL']

# Getting the articles base url
article_base_url = app.config['ARTICLE_API_BASE_URL']
