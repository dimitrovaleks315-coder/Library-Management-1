
from flask import Flask, request, redirect, url_for, render_template_string
import json
import os

app = Flask(__name__)

FILE_NAME = "books.json"


# Зареждане на книгите в LIST
def load_books():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r", encoding="utf-8") as file:
                data = json.load(file)
                if isinstance(data, list):
                    return data
        except (json.JSONDecodeError, OSError):
            pass

    return []


books = load_books()


# Запазване на книгите
def save_books():
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(books, file, ensure_ascii=False, indent=4)


# Добавяне на книга
@app.route("/add", methods=["POST"])
def add_book():
    title = request.form.get("title", "").strip()

    if title:
        books.append(title)
        save_books()

    return redirect(url_for("home"))


# Изтриване на книга
@app.route("/delete", methods=["POST"])
def delete_book():
    title = request.form.get("title", "")

    if title in books:
        books.remove(title)
        save_books()

    return redirect(url_for("home"))


# Начална страница
@app.route("/")
def home():
    search = request.args.get("search", "").strip()

    displayed_books = []

    # Търсене чрез LIST
    for book in books:
        if search.casefold() in book.casefold():
            displayed_books.append(book)

    # Сортиране
    if request.args.get("sort") == "1":
        displayed_books.sort(key=str.casefold)

    return render_template_string(
        HTML,
        displayed_books=displayed_books,
        total=len(books),
        results=len(displayed_books),
        search=search
    )


HTML = """
<!DOCTYPE html>
<html lang="bg">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>BookSpace</title>
<style>
body {
    margin: 0;
    font-family: Arial, sans-serif;
    background: #0b1020;
    color: white;
}
.container {
    width: 90%;
    max-width: 1100px;
    margin: auto;
}
nav {
    padding: 25px;
    border-bottom: 1px solid #29314b;
}
.logo {
    font-size: 26px;
    font-weight: bold;
}
.logo span {
    color: #9b8cff;
}
.hero {
    text-align: center;
    padding: 65px 10px;
}
.hero h1 {
    font-size: 48px;
}
.hero h1 span {
    color: #9b8cff;
}
.hero p {
    color: #a0a8c0;
    line-height: 1.7;
}
.stats {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 20px;
    margin-bottom: 40px;
}
.stat {
    background: #171e34;
    padding: 25px;
    border-radius: 15px;
    border: 1px solid #303852;
}
.stat h2 {
    font-size: 30px;
    color: #a99aff;
}
.stat p {
    color: #a0a8c0;
}
.panel {
    background: #191f39;
    padding: 25px;
    border-radius: 15px;
    margin-bottom: 30px;
}
input {
    padding: 15px;
    background: #0e1529;
    color: white;
    border: 1px solid #414966;
    border-radius: 9px;
    font-size: 14px;
    box-sizing: border-box;
    min-width: 0;
}
form {
    display: flex;
    gap: 10px;
}
form input {
    flex: 1;
}
button, .sort {
    background: #8b78ff;
    color: white;
    padding: 14px 20px;
    border: none;
    border-radius: 9px;
    cursor: pointer;
    text-decoration: none;
    font-weight: bold;
}
button:hover, .sort:hover {
    background: #705de0;
}
.search {
    margin-bottom: 30px;
}
.grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 20px;
    margin-bottom: 70px;
}
.book {
    background: #171e34;
    border: 1px solid #303852;
    border-radius: 15px;
    padding: 22px;
    transition: .3s;
}
.book:hover {
    transform: translateY(-5px);
    border-color: #9b8cff;
}
.cover {
    background: linear-gradient(135deg, #5145a6, #252c59);
    height: 130px;
    border-radius: 10px;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 45px;
    margin-bottom: 20px;
}
.book h3 {
    overflow-wrap: anywhere;
}
.book form {
    justify-content: flex-end;
    border-top: 1px solid #303852;
    padding-top: 15px;
}
.delete {
    background: #713044;
    padding: 10px 15px;
}
.empty {
    grid-column: 1 / -1;
    text-align: center;
    padding: 50px;
    background: #171e34;
    border-radius: 15px;
    color: #a0a8c0;
}
footer {
    text-align: center;
    padding: 25px;
    color: #7d87a4;
    border-top: 1px solid #29314b;
}
@media(max-width: 700px) {
    .stats, .grid {
        grid-template-columns: 1fr;
    }
    .hero h1 {
        font-size: 34px;
    }
    form {
        flex-direction: column;
    }
}
</style>
</head>
<body>

<nav>
    <div class="container logo">
        Book<span>Space.</span>
    </div>
</nav>

<div class="container">

    <section class="hero">
        <h1>Твоят свят от<br><span>безкрайни истории.</span></h1>
        <p>Открий, организирай и управлявай любимите си книги.</p>
    </section>

    <section class="stats">
        <div class="stat">
            <h2>{{ total }}</h2>
            <p>Общо книги</p>
        </div>
        <div class="stat">
            <h2>{{ results }}</h2>
            <p>Намерени книги</p>
        </div>
        <div class="stat">
            <h2>∞</h2>
            <p>Нови истории</p>
        </div>
    </section>

    <section class="panel">
        <h3>✦ Добави нова книга</h3>
        <form action="/add" method="POST">
            <input type="text" name="title"
                   placeholder="Заглавие на книгата..." required>
            <button type="submit">+ Добави</button>
        </form>
    </section>

    <h2>📚 Моята библиотека</h2>

    <form class="search" action="/" method="GET">
        <input type="text" name="search"
               placeholder="Търси книга..."
               value="{{ search }}">
        <button type="submit">Търси</button>
        <a class="sort" href="/?sort=1">Сортирай ↑</a>
    </form>

    <div class="grid">
        {% for book in displayed_books %}
        <div class="book">
            <div class="cover">📖</div>
            <small>MY COLLECTION</small>
            <h3>{{ book }}</h3>
            <form action="/delete" method="POST"
                  onsubmit="return confirm('Изтриване на книгата?')">
                <input type="hidden" name="title" value="{{ book }}">
                <button class="delete" type="submit">🗑 Изтрий</button>
            </form>
        </div>
        {% else %}
        <div class="empty">
            <h2>📚</h2>
            <h3>Няма намерени книги</h3>
            <p>Добави нова книга в своята библиотека!</p>
        </div>
        {% endfor %}
    </div>

</div>

<footer>
    © 2026 BookSpace | Made for book lovers ♥
</footer>

</body>
</html>
"""


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False,
        use_reloader=False
    )
