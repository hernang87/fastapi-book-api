from pydantic import BaseModel


class Book(BaseModel):
    title: str
    author: str
    isbn: str

    def __init__(self, title: str, author: str, isbn: str):
        super().__init__(title=title, author=author, isbn=isbn)
        self.title = title
        self.author = author
        self.isbn = isbn

    def __repr__(self):
        return f"Book({self.title}, {self.author}, {self.isbn})"
