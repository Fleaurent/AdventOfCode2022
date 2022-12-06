from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parents[1]
FILE_DIR    = Path(__file__).resolve().parents[0]
INPUT_FILE         = FILE_DIR / "input.txt"
EXAMPLE_INPUT_FILE = FILE_DIR / "example_input.txt"


def get_input(filepath: Path) -> str:
    """ read input into str"""
    data = ""

    with open(filepath, "r") as f:
        data = f.readline().strip()

    return data

def part_1(data: list) -> int:
    """ 
    start-of-packet marker: i.e. nth character with 4 different repeating characters
    """
    n_chars = len(data)
    n_different_chars = 4

    for char_i in range(n_chars - n_different_chars):
        temp_chars = set(data[char_i:char_i+n_different_chars])
        if len(temp_chars) == n_different_chars:
            return char_i + n_different_chars

    return 0


def part_2(data: list) -> int:
    """ 
    start-of-message marker: i.e. nth character with 14 different repeating characters
    """
    n_chars = len(data)
    n_different_chars = 14

    for char_i in range(n_chars - n_different_chars):
        temp_chars = set(data[char_i:char_i+n_different_chars])
        if len(temp_chars) == n_different_chars:
            return char_i + n_different_chars

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
    print(part_2(example_data))
    print(part_2(data))
