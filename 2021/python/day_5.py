import re
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import List, NamedTuple


class Point(NamedTuple):
    x: int
    y: int


class Segment(NamedTuple):
    start: Point
    end: Point

    def points(self) -> List[Point]:
        x1, y1 = self.start
        x2, y2 = self.end

        xs = range(x1, x2, 1 if x2 > x1 else -1) or [x1] * abs(y2 - y1)
        ys = range(y1, y2, 1 if y2 > y1 else -1) or [y1] * abs(x2 - x1)

        points = [Point(x, y) for x, y in zip(xs, ys)]
        points.append(Point(x2, y2))

        return points


@dataclass
class Map:
    segments: List[Segment]

    def part1(self) -> int:
        segments = [
            segment
            for segment in self.segments
            if (segment.start.x == segment.end.x) or (segment.start.y == segment.end.y)
        ]
        points: List[Point] = [
            point for segment in segments for point in segment.points()
        ]
        counts = Counter(points)
        multiples = [value for value, count in counts.items() if count > 1]

        return len(multiples)

    def part2(self) -> int:
        points: List[Point] = [
            point for segment in self.segments for point in segment.points()
        ]
        counts = Counter(points)
        multiples = [value for value, count in counts.items() if count > 1]

        return len(multiples)

    @classmethod
    def from_lines(cls, lines: List[str]):
        pattern = re.compile(r"([0-9]+),([0-9]+) -> ([0-9]+),([0-9]+)")

        segments: List[Segment] = []
        for line in lines:
            match = pattern.match(line)
            if not match:
                raise ValueError(f"Could not match line '{line}'")
            x1, y1, x2, y2 = [int(x) for x in match.group(1, 2, 3, 4)]
            segment = Segment(Point(x1, y1), Point(x2, y2))
            segments.append(segment)

        return cls(segments)


if __name__ == "__main__":
    input = Path("inputs/day_5.txt")
    lines = input.read_text().splitlines()
    map = Map.from_lines(lines)

    print(f"part 1: {map.part1()}")
    print(f"part 2: {map.part2()}")
