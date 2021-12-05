from dataclasses import dataclass, field
from pathlib import Path
from typing import List, Optional, Tuple

import numpy as np
from numpy.typing import NDArray


@dataclass
class Board:
    board: NDArray[np.int_]

    def play(self, numbers: List[int]):
        bingo_sum = self.board.shape[0]
        for i, _ in enumerate(numbers):
            subset = numbers[: (i + 1)]
            mask = np.isin(self.board, subset)
            if bingo_sum in np.concatenate([mask.sum(0), mask.sum(1)]):
                score = self.board[~mask].sum() * numbers[i]
                return score, i


@dataclass
class Bingo:
    numbers: List[int]
    boards: List[Board]

    @classmethod
    def from_file(cls, path: Path):
        numbers_txt, *boards_txt = path.read_text().split("\n\n")

        numbers = [int(x) for x in numbers_txt.split(",")]
        boards = [
            Board(
                np.array(
                    [
                        [int(x) for x in line.split()]
                        for line in board.strip().split("\n")
                    ]
                )
            )
            for board in boards_txt
        ]

        return cls(numbers, boards)

    def play(self):

        results: List[Tuple[int, int]] = [
            board.play(self.numbers) for board in self.boards
        ]
        return sorted(results, key=lambda x: x[1])


if __name__ == "__main__":
    input = Path("inputs/day_4.txt")
    game = Bingo.from_file(input)
    scores = game.play()
    print(scores)
    print(f"part 1: {scores[0][0]}")
    print(f"part 2: {scores[-1][0]}")
