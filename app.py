import math
import os
from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import or_
from models import db, Post

app = Flask(__name__)

database_url = os.environ.get("DATABASE_URL")
if database_url:
    database_url = database_url.replace("postgres://", "postgresql://", 1)
    app.config["SQLALCHEMY_DATABASE_URI"] = database_url
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
        os.path.abspath(os.path.dirname(__file__)), "instance", "tasks.db"
    )

db.init_app(app)

with app.app_context():
    os.makedirs("instance", exist_ok=True)
    db.create_all()


@app.route("/")
def index():
    page = request.args.get("page", 1, type=int)
    query = request.args.get("q", "", type=str).strip()
    sort = request.args.get("sort", "latest", type=str)
    per_page = 10

    if sort not in {"latest", "oldest", "title"}:
        sort = "latest"

    posts_query = Post.query
    if query:
        like_query = f"%{query}%"
        posts_query = posts_query.filter(
            or_(Post.title.ilike(like_query), Post.content.ilike(like_query))
        )

    if sort == "oldest":
        posts_query = posts_query.order_by(Post.created_at.asc(), Post.id.asc())
    elif sort == "title":
        posts_query = posts_query.order_by(Post.title.asc(), Post.id.desc())
    else:
        posts_query = posts_query.order_by(Post.created_at.desc(), Post.id.desc())

    total_posts = posts_query.count()
    total_pages = max(1, math.ceil(total_posts / per_page))
    page = min(max(1, page), total_pages)

    posts = posts_query.offset((page - 1) * per_page).limit(per_page).all()

    return render_template(
        "index.html",
        posts=posts,
        page=page,
        total_pages=total_pages,
        has_prev=page > 1,
        has_next=page < total_pages,
        query=query,
        sort=sort,
        is_search=bool(query),
    )


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


@app.route("/post/<int:post_id>/edit", methods=["GET", "POST"])
def edit_post(post_id):
    post = Post.query.get_or_404(post_id)
    if request.method == "POST":
        post.title = request.form["title"]
        post.content = request.form["content"]
        db.session.commit()
        return redirect(url_for("post_detail", post_id=post.id))
    return render_template("create.html", post=post)


@app.route("/post/<int:post_id>/delete", methods=["POST"])
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
