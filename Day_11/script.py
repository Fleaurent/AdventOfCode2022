from __future__ import annotations  # problem: use custom class as typehint
from pathlib import Path
import copy
import math
import re


PROJECT_DIR = Path(__file__).resolve().parents[1]
FILE_DIR    = Path(__file__).resolve().parents[0]
INPUT_FILE         = FILE_DIR / "input.txt"
EXAMPLE_INPUT_FILE = FILE_DIR / "example_input.txt"


def get_input(filepath: Path) -> list[Monkey]:
    """read input into array of monkeys"""
    data: list[Monkey] = []

    with open(filepath, "r") as f:
        for line in f:
            temp_line = line.strip()
            if temp_line.startswith("Monkey"):
                number = int(re.search(r'\d+', temp_line)[0])
                data.append(Monkey(number=number))
            elif temp_line.startswith("Starting items:"):
                # items_str = re.sub(r'Starting items: ', '', temp_line)
                # data[-1].items = [int(i) for i in items_str.split(',')]
                # data[-1].items = map(int, items)
                items = re.findall(r'\d+', temp_line)
                data[-1].items = [int(i) for i in items]
            elif temp_line.startswith("Operation:"):
                data[-1].operation_str = re.sub(r'Operation: new = ', '', temp_line)
            elif temp_line.startswith("Test:"):
                data[-1].test_divisible = int(re.search(r'\d+', temp_line)[0])
            elif temp_line.startswith("If true:"):
                data[-1].test_true = int(re.search(r'\d+', temp_line)[0])
            elif temp_line.startswith("If false:"):
                data[-1].test_false = int(re.search(r'\d+', temp_line)[0])

    return data


class Monkey:
    def __init__(self, number: int=0, items: list[int]=None, operation_str: str=None, test_divisible: int=None, test_true: int=None, test_false: int=None) -> None:
        self.number: int = number
        self.items: list[int] = items
        self.operation_str: str = operation_str
        self.test_divisible: int = test_divisible
        self.test_true: int = test_true
        self.test_false: int = test_false
        self.n_inspected_items: int = 0
        
    
    def __repr__(self) -> str:
        temp_str = f"\nmonkey {self.number}: "
        temp_str += f"\n items: {self.items}"
        temp_str += f"\n operation_str: {self.operation_str}"
        temp_str += f"\n test_divisible: {self.test_divisible}"
        temp_str += f"\n test_true: {self.test_true}"
        temp_str += f"\n test_false: {self.test_false}"

        return temp_str

    def inspect_part1(self, old=0, divisor=1) -> tuple(int, int):
        self.n_inspected_items += 1

        # 1. apply operation
        new = eval(self.operation_str)
        # print(self.operation_str)

        # 2. reduce level 
        # print((new // 3), self.test_divisible, (new // 3) % self.test_divisible)
        new = new // divisor

        # 3. move item
        if (new) % self.test_divisible == 0:
            # -> self.test_true
            return self.test_true, new
        else:
            # -> self.test_false
            return self.test_false, new
    
    def inspect_part2(self, old=0, lcm=1) -> tuple(int, int):
        self.n_inspected_items += 1

        # 1. apply operation
        new = eval(self.operation_str)
        # print(self.operation_str)

        # 2. reduce level
        new = new % lcm

        # 3. move item
        if (new) % self.test_divisible == 0:
            # -> self.test_true
            return self.test_true, new
        else:
            # -> self.test_false
            return self.test_false, new


def part_1(data: list[Monkey]) -> int:
    """ 
    run 20 rounds and find most active monkeys
    divide by 3 to decrease level when inspecting
    """
    n_rounds = 20

    for round_i in range(n_rounds):
        # run each monkey: until all items processed
        for monkey_i in range(len(data)):
            # 1. save items temporary
            monkey_i_items = data[monkey_i].items
            data[monkey_i].items = []

            # 2. run operation for each item
            for item_i in monkey_i_items:
                monkey_j, item_j = data[monkey_i].inspect_part1(item_i, divisor=3)
                data[monkey_j].items.append(item_j)
        
        # print all monkeys after each round
        # print(f"\nround_{round_i+1}:")
        # print_monkeys(data)
    
    # 3. find most active monkeys
    active_monkeys = sorted([monkey_i.n_inspected_items for monkey_i in data])
    # print(active_monkeys)

    return active_monkeys[-1] * active_monkeys[-2]


def print_monkeys(data: list[Monkey]) -> None:
    for monkey_i in data:
        print(f"monkey {monkey_i.number}: {monkey_i.items}")


def part_2(data: list[Monkey]) -> int:
    """ 
    run 20 rounds and find most active monkeys
    run modulo of least common multiplier to decrease level when inspecting
    """
    # 1. find common multiplier
    lcm = 1
    for monkey_i in data:
        lcm *= monkey_i.test_divisible
    # print(lcm)

    # optional least common multiplier
    lcm = math.lcm(*[monkey_i.test_divisible for monkey_i in data])
    # print(lcm)

    # 2. run 10000 rounds
    n_rounds = 10000
    for round_i in range(1, n_rounds+1):
        # run each monkey: until all items processed
        for monkey_i in range(len(data)):
            # 1. save items temporary
            monkey_i_items = data[monkey_i].items
            data[monkey_i].items = []

            # 2. run operation for each item
            for item_i in monkey_i_items:
                monkey_j, item_j = data[monkey_i].inspect_part2(item_i, lcm=lcm)
                data[monkey_j].items.append(item_j)

        # print all monkeys after 1000 rounds
        if round_i % 1000 == 0:
            pass
            # print(f"\nround_{round_i}:")
            # print_monkeys(data)

    # 3. find most active monkeys
    active_monkeys = sorted([monkey_i.n_inspected_items for monkey_i in data])
    # print(active_monkeys)

    return active_monkeys[-1] * active_monkeys[-2]


if __name__ == '__main__':
    print(INPUT_FILE)

    example_data = get_input(EXAMPLE_INPUT_FILE)
    print(example_data)

    data = get_input(INPUT_FILE)
    print(len(data))

    # Part 1
    print(part_1(copy.deepcopy(example_data)))
    print(part_1(copy.deepcopy(data)))

    # Part 2
    print(part_2(copy.deepcopy(example_data)))
    print(part_2(copy.deepcopy(data)))
