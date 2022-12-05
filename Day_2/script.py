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

score_dict_1 = {
    "A X": 3+1, # Rock vs. Rock = 1
    "A Y": 6+2, # Rock vs. Paper = 2
    "A Z": 0+3, # Rock vs. Scissors = 3
    "B X": 0+1, # Paper vs. Rock
    "B Y": 3+2, # Paper vs. Paper
    "B Z": 6+3, # Paper vs. Scissors
    "C X": 6+1, # Scissors vs. Rock
    "C Y": 0+2, # Scissors vs. Paper
    "C Z": 3+3, # Scissors vs. Scissors
}

def part_1(data: list) -> int:
    """ 
    find sum of game scores:
    A=Rock, B=Paper, C=Scissors
    X=Rock(1), Y=Paper(2), Z=Scissors(3)
    -> lose(0), draw(3), win(6)
    """
    scores = [score_dict_1[game] for game in data]

    return sum(scores)

score_dict_2 = {
    "A X": 0+3, # Rock vs. Scissors(3)  = lose(0)
    "A Y": 3+1, # Rock vs. Rock(1)      = draw(3)
    "A Z": 6+2, # Rock vs. Paper(2)     = win(6)
    "B X": 0+1, # Paper vs. Rock(1)     = lose(0)
    "B Y": 3+2, # Paper vs. Paper(2)    = draw(3)
    "B Z": 6+3, # Paper vs. Scissors(3) = win(6)
    "C X": 0+2, # Scissors vs. Paper(2) = lose(0)
    "C Y": 3+3, # Scissors vs. Scissors(3) = draw(3)
    "C Z": 6+1, # Scissors vs. Rock(1)  = win(6)
}

def part_2(data: list) -> int:
    """ 
    find sum of game scores:
    A=Rock, B=Paper, C=Scissors
    X=lose(0), Y=draw(3), Z=win(6)
    -> Rock(1), Paper(2), Scissors(3)
    """
    scores = [score_dict_2[game] for game in data]

    return sum(scores)


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
