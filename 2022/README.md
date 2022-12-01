# Advent of Code 2022

[website](https://adventofcode.com/2022)

Here we go again!

## Day 1

For the example


```python
EXAMPLE = """
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
"""
```

We treat each line as a weight of an item, and each blankline-delimited block as the items for a person.


```python
from typing import Iterator


def read_example(example: str = EXAMPLE) -> Iterator[str]:
    return (line for line in example.strip().split("\n"))

list(read_example())
```




    ['1000',
     '2000',
     '3000',
     '',
     '4000',
     '',
     '5000',
     '6000',
     '',
     '7000',
     '8000',
     '9000',
     '',
     '10000']




```python
from dataclasses import dataclass
from functools import cache


@dataclass(frozen=True)
class Elf:
    weights: tuple[int]

    @cache
    def total(self):
        return sum(self.weights)

def parse_elves(input: Iterator[str]):
    weights: list[int] = []
    for line in input:
        if line != "":
            weights.append(int(line))
        else:
            yield Elf(tuple(weights))
            weights = []

    yield Elf(tuple(weights))

list(parse_elves(read_example()))
```




    [Elf(weights=(1000, 2000, 3000)),
     Elf(weights=(4000,)),
     Elf(weights=(5000, 6000)),
     Elf(weights=(7000, 8000, 9000)),
     Elf(weights=(10000,))]



Finally, we need an argmax of the sums of each elf, and we know the answer should be 24000.


```python
def argmax_total_weight(elves: Iterator[Elf]) -> int:
    argmax: int = 0
    for elf in elves:
        argmax = max(argmax, elf.total())
    return argmax

assert argmax_total_weight(parse_elves(read_example())) == 24000
```

### Part 1

Now we need to repeat that process, but using the file `data/01.txt`.


```python
from itertools import islice
from pathlib import Path


file = Path("data/01.txt")

def read_file(file: Path = Path("data/01.txt")) -> Iterator[str]:
    for line in file.open():
        yield line.strip()

list(islice(read_file(), 30))
```




    ['5916',
     '7281',
     '1715',
     '3853',
     '10283',
     '1455',
     '7807',
     '6117',
     '',
     '33711',
     '6672',
     '',
     '3988',
     '6947',
     '1674',
     '1928',
     '6128',
     '6361',
     '3817',
     '6141',
     '3301',
     '5473',
     '2609',
     '4262',
     '6105',
     '',
     '2725',
     '7430',
     '7415',
     '6997']




```python
argmax_total_weight(parse_elves(read_file()))
```




    71124



### Part 2

For part 2, we need to identify the _top 3_ calorie-sums and add them together.


```python
class TopN:
    def __init__(self, n):
        self.values: list[int, int, int] = [0]*n

    def insert(self, x):
        for i, value in enumerate(self.values):  # high to low
            if x > value:
                self.values = [*self.values[:i], x, *self.values[i:-1]]
                break

    def total(self):
        return sum(self.values)

def part_2(elves: Iterator[Elf]):
    top_3 = TopN(3)
    for elf in elves:
        top_3.insert(elf.total())
    return top_3.total()

part_2(parse_elves(read_example())) == 45000

part_2(parse_elves(read_file()))
```




    204639




```python

```
