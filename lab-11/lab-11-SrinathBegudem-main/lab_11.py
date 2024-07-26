# Lab 11
# Replace "WRITE CODE HERE" with your python code and remove the "pass" statement
# Do not invoke the functions outside main block
import sqlite3

DB_NAME = "bookstore.db"

# ----------------- Question 1 -----------------


def create_tables() -> None:
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute("""
    CREATE TABLE books (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        publisher TEXT,
        year INTEGER
    )
    """)
    
    c.execute("""
    CREATE TABLE authors (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL
    )
    """)
    
    c.execute("""
    CREATE TABLE book_authors (
        book_id INTEGER,
        author_id INTEGER,
        FOREIGN KEY (book_id) REFERENCES books(id),
        FOREIGN KEY (author_id) REFERENCES authors(id),
        PRIMARY KEY (book_id, author_id)
    )
    """)
    
    c.execute("""
    CREATE TABLE bookstores (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        address TEXT
    )
    """)
    
    c.execute("""
    CREATE TABLE sells (
        bookstore_id INTEGER,
        book_id INTEGER,
        sale_price REAL,
        FOREIGN KEY (bookstore_id) REFERENCES bookstores(id),
        FOREIGN KEY (book_id) REFERENCES books(id)
    )
    """)

    conn.commit()
    conn.close()

# ----------------- Question 2 -----------------


def insert_data() -> None:
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    # Sample data insertion
    books_data = [
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
        (11, "Good Omens", "Gollancz", 1990)
    ]

    authors_data = [
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
        (11, "Neil Gaiman")
    ]

    book_authors_data = [
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
        (11, 11)
    ]

    bookstores_data = [
        (1, "Novel Finds", "123 Book Lane, Litville, LV 90909"),
        (2, "Readers Cove", "456 Page St, Storytown, ST 80808"),
        (3, "The Book Nook", "789 Chapter Ave, Tome City, TC 70707")
    ]

    sells_data = [
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
        (3, 11, 17.49)
    ]


    c.executemany("INSERT INTO books VALUES (?, ?, ?, ?)", books_data)
    c.executemany("INSERT INTO authors VALUES (?, ?)", authors_data)
    c.executemany("INSERT INTO book_authors VALUES (?, ?)", book_authors_data)
    c.executemany("INSERT INTO bookstores VALUES (?, ?, ?)", bookstores_data)
    c.executemany("INSERT INTO sells (bookstore_id, book_id, sale_price) VALUES (?, ?, ?)", sells_data)

    conn.commit()
    conn.close()


# ----------------- Question 3 -----------------


def execute_queries() -> None:
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    # Query 1
    c.execute("""
    SELECT books.title 
    FROM books 
    JOIN book_authors ON books.id = book_authors.book_id 
    JOIN authors ON book_authors.author_id = authors.id 
    WHERE authors.name = 'Neil Gaiman'
    """)
    result = c.fetchall()
    print("Books authored by 'Neil Gaiman':", result)

    # Query 2
    c.execute("""
    SELECT title 
    FROM books 
    WHERE publisher = 'George Allen & Unwin' 
    AND year = 1954
    """)
    result = c.fetchall()
    print("Books published by 'George Allen & Unwin' in 1954:", result)

    # Query 3
    c.execute("""
    SELECT AVG(sale_price) 
    FROM sells 
    JOIN books ON sells.book_id = books.id 
    WHERE books.publisher = 'Bloomsbury'
    """)
    result = c.fetchone()[0]
    print("Average sale price of books published by 'Bloomsbury':", result)

    # Query 4
    c.execute("""
    SELECT AVG(sale_price) 
    FROM sells 
    JOIN books ON sells.book_id = books.id 
    JOIN book_authors ON books.id = book_authors.book_id 
    JOIN authors ON book_authors.author_id = authors.id 
    WHERE authors.name = 'J.R.R. Tolkien'
    """)
    result = c.fetchone()[0]
    print("Average sale price of books authored by 'J.R.R. Tolkien':", result)

    conn.close()


if __name__ == "__main__":
    create_tables()
    insert_data()
    execute_queries()
