import sys

from .solve import main

if __name__ == "__main__":
    if len(sys.argv) > 3:
        raise ValueError("wrong cli arguments")

    main(sys.argv[1], sys.argv[2])
