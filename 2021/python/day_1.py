from pathlib import Path
from typing import List


def part1(input):
    last = None
    increases = 0
    for line in input:
        current = int(line)
        if last and current > last:
            increases += 1
        last = current

    return increases


def part2(input):
    numbers = [int(x) for x in input]

    past_sum = None
    increases = 0
    for a, b, c in zip(numbers[:-2], numbers[1:-1], numbers[2:]):
        sum = a + b + c
        if past_sum and sum > past_sum:
            increases += 1
        past_sum = sum

    return increases


if __name__ == "__main__":
    stem: str = Path(__file__).stem
    input_file = Path("inputs") / (stem + ".txt")
    input: List[str] = input_file.read_text().splitlines()

    print(part1(input), part2(input))
