from pathlib import Path
from typing import List


def part1(input):
    horizontal, vertical = 0, 0
    for line in input:
        direction, amount = line.split(" ")
        amount = int(amount)
        if direction == "forward":
            horizontal += amount
        elif direction == "up":
            vertical -= amount
        elif direction == "down":
            vertical += amount

    return horizontal * vertical


def part2(input):
    horizontal, depth, aim = 0, 0, 0
    for line in input:
        direction, amount = line.split(" ")
        amount = int(amount)
        if direction == "forward":
            horizontal += amount
            depth += amount * aim
        elif direction == "down":
            aim += amount
        elif direction == "up":
            aim -= amount

    return horizontal * depth


if __name__ == "__main__":
    stem: str = Path(__file__).stem
    input_file = Path("inputs") / (stem + ".txt")
    input: List[str] = input_file.read_text().splitlines()

    print(part1(input), part2(input))
