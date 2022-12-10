from __future__ import annotations  # problem: use custom class as typehint
from pathlib import Path
import numpy as np


PROJECT_DIR = Path(__file__).resolve().parents[1]
FILE_DIR    = Path(__file__).resolve().parents[0]
INPUT_FILE         = FILE_DIR / "input.txt"
EXAMPLE_INPUT_FILE = FILE_DIR / "example_input.txt"


class TreeMap():
    def __init__(self, n_elements=3) -> None:
        self.n_elements = n_elements
        self.data = np.array([[0 for _ in range(n_elements)] for _ in range(n_elements)])

    def __repr__(self) -> str:
        temp_str = ""
        for row_i in self.data:  
            for element_i in row_i:
                temp_str += str(element_i)
            temp_str += '\n'
        return temp_str
        
def get_input(filepath: Path) -> TreeMap:
    """read input into TreeMap"""
    data = []

    with open(filepath, "r") as f:
        # data.extend([int(letter) for letter in line.strip()] for line in f)
        for line in f.readlines():
            data.append([int(letter) for letter in line.strip()])

    tree_map = TreeMap(n_elements=len(data))
    tree_map.data = np.array(data)

    return tree_map


def part_1(tree_map: TreeMap) -> int:
    """ 
    find number of visibles trees from outside the grid
    """
    
    # print(tree_map)

    # 1. build visible tree map
    # default: no trees visible
    visible_tree_map = TreeMap(n_elements=tree_map.n_elements)

    # 1.1 visible from left to right
    for row_i in range(tree_map.n_elements):  
        # front trees are always visible
        visible_tree_map.data[row_i][0] = 1
        temp_visible_height = tree_map.data[row_i][0]

        for column_i in range(1, tree_map.n_elements):
            # next tree visible?
            tree_height = tree_map.data[row_i][column_i]
            if tree_height > temp_visible_height:
                # tree is visible
                visible_tree_map.data[row_i][column_i] = 1
                temp_visible_height = tree_height

    # 1.2 visible from right to left
    for row_i in range(tree_map.n_elements):  
        # front trees are always visible
        visible_tree_map.data[row_i][-1] = 1
        temp_visible_height = tree_map.data[row_i][-1]

        for column_i in reversed(range(1, tree_map.n_elements)):
            # next tree visible?
            tree_height  = tree_map.data[row_i][column_i-1]
            if tree_height > temp_visible_height:
                # tree is visible
                visible_tree_map.data[row_i][column_i-1] = 1
                temp_visible_height = tree_height

    # 1.3 visible from top to down
    for column_i in range(tree_map.n_elements):  
        # front trees are always visible
        visible_tree_map.data[0][column_i] = 1
        temp_visible_height = tree_map.data[0][column_i]

        for row_i in range(1, tree_map.n_elements):
            # next tree visible?
            tree_height = tree_map.data[row_i][column_i]
            if tree_height > temp_visible_height:
                # tree is visible
                visible_tree_map.data[row_i][column_i] = 1
                temp_visible_height = tree_height

    # 1.4 visible from down to top
    for column_i in range(tree_map.n_elements):  
        # front trees are always visible
        visible_tree_map.data[-1][column_i] = 1
        temp_visible_height = tree_map.data[-1][column_i]

        for row_i in reversed(range(1, tree_map.n_elements)):
            # next tree visible?
            tree_height = tree_map.data[row_i-1][column_i]
            if tree_height > temp_visible_height:
                # tree is visible
                visible_tree_map.data[row_i-1][column_i] = 1
                temp_visible_height = tree_height

    # 2. count visible trees
    # print(visible_tree_map)
    # return sum(sum(tree_row) for tree_row in visible_tree_map.data)
    n_visible_trees = 0
    for tree_row in visible_tree_map.data:
        n_visible_trees += sum(tree_row)

    return n_visible_trees


def part_2(tree_map: TreeMap) -> int:
    """ 
    find tree with highest scenic score
    i.e. multiply viewing distances in each direction
    """
    # calculate scenic score for each tree
    max_scenic_score = 0

    for tree_row_i in range(1, tree_map.n_elements-1):
        for tree_column_i in range(1, tree_map.n_elements-1):
            temp_scenic_score = calculate_scenic_score(tree_map, tree_row_i, tree_column_i)
            if temp_scenic_score > max_scenic_score:
                max_scenic_score = temp_scenic_score
    
    return max_scenic_score

def calculate_scenic_score(tree_map: TreeMap, tree_row_i: int, tree_column_i: int) -> int:
    # viewing distance as long trees smaller or same height
    # stop when tree same height or taller
    tree_height = tree_map.data[tree_row_i][tree_column_i]

    # 1.1 viewing distance to left i.e. tree_row_i, tree_column_i-1 -> 0
    viewing_distance_left = calculate_viewing_distance(tree_height, list(reversed(tree_map.data[tree_row_i, :tree_column_i])))

    # 1.2 visible to right i.e. tree_row_i, tree_column_i+1 -> n_elements
    viewing_distance_right = calculate_viewing_distance(tree_height, tree_map.data[tree_row_i, tree_column_i+1:])

    # 1.3 visible up i.e. tree_row_i-1 -> 0, tree_column_i
    viewing_distance_up = calculate_viewing_distance(tree_height, list(reversed(tree_map.data[:tree_row_i, tree_column_i])))

    # 1.4 visible down i.e. tree_row_i+1 -> n_elements, tree_column_i
    viewing_distance_down = calculate_viewing_distance(tree_height, (tree_map.data[tree_row_i+1:, tree_column_i]))

    # 2. calculate scenic score
    scenic_score = viewing_distance_left * viewing_distance_right * viewing_distance_up * viewing_distance_down
    # print(viewing_distance_left, viewing_distance_right, viewing_distance_up, viewing_distance_down, scenic_score)

    return scenic_score

def calculate_viewing_distance(tree_height: int, tree_list: list[int]):
    """check which tree blocks the view i.e. same height or larger"""
    viewing_distance = 0
    for tree_i in tree_list:
        viewing_distance += 1
        # does tree block the view?
        if tree_i >= tree_height:
            break

    # print(f"{tree_height}: {list(tree_list)} -> {viewing_distance}")
    return viewing_distance

if __name__ == '__main__':
    print(INPUT_FILE)

    example_data = get_input(EXAMPLE_INPUT_FILE)
    print(example_data)

    data = get_input(INPUT_FILE)
    print(data.n_elements)

    # Part 1
    print(part_1(example_data))
    print(part_1(data))

    # Part 2
    print(part_2(example_data))
    print(part_2(data))
