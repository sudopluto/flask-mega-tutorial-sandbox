from flask import render_template
from app import app

@app.route('/')
@app.route('/index')

def index():
    user = {'username': 'Pranav'}
    posts = [
        {
            'author': {'username': 'Johnny'},
            'body': 'I like beer!'
        },
        {
            'author': {'username': 'Danny'},
            'body': 'I like bonsais!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
