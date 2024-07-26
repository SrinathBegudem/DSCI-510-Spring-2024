import os

import pytest
import sqlite3

from lab_11 import create_tables
from lab_11 import insert_data
from lab_11 import execute_queries

TEST_DB_NAME = "bookstore.db"


@pytest.mark.timeout(0.5)
def test_create_tables():
    if os.path.exists(TEST_DB_NAME):
        os.remove(TEST_DB_NAME)

    create_tables()

    conn = sqlite3.connect(TEST_DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    table_names = [table[0] for table in tables]

    # Assert that all tables are created
    assert "books" in table_names
    assert "authors" in table_names
    assert "book_authors" in table_names
    assert "bookstores" in table_names
    assert "sells" in table_names
    conn.close()


@pytest.mark.timeout(0.5)
def test_insert_data():
    conn = sqlite3.connect(TEST_DB_NAME)
    cursor = conn.cursor()
    for table in ["books", "authors", "book_authors", "bookstores", "sells"]:
        cursor.execute(f"DELETE FROM {table};")
    conn.close()

    insert_data()

    conn = sqlite3.connect(TEST_DB_NAME)
    cursor = conn.cursor()

    # Check the 'books' table
    cursor.execute("SELECT * FROM books;")
    books_rows = list(cursor.fetchall())
    assert list(books_rows) == [
        (1, "A Tale of Two Cities", "Chapman & Hall", 1859),
        (2, "Pride and Prejudice", "T. Egerton", 1813),
        (3, "The Hobbit", "George Allen & Unwin", 1937),
        (4, "The Great Gatsby", "Charles Scribner's Sons", 1925),
        (5, "1984", "Secker & Warburg", 1949),
        (6, "Harry Potter and the Philosopher's Stone", "Bloomsbury", 1997),
        (7, "The Catcher in the Rye", "Little, Brown and Company", 1951),
        (8, "To Kill a Mockingbird", "J. B. Lippincott & Co.", 1960),
        (9, "Brave New World", "Chatto & Windus", 1932),
        (10, "The Lord of the Rings", "George Allen & Unwin", 1954),
        (11, "Good Omens", "Gollancz", 1990),
    ]

    # Check the 'authors' table
    cursor.execute("SELECT * FROM authors;")
    authors_rows = list(cursor.fetchall())
    assert authors_rows == [
        (1, "Charles Dickens"),
        (2, "Jane Austen"),
        (3, "J.R.R. Tolkien"),
        (4, "F. Scott Fitzgerald"),
        (5, "George Orwell"),
        (6, "J.K. Rowling"),
        (7, "J.D. Salinger"),
        (8, "Harper Lee"),
        (9, "Aldous Huxley"),
        (10, "Terry Pratchett"),
        (11, "Neil Gaiman"),
    ]

    # Check the 'book_authors' table
    cursor.execute("SELECT * FROM book_authors;")
    book_authors_rows = list(cursor.fetchall())
    assert book_authors_rows == [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
        (7, 7),
        (8, 8),
        (9, 9),
        (10, 3),
        (11, 10),
        (11, 11),
    ]

    # Check the 'bookstores' table
    cursor.execute("SELECT * FROM bookstores;")
    bookstores_rows = list(cursor.fetchall())
    assert bookstores_rows == [
        (1, "Novel Finds", "123 Book Lane, Litville, LV 90909"),
        (2, "Readers Cove", "456 Page St, Storytown, ST 80808"),
        (3, "The Book Nook", "789 Chapter Ave, Tome City, TC 70707"),
    ]

    # Check the 'sells' table
    cursor.execute("SELECT * FROM sells;")
    sells_rows = list(cursor.fetchall())
    assert sells_rows == [
        (1, 1, 12.99),
        (1, 2, 9.99),
        (1, 3, 15.49),
        (2, 4, 8.99),
        (2, 5, 7.99),
        (2, 6, 10.99),
        (3, 7, 6.99),
        (3, 8, 11.99),
        (3, 9, 5.99),
        (1, 10, 22.99),
        (2, 10, 20.99),
        (3, 10, 21.99),
        (2, 11, 18.99),
        (3, 11, 17.49),
    ]
    conn.close()


@pytest.mark.timeout(0.5)
def test_execute_queries_1(capsys):
    execute_queries()
    assert "Good Omens" in capsys.readouterr().out


@pytest.mark.timeout(0.5)
def test_execute_queries_2(capsys):
    execute_queries()
    assert "The Lord of the Rings" in capsys.readouterr().out


@pytest.mark.timeout(0.5)
def test_execute_queries_3(capsys):
    execute_queries()
    assert "10.99" in capsys.readouterr().out


@pytest.mark.timeout(0.5)
def test_execute_queries_4(capsys):
    execute_queries()
    assert "20.365" in capsys.readouterr().out


@pytest.mark.timeout(0.5)
def test_execute_queries_5(capsys):
    execute_queries()
    assert "5" in capsys.readouterr().out


@pytest.mark.timeout(0.5)
def test_execute_queries_6(capsys):
    execute_queries()
    assert "1" in capsys.readouterr().out
