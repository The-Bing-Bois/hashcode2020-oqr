from __future__ import annotations

from pathlib import Path
import typing
import attr


class Book:
    def __init__(self, bid: int, score: int) -> None:
        self.bid = bid
        self.score = score
        self.libraries: typing.List[Library] = []

    def assignLibraries(self, library: Library) -> None:
        self.libraries.append(library)


class Library:
    def __init__(self, lid: int, signin: int, bookPerDay: int) -> None:
        self.lid = lid
        self.signin = signin
        self.booksPerDay = bookPerDay
        self.currentBooksPerDay = bookPerDay
        self.books: typing.List[Book] = []
        self.booksScanned: typing.List[Book] = []
        self.scanned = False

    def addBook(self, book: Book) -> None:
        self.books.append(book)
        book.assignLibraries(self)

    def setScanned(self) -> None:
        self.scanned = True

    def scanBook(self, book: Book) -> int:
        self.currentBooksPerDay -= 1
        return self.currentBooksPerDay

    def resetCountBooksPerDay(self) -> None:
        self.currentBooksPerDay = self.booksPerDay


class LibrariesCollection:
    def __init__(self) -> None:
        self.libraries: typing.List[Library] = []

    def addLibrary(self, library: Library) -> None:
        self.libraries.append(library)


class BooksCollection:
    def __init__(self) -> None:
        self.books: typing.List[Book] = []

    def addBook(self, book: Book) -> None:
        self.books.append(book)

    def removeBook(self, book: Book) -> None:
        self.books.remove(book)


class Solution:
    def __init__(self, idLibrary, books: typing.List[Book]) -> None:
        self.idLibrary = idLibrary
        self.books = books


@attr.s(frozen=True, slots=True, auto_attribs=True)
class InputReader:
    filename: str = attr.ib(converter=str)

    def parse(self) -> typing.Tuple[BooksCollection, LibrariesCollection]:
        content = Path(self.filename).read_text().split("\n")

        booksNumber, librariesNumber, days = (int(x) for x in content[0].split(" "))

        bookScores = [int(x) for x in content[1].split(" ")]

        assert len(bookScores) == booksNumber

        books = [Book(bid, score) for bid, score in enumerate(bookScores)]

        for book in books:
            print(book.bid, book.score)

        raise NotImplementedError()


@attr.s(frozen=True, slots=True, auto_attribs=True)
class OutputWriter:
    filename: str = attr.ib(converter=str)

    def save(self, solutions: typing.List[Solution]) -> None:
        solved = str(len(solutions)) + "\n"
        for solution in solutions:
            solved += str(solution.idLibrary) + " " + str(len(solution.books)) + "\n"
            for book in solution.books:
                solved += str(book.bid) + " "
            solved += "\n"

        outfile = Path("out").joinpath(self.filename)

        outfile.write_text(solved)
