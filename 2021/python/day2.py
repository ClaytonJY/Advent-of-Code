from pathlib import Path

INPUT = Path("./2.txt")


def part1():
    horizontal, vertical = 0, 0
    for line in INPUT.read_text().splitlines():
        direction, amount = line.split(" ")
        amount = int(amount)
        if direction == "forward":
            horizontal += amount
        elif direction == "up":
            vertical -= amount
        elif direction == "down":
            vertical += amount

    return horizontal * vertical


def part2():
    horizontal, depth, aim = 0, 0, 0
    for line in INPUT.read_text().splitlines():
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
    print(part1(), part2())
