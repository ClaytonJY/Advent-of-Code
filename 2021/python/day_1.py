from utils import Runner


class Day1(Runner):
    def part1(self):
        last = None
        increases = 0
        for line in self.lines:
            current = int(line)
            if last and current > last:
                increases += 1
            last = current

        return increases

    def part2(self):
        numbers = [int(x) for x in self.lines]

        past_sum = None
        increases = 0
        for a, b, c in zip(numbers[:-2], numbers[1:-1], numbers[2:]):
            sum = a + b + c
            if past_sum and sum > past_sum:
                increases += 1
            past_sum = sum

        return increases


if __name__ == "__main__":
    Day1(__file__).run()
