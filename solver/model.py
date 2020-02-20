from pathlib import Path
import attr


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
    content: str = attr.ib(converter=str)

    def save(self) -> None:
        outfile = Path("out").joinpath(self.filename)

        outfile.write_text(self.content)


class Library:
    def __init__(self, lid, signin, signout) -> None:
        self.lid = lid
        self.signin = signin
        self.signout = signout
        self.books = []

    def addbook(self, book) -> None:
        self.books.append(book)
        book.assignLibraries(self)


class Book:
    def __init__(self, bid, score):
        self.bid = bid
        self.score = score
        self.libraries = []

    def assignLibraries(self, library):
        self.libraries.append(library)


class LibraryCollection:
    def __init__(self):
        self.libraries = []

    def addLibrary(self, Library):
        self.libraries.append(Library)


class BooksCollection:
    books: list[Book] = attr.ib(converter=list[Book])

