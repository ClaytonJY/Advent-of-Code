from dataclasses import dataclass
from pathlib import Path


@dataclass
class Something:
    ...

    @classmethod
    def from_file(cls, file: str):
        Path(file)
        # return cls(...)


if __name__ == "__main__":
    something = Something.from_file("example.txt")

    something_else = Something.from_file("input.txt")

    print(f"part1: {None}")
    print(f"part2: {None}")
