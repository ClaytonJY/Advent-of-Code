from .utils import Solution


class Day1(Solution):
    day: 1

    def part_1(self) -> int:
        numbers = []
        for number in self.lines(int):
            for n in numbers:
                if n + number == 2020:
                    return n * number
            numbers.append(number)
