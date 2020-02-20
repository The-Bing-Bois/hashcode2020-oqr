from pathlib import Path
import attr


@attr.s(frozen=True, slots=True, auto_attribs=True)
class InputReader:
    filename: str = attr.ib(converter=str)

    def parse(self) -> None:
        content = Path(self.filename).read_text(encoding="UTF-8")

        print(content)

        raise NotImplementedError()


@attr.s(frozen=True, slots=True, auto_attribs=True)
class OutputWriter:
    filename: str = attr.ib(converter=str)

    def save(self, content: str) -> None:
        outfile = Path("out").joinpath(self.filename)

        outfile.write_text(content)

        raise NotImplementedError()
