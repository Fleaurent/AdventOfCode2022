from __future__ import annotations  # problem: use custom class as typehint
from pathlib import Path
from collections import defaultdict


PROJECT_DIR = Path(__file__).resolve().parents[1]
FILE_DIR    = Path(__file__).resolve().parents[0]
INPUT_FILE         = FILE_DIR / "input.txt"
EXAMPLE_INPUT_FILE = FILE_DIR / "example_input.txt"


def get_input(filepath: Path) -> list:
    """read input into array of string"""
    data = []

    with open(filepath, "r") as f:
        for line in f:
            data.append(line.strip())

    return data


class CPU:
    def __init__(self) -> None:
        self.program_counter = 0
        self.cycle = 0
        self.X = [1]  # = sprite position i.e. [0, 1, 2]
        self.crt = [["." for _ in range(40)] for _ in range(6)]

    def run(self, commands: list[str]) -> None:
        for command in commands:
            if command.startswith("noop"):
                self._noop()
            elif command.startswith("addx"):
                x = int(command[4:])
                self._addx(num=x)
        
        # print(f"{cpu.cycle}: {(cpu.X[cpu.cycle])}")

    def _addx(self, num: int) -> None:
        self._noop()
        self._update_crt()
        self.X.append(self.X[self.cycle] + num)
        self.cycle += 1
    
    def _noop(self) -> None:
        self._update_crt()
        self.X.append(self.X[self.cycle])
        self.cycle += 1
    
    def signal_strength(self, cycle_i: int) -> int:
        return cycle_i *self.X[cycle_i - 1]

    def _update_crt(self) -> None:
        sprite_position = self.X[self.cycle]
        pixel_column = self.cycle % 40
        pixel_row = self.cycle // 40
        if abs(sprite_position - pixel_column) <= 1:
            self.crt[pixel_row][pixel_column] = '#'

        # print(f"{self.cycle}: ({pixel_row}, {pixel_column}) -> {sprite_position}")
    
    def print_crt(self) -> None:
        for row_i in range(6):
            print("".join(self.crt[row_i]))


def part_1(data: list[str]) -> int:
    """ 
    run cpu and calculate signal strength
    """
    cpu = CPU()

    # 1. run cpu cycles
    cpu.run(commands=data)

    # 2. calculate signal strength
    signal_strength = 0
    for cpu_cycle_i in range(20, 241, 40):
        signal_strength += cpu.signal_strength(cpu_cycle_i)
        # print(f"{cpu_cycle_i * cpu.X[cpu_cycle_i]}: {cpu_cycle_i} {cpu.X[cpu_cycle_i]}")

    return signal_strength


def part_2(data: list) -> None:
    """ 
    visualize crt
    """
    cpu = CPU()

    # 1. run cpu cycles
    cpu.run(commands=data)

    # 2. display crt
    cpu.print_crt()

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
    part_2(example_data)
    part_2(data)
