#!/usr/bin/env python3
from dataclasses import dataclass

@dataclass
class Shelf:
    name: str
    num_books : int
    link: str

@dataclass
class Book:
    title: str
    author: str
    link: str
    isbn13: str
    shelf_url : str


