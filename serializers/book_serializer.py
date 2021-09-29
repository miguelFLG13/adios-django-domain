from domain.entities.book import Book
from domain.serializers.serializer import Serializer


class BookSerializer(Serializer):
    cls = Book

    read_fields = [
        'id', 'title', 'author', 'isbn', 'release_date', 'price'
    ]

    write_fields = [
        'title', 'author', 'isbn', 'release_date', 'price'
    ]
