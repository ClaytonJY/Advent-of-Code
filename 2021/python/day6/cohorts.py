from dataclasses import dataclass
from pathlib import Path
from typing import Counter, Dict, List, NamedTuple


@dataclass
class FishSimulator:
    cohorts: Counter[int]

    @property
    def n_fish(self):
        return self.cohorts.total()

    def age_days(self, days: int):
        cohorts = self.cohorts
        for _ in range(days):
            cohorts = Counter({age - 1: n for age, n in cohorts.items()})
            spawned: int = cohorts.get(-1, 0)
            cohorts.update({-1: -spawned, 6: spawned, 8: spawned})

        self.cohorts = cohorts

    @classmethod
    def from_file(cls, file: str):
        line = Path(file).read_text().strip()
        ages = [int(x) for x in line.split(",")]
        return cls(Counter(ages))


if __name__ == "__main__":
    simulator = FishSimulator.from_file("example.txt")

    simulator.age_days(18)
    assert simulator.n_fish == 26

    simulator.age_days(80 - 18)
    assert simulator.n_fish == 5934

    simulator.age_days(256 - 80)
    assert simulator.n_fish == 26984457539

    simulator = FishSimulator.from_file("input.txt")

    simulator.age_days(80)
    print(f"part1: {simulator.n_fish}")  # 391888

    simulator.age_days(256 - 80)
    print(f"part2: {simulator.n_fish}")  # 1754597645339
