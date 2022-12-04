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
    find complete overlapping sections
    """

    total_score = 0
    for content in data:
        # 1. parse sections
        sections = content.split(",")

        section1 = sections[0].split("-")
        section1_start = int(section1[0])
        section1_end   = int(section1[1])

        section2 = sections[1].split("-")
        section2_start = int(section2[0])
        section2_end   = int(section2[1])

        # 2. find complete overlap
        section1_set = set(range(section1_start, section1_end+1))
        section2_set = set(range(section2_start, section2_end+1))
        section_overlap_set = section1_set | section2_set

        if section_overlap_set in [section1_set, section2_set]:
            total_score += 1

    return total_score


def part_2(data: list) -> int:
    """ 
    find all overlapping sections
    """
    total_score = 0
    for content in data:
        # 1. parse sections
        sections = content.split(",")

        section1 = sections[0].split("-")
        section1_start = int(section1[0])
        section1_end   = int(section1[1])

        section2 = sections[1].split("-")
        section2_start = int(section2[0])
        section2_end   = int(section2[1])

        # 2. find overlap
        section1_set = set(range(section1_start, section1_end+1))
        section2_set = set(range(section2_start, section2_end+1))
        section_overlap_set = section1_set & section2_set

        if section_overlap_set:
            total_score += 1

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
