from dataclasses import dataclass
from functools import reduce
from pathlib import Path
from typing import Dict, List, Set


@dataclass
class DigitRow:
    inputs: List[Set[str]]  # 10
    outputs: List[Set[str]]  # 4

    def decode(self) -> Dict[str, int]:
        """Determine the string for each digit 0-9"""
        map: Dict[int, Set[str]] = {}
        # easy ones
        digits = self.inputs
        for digit in digits:
            match len(digit):
                case 2:
                    map[1] = digit
                case 4:
                    map[4] = digit
                case 3:
                    map[7] = digit
                case 7:
                    map[8] = digit

        # group up 5- and 6-letter digits
        fives = [digit for digit in digits if len(digit) == 5]  # 2, 3, 5
        sixes = [digit for digit in digits if len(digit) == 6]  # 0, 6, 9

        # 3 is the only five w/ both parts from 1
        map[3] = [digit for digit in fives if len(map[1] & digit) == 2][0]

        # 6 is the only len-6 digit w/o both parts from 1
        map[6] = [digit for digit in sixes if len(map[1] & digit) == 1][0]

        # 3 letters all fives share must be center column
        columns: Set[str] = reduce(lambda a, b: a & b, [digit for digit in fives])

        # 0 is only one w/ only 2 columns (middle missing)
        map[0] = [digit for digit in sixes if len(columns & digit) == 2][0]

        # 9 is the last sixer
        map[9] = [digit for digit in sixes if digit not in [map[0], map[6]]][0]

        # 5 contains the same half of 1 as 6
        map[5] = [digit for digit in fives if len(digit & map[6] & map[1]) == 1 and digit != map[3]][0]

        # 2 is the last five
        map[2] = [digit for digit in fives if digit not in [map[3], map[5]]][0]

        new_map =  {"".join(sorted(digit)): score for score, digit in map.items()}

        if len(new_map.keys()) < 10:
            print(map, new_map)

        return new_map

    def score(self) -> int:
        map = self.decode()
        scores = []
        for output in self.outputs:
            string = "".join(sorted(output))
            try:
                scores.append(map[string])
            except KeyError:
                pass

        return int("".join([str(x) for x in scores]))

    @classmethod
    def from_line(cls, line: str):
        inputs, outputs = [
            [set(piece) for piece in piece.split()] for piece in line.split(" | ")
        ]
        return cls(inputs, outputs)


@dataclass
class DigitDecoder:
    digit_rows: List[DigitRow]

    def part1(self):
        """count the 1/4/7/8s in outputs"""
        distinct_outputs = [
            output
            for row in self.digit_rows
            for output in row.outputs
            if len(output) in [2, 4, 3, 7]
        ]
        return len(distinct_outputs)

    def part2(self):
        return(sum([row.score() for row in self.digit_rows]))

    @classmethod
    def from_file(cls, file: str):
        lines: List[str] = Path(file).read_text().splitlines()
        rows: List[DigitRow] = [DigitRow.from_line(line) for line in lines]
        return cls(rows)


if __name__ == "__main__":
    digit_decoder = DigitDecoder.from_file("example.txt")
    digit_decoder.part1() == 26
    digit_decoder.part2() == 61229

    digit_decoder = DigitDecoder.from_file("input.txt")

    print(f"part1: {digit_decoder.part1()}")
    print(f"part2: {digit_decoder.part2()}")
