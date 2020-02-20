import sys

##from solver.solve import main
from .model import Book, OutputWriter, Solution

if __name__ == "__main__":
    ##if len(sys.argv) > 2:
    ##  raise ValueError("wrong cli arguments")
    ##
    ##  main(sys.argv[1])
    out = OutputWriter("FileOut")
    solutions = []
    books = []
    books.append(Book(0, 10))
    books.append(Book(1, 11))
    solutions.append(Solution(1, books))
    solutions.append(Solution(2, books))
    out.save(solutions)
