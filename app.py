
import streamlit as st
import json
import os

# PAGE CONFIG
st.set_page_config(
    page_title="BookSpace",
    page_icon="📚",
    layout="wide"
)

FILE_NAME = "books.json"


# LOAD BOOKS - LIST
def load_books():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r", encoding="utf-8") as file:
                data = json.load(file)
                if isinstance(data, list):
                    return data
        except (json.JSONDecodeError, OSError):
            return []
    return []


# SAVE BOOKS
def save_books():
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(books, file, ensure_ascii=False, indent=4)


if "books" not in st.session_state:
    st.session_state.books = load_books()

books = st.session_state.books


# CUSTOM CSS
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #0b1020, #15142c);
    color: white;
}

header {
    background: transparent !important;
}

.block-container {
    padding-top: 2rem;
    max-width: 1200px;
}

.hero {
    text-align: center;
    padding: 55px 20px;
    border-radius: 25px;
    background: linear-gradient(120deg, #211d46, #182b49);
    border: 1px solid #38345f;
    margin-bottom: 35px;
}

.hero h1 {
    font-size: 48px;
    font-weight: 800;
    color: white;
}

.hero h1 span {
    color: #a494ff;
}

.hero p {
    color: #b5b8d2;
    font-size: 17px;
}

.stat-card {
    background: #191e36;
    border: 1px solid #343b5c;
    padding: 25px;
    border-radius: 18px;
    text-align: center;
}

.stat-card h2 {
    color: #a494ff;
    font-size: 35px;
    margin: 0;
}

.stat-card p {
    color: #aab0c9;
}

.book-card {
    background: #191e36;
    border: 1px solid #343b5c;
    padding: 22px;
    border-radius: 18px;
    margin-bottom: 15px;
    min-height: 170px;
}

.book-card:hover {
    border-color: #a494ff;
}

.book-icon {
    font-size: 40px;
}

.book-title {
    color: white;
    font-size: 18px;
    font-weight: bold;
    overflow-wrap: anywhere;
}

.stTextInput input {
    background: #191e36;
    color: white;
    border-radius: 10px;
    border: 1px solid #414969;
}

.stButton button {
    background: #8b78ff;
    color: white;
    border: none;
    border-radius: 10px;
    font-weight: bold;
    min-height: 42px;
}

.stButton button:hover {
    background: #705de0;
    color: white;
    border: none;
}

.section-title {
    font-size: 27px;
    font-weight: bold;
    margin-top: 25px;
    margin-bottom: 20px;
    color: white;
}

div[data-testid="stMetric"] {
    background: #191e36;
    padding: 18px;
    border-radius: 15px;
    border: 1px solid #343b5c;
}

footer {
    visibility: hidden;
}
</style>
""", unsafe_allow_html=True)


# HEADER
st.markdown("""
<div class="hero">
    <h1>Book<span>Space.</span></h1>
    <p>Твоят свят от безкрайни истории.</p>
    <p>Открий, организирай и управлявай любимите си книги.</p>
</div>
""", unsafe_allow_html=True)


# STATISTICS
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("📚 Общо книги", len(books))

with col2:
    st.metric("✨ Колекция", "BookSpace")

with col3:
    st.metric("📖 Нови истории", "∞")


st.markdown('<div class="section-title">✦ Добави нова книга</div>',
            unsafe_allow_html=True)

# ADD BOOK
with st.form("add_book_form", clear_on_submit=True):
    new_book = st.text_input(
        "Заглавие",
        placeholder="Въведи заглавие на книгата..."
    )

    submitted = st.form_submit_button(
        "＋ Добави книга",
        use_container_width=True
    )

    if submitted:
        if new_book.strip():
            books.append(new_book.strip())
            save_books()
            st.success("Книгата е добавена успешно!")
            st.rerun()
        else:
            st.warning("Моля, въведи заглавие!")


# SEARCH AND SORT
st.markdown('<div class="section-title">📚 Моята библиотека</div>',
            unsafe_allow_html=True)

search_col, sort_col = st.columns([3, 1])

with search_col:
    search = st.text_input(
        "Търсене",
        placeholder="🔍 Търси книга по заглавие..."
    )

with sort_col:
    st.write("")
    st.write("")
    sort_button = st.button(
        "↕ Сортирай",
        use_container_width=True
    )

if sort_button:
    books.sort(key=str.casefold)
    save_books()
    st.rerun()


# FILTER BOOKS - LIST
displayed_books = []

for book in books:
    if search.casefold() in book.casefold():
        displayed_books.append(book)


st.caption(f"Намерени книги: {len(displayed_books)}")


# DISPLAY BOOKS
if not displayed_books:
    st.info("📚 Няма намерени книги. Добави първата си книга!")

else:
    columns = st.columns(3)

    for index, book in enumerate(displayed_books):
        with columns[index % 3]:
            st.markdown(f"""
            <div class="book-card">
                <div class="book-icon">📖</div>
                <p style="color:#a494ff;font-size:11px;">
                    MY COLLECTION
                </p>
                <div class="book-title">{book}</div>
            </div>
            """, unsafe_allow_html=True)

            if st.button(
                "🗑 Изтрий",
                key=f"delete_{index}_{book}",
                use_container_width=True
            ):
                books.remove(book)
                save_books()
                st.rerun()


# FOOTER
st.markdown("""
<hr>
<div style="text-align:center;color:#858da9;padding:20px;">
    © 2026 BookSpace · Made with ♥ for book lovers
</div>
""", unsafe_allow_html=True)

