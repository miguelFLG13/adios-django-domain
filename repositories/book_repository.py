from abc import ABC, abstractmethod
from typing import List

from domain.entities.book import Book

class BookRepository(ABC):

    def __init__(
        self,
        database: Database
    ) -> None:
        self._database = database

    @abstractmethod
    def find_by_author(self, author_id: int) -> List[Book]:
        pass

    @abstractmethod
    def create(self, book: Book) -> Book:
        pass

