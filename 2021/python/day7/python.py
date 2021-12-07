from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path
from typing import List, Tuple


@dataclass
class CrabController:
    positions: List[int]

    def cost(self, target: int) -> int:
        return sum([abs(target - pos) for pos in self.positions])

    def cost2(self, target: int) -> int:
        return sum([sum(range(1, abs(target - pos) + 1)) for pos in self.positions])

    def optimize(self, func) -> Tuple[int, int]:  # (position, cost)
        x: int = max(self.positions) // 2  # start in center
        cost = func(x)
        while True:
            if (new_cost := func(x + 1)) < cost:
                x += 1
            elif (new_cost := func(x - 1)) < cost:
                x -= 1
            else:
                return x, cost
            cost = new_cost

    @classmethod
    def from_file(cls, file: str):
        positions = [int(x) for x in Path(file).read_text().split(",")]
        return cls(positions)


if __name__ == "__main__":
    controller = CrabController.from_file("example.txt")
    assert controller.cost(2) == 37
    assert controller.cost(1) == 41
    assert controller.cost(3) == 39
    assert controller.cost(10) == 71

    assert controller.optimize(controller.cost) == (2, 37)
    assert controller.optimize(controller.cost2) == (5, 168)

    controller = CrabController.from_file("input.txt")

    print(f"part1: {controller.optimize(controller.cost)}")
    print(f"part2: {controller.optimize(controller.cost2)}")
