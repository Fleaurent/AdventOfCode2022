from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parents[1]
INPUT_FILE         = PROJECT_DIR / "Day_1" / "input.txt"
EXAMPLE_INPUT_FILE = PROJECT_DIR / "Day_1" / "example_input.txt"


def get_input(filepath: Path) -> list:
    """ read input into 2 dimensional list of integers i.e. [n_elves, calories] """
    data = []
    temp_data = []

    with open(filepath, "r") as f:
        lines = f.readlines()

        for line in lines:
            if line == "\n":
                data.append(temp_data)
                temp_data = []
            else:
                temp_data.append(int(line))
        
        data.append(temp_data)

    return data


def part_1(data: list) -> int:
    """ find largest sum """
    largest_sum = 0

    for values_i in data:
        sum_i = sum(values_i)

        if(sum_i > largest_sum):
            largest_sum = sum_i
    
    return largest_sum

def part_2(data: list) -> list:
    """ find top 3 largest sum """
    sum_list = []

    sum_list = [sum(values_i) for values_i in data]
    sum_list.sort(reverse=True)

    # return top_3_sum
    return sum(sum_list[:3])

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
