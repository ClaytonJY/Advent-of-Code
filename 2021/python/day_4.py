from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List

import numpy as np
from numpy.typing import NDArray


@dataclass
class Board:
    board: NDArray[np.int_]

    def play(self, numbers: List[int]) -> Dict[str, int]:
        bingo_sum = self.board.shape[0]
        for i, _ in enumerate(numbers):
            subset = numbers[: (i + 1)]
            mask = np.isin(self.board, subset)
            if bingo_sum in np.concatenate([mask.sum(0), mask.sum(1)]):
                score = self.board[~mask].sum() * numbers[i]
                return {"score": score, "turns": i}


@dataclass
class Bingo:
    numbers: List[int]
    boards: List[Board]

    def play(self) -> List[Dict[str, int]]:

        results = [board.play(self.numbers) for board in self.boards]
        return sorted(results, key=lambda x: x["turns"])

    @classmethod
    def from_file(cls, path: Path):
        numbers_txt, *boards_txt = path.read_text().split("\n\n")

        numbers = [int(x) for x in numbers_txt.split(",")]
        boards = []
        for board_txt in boards_txt:
            lines: List[str] = board_txt.strip().splitlines()
            rows: List[List[int]] = [[int(x) for x in line.split()] for line in lines]
            board = Board(np.array(rows))
            boards.append(board)

        return cls(numbers, boards)


if __name__ == "__main__":
    input = Path("inputs/day_4.txt")
    game = Bingo.from_file(input)
    scores = game.play()

    print(f"part 1: {scores[0]['score']}")
    print(f"part 2: {scores[-1]['score']}")
