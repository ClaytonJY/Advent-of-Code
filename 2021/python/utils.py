from abc import ABC, abstractmethod
from dataclasses import dataclass
from pathlib import Path
from typing import Any, List

DATA_DIR = Path("inputs")


@dataclass
class Runner(ABC):
    file: str
    data_dir: Path = DATA_DIR

    @property
    def input_file(self) -> Path:
        stem = Path(self.file).stem
        return Path(self.data_dir) / (stem + ".txt")

    @property
    def lines(self) -> List[str]:
        return self.input_file.read_text().splitlines()

    @abstractmethod
    def part1(self) -> Any:
        raise NotImplementedError

    @abstractmethod
    def part2(self) -> Any:
        return NotImplementedError

    def run(self):
        print(f"part 1: {self.part1()}")
        print(f"part 2: {self.part2()}")
