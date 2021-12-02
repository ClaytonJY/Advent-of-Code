from pathlib import Path

INPUT = Path("./1.txt")


def part1():
    last = None
    increases = 0
    for line in INPUT.read_text().splitlines():
        current = int(line)
        if last and current > last:
            increases += 1
        last = current

    return increases


def part2():
    numbers = [int(x) for x in INPUT.read_text().splitlines()]

    past_sum = None
    increases = 0
    for a, b, c in zip(numbers[:-2], numbers[1:-1], numbers[2:]):
        sum = a + b + c
        if past_sum and sum > past_sum:
            increases += 1
        past_sum = sum

    return increases


if __name__ == "__main__":
    print(part1(), part2())
