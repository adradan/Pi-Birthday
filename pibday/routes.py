from flask import render_template
from pibday import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Mike'}
    posts = [
        {
            'author': 'expertgamers',
            'body': 'Flask is mad work...'
        },
        {
            'author': 'adradan',
            'body': 'How python?!?!?!???'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)