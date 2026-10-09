from fastapi import HTTPException
from fastapi import FastAPI
app = FastAPI()
from pydantic import BaseModel
class Book(BaseModel):
    title: str
    author: str
    year: int

books = []
###Welcome msg
@app.get("/")
def read_root():
    return {"message": "Bienvenido a mi libreria"}


###POST Book
@app.post("/books", status_code=201)
def create_book(book: Book):
    books.append(book)
    return book


###Search Book
@app.get("/books/{book_id}")
def get_book(book_id: int):
    if book_id < 0 or book_id >= len(books):
        raise HTTPException(status_code=404, detail="No se encuentra este libro")
    return books[book_id]

###List Books
@app.get ("/books")
def list_books():
    return books

###Delete Book
@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    if book_id < 0 or book_id >= len(books):
        raise HTTPException(status_code=404, detail="No existe este libro")
    return books.pop(book_id)
