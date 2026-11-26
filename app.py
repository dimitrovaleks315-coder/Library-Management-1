
import streamlit as st
import json
import os
import html

st.set_page_config(
    page_title="BookSpace | Digital Library",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

FILE_NAME = "books.json"

# ---------------- DATA ----------------

def load_books():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r", encoding="utf-8") as file:
                data = json.load(file)
                if isinstance(data, list):
                    return data
        except (json.JSONDecodeError, OSError):
            pass

    return [
        "Хари Потър и Философският камък",
        "Малкият принц",
        "Под игото",
        "Бай Ганьо",
        "1984",
        "Властелинът на пръстените",
        "Алхимикът",
        "Гордост и предразсъдъци",
        "Шерлок Холмс",
        "Пътеводител на галактическия стопаджия",
        "Момичето с драконовата татуировка",
        "Престъпление и наказание"
    ]


def save_books():
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(books, file, ensure_ascii=False, indent=4)


if "books" not in st.session_state:
    st.session_state.books = load_books()

books = st.session_state.books

# ---------------- DESIGN ----------------

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&family=Playfair+Display:wght@600;700;800&display=swap');

.stApp {
    background: #0c1020;
    color: #f5f3ff;
    font-family: 'DM Sans', sans-serif;
}

header[data-testid="stHeader"] {
    background: transparent;
}

.block-container {
    max-width: 1450px;
    padding: 2rem 3rem 4rem;
}

[data-testid="stSidebar"] {
    background: #111629;
    border-right: 1px solid #252d45;
}

[data-testid="stSidebar"] * {
    color: #e7e5f5;
}

.brand {
    font-family: 'Playfair Display', serif;
    font-size: 30px;
    font-weight: 800;
    color: #ffffff;
    margin-bottom: 4px;
}

.brand span {
    color: #aa92ff;
}

.sidebar-sub {
    color: #8992af;
    font-size: 12px;
    letter-spacing: 2px;
    margin-bottom: 35px;
}

.side-label {
    color: #78839f;
    font-size: 11px;
    letter-spacing: 2px;
    font-weight: 700;
    margin: 25px 0 12px;
}

.side-info {
    background: #1b2240;
    border: 1px solid #34365c;
    padding: 18px;
    border-radius: 15px;
    margin-top: 30px;
}

.side-info p {
    color: #a8a8c3;
    font-size: 12px;
}

.hero {
    position: relative;
    background: linear-gradient(115deg, #25214e, #252b50 60%, #193b4c);
    border: 1px solid #49446d;
    border-radius: 25px;
    padding: 55px 45px;
    margin-bottom: 35px;
    overflow: hidden;
}

.hero:after {
    content: '✦';
    position: absolute;
    right: 65px;
    top: 15px;
    font-size: 150px;
    color: rgba(255,255,255,0.07);
}

.hero-tag {
    color: #c7b9ff;
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 3px;
    margin-bottom: 18px;
}

.hero h1 {
    font-family: 'Playfair Display', serif;
    font-size: clamp(35px, 5vw, 58px);
    color: white;
    line-height: 1.2;
    margin: 0;
}

.hero h1 span {
    color: #b8a5ff;
}

.hero p {
    color: #c0c3db;
    max-width: 520px;
    font-size: 15px;
    line-height: 1.8;
    margin-top: 18px;
}

.section-title {
    font-family: 'Playfair Display', serif;
    font-size: 27px;
    color: #fff;
    font-weight: 700;
}

.section-sub {
    color: #8d96b2;
    font-size: 13px;
    margin-top: 5px;
    margin-bottom: 22px;
}

.metric-card {
    background: linear-gradient(145deg, #191f38, #171b30);
    border: 1px solid #303955;
    border-radius: 17px;
    padding: 22px;
    min-height: 125px;
}

.metric-icon {
    font-size: 22px;
}

.metric-number {
    font-size: 30px;
    font-weight: 800;
    color: #b8a5ff;
    margin-top: 9px;
}

.metric-label {
    color: #9ba4bf;
    font-size: 12px;
}

.book-card {
    background: #171d32;
    border: 1px solid #2d3651;
    border-radius: 17px;
    padding: 15px;
    transition: all .25s ease;
    margin-bottom: 10px;
}

.book-card:hover {
    border-color: #a18bff;
    transform: translateY(-5px);
}

.book-cover {
    height: 175px;
    border-radius: 11px;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 65px;
    margin-bottom: 18px;
}

.cover-1 {
    background: linear-gradient(145deg, #6146a3, #29244e);
}

.cover-2 {
    background: linear-gradient(145deg, #256b78, #193849);
}

.cover-3 {
    background: linear-gradient(145deg, #a05b70, #492b54);
}

.cover-4 {
    background: linear-gradient(145deg, #9b793c, #4d3c2b);
}

.cover-5 {
    background: linear-gradient(145deg, #425c9b, #252c55);
}

.cover-6 {
    background: linear-gradient(145deg, #627b62, #283d3b);
}

.book-category {
    color: #b39fff;
    font-size: 10px;
    font-weight: 800;
    letter-spacing: 2px;
}

.book-title {
    color: #fff;
    font-size: 15px;
    font-weight: 700;
    line-height: 1.5;
    min-height: 47px;
    margin-top: 9px;
    overflow-wrap: anywhere;
}

.book-number {
    color: #78839e;
    font-size: 11px;
    margin-top: 12px;
}

.add-panel {
    background: linear-gradient(120deg, #1d2041, #192c43);
    border: 1px solid #3a4264;
    border-radius: 19px;
    padding: 25px;
    margin: 20px 0 35px;
}

.stTextInput input {
    background: #11182c;
    border: 1px solid #3b4662;
    color: white;
    border-radius: 10px;
}

.stTextInput input:focus {
    border-color: #a18bff;
}

.stButton button, .stFormSubmitButton button {
    background: #8d76ec;
    color: white;
    border: none;
    border-radius: 10px;
    font-weight: 700;
    transition: .2s;
}

.stButton button:hover, .stFormSubmitButton button:hover {
    background: #a18bff;
    color: white;
    border: none;
}

hr {
    border-color: #2a334c;
}

.stAlert {
    border-radius: 12px;
}

.footer {
    text-align: center;
    padding: 35px 10px;
    color: #77819c;
    font-size: 12px;
    border-top: 1px solid #252d43;
    margin-top: 40px;
}

@media(max-width: 700px) {
    .block-container {
        padding: 1rem;
    }
    .hero {
        padding: 35px 22px;
    }
}
</style>
""", unsafe_allow_html=True)


# ---------------- SIDEBAR ----------------

with st.sidebar:
    st.markdown(
        '<div class="brand">Book<span>Space.</span></div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sidebar-sub">DIGITAL LIBRARY</div>',
        unsafe_allow_html=True
    )

    st.markdown('<div class="side-label">MAIN MENU</div>',
                unsafe_allow_html=True)

    page = st.radio(
        "Navigation",
        ["🏠 Начало", "📚 Всички книги", "➕ Добави книга"],
        label_visibility="collapsed"
    )

    st.markdown('<div class="side-info">'
                '<div style="font-size:25px">✨</div>'
                '<b>Добре дошъл в BookSpace!</b>'
                '<p>Всяка книга е нов свят, който те очаква.</p>'
                '</div>', unsafe_allow_html=True)

    st.markdown(
        '<div style="margin-top:35px;color:#707b99;font-size:11px">'
        'BOOKSPACE © 2026</div>',
        unsafe_allow_html=True
    )


# ---------------- HERO ----------------

st.markdown("""
<div class="hero">
    <div class="hero-tag">✦ YOUR PERSONAL LIBRARY</div>
    <h1>Открий своя<br><span>следващ свят.</span></h1>
    <p>
        Добре дошъл в твоето лично пространство за книги.
        Организирай любимите си истории и откривай нови приключения.
    </p>
</div>
""", unsafe_allow_html=True)


# ---------------- STATISTICS ----------------

col1, col2, col3 = st.columns(3)

statistics = [
    ("📚", len(books), "ОБЩО КНИГИ"),
    ("✨", "∞", "БЕЗКРАЙНИ ИСТОРИИ"),
    ("💜", "24/7", "ТВОЯТА БИБЛИОТЕКА")
]

for column, item in zip([col1, col2, col3], statistics):
    with column:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-icon">{item[0]}</div>
            <div class="metric-number">{item[1]}</div>
            <div class="metric-label">{item[2]}</div>
        </div>
        """, unsafe_allow_html=True)


# ---------------- ADD BOOK ----------------

def add_book():
    st.markdown('<div class="section-title">Добави нова книга</div>',
                unsafe_allow_html=True)
    st.markdown(
        '<div class="section-sub">Разшири своята колекция с нова история.</div>',
        unsafe_allow_html=True
    )

    with st.form("add_form", clear_on_submit=True):
        title = st.text_input(
            "Заглавие на книгата",
            placeholder="Например: Малкият принц..."
        )

        submitted = st.form_submit_button(
            "＋ Добави към библиотеката",
            use_container_width=True
        )

        if submitted:
            title = title.strip()

            if title:
                books.append(title)
                save_books()
                st.success("Книгата е добавена успешно!")
                st.rerun()
            else:
                st.warning("Въведи заглавие на книгата.")


# ---------------- BOOK CATALOG ----------------

def show_books():
    st.markdown('<div class="section-title">Твоята библиотека</div>',
                unsafe_allow_html=True)
    st.markdown(
        '<div class="section-sub">Разгледай всички книги в твоята колекция.</div>',
        unsafe_allow_html=True
    )

    search = st.text_input(
        "Търсене",
        placeholder="🔍 Търси книга по заглавие..."
    )

    sort = st.selectbox(
        "Подреди книгите",
        ["По ред на добавяне", "По азбучен ред", "Обратно по азбучен ред"]
    )

    displayed_books = []

    for book in books:
        if search.casefold() in book.casefold():
            displayed_books.append(book)

    if sort == "По азбучен ред":
        displayed_books.sort(key=str.casefold)
    elif sort == "Обратно по азбучен ред":
        displayed_books.sort(key=str.casefold, reverse=True)

    st.caption(f"Показани {len(displayed_books)} от {len(books)} книги")

    if not displayed_books:
        st.info("📖 Няма намерени книги. Опитай с друго заглавие.")
        return

    columns = st.columns(3)

    for index, book in enumerate(displayed_books):
        with columns[index % 3]:
            cover_number = (index % 6) + 1
            safe_title = html.escape(book)

            st.markdown(f"""
            <div class="book-card">
                <div class="book-cover cover-{cover_number}">
                    📖
                </div>
                <div class="book-category">BOOKSPACE COLLECTION</div>
                <div class="book-title">{safe_title}</div>
                <div class="book-number">BOOK NO. {index + 1:02d}</div>
            </div>
            """, unsafe_allow_html=True)

            if st.button(
                "🗑 Изтрий книга",
                key=f"delete_{index}_{book}",
                use_container_width=True
            ):
                books.remove(book)
                save_books()
                st.rerun()


# ---------------- PAGES ----------------

if page == "🏠 Начало":
    st.markdown('<div class="section-title">Добре дошъл в твоя свят от книги</div>',
                unsafe_allow_html=True)

    st.markdown(
        '<div class="section-sub">Твоите истории, събрани на едно място.</div>',
        unsafe_allow_html=True
    )

    show_books()

elif page == "📚 Всички книги":
    show_books()

elif page == "➕ Добави книга":
    add_book()


# ---------------- FOOTER ----------------

st.markdown("""
<div class="footer">
    BOOKSPACE © 2026<br><br>
    Made with ♥ for people who love reading.
</div>
""", unsafe_allow_html=True)
