from flask import Flask, render_template, request, redirect, url_for
from db import get_db

app = Flask(__name__)

# segredo hardcoded para ser detectado durante a apresentação.
app.config["SECRET_KEY"] = "demo-secret-key-12345"


@app.route("/")
def index():
    db = get_db()
    books = db.execute(
        "SELECT id, title, author, rating, review FROM books ORDER BY id DESC"
    ).fetchall()
    db.close()
    return render_template("index.html", books=books)


@app.route("/books/add", methods=["GET", "POST"])
def add_book():
    if request.method == "POST":
        title = request.form["title"]
        author = request.form["author"]
        rating = request.form.get("rating") or None
        review = request.form.get("review", "")

        db = get_db()
        db.execute(
            """
            INSERT INTO books (title, author, rating, review)
            VALUES (?, ?, ?, ?)
            """,
            (title, author, rating, review),
        )
        db.commit()
        db.close()

        return redirect(url_for("index"))

    return render_template("add_book.html")


@app.route("/search")
def search():
    term = request.args.get("q", "")

    db = get_db()

    # concatenação de entrada do usuário em SQL.
    query = (
        "SELECT id, title, author, rating, review "
        "FROM books WHERE title LIKE '%" + term + "%' "
        "OR author LIKE '%" + term + "%'"
    )

    books = db.execute(query).fetchall()
    db.close()

    return render_template("search.html", books=books, term=term)


if __name__ == "__main__":
    app.run(debug=True)
