from __future__ import annotations  # problem: use custom class as typehint
from collections import defaultdict
from pathlib import Path
import numpy as np
import copy


PROJECT_DIR = Path(__file__).resolve().parents[1]
FILE_DIR    = Path(__file__).resolve().parents[0]
INPUT_FILE         = FILE_DIR / "input.txt"
EXAMPLE_INPUT_FILE = FILE_DIR / "example_input.txt"


def get_input(filepath: Path) -> list[str]:
    """read input into array str"""
    data: list[str] = []

    with open(filepath, "r") as f:
        for line in f:
            data.append(line.strip())

    return data


# This class represents a directed graph
# using adjacency list representation
class Graph:

    # Constructor
    def __init__(self):

        # default dictionary to store graph
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def addEdge(self,u,v):
        self.graph[u].append(v)

    # Function to print a BFS of graph
    def BFS(self, s):

        # Mark all the vertices as not visited
        visited = [False] * (max(self.graph) + 1)

        # Create a queue for BFS
        queue = []

        # Mark the source node as
        # visited and enqueue it
        queue.append(s)
        visited[s] = True

        while queue:

            # Dequeue a vertex from
            # queue and print it
            s = queue.pop(0)
            print (s, end = " ")

            # Get all adjacent vertices of the
            # dequeued vertex s. If a adjacent
            # has not been visited, then mark it
            # visited and enqueue it
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

def part_1(data: list[str]) -> int:
    """ 
    run 20 rounds and find most active monkeys
    divide by 3 to decrease level when inspecting
    """
    # 1. build graph
    # distance a -> b = 1
    # distance a -> c = -
    # distance b -> a = 1
    # distance c -> a = 1
    n_rows = len(data)
    n_columns = len(data[0])

    distance_map = np.ones((n_rows, n_columns)) * 999
    visited_map = np.zeros((n_rows, n_columns))

    # build elevation_map = np.zeros((n_rows, n_columns))
    elevation_map = np.zeros((n_rows, n_columns))
    for i, line in enumerate(data):
        for j, char in enumerate(line):
            if char == 'S':
                start_point = (i, j)
                elevation = 0
            elif char == 'E':
                end_point = (i, j)
                elevation = 26
            else:
                elevation = ord(char) - ord('a')
            elevation_map[i, j] = elevation
    print(elevation_map)

    # 2. run path finding algorithm from S to E
    # 0. add start to queue
    queue = []
    queue.append(start_point)
    distance_map[start_point] = 0

    while queue:
        # 1. take next element from queue
        temp_point = queue.pop()
        temp_y, temp_x = temp_point
        height_temp = elevation_map[temp_point]

        # 2. add neighbours to queue
        # right
        if temp_x < n_columns-1: 
            neighbor = (temp_y, temp_x+1)
            height_neighbor = elevation_map[neighbor]
            if height_neighbor - height_temp <= 1:
                temp_distance = distance_map[temp_point] + 1
                if temp_distance <= distance_map[neighbor]:
                    distance_map[neighbor] = temp_distance
                    queue.append(neighbor)

        # left
        if temp_x > 0:
            neighbor = (temp_y, temp_x-1)
            height_neighbor = elevation_map[neighbor]
            if height_neighbor - height_temp <= 1:
                temp_distance = distance_map[temp_point] + 1
                if temp_distance <= distance_map[neighbor]:
                    distance_map[neighbor] = temp_distance
                    queue.append(neighbor)
        # up
        if temp_y > 0:
            neighbor = (temp_y-1, temp_x)
            height_neighbor = elevation_map[neighbor]
            if height_neighbor - height_temp <= 1:
                temp_distance = distance_map[temp_point] + 1
                if temp_distance <= distance_map[neighbor]:
                    distance_map[neighbor] = temp_distance
                    queue.append(neighbor)

        # down
        if temp_y < n_rows-1:
            neighbor = (temp_y+1, temp_x)
            height_neighbor = elevation_map[neighbor]
            if height_neighbor - height_temp <= 1:
                temp_distance = distance_map[temp_point] + 1
                if temp_distance <= distance_map[neighbor]:
                    distance_map[neighbor] = temp_distance
                    queue.append(neighbor)

    print(visited_map)
    print(distance_map)
    
    return distance_map[end_point]


def part_2(data: list[str]) -> int:
    """ 
    run 20 rounds and find most active monkeys
    run modulo of least common multiplier to decrease level when inspecting
    """
    
    return 0


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
    # print(part_2(copy.deepcopy(example_data)))
    # print(part_2(copy.deepcopy(data)))
