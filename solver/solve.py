from tqdm import tqdm

from . import model


def main(filename: str) -> None:

    model.InputReader(filename).parse()


def solve() -> None:
    pass
