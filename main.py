import sqlite3

import eel

# Connection to SQLite database
conn = sqlite3.connect("books.db")
c = conn.cursor()

# Create the table if it does not already exist
c.execute(
    """CREATE TABLE IF NOT EXISTS books
             (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, description TEXT)"""
)
conn.commit()

# Initialize Eel
eel.init("static")


@eel.expose
def create_book(title: str, description: str) -> str:
    """ Inserting a new entry into the database """
    c.execute(
        "INSERT INTO books (title, description) VALUES (?, ?)", (title, description)
    )
    conn.commit()
    return "Книга успішно створена!"


@eel.expose
def get_books() -> list[tuple[int, str, str]]:
    """  Getting all the books from the database """
    c.execute("SELECT * FROM books")
    books = c.fetchall()
    return books


@eel.expose
def delete_book(book_id: int, ) -> str:
    """ Deleting a book from the database by its ID """
    c.execute("DELETE FROM books WHERE id=?", (book_id,))
    conn.commit()
    return "Книга успішно видалена!"


eel.start(
    "create_book.html",
)
