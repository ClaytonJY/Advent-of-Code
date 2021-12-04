from typing import List, Optional, Tuple
from utils import Runner


class Day3(Runner):
    def part1(self) -> int:
        sums: Optional[List] = None
        total = 0
        for line in self.lines:
            new = [int(val) for val in line]
            if sums:
                sums = [a + b for a, b in zip(new, sums)]
            else:
                sums = new
            total += 1

        gamma_l = [sum > total / 2 for sum in sums]
        epsilon_l = [not g for g in gamma_l]

        gamma, epsilon = [
            int("".join(["1" if val else "0" for val in x]), 2)
            for x in (gamma_l, epsilon_l)
        ]

        return gamma * epsilon

    def part2(self):

        rows: List[List[int]] = []
        totals: List[int] = []
        for line in self.lines:
            row: List[int] = [int(value) for value in line]
            rows.append(row)

        survivors = rows
        for i in range(0, len(rows[0])):
            sum = 0
            for row in survivors:
                sum += row[i]
            most_common = 1 if sum >= len(survivors) / 2 else 0

            new_survivors = []
            for row in survivors:
                if row[i] == most_common:
                    new_survivors.append(row)

            survivors = new_survivors
            if len(survivors) == 1:
                break

        oxy_gen_row = survivors[0]

        survivors = rows
        for i in range(0, len(rows[0])):
            sum = 0
            for row in survivors:
                sum += row[i]
            least_common = 0 if sum >= len(survivors) / 2 else 1

            new_survivors = []
            for row in survivors:
                if row[i] == least_common:
                    new_survivors.append(row)

            survivors = new_survivors
            if len(survivors) == 1:
                break

        co2_scrub_row = survivors[0]

        oxy_gen_rating = int("".join([str(x) for x in oxy_gen_row]), 2)
        co2_scrub_rating = int("".join([str(x) for x in co2_scrub_row]), 2)

        return oxy_gen_rating * co2_scrub_rating


if __name__ == "__main__":
    Day3(__file__).run()
