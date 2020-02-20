from sys import argv

from solver import model


def main(filename: str) -> None:

    model.InputReader(filename).parse()


if __name__ == "__main__":
    main(argv[1])
