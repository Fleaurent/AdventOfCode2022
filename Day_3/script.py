from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parents[1]
FILE_DIR    = Path(__file__).resolve().parents[0]
INPUT_FILE         = FILE_DIR / "input.txt"
EXAMPLE_INPUT_FILE = FILE_DIR / "example_input.txt"

def get_input(filepath: Path) -> list:
    """ read input into list of strings"""
    data = []

    with open(filepath, "r") as f:
        data = [line.strip() for line in f.readlines()]

    return data

def part_1(data: list) -> int:
    """ 
    find common rucksack item
    """

    total_score = 0
    for content in data:
        rucksack_size = len(content) // 2  # int!

        rucksack1 = set(content[:rucksack_size])
        rucksack2 = set(content[rucksack_size:])

        common_content = list(rucksack1 & rucksack2)

        # convert to score
        if(common_content[0].isupper()):
            score = ord(common_content[0]) - 64 + 26  # A = 65, ..., Z = 90  -> 27 - 52
        else:
            score = ord(common_content[0]) - 96  # a = 97, ..., z = 122 -> 1-26
        
        # print(f"{rucksack1} - {rucksack2} = {common_content} {score}")
        total_score += score

    return total_score

def part_2(data: list) -> int:
    """ 
    find common badges in groups = 3 lines
    """
    total_score = 0
    n_groups = len(data) // 3
    for group_i in range(n_groups):
        rucksack1 = set(data[group_i * 3 + 0])
        rucksack2 = set(data[group_i * 3 + 1])
        rucksack3 = set(data[group_i * 3 + 2])

        common_content = list(rucksack1 & rucksack2 & rucksack3)

        # convert to score
        if(common_content[0].isupper()):
            score = ord(common_content[0]) - 64 + 26  # A = 65, ..., Z = 90  -> 27 - 52
        else:
            score = ord(common_content[0]) - 96  # a = 97, ..., z = 122 -> 1-26
        
        # print(f"{rucksack1} - {rucksack2} = {common_content} {score}")
        total_score += score


    return total_score


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
