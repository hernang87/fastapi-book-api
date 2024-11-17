from data.book import Book
from pydantic import BaseModel


class Library(BaseModel):
    books: dict[str, Book]

    def __init__(self):
        books = {}
        super().__init__(books=books)
        self.books = books

    def has_book(self, isbn: str):
        return isbn in self.books

    def add_book(self, book: Book):
        if self.has_book(book.isbn):
            raise ValueError(f"Book {book.isbn} already exists")

        self.books[book.isbn] = book

    def get_books(self):
        return self.books

    def get_book(self, isbn: str):
        if not self.has_book(isbn):
            raise ValueError(f"Book {isbn} not found")

        return self.books[isbn]

    def remove_book(self, isbn: str):
        if not self.has_book(isbn):
            raise ValueError(f"Book {isbn} not found")

        del self.books[isbn]

    def update_book(self, isbn: str, title: str = None, author: str = None):
        if not self.has_book(isbn):
            raise ValueError(f"Book {isbn} not found")
        book = self.books[isbn]
        book.title = title if title and title != book.title else book.title
        book.author = author if author and author != book.author else book.author
        return book

    def __str__(self):
        return f"Library with {len(self.books)} books"

    def __repr__(self):
        return f"Library({[book for book in self.books]})"
