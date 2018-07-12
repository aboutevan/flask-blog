# export FLASK_APP=flask-blog.py
# export FLASK_DEBUG=1
# flask run
from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'Evan S',
        'title': 'Blog Post 1',
        'content': 'First Post',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second Post',
        'date_posted': 'April 20, 2018'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)