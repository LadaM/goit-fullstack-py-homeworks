from abc import ABC, abstractmethod
import logging

class LibraryInterface(ABC):
    @abstractmethod
    def add_book(self, book):
        pass

    @abstractmethod
    def remove_book(self, title):
        pass

    @abstractmethod
    def show_books(self):
        pass


# Extend the Library class to implement the interface
class Library(LibraryInterface):
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                break

    def show_books(self):
        for book in self.books:
            print(book)


# Extending Library functionality with SearchableLibrary (OCP)
class SearchableLibrary(Library):
    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        logging.info("Book not found")
        return None


class LibraryManager:
    def __init__(self, library: LibraryInterface):
        self.library = library

    def add_book(self, title, author, year):
        self.library.add_book(Book(title, author, year))

    def remove_book(self, title):
        self.library.remove_book(title)

    def show_books(self):
        self.library.show_books()

    def find_book(self, title):
        if isinstance(self.library, SearchableLibrary):
            book = self.library.find_book(title)
            if book:
                print(f"Found: {book}")
        else:
            logging.info("Find book functionality is not supported in this library")


class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f'Title: {self.title}, Author: {self.author}, Year: {self.year}'
