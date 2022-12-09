from __future__ import annotations  # problem: use custom class as typehint
from pathlib import Path
from collections import defaultdict
import numpy as np
import re


PROJECT_DIR = Path(__file__).resolve().parents[1]
FILE_DIR    = Path(__file__).resolve().parents[0]
INPUT_FILE         = FILE_DIR / "input.txt"
EXAMPLE_INPUT_FILE = FILE_DIR / "example_input.txt"


def get_input(filepath: Path) -> list:
    """read input into 2d int array"""
    data = []

    with open(filepath, "r") as f:
        # data.extend([int(letter) for letter in line.strip()] for line in f)
        for line in f:
            parsed_line = re.search('\w \d+', line.strip())
            direction   = parsed_line[0][0]
            repetitions = int(parsed_line[0][2:])
            data.extend(direction for _ in range(repetitions))

    return data


class Rope:
    def __init__(self) -> None:
        self.head = (0, 0)
        self.tail = (0, 0)
        self.trail = defaultdict(int)

    def move_rope(self, command: str) -> None:
        self._update_head(command)
        self._update_tail()

    def _update_head(self, command: str) -> None:
        match command:
            case 'R':
                x_new = self.head[0] + 1
                y_new = self.head[1]
            case 'L':
                x_new = self.head[0] - 1
                y_new = self.head[1]
            case 'U':
                x_new = self.head[0]
                y_new = self.head[1] + 1
            case 'D':
                x_new = self.head[0]
                y_new = self.head[1] - 1

        self.head = (x_new, y_new)

    def _update_tail(self):
        x_tail = self.tail[0]
        y_tail = self.tail[1]
        x_head = self.head[0]
        y_head = self.head[1]

        x_diff = x_head - x_tail
        y_diff = y_head - y_tail

        if(abs(x_diff) <= 1 and abs(y_diff) <= 1):
            # a) tail is touching head:
            pass
        elif(y_head == y_tail):
            # b) horizontal
            if x_diff > 1:
                # -> move tail right
                x_tail += 1
            else:
                # -> move tail left
                x_tail -= 1
        elif (x_head == x_tail):
            # c) vertical
            if y_diff > 1:
                # -> move tail up
                y_tail += 1
            else:
                # -> move tail down
                y_tail -= 1
        else:
            # c) diagonal
            if x_diff > 0 and y_diff > 0:
                # -> move tail right and up
                x_tail += 1
                y_tail += 1
            elif x_diff > 0 and y_diff < 0:
                # -> move tail right and down
                x_tail += 1
                y_tail -= 1
            elif x_diff < 0 and y_diff > 0:
                # -> move tail left and up
                x_tail -= 1
                y_tail += 1
            elif x_diff < 0 and y_diff < 0:
                # -> move tail left and up
                x_tail -= 1
                y_tail -= 1

        # update tail
        self.tail = (x_tail, y_tail)

        # save trail of tail
        # a) dict: only map if visited or not
        # self.trail[self.tail] = 1
        # b) defaultdict: init new key with 0 by default
        self.trail[self.tail] += 1


def part_1(data: list) -> int:
    """ 
    find number of visibles trees from outside the grid
    """
    rope = Rope()

    for command in data:
        rope.move_rope(command)
        # print(f"{command}: {rope.tail} -> {rope.head}")

    return len(rope.trail)


def part_2(data: list) -> int:
    """ 
    find tree with highest scenic score
    i.e. multiply viewing distances in each direction
    """

    
    return 0

if __name__ == '__main__':
    print(INPUT_FILE)

    example_data = get_input(EXAMPLE_INPUT_FILE)
    print(example_data)

    data = get_input(INPUT_FILE)
    print(len(data))

    # Part 1
    print(part_1(example_data))
    print(part_1(data))

    # Part 2
    # print(part_2(example_data))
    # print(part_2(data))
