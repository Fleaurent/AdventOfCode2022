from pathlib import Path
import re

PROJECT_DIR = Path(__file__).resolve().parents[1]
FILE_DIR    = Path(__file__).resolve().parents[0]
INPUT_FILE         = FILE_DIR / "input.txt"
EXAMPLE_INPUT_FILE = FILE_DIR / "example_input.txt"

def get_input(filepath: Path) -> list:
    """ read input into list of strings"""
    stack_str = []
    commands_str = []
    input_part_1 = True

    with open(filepath, "r") as f:
        for line in f:
            if line == "\n":
                input_part_1 = False
            elif input_part_1:
                stack_str.append(line)
            else:
                commands_str.append(line.strip())

    return stack_str, commands_str


def parse_stack(stack_str: list[str]) -> list:
    """parse stack_str into stack 2D array"""
    # 1. init stack
    n_items = len(stack_str[-1].split())
    stack = [[] for _ in range(n_items)]

    # 2. assign items
    for stack_items in reversed(stack_str[:-1:]):
        # 1, 5, 9, +4...
        for i in range(n_items):
            item_i = stack_items[1+i*4]
            if item_i != " ":
                stack[i].append(item_i)
                # print(f"{i}: {item_i}")

    return stack
´

def part_1(stack_str: list, commands_str: list) -> int:
    """ 
    move items one by one
    """
    # 1. parse stack into 2D array
    stack = parse_stack(stack_str)

    # 2. permutate stack using commands
    for command_str in commands_str:
        """ move 1 from 2 to 1 """
        numbers = re.findall('[0-9]+', command_str)
        n_items, from_a, to_b = int(numbers[0]), int(numbers[1])-1, int(numbers[2])-1
        temp_items = [stack[from_a].pop() for _ in range(n_items)]
        stack[to_b] += temp_items       

    return "".join(stack[i][-1] for i in range(len(stack)))


def part_2(stack_str: list, commands_str: list) -> int:
    """ 
    move items all at once
    """
    # 1. parse stack into 2D array
    stack = parse_stack(stack_str)

    # 2. permutate stack using commands
    for command_str in commands_str:
        """ move 1 from 2 to 1 """
        numbers = re.findall('[0-9]+', command_str)
        n_items, from_a, to_b = int(numbers[0]), int(numbers[1])-1, int(numbers[2])-1
        temp_items = [stack[from_a].pop() for _ in range(n_items)]
        stack[to_b] += reversed(temp_items)

    return "".join(stack[i][-1] for i in range(len(stack)))


if __name__ == '__main__':
    print(INPUT_FILE)

    example_stack, example_commands = get_input(EXAMPLE_INPUT_FILE)
    print(example_stack, example_commands)

    stack, commands = get_input(INPUT_FILE)
    print(len(commands))

    # Part 1
    print(part_1(example_stack, example_commands))
    print(part_1(stack, commands))

    # Part 2
    print(part_2(example_stack, example_commands))
    print(part_2(stack, commands))
