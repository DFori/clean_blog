from flask import Flask, render_template
import requests

posts = requests.get("https://api.npoint.io/1ba3bf27f8c2c9f68e14").json()


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("blog.html", post=requested_post)


if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0gi")