from __future__ import annotations

import typing
from pathlib import Path

import attr


class Book:
    def __init__(self, bid: int, score: int) -> None:
        self.bid = bid
        self.score = score
        self.libraries: typing.List[Library] = []

    def __repr__(self) -> str:
        return f"{self.bid}, {self.score}"

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

    def __repr__(self) -> str:
        return f"id: {self.lid}, {self.booksScanned}"

    def addBook(self, book: Book) -> None:
        self.books.append(book)
        book.assignLibraries(self)

    def setScanned(self) -> None:
        self.scanned = True

    def scanBook(self, book: Book) -> int:
        self.currentBooksPerDay -= 1
        self.booksScanned.append(book)
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
    def __init__(self, idLibrary: int, books: typing.List[Book]) -> None:
        self.idLibrary = idLibrary
        self.books = books


@attr.s(frozen=True, slots=True, auto_attribs=True)
class InputReader:
    filename: str = attr.ib(converter=str)

    def parse(self) -> typing.Tuple[BooksCollection, LibrariesCollection, int]:
        content = Path(self.filename).read_text().split("\n")

        booksNumber, librariesNumber, totalDays = (
            int(x) for x in content[0].split(" ")
        )

        bookScores = [int(x) for x in content[1].split(" ")]

        assert len(bookScores) == booksNumber

        books = [Book(bid, score) for bid, score in enumerate(bookScores)]

        booksCollection = BooksCollection()

        for book in books:
            booksCollection.addBook(book)

        librariesCollection = LibrariesCollection()

        librariesLines = iter(content[2:-2])

        currentLibraryId = 0
        for line in librariesLines:
            booksNumber, daysToSignup, booksShippedPerDay = (
                int(x) for x in line.split(" ")
            )

            nextLine = next(librariesLines)
            bookIds = [int(x) for x in nextLine.split(" ")]

            assert len(bookIds) == booksNumber

            library = Library(currentLibraryId, daysToSignup, booksShippedPerDay)

            for bookId in bookIds:
                # book = next(filter(lambda b: b.bid == bookId, booksCollection.books))

                library.addBook(booksCollection.books[bookId])
                booksCollection.books[bookId].assignLibraries(library)

            librariesCollection.addLibrary(library)
            currentLibraryId += 1

        booksCollection.books = sorted(
            booksCollection.books, key=lambda b: b.score, reverse=True
        )

        return booksCollection, librariesCollection, totalDays


@attr.s(frozen=True, slots=True, auto_attribs=True)
class OutputWriter:
    filename: str = attr.ib(converter=str)

    def save(self, solutions: typing.List[Library]) -> None:
        solved = str(len(solutions)) + "\n"
        for solution in solutions:
            solved += str(solution.lid) + " " + str(len(solution.booksScanned)) + "\n"
            for book in solution.booksScanned:
                solved += str(book.bid) + " "
            solved += "\n"

        outfile = Path("out").joinpath(self.filename)

        outfile.write_text(solved)
