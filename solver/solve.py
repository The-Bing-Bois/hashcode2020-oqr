from tqdm import tqdm

from . import model


def main(filename: str, outname: str) -> None:

    reader = model.InputReader(filename)
    booksCollection, librariesCollection, totalDays = reader.parse()

    solved = solveBestBook(booksCollection, librariesCollection,totalDays)

    writer = model.OutputWriter(outname)

    writer.save(solved)


def solveBestBook(
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

    while (totalDays > 0):
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
                if currentlyOpening == nil:
                    currentlyOpening = min(currentBook.libraries, key=lambda x: if x.signin > 0: x.signin else: return 100000)
            i += 1

        if currentlyOpening == nil:
            for l in booksCollection[i].libraries:
                currentlyOpening = min(currentBook.libraries, key=lambda x: if x.signin > 0: x.signin else: return 100000)
        else:
            currentlyOpening.signin -= 1
            if currentlyOpening == 0:
                currentlyOpening = nil
                openLibraries += 1

        totalDays -= 1

    return libraries


"""
def solveFastLibrary() -> None:
    ## opt2 FastLibraryFirst
    pass
"""
