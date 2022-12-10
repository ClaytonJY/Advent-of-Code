from pathlib import Path

from solutions.day_1 import Day1

file = Path("data/day_1.txt")


def test_day_1():
    day_1 = Day1(file)
    assert day_1.solve() == (71124, 204639)
