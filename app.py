import streamlit as st

# Настройки на страницата
st.set_page_config(
    page_title="Лист&Литера",
    page_icon="📚",
    layout="wide"
)

# Дизайн
st.markdown("""
<style>
.stApp {
    background-color: #f4f7f4;
}

h1, h2, h3 {
    color: #174c38;
}

.stButton>button {
    background-color: #176b50;
    color: white;
    border-radius: 10px;
    border: none;
    padding: 10px 20px;
}

.stButton>button:hover {
    background-color: #104832;
    color: white;
}

.book-card {
    background-color: white;
    padding: 18px;
    border-radius: 12px;
    margin-bottom: 12px;
    border: 1px solid #dce8df;
}
</style>
""", unsafe_allow_html=True)


# Списък с книги
if "books" not in st.session_state:
    st.session_state.books = []


# Заглавна част
st.title("📚 Лист&Литера")
st.subheader("Твоята лична дигитална библиотека")

st.write("---")


# Меню
menu = st.sidebar.radio(
    "📖 Основно меню",
    [
        "Начало",
        "Добавяне на книга",
        "Всички книги",
        "Търсене",
        "Изтриване",
        "Сортиране"
    ]
)


# НАЧАЛО
if menu == "Начало":

    st.header("Добре дошъл в своята библиотека!")

    st.write(
        "Тук можеш да добавяш, разглеждаш, "
        "търсиш и подреждаш любимите си книги."
    )

    st.write("### 📊 Статистика")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Общ брой книги",
            len(st.session_state.books)
        )

    with col2:
        st.metric(
            "Различни автори",
            len(set(
                book["author"]
                for book in st.session_state.books
                if book["author"]
            ))
        )

    st.write("---")
    st.success("Твоята библиотека е готова за нови заглавия! 📖")


# ДОБАВЯНЕ НА КНИГА
elif menu == "Добавяне на книга":

    st.header("➕ Добавяне на нова книга")

    title = st.text_input("Заглавие на книгата")
    author = st.text_input("Автор на книгата")

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
            "Друг"
        ]
    )

    year = st.number_input(
        "Година на издаване",
        min_value=0,
        max_value=2100,
        value=2024
    )

    if st.button("Добави книга"):

        if title.strip() == "":
            st.error("Моля, въведи заглавие!")

        else:

            book = {
                "title": title,
                "author": author,
                "genre": genre,
                "year": year
            }

            st.session_state.books.append(book)

            st.success("Книгата беше добавена успешно! 📚")


# ВСИЧКИ КНИГИ
elif menu == "Всички книги":

    st.header("📚 Всички книги")

    books = st.session_state.books

    if len(books) == 0:

        st.info("Все още няма добавени книги.")

    else:

        for i, book in enumerate(books, start=1):

            st.markdown(
                f"""
                <div class="book-card">
                    <h3>📗 {i}. {book['title']}</h3>
                    <p><b>Автор:</b> {book['author']}</p>
                    <p><b>Жанр:</b> {book['genre']}</p>
                    <p><b>Година:</b> {book['year']}</p>
                </div>
                """,
                unsafe_allow_html=True
            )


# ТЪРСЕНЕ ПО ЗАГЛАВИЕ
elif menu == "Търсене":

    st.header("🔎 Търсене на книга")

    search = st.text_input("Въведи заглавие")

    if search:

        found = False

        for book in st.session_state.books:

            if search.lower() in book["title"].lower():

                st.success(
                    f"Намерена книга: {book['title']}"
                )

                st.write("Автор:", book["author"])
                st.write("Жанр:", book["genre"])
                st.write("Година:", book["year"])

                found = True

        if not found:
            st.warning("Не е намерена такава книга.")


# ИЗТРИВАНЕ НА КНИГА
elif menu == "Изтриване":

    st.header("🗑️ Изтриване на книга")

    books = st.session_state.books

    if len(books) == 0:

        st.info("Няма книги за изтриване.")

    else:

        titles = [
            book["title"]
            for book in books
        ]

        selected = st.selectbox(
            "Избери книга",
            titles
        )

        if st.button("Изтрий избраната книга"):

            for book in books:

                if book["title"] == selected:

                    books.remove(book)
                    st.success("Книгата беше изтрита!")
                    st.rerun()


# СОРТИРАНЕ ПО АЗБУЧЕН РЕД
elif menu == "Сортиране":

    st.header("🔤 Сортиране на книгите")

    books = st.session_state.books

    if len(books) == 0:

        st.info("Няма добавени книги.")

    else:

        sorted_books = sorted(
            books,
            key=lambda book: book["title"].lower()
        )

        st.write("### Книги по азбучен ред:")

        for i, book in enumerate(sorted_books, start=1):

            st.write(
                f"{i}. 📘 {book['title']} - {book['author']}"
            )

st.write("---")

st.caption("© 2026 Лист&Литера | Твоята лична библиотека 📚")
