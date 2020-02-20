from tqdm import tqdm

from . import model


def main(filename: str) -> None:

    model.InputReader(filename).parse()


def solveBestBook(model: Model??) -> None:
    day = model.day
    books = model.books // need a copy to do stuff
    libraries = model.libraries // need a copy to do stuff
    currentlyOpening = nil // to tack currentlyOpeningLibraries
    booksToRestore = [] // to track currently added books in that fancy book[i]
    openLibraries = 0 // ++ on open

    while (day > 0):
        openLibrariesToFill = openLibraries
        for b in booksToRestore:
            books.remove(b)
        i = 0
        while openLibrariesToFill > 0:
            currentBook = books[i]
            if l = any(currentBook.libraries, .isOpen):
                if l.appendBook(currentBook): // ritorna true se ultimo libro aggiungibile nella libreria
                    openLibrarisToFill -= 1
                booksToRestore.append(currentBook)
            else:
                if !currentlyOpening:
                    l = min(currentBook.libraries, .signupTime):
                    l.isOpening = True
                    currentlyOpening = l
            i += 1

        if !currentlyOpening:
            l = any(books[i].libraries, !.isOpen)

        if currentlyOpening:
            if (l.tempoDiAttesa -= 1) == 0:
                currentlyOpening = nil
                openLibraries += 1

        day -= 1

    return libraries

                

            
    

def solveFastLibrary() -> None:
    // opt2 FastLibraryFirst
    pass
