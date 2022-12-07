from __future__ import annotations  # problem: use custom class as typehint
from pathlib import Path


PROJECT_DIR = Path(__file__).resolve().parents[1]
FILE_DIR    = Path(__file__).resolve().parents[0]
INPUT_FILE         = FILE_DIR / "input.txt"
EXAMPLE_INPUT_FILE = FILE_DIR / "example_input.txt"


class Tree:
    def __init__(self, name: str, size: int, parent: Tree=None):
        self.name = name
        self.size = size
        self.parent = parent
        self.children = []
    
    def add_node(self, name: str, size: int) -> Tree:
        node = Tree(name=self.name + name, size=size, parent=self)
        self.size += size
        self.children.append(node)
        return node

    def get_children_dir(self, children_name: str) -> Tree:
        children_filepath = self.name + children_name + "/"
        for children in self.children:
            if children.name == children_filepath:
                return children
        
        return None

    def __repr__(self) -> str:
        temp_str = f"{self.name}: {self.size}"
        for children in self.children:  
            temp_str += f"\n{children}"
        return temp_str


def get_input(filepath: Path) -> list:
    """ read input into list of strings"""
    data = []

    with open(filepath, "r") as f:
        data = [line.strip() for line in f.readlines()]

    return data

def parse_tree(data: list[str]) -> Tree:
    # 1. build tree
    # read line, navigate through tree, insert data
    # parse commands: 
    # 1. cd: navigate
    # a) cd name -> temp_node.add_node
    # -> update temp_node
    # 2. ls: fill tree ls
    # a) dir: name, size=0 -> fill children
    # b) file: name, size!=0, children=[]
    root = Tree(name="/", size=0)
    temp_node = root

    for line in data[1:]:
        # 1. navigate
        if line.startswith("$ cd "):
            children_name = line[5:].strip()
            if children_name == "..":
                # a) one up
                # append size!
                temp_node.parent.size += temp_node.size
                temp_node = temp_node.parent
            else:
                # b) one down
                temp_node = temp_node.get_children_dir(children_name)
        # 2. content
        elif line.startswith("$ ls"):
            pass
        elif line.startswith("dir"):
            # a) append dir
            dir_name = f"{line[4:].strip()}/"
            temp_node.add_node(name=dir_name, size=0)
        else:
            # b) append file
            # parse regex: "number filename"
            number, name = line.strip().split(" ")
            temp_node.add_node(name=name, size=int(number))

    while temp_node.name != "/":
        temp_node.parent.size += temp_node.size
        temp_node = temp_node.parent

    return root


def part_1(data: list[str]) -> int:
    """ 
    find total size of dirs < 100000
    """
    # 1. build tree
    tree = parse_tree(data)
    # print(tree)

    # 2. count dir < 10000
    total_size = 0
    tree_str = str(tree)
    for tree_path in tree_str.split("\n"):
        path, size = tree_path.split(": ")
        if (path.endswith("/")) and int(size) < 100000:
            total_size += int(size)

    return total_size


def part_2(data: list) -> int:
    """ 
    total disk space 70000000
    delete smallest dir to free up at least 30000000
    1. find total 
    """
    # 1. build tree
    tree = parse_tree(data)
    # print(tree)

    # 2. calculate space
    total_tree_size = tree.size
    print(f"\ntotal_tree_size: {total_tree_size}")
    free_space = 70000000 - total_tree_size
    print(f"free_space: {free_space}")
    free_up = 30000000 - free_space
    print(f"free_up: {free_up}")

    # 2. find smallest dir > free_up
    delete_dir_size = 70000000
    tree_str = str(tree)
    for tree_path in tree_str.split("\n"):
        path, size = tree_path.split(": ")
        if (path.endswith("/")) and int(size) > free_up and int(size) < delete_dir_size:
            delete_dir_size = int(size)

    return delete_dir_size


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
