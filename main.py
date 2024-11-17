from fastapi import FastAPI, HTTPException
from data.book import Book
from data.library import Library

app = FastAPI()

library = Library()

def handle_exceptions(func, status_code):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            raise HTTPException(status_code=status_code, detail=str(e))
    return wrapper


@app.post("/books")
@handle_exceptions(status_code=400)
def add_book(book: Book):
    library.add_book(book)
    return book


@app.get("/books")
def get_books():
    return library.get_books()


@app.get("/books/{isbn}")
@handle_exceptions(status_code=404)
def get_book(isbn: str):
    book: Book = library.get_book(isbn)
    return book


@app.put("/books/{isbn}")
@handle_exceptions(status_code=404)
def update_book(isbn: str, title: str = None, author: str = None):
    book = library.update_book(isbn, title, author)
    return book


@app.delete("/books/{isbn}")
@handle_exceptions(status_code=404)
def delete_book(isbn: str):
    library.remove_book(isbn)
    return {"message": f"Book {isbn} deleted"}
