"""Utility functions."""
from abc import ABC, abstractmethod
from importlib.resources import as_file, files
from pathlib import Path
from typing import Any, Callable, Iterator, Optional

from . import data


def daily_input(day: int) -> Path:
    """Return path to input file of given day."""

    with as_file(files(data).joinpath(f"{day}.txt")) as input_file:
        return input_file


def lines(file: Path, parser: Optional[Callable] = None) -> Iterator:
    """Generator to yield lines of file, cleaned up nicely."""

    with file.open() as f:
        for line in f:
            if parser:
                yield parser(line.strip())
            else:
                yield line.strip()


class Solution(ABC):
    @property
    @abstractmethod
    def day(self) -> int:
        raise NotImplementedError

    @property
    def file(self) -> Path:
        return daily_input(self.day)

    def lines(self, parser) -> Iterator:
        return lines(self.file, parser)

    @abstractmethod
    def part_1(self) -> Any:
        raise NotImplementedError

    def part_2(self) -> Any:
        return None

    def solve(self):
        return self.part_1(), self.part_2()
