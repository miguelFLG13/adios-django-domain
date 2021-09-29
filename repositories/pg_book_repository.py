from typing import List

from domain.entities.book import Book
from domain.repositories.database import Database
from domain.repositories.book_repository import BookRepository


class PgBookRepository(BookRepository):

    def __init__(
        self,
        database: Database
    ) -> None:
        super().__init__(database)

    def find_by_author(self, author_id: int) -> List[Book]:
        self._database.cursor.execute(
            "SELECT * FROM books WHERE author = '{}'".format(author_id)
        )

        db_books = self._database.cursor.fetchall()
        books = self.__convert_to_book(db_books)

        return books

    def create(self, book: Book) -> Book:
        self._database.cursor.execute(
            "INSERT INTO books (\"title\", \"author\", \"isbn\", \"release_date\", \"price\") VALUES ('{}', '{}', '{}', '{}', '{}');".format(
                book.title,
                book.author,
                book.isbn,
                book.release_date,
                book.price
            )
        )
        self._database.connection.commit()

        return book

