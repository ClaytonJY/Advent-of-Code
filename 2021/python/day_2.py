from utils import Runner


class Day2(Runner):
    def part1(self) -> int:
        horizontal, vertical = 0, 0
        for line in self.lines:
            direction, amount = line.split(" ")
            amount = int(amount)
            if direction == "forward":
                horizontal += amount
            elif direction == "up":
                vertical -= amount
            elif direction == "down":
                vertical += amount

        return horizontal * vertical

    def part2(self) -> int:
        horizontal, depth, aim = 0, 0, 0
        for line in self.lines:
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
    Day2(__file__).run()
