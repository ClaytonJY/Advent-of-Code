from pathlib import Path
from typing import Any, Generator


class Solution:
    def __init__(self, data: str | Path) -> None:
        super().__init__()
        self.data = data

    def lines(self) -> Generator[str, None, None]:
        """Yield lines from the input."""
        if isinstance(self.data, str):
            lines = iter(self.data.splitlines())
        elif isinstance(self.data, Path):
            lines = self.data.open()

        for line in lines:
            yield line.strip()

    def objects(self) -> Generator[Any, None, None]:
        for line in self.lines():
            yield line

    def part_1(self) -> Any:
        ...

    def part_2(self):
        ...

    def solve(self) -> list[int]:
        return self.part_1(), self.part_2()
