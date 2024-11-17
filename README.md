# Books API

This is a simple Books API built with Python. The database is in memory for this attempt, defined by the `Library` class.

## Initialization

To initialize the repository, follow these steps:

1. Clone the repository:
  ```bash
  git clone https://github.com/hernang87/fastapi-book-api.git
  cd fastapi-book-api
  ```

2. Create a virtual environment and activate it:
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

3. Install the dependencies:
  ```bash
  pip install -r requirements.txt
  ```

4. Run the application:
  ```bash
  python main.py
  ```

## Endpoints

The following endpoints are defined in `main.py`:

- **GET /books**
  - Description: Retrieve a list of all books.
  - Response: JSON array of books.

- **GET /books/<id>**
  - Description: Retrieve a specific book by its ID.
  - Parameters: `id` (integer) - The ID of the book.
  - Response: JSON object of the book.

- **POST /books**
  - Description: Add a new book.
  - Request Body: JSON object containing book details (title, author, etc.).
  - Response: JSON object of the created book.

- **PUT /books/<id>**
  - Description: Update an existing book by its ID.
  - Parameters: `id` (integer) - The ID of the book.
  - Request Body: JSON object containing updated book details.
  - Response: JSON object of the updated book.

- **DELETE /books/<id>**
  - Description: Delete a book by its ID.
  - Parameters: `id` (integer) - The ID of the book.
  - Response: JSON object confirming deletion.

## Database

The database is in memory for this attempt and is defined by the `Library` class. This means that all data will be lost when the application is stopped.
