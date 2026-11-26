import json
from pathlib import Path
from uuid import uuid4

import streamlit as st

# -------------------- НАСТРОЙКИ --------------------

st.set_page_config(
    page_title="Лист&Литера | Лична библиотека",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded",
)

DATA_FILE = Path(__file__).with_name("books.json")


def load_books():
    if DATA_FILE.exists():
        try:
            data = json.loads(DATA_FILE.read_text(encoding="utf-8"))
            return data if isinstance(data, list) else []
        except (OSError, json.JSONDecodeError):
            return []
    return []


def save_books():
    DATA_FILE.write_text(
        json.dumps(st.session_state.books, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )


if "books" not in st.session_state:
    st.session_state.books = load_books()

books = st.session_state.books


# -------------------- ДИЗАЙН --------------------

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&family=Playfair+Display:wght@600;700;800&display=swap');

:root {
    --forest: #173d30;
    --forest2: #245b45;
    --sage: #dcebe0;
    --cream: #f7f8f4;
    --ink: #1c2b24;
    --muted: #78877e;
    --line: #e7ece6;
}

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}

.stApp {
    background: var(--cream);
    color: var(--ink);
}

[data-testid="stHeader"] {
    background: rgba(247,248,244,.92);
}

.block-container {
    padding-top: 2.1rem;
    padding-bottom: 3rem;
    max-width: 1440px;
}

[data-testid="stSidebar"] {
    background: #15382c;
    border-right: 1px solid #244b3b;
}

[data-testid="stSidebar"] > div {
    padding-top: 1.4rem;
}

[data-testid="stSidebar"] * {
    color: #f0f6f1 !important;
}

[data-testid="stSidebar"] [data-testid="stRadio"] label {
    padding: 11px 13px;
    border-radius: 12px;
    margin: 3px 0;
    font-weight: 600;
    transition: .2s ease;
}

[data-testid="stSidebar"] [data-testid="stRadio"] label:hover {
    background: #285440;
}

[data-testid="stSidebar"] [data-testid="stRadio"] label:has(input:checked) {
    background: #2b6048;
}

.brand-wrap {
    display: flex;
    gap: 12px;
    align-items: center;
    padding: 8px 5px 28px;
}

.brand-symbol {
    width: 48px;
    height: 48px;
    display: flex;
    align-items: center;
    justify-content: center;
    background: #e1efe4;
    color: #173d30;
    border-radius: 16px;
    font-size: 25px;
    box-shadow: 0 8px 18px rgba(0,0,0,.12);
}

.brand-title {
    font-family: 'Playfair Display', serif;
    font-size: 22px;
    font-weight: 700;
    color: white;
    line-height: 1.1;
}

.brand-caption {
    color: #a9c7b5;
    font-size: 10px;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-top: 5px;
}

.sidebar-foot {
    margin-top: 28px;
    padding: 17px 13px;
    border: 1px solid #315743;
    border-radius: 14px;
    color: #bad0c2;
    font-size: 12px;
    line-height: 1.6;
    background: rgba(255,255,255,.035);
}

.hero {
    position: relative;
    overflow: hidden;
    padding: 34px 38px;
    border-radius: 25px;
    color: white;
    background: linear-gradient(115deg,#153b2e 0%,#28684c 100%);
    box-shadow: 0 15px 35px rgba(24,67,47,.14);
    margin-bottom: 26px;
}

.hero:after {
    content: "";
    position: absolute;
    width: 300px;
    height: 300px;
    border-radius: 50%;
    right: -75px;
    top: -145px;
    border: 1px solid rgba(255,255,255,.12);
    box-shadow: 0 0 0 35px rgba(255,255,255,.035),
                0 0 0 75px rgba(255,255,255,.025);
}

.hero-kicker {
    color: #b8d8c3;
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 12px;
}

.hero-title {
    font-family: 'Playfair Display', serif;
    color: white;
    font-size: 42px;
    line-height: 1.12;
    font-weight: 700;
    letter-spacing: -.5px;
    margin: 0 0 12px;
}

.hero-copy {
    color: #d8e9dd;
    font-size: 15px;
    max-width: 580px;
    line-height: 1.7;
}

.hero-art {
    font-size: 76px;
    text-align: center;
    filter: drop-shadow(0 12px 12px rgba(0,0,0,.18));
}

.eyebrow {
    color: #84938a;
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 1.6px;
    text-transform: uppercase;
    margin-bottom: 7px;
}

.section-heading {
    font-family: 'Playfair Display', serif;
    color: #1b3e2f;
    font-size: 26px;
    font-weight: 700;
    margin: 0 0 4px;
}

.section-description {
    color: var(--muted);
    font-size: 13px;
    margin-bottom: 19px;
}

.metric {
    background: white;
    border: 1px solid var(--line);
    border-radius: 18px;
    padding: 20px 21px;
    min-height: 124px;
    box-shadow: 0 5px 18px rgba(25,54,38,.035);
}

.metric-top {
    display: flex;
    align-items: center;
    justify-content: space-between;
}

.metric-label {
    color: #7b8980;
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 1px;
    text-transform: uppercase;
}

.metric-icon {
    width: 38px;
    height: 38px;
    border-radius: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
    background: #edf5ef;
    font-size: 19px;
}

.metric-number {
    color: #1b4a35;
    font-family: 'Playfair Display', serif;
    font-size: 34px;
    font-weight: 700;
    margin-top: 7px;
}

.metric-note {
    color: #9aa59e;
    font-size: 11px;
    margin-top: -2px;
}

.book-card {
    background: #fff;
    border: 1px solid var(--line);
    border-radius: 17px;
    padding: 17px 18px;
    margin-bottom: 11px;
    box-shadow: 0 4px 14px rgba(25,54,38,.025);
    transition: transform .18s ease, box-shadow .18s ease;
}

.book-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 10px 22px rgba(25,54,38,.07);
}

.book-cover {
    width: 45px;
    height: 54px;
    border-radius: 7px 11px 11px 7px;
    background: linear-gradient(145deg,#dcebe0,#b7d3c0);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 22px;
    box-shadow: inset 4px 0 rgba(23,61,48,.08);
}

.book-name {
    color: #213b2e;
    font-size: 15px;
    font-weight: 800;
    margin-bottom: 4px;
}

.book-detail {
    color: #849188;
    font-size: 12px;
}

.genre-pill {
    display: inline-block;
    padding: 5px 10px;
    background: #edf5ef;
    color: #397052;
    border-radius: 20px;
    font-size: 10px;
    font-weight: 800;
}

.empty {
    text-align: center;
    background: #fff;
    border: 1px dashed #d5e1d7;
    border-radius: 20px;
    padding: 42px 20px;
    margin-top: 8px;
}

.empty-icon {
    font-size: 42px;
    margin-bottom: 10px;
}

.empty-title {
    font-family: 'Playfair Display', serif;
    color: #284936;
    font-size: 21px;
    font-weight: 700;
}

.empty-copy {
    color: #89968e;
    font-size: 13px;
    margin-top: 6px;
}

div.stButton > button,
div[data-testid="stFormSubmitButton"] > button {
    border-radius: 11px;
    min-height: 43px;
    font-weight: 700;
    border: 1px solid #176447;
    background: #176447;
    color: white;
    transition: all .2s ease;
}

div.stButton > button:hover,
div[data-testid="stFormSubmitButton"] > button:hover {
    background: #104b35;
    border-color: #104b35;
    color: white;
}

div[data-testid="stForm"] {
    background: white;
    border: 1px solid var(--line);
    border-radius: 20px;
    padding: 24px;
    box-shadow: 0 5px 18px rgba(25,54,38,.035);
}

input, textarea {
    border-radius: 10px !important;
}

[data-testid="stSelectbox"] [role="combobox"] {
    border-radius: 10px;
}

.stAlert {
    border-radius: 12px;
}

hr {
    border-color: #e6ece6;
}

footer {
    visibility: hidden;
}
</style>
""", unsafe_allow_html=True)


# -------------------- СТРАНИЧНО МЕНЮ --------------------

with st.sidebar:
    st.markdown("""
    <div class="brand-wrap">
      <div class="brand-symbol">📚</div>
      <div>
        <div class="brand-title">Лист&Литера</div>
        <div class="brand-caption">Твоята лична библиотека</div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    page = st.radio(
        "НАВИГАЦИЯ",
        [
            "Начало",
            "Всички книги",
            "Добави книга",
            "Препоръчани книги",
            "Търсене",
            "Управление"
        ],
        label_visibility="visible"
    )

    st.markdown(f"""
    <div class="sidebar-foot">
      <div style="font-size:20px;margin-bottom:5px">✦</div>
      <b>Място за всяка история.</b><br>
      Твоята колекция в един красив и подреден дом.<br><br>
      <span style="color:#e4f0e7">
        {len(books)} запазени заглавия
      </span>
    </div>
    """, unsafe_allow_html=True)


# -------------------- ПОМОЩНИ ФУНКЦИИ --------------------

def section(title, description=""):
    st.markdown(
        f'<div class="eyebrow">ЛИЧНА БИБЛИОТЕКА</div>'
        f'<div class="section-heading">{title}</div>'
        f'<div class="section-description">{description}</div>',
        unsafe_allow_html=True
    )


def metric(label, number, icon, note):
    st.markdown(f"""
    <div class="metric">
      <div class="metric-top">
        <div class="metric-label">{label}</div>
        <div class="metric-icon">{icon}</div>
      </div>
      <div class="metric-number">{number}</div>
      <div class="metric-note">{note}</div>
    </div>
    """, unsafe_allow_html=True)


def empty_state(
    title="Тук все още е тихо…",
    copy="Добави първата си книга и започни своята колекция."
):
    st.markdown(f"""
    <div class="empty">
      <div class="empty-icon">📖</div>
      <div class="empty-title">{title}</div>
      <div class="empty-copy">{copy}</div>
    </div>
    """, unsafe_allow_html=True)


def render_books(items):
    if not items:
        empty_state()
        return

    for i, book in enumerate(items, 1):
        title = book.get("title", "Без заглавие")
        author = book.get("author") or "Авторът не е посочен"
        genre = book.get("genre") or "Без категория"
        year = book.get("year") or "—"

        st.markdown(f"""
        <div class="book-card">
          <div style="display:flex;align-items:center;gap:15px">
            <div class="book-cover">📗</div>
            <div style="flex:1">
              <div class="book-name">
                {i:02d} &nbsp; {title}
              </div>
              <div class="book-detail">
                {author} &nbsp; · &nbsp; {year}
              </div>
            </div>
            <div class="genre-pill">{genre}</div>
          </div>
        </div>
        """, unsafe_allow_html=True)


# -------------------- ПРЕПОРЪЧАНИ КНИГИ --------------------

recommendations = [
    {
        "title": "Малкият принц",
        "author": "Антоан дьо Сент-Екзюпери",
        "genre": "Класика",
        "year": 1943,
        "description": "Нежна и мъдра история за приятелството, любовта и нещата, които са невидими за очите.",
        "emoji": "🌟"
    },
    {
        "title": "Под игото",
        "author": "Иван Вазов",
        "genre": "Класика",
        "year": 1894,
        "description": "Един от най-значимите български романи, който разказва за живота и духа на българите преди Освобождението.",
        "emoji": "🏛️"
    },
    {
        "title": "Хари Потър и Философският камък",
        "author": "Дж. К. Роулинг",
        "genre": "Фентъзи",
        "year": 1997,
        "description": "Магическо приключение за приятелството, смелостта и откриването на един необикновен свят.",
        "emoji": "⚡"
    },
    {
        "title": "1984",
        "author": "Джордж Оруел",
        "genre": "Антиутопия",
        "year": 1949,
        "description": "Въздействащ роман за свободата, истината и силата на контрола над обществото.",
        "emoji": "👁️"
    },
    {
        "title": "Гордост и предразсъдъци",
        "author": "Джейн Остин",
        "genre": "Роман",
        "year": 1813,
        "description": "Остроумен и романтичен разказ за първите впечатления, любовта и обществените очаквания.",
        "emoji": "🌷"
    },
    {
        "title": "Алхимикът",
        "author": "Паулу Коелю",
        "genre": "Роман",
        "year": 1988,
        "description": "Философска притча за мечтите, смелостта да следваш пътя си и търсенето на личното щастие.",
        "emoji": "🧭"
    },
    {
        "title": "Властелинът на пръстените: Задругата на пръстена",
        "author": "Дж. Р. Р. Толкин",
        "genre": "Фентъзи",
        "year": 1954,
        "description": "Епично пътешествие из Средната земя, изпълнено с магия, опасности и незабравими герои.",
        "emoji": "🧙"
    },
    {
        "title": "Човек на име Уве",
        "author": "Фредрик Бакман",
        "genre": "Роман",
        "year": 2012,
        "description": "Топла, забавна и трогателна история за неочакваните приятелства и малките жестове.",
        "emoji": "☕"
    },
    {
        "title": "Бай Ганьо",
        "author": "Алеко Константинов",
        "genre": "Българска класика",
        "year": 1895,
        "description": "Сатирични истории, които с хумор и наблюдателност представят различни черти на обществото.",
        "emoji": "✒️"
    },
]


# -------------------- НАЧАЛО --------------------

if page == "Начало":

    st.markdown("""
    <div class="hero">
      <div class="eyebrow" style="color:#b9d8c4">
        ДОБРЕ ДОШЪЛ В СВОЯ СВЯТ ОТ ИСТОРИИ
      </div>

      <div style="display:flex;align-items:center;gap:20px">
        <div style="flex:1">
          <div class="hero-title">
            Всяка книга е<br>ново приключение.
          </div>

          <div class="hero-copy">
            Подреди любимите си заглавия, откривай историите си отново
            и създай библиотека, която носи твоя почерк.
          </div>
        </div>

        <div class="hero-art">📚</div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    section(
        "Твоята библиотека",
        "Малко пространство за големите истории в живота ти."
    )

    authors = {
        b.get("author", "").strip().casefold()
        for b in books if b.get("author", "").strip()
    }

    genres = {
        b.get("genre", "").strip().casefold()
        for b in books if b.get("genre", "").strip()
    }

    a, b, c = st.columns(3)

    with a:
        metric("Общо книги", len(books), "📚", "Всички заглавия в колекцията")

    with b:
        metric("Автори", len(authors), "✍️", "Различни автори")

    with c:
        metric("Жанрове", len(genres), "🏷️", "Категории в библиотеката")

    st.write("")

    section(
        "Последни попълнения",
        "Книгите, които добави последно."
    )

    render_books(list(reversed(books[-4:])))


# -------------------- ВСИЧКИ КНИГИ --------------------

elif page == "Всички книги":

    section(
        "Всички книги",
        "Цялата ти колекция, събрана на едно място."
    )

    if books:

        left, right = st.columns([3, 1])

        with left:
            order = st.selectbox(
                "Подреди заглавията",
                ["По ред на добавяне", "А → Я", "Я → А"]
            )

        with right:
            st.metric("Заглавия", len(books))

        result = books.copy()

        if order == "А → Я":
            result.sort(key=lambda x: x["title"].casefold())

        elif order == "Я → А":
            result.sort(
                key=lambda x: x["title"].casefold(),
                reverse=True
            )

        render_books(result)

    else:
        empty_state()


# -------------------- ДОБАВИ КНИГА --------------------

elif page == "Добави книга":

    section(
        "Ново заглавие",
        "Добави книга към своята колекция."
    )

    with st.form("new_book", clear_on_submit=True):

        title = st.text_input(
            "Заглавие *",
            placeholder="Например: Малкият принц"
        )

        author = st.text_input(
            "Автор",
            placeholder="Например: Антоан дьо Сент-Екзюпери"
        )

        col1, col2 = st.columns(2)

        with col1:
            genre = st.selectbox(
                "Жанр",
                [
                    "Роман",
                    "Фентъзи",
                    "Класика",
                    "Мистерия",
                    "Научна литература",
                    "Биография",
                    "Поезия",
                    "Друго"
                ]
            )

        with col2:
            year = st.number_input(
                "Година на издаване",
                min_value=0,
                max_value=2100,
                value=0,
                help="Остави 0, ако не знаеш годината."
            )

        note = st.text_area(
            "Лична бележка",
            placeholder="Любим цитат, впечатление или нещо, което искаш да запомниш…",
            height=90
        )

        submitted = st.form_submit_button(
            "＋  Запази в библиотеката",
            use_container_width=True
        )

        if submitted:

            if not title.strip():
                st.error("Моля, въведи заглавие на книгата.")

            elif any(
                x["title"].casefold() == title.strip().casefold()
                for x in books
            ):
                st.warning(
                    "Това заглавие вече съществува в библиотеката."
                )

            else:

                books.append({
                    "id": str(uuid4()),
                    "title": title.strip(),
                    "author": author.strip(),
                    "genre": genre,
                    "year": int(year) if year else "",
                    "note": note.strip()
                })

                save_books()

                st.success(
                    f"„{title.strip()}“ е добавена успешно!"
                )

                st.rerun()


# -------------------- ПРЕПОРЪЧАНИ КНИГИ --------------------

elif page == "Препоръчани книги":

    section(
        "Подбрани за теб",
        "Открий вдъхновяващи истории за следващото си четиво."
    )

    categories = [
        "Всички",
        "Класика",
        "Фентъзи",
        "Роман",
        "Антиутопия",
        "Българска класика"
    ]

    chosen_category = st.selectbox(
        "Избери категория",
        categories
    )

    if chosen_category == "Всички":
        visible_recommendations = recommendations
    else:
        visible_recommendations = [
            book for book in recommendations
            if book["genre"] == chosen_category
        ]

    st.markdown(
        f"**{len(visible_recommendations)} предложения за четене**"
    )

    for idx, rec in enumerate(visible_recommendations):

        already_added = any(
            b.get("title", "").casefold() == rec["title"].casefold()
            for b in books
        )

        with st.container(border=True):

            left, middle, right = st.columns([0.7, 4, 1.35])

            with left:
                st.markdown(
                    f"<div style='font-size:34px;padding-top:8px'>"
                    f"{rec['emoji']}</div>",
                    unsafe_allow_html=True
                )

            with middle:

                st.markdown(f"#### {rec['title']}")

                st.markdown(
                    f"<span style='color:#718078;font-size:12px'>"
                    f"{rec['author']} &nbsp; · &nbsp; "
                    f"{rec['year']} &nbsp; · &nbsp; "
                    f"{rec['genre']}</span>",
                    unsafe_allow_html=True
                )

                st.write(rec["description"])

            with right:

                st.write("")
                st.write("")

                if already_added:

                    st.button(
                        "✓ В библиотеката",
                        key=f"rec_added_{idx}",
                        disabled=True,
                        use_container_width=True
                    )

                elif st.button(
                    "＋ Добави",
                    key=f"rec_add_{idx}",
                    type="primary",
                    use_container_width=True
                ):

                    books.append({
                        "id": str(uuid4()),
                        "title": rec["title"],
                        "author": rec["author"],
                        "genre": rec["genre"],
                        "year": rec["year"],
                        "note": "Добавена от препоръчаните книги."
                    })

                    save_books()

                    st.success(
                        f"„{rec['title']}“ е добавена в библиотеката!"
                    )

                    st.rerun()

    st.caption(
        "Можеш да добавиш всяко препоръчано заглавие директно "
        "в личната си библиотека."
    )


# -------------------- ТЪРСЕНЕ --------------------

elif page == "Търсене":

    section(
        "Открий своята книга",
        "Потърси по заглавие, автор или жанр."
    )

    query = st.text_input(
        "Търсене",
        placeholder="Напиши заглавие, автор или жанр…"
    )

    if query.strip():

        q = query.casefold().strip()

        found = [
            x for x in books
            if q in x["title"].casefold()
            or q in x.get("author", "").casefold()
            or q in x.get("genre", "").casefold()
        ]

        st.markdown(f"**Резултати: {len(found)}**")

        render_books(found)

    else:
        st.info(
            "Въведи дума в полето, за да започнеш търсенето."
        )


# -------------------- УПРАВЛЕНИЕ --------------------

elif page == "Управление":

    section(
        "Управление",
        "Поддържай библиотеката си подредена."
    )

    if books:

        st.markdown("#### 🗑️ Изтриване на книга")

        options = {
            f'{x["title"]} — {x.get("author") or "непосочен автор"}': x["id"]
            for x in books
        }

        selected = st.selectbox(
            "Избери заглавие",
            list(options.keys())
        )

        confirm = st.checkbox(
            "Потвърждавам изтриването на избраната книга."
        )

        if st.button(
            "Изтрий книгата",
            disabled=not confirm
        ):

            target_id = options[selected]

            st.session_state.books = [
                x for x in books
                if x["id"] != target_id
            ]

            save_books()

            st.success("Книгата беше изтрита.")

            st.rerun()

    else:

        empty_state(
            "Няма книги за управление.",
            "Добави заглавие, за да започнеш."
        )


# -------------------- FOOTER --------------------

st.markdown("<br><hr>", unsafe_allow_html=True)

st.markdown("""
<div style='text-align:center;color:#9aa69e;
font-size:11px;letter-spacing:.5px'>
ЛИСТ&ЛИТЕР &nbsp; · &nbsp;
ТВОЯТА ЛИЧНА БИБЛИОТЕКА &nbsp; · &nbsp; 2026
</div>
""", unsafe_allow_html=True)
