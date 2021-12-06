from pathlib import Path
from typing import List


class FishSimulator:
    def __init__(self, ages: List[int]):
        self.ages = ages

    @property
    def n_fish(self):
        return len(self.ages)

    def age_day(self):
        new = [8] * self.ages.count(0)
        ages = [(age - 1) if age > 0 else 6 for age in self.ages]
        self.ages = ages + new

    def age_days(self, days: int):
        for _ in range(days):
            self.age_day()

    @classmethod
    def from_file(cls, file: str):
        line = Path(file).read_text().strip()
        ages = [int(x) for x in line.split(",")]
        return cls(ages)


if __name__ == "__main__":
    simulator = FishSimulator.from_file("example.txt")

    simulator.age_days(18)
    assert simulator.n_fish == 26

    simulator.age_days(80 - 18)
    assert simulator.n_fish == 5934

    # simulator.age_days(256 - 80)
    # assert simulator.n_fish == 26984457539

    simulator = FishSimulator.from_file("input.txt")

    simulator.age_days(80)
    print(f"part1: {simulator.n_fish}")

    # simulator.age_days(256 - 80)
    print(f"part2: {simulator.n_fish}")
