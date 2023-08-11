import requests
from flask import Flask, render_template

posts = requests.get('https://api.npoint.io/d00185ecc8d43d01f4d9').json()
app = Flask(__name__)

@app.route('/')
def home():

    return render_template('index.html', posts=posts)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/post/<int:index>')
def single_post(index):
    selected_post = None
    for post in posts:
        if post["id"] == index:
            selected_post = post
    return render_template("post.html", post=selected_post)


if __name__ == '__main__':
    app.run(debug=True)