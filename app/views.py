from flask import render_template
from app import app

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    return render_template('index.html')

@app.route('/news/<id>')
def news_news(id):
   
   '''
   View news page function that returns the news details page and its data
   '''
   