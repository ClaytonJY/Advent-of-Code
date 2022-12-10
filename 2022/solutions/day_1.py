from dataclasses import dataclass
from typing import Generator

from utils.solution import Solution


@dataclass
class Elf:
    weights: tuple[int]

    @property
    def total(self):
        return sum(self.weights)


class TopN:
    def __init__(self, n):
        self.values: list[int] = [0] * n

    def insert(self, x):
        for i, value in enumerate(self.values):  # high to low
            if x > value:
                self.values = [*self.values[:i], x, *self.values[i:-1]]
                break

    def total(self):
        return sum(self.values)


class Day1(Solution):
    """
    >>> example = '''1000
    ... 2000
    ... 3000
    ...
    ... 4000
    ...
    ... 5000
    ... 6000
    ...
    ... 7000
    ... 8000
    ... 9000
    ...
    ... 10000
    ... '''
    >>> Day1(example).solve()
    (24000, 45000)
    """

    def objects(self) -> Generator[Elf, None, None]:
        weights: list[int] = []
        for line in self.lines():
            if line != "":
                weights.append(int(line))
            else:
                yield Elf(tuple(weights))
                weights = []

        yield Elf(tuple(weights))

    def part_1(self) -> int:
        highest_weight = 0
        for elf in self.objects():
            highest_weight = max(highest_weight, elf.total)

        return highest_weight

    def part_2(self) -> int:
        top_3 = TopN(3)
        for elf in self.objects():
            top_3.insert(elf.total)
        return top_3.total()
