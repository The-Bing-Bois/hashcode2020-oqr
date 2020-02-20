import sys

from solver.solve import main

if __name__ == "__main__":
    if len(sys.argv) > 2:
        raise ValueError("wrong cli arguments")

    main(sys.argv[1])
