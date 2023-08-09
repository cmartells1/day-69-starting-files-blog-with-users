import requests
from flask import Flask, render_template

from post import Post

app = Flask(__name__)

blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
posts = requests.get(blog_url).json()
post_objects = []
for post in posts:
    post_obj = Post(title=post['title'], subtitle=post['subtitle'], body=post['body'], id=post['id'])
    post_objects.append(post_obj)

@app.route('/')
def home():
    return render_template("index.html", posts=post_objects)


@app.route('/post/<int:index>')
def get_post(index):
    selected_post = None
    for single_post in post_objects:
        if index == single_post.id:
            selected_post = single_post

    return render_template("post.html", post=selected_post)


if __name__ == "__main__":
    app.run(debug=True)
