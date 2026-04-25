import os
from flask import Flask, render_template, request, redirect, url_for
from models import db, Post

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
    os.path.abspath(os.path.dirname(__file__)), "instance", "tasks.db"
)
db.init_app(app)

with app.app_context():
    os.makedirs("instance", exist_ok=True)
    db.create_all()


@app.route("/")
def index():
    posts = Post.query.order_by(Post.created_at.desc()).all()
    return render_template("index.html", posts=posts)


@app.route("/post/new", methods=["GET", "POST"])
def create_post():
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]
        post = Post(title=title, content=content)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("create.html")


@app.route("/post/<int:post_id>")
def post_detail(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template("detail.html", post=post)


if __name__ == "__main__":
    app.run(debug=True)
