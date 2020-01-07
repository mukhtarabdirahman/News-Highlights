from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_news,get_article
from ..models import Articles,News

#Views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and it's data
    '''
    # getting general news sources
    general_news = get_news()
    title ='News Highlights - Homepage'
    return render_template('index.html', title = title, new = general_news)


@main.route('/news/<id>')
def news_news(id):

    '''
    View news page function that returns the news details page and its data
    '''

    results = get_article(id)
    return render_template('article.html', data = results)
   