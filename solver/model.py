from pathlib import Path
import attr


@attr.s(frozen=True, slots=True, auto_attribs=True)
class InputReader:
    filename: str = attr.ib(converter=str)

    def parse(self) -> None:
        path = Path(self.filename)

        content = path.read_text().split("\n")

        books_number, libraries_number, days = content[0].split(" ")

        print(books_number, libraries_number, days)

        raise NotImplementedError()


@attr.s(frozen=True, slots=True, auto_attribs=True)
class OutputWriter:
    filename: str = attr.ib(converter=str)

    def save(self, content: str) -> None:
        outfile = Path("out").joinpath(self.filename)

        outfile.write_text(content)

        raise NotImplementedError()
