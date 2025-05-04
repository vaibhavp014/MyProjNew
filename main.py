
from flask import Flask, render_template, send_from_directory
import markdown
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/blog")
def blog():
    posts = []
    for filename in os.listdir("blog_posts"):
        if filename.endswith(".md"):
            with open(os.path.join("blog_posts", filename), "r") as f:
                content = f.read()
                html = markdown.markdown(content)
                posts.append({"title": filename.replace(".md", ""), "content": html})
    return render_template("blog.html", posts=posts)

if __name__ == "__main__":
    app.run(debug=True)
