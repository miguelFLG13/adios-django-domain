from dataclasses import dataclass
from datetime import date
from decimal import Decimal
from typing import Optional


@dataclass
class Book:
    """ Class to represent a book """
    id: int
    title: Optional[str] = None
    author: Optional[str] = None
    isbn: Optional[str] = None
    release_date: Optional[date] = None
    price: Optional[Decimal] = None

