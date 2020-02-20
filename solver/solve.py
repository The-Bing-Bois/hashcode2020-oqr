from tqdm import tqdm

from . import model


def main(filename: str) -> None:

    booksCollection, librariesCollection = model.InputReader(filename).parse()

    solved = solve(booksCollection, librariesCollection)

    writer = model.OutputWriter("example_output")

    writer.save(solved)


def solve(
    booksCollection: model.BooksCollection,
    librariesCollection: model.LibrariesCollection,
) -> any:

    raise NotImplementedError()
