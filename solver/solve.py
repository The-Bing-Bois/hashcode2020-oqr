from tqdm import tqdm
import typing

from . import model


def main(filename: str, outname: str) -> None:

    reader = model.InputReader(filename)
    booksCollection, librariesCollection, totalDays = reader.parse()

    solved = solveBestBook(booksCollection, librariesCollection, totalDays)

    writer = model.OutputWriter(outname)

    writer.save(solved)


def solveBestBook(
<<<<<<< HEAD
        booksCollection: model.BooksCollection,
        librariesCollection: model.LibrariesCollection,
        totalDays: int
    ) -> any:
    books = model.books ## need a copy to do stuff
    libraries = model.libraries ## need a copy to do stuff

    currentlyOpening = nil ## to tack currentlyOpeningLibraries
    booksToRestore = [] ## to track currently added books in that fancy book[i]
    librariesToRestoe = []
    openLibraries = 0 ## ++ on open
    librariesToReturn = []

    while (totalDays > 0):
=======
    booksCollection: model.BooksCollection,
    librariesCollection: model.LibrariesCollection,
    totalDays: int,
) -> any:
    books = booksCollection.books  ## need a copy to do stuff
    libraries = librariesCollection.libraries  ## need a copy to do stuff

    currentlyOpening: model.Library = None  ## to tack currentlyOpeningLibraries
    booksToRestore = []  ## to track currently added books in that fancy book[i]
    librariesToRestore = []
    openLibraries = 0  ## ++ on open

    while totalDays > 0:
>>>>>>> 6eb9995150b6593315a66f75bcbbb8f9d0181abd
        openLibrariesToFill = openLibraries
        for b in booksToRestore:
            booksCollection.removeBook(b)
        for l in librariesToRestore:
            l.resetCountBooksPerDay()
        booksToRestore = []
        i = 0

        while openLibrariesToFill > 0:
            currentBook = books[i]
            isThereOneOpen = False
            for l in currentBook.libraries:
                if l.singin == 0:
                    isThereOneOpen = True
                    librariesToRestore.append(l)
                    booksToRestore.append(currentBook)
                    if l.scanBook(currentBook) == 0:
                        openLibrariesToFill -= 1
                    break
            if not isThereOneOpen:
                if currentlyOpening == None:
                    currentlyOpening = min(
                        currentBook.libraries,
                        key=lambda x: x.signin if x.signin > 0 else 100000,
                    )
            i += 1

        if currentlyOpening == None:
            for l in booksCollection.books[i].libraries:
                currentlyOpening = min(
                    currentBook.libraries,
                    key=lambda x: x.signin if x.signin > 0 else 100000,
                )
        else:
            currentlyOpening.signin -= 1
            if currentlyOpening == 0:
                librariesToReturn.append(currentlyOpening)
                currentlyOpening = None
                openLibraries += 1

        totalDays -= 1

    return librariesToReturn
