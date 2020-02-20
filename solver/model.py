from pathlib import Path
import typing
import attr


class Book:
    def __init__(self, bid, score):
        self.bid = bid
        self.score = score
        self.libraries = []

    def assignLibraries(self, library):
        self.libraries.append(library)


class Library:
    def __init__(self, lid: int, signin: int, bookPerDay: int) -> None:
        self.lid = lid
        self.signin = signin
        self.booksPerDay = bookPerDay
        self.books = []
        self.read = False

    def addBook(self, book: Book) -> None:
        self.books.append(book)
        book.assignLibraries(self)

    def setRead(self):
        self.read = False


class LibrariesCollection:
    def __init__(self) -> None:
        self.libraries = []

    def addLibrary(self, library: Library):
        self.libraries.append(library)


class BooksCollection:
    def __init__(self) -> None:
        self.books = []

    def addBook(self, book: Book):
        self.books.append(book)


class Solution:
    def __init__(self, idLibrary, books: typing.List[Book]) -> None:
        self.idLibrary = idLibrary
        self.books = books


@attr.s(frozen=True, slots=True, auto_attribs=True)
class InputReader:
    filename: str = attr.ib(converter=str)

    def parse(self) -> None:
        content = Path(self.filename).read_text().split("\n")

        books_number, libraries_number, days = (int(x) for x in content[0].split(" "))

        book_scores = [int(x) for x in content[1].split(" ")]

        assert len(book_scores) == books_number

        print(books_number, libraries_number, days)
        print(book_scores)

        raise NotImplementedError()


@attr.s(frozen=True, slots=True, auto_attribs=True)
class OutputWriter:
    filename: str = attr.ib(converter=str)

    def save(self, solved) -> None:
        outfile = Path("out").joinpath(self.filename)

        outfile.write_text(solved)
