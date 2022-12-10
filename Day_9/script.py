from __future__ import annotations  # problem: use custom class as typehint
from pathlib import Path
from collections import defaultdict


PROJECT_DIR = Path(__file__).resolve().parents[1]
FILE_DIR    = Path(__file__).resolve().parents[0]
INPUT_FILE         = FILE_DIR / "input.txt"
EXAMPLE_INPUT_FILE = FILE_DIR / "example_input.txt"


def get_input(filepath: Path) -> list:
    """read input into char array"""
    data = []

    with open(filepath, "r") as f:
        for line in f:
            direction, repetitions = line.split()
            data.extend(direction for _ in range(int(repetitions)))

    return data


class Rope:
    def __init__(self, n_elements) -> None:
        self.n_elements = n_elements
        self.knots = [(0, 0) for _ in range(n_elements)]
        self.trail = defaultdict(int)

    def move_rope(self, command: str) -> None:
        self._update_head(command)
        self._update_knots()

    def _update_head(self, command: str) -> None:
        match command:
            case 'R':
                x_new = self.knots[0][0] + 1
                y_new = self.knots[0][1]
            case 'L':
                x_new = self.knots[0][0] - 1
                y_new = self.knots[0][1]
            case 'U':
                x_new = self.knots[0][0]
                y_new = self.knots[0][1] + 1
            case 'D':
                x_new = self.knots[0][0]
                y_new = self.knots[0][1] - 1

        self.knots[0] = (x_new, y_new)

    def _update_knots(self):
        for i in range(0, self.n_elements-1):
            x_front = self.knots[i][0]
            y_front = self.knots[i][1]
            x_back  = self.knots[i+1][0]
            y_back  = self.knots[i+1][1]

            x_diff = x_front - x_back
            y_diff = y_front - y_back

            if(abs(x_diff) <= 1 and abs(y_diff) <= 1):
                # a) back is touching front:
                pass
            elif(y_front == y_back):
                # b) horizontal
                if x_diff > 1:
                    # -> move knots right
                    x_back += 1
                else:
                    # -> move knots left
                    x_back -= 1
            elif (x_front == x_back):
                # c) vertical
                if y_diff > 1:
                    # -> move knots up
                    y_back += 1
                else:
                    # -> move knots down
                    y_back -= 1
            else:
                # c) diagonal
                if x_diff > 0 and y_diff > 0:
                    # -> move knots right and up
                    x_back += 1
                    y_back += 1
                elif x_diff > 0 and y_diff < 0:
                    # -> move knots right and down
                    x_back += 1
                    y_back -= 1
                elif x_diff < 0 and y_diff > 0:
                    # -> move knots left and up
                    x_back -= 1
                    y_back += 1
                elif x_diff < 0 and y_diff < 0:
                    # -> move knots left and up
                    x_back -= 1
                    y_back -= 1

            # update knots
            self.knots[i+1] = (x_back, y_back)

        # save trail of tail
        # a) dict: only map if visited or not
        # self.trail[self.tail] = 1
        # b) defaultdict: init new key with 0 by default
        self.trail[self.knots[-1]] += 1

def part_1(data: list) -> int:
    """ 
    move rope with 2 knots i.e. only head and 1 knot = tail
    follow trail of the tail
    return number of visited coordinates
    """
    rope = Rope(n_elements=2)

    for command in data:
        rope.move_rope(command)
        # print(f"{command}: {rope.tail} -> {rope.head}")

    return len(rope.trail)


def part_2(data: list) -> int:
    """ 
    move rope with 10 knots i.e. head and 9 knots
    follow trail of the tail
    return number of visited coordinates
    """
    rope = Rope(n_elements=10)

    for command in data:
        rope.move_rope(command)
        # print(f"{command}: {rope.tail} -> {rope.head}")

    return len(rope.trail)


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
    print(part_2(example_data))
    print(part_2(data))
