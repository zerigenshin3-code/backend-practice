import sqlite3

conn = sqlite3.connect("library.db")    #crea el archivo sino existe
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    year INTEGER
)
""")

books_to_add = [
        ("Olas Salvajes", "Gonzalo Tarriba", 1993),
        ("Olas Tranquilas", "Gonzalo Tarriba", 1996),
        ("La Tormenta de ayer", "Gonzalo Tarriba", 1999),
]

cursor.executemany(
    "INSERT INTO books (title, author, year) VALUES (?, ?, ?)",
    books_to_add,
)

conn.commit() #guarda los cambios en el archivo



###Read Data with Select
cursor.execute("SELECT title, author, year FROM books ORDER BY year")
for row in cursor.fetchall():
    print(row)  #cada fila es un tuple

###User selects year
year = int(input("Elige el año"))

cursor.execute("SELECT title, author, year FROM books WHERE year > ?", (year,))
for row in cursor.fetchall():
    print(row)

cursor.execute("UPDATE books SET year = ? WHERE id = ?", (1995, 1))
conn.commit()

cursor.execute("SELECT id, title, author, year FROM books")
for row in cursor.fetchall():
    print(row)

cursor.execute("DELETE FROM books WHERE id = ?", (2,))
conn.commit()

cursor.execute("SELECT id, title, author, year FROM books")
for row in cursor.fetchall():
    print(row)

conn.close()
