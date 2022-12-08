from typing import List
from functools import reduce
from common import *


def parse_row(elem):
    return [int(x) for x in elem]


def get_max_surrounding_trees(data, r, c):
    n_cols = len(data[0])
    n_rows = len(data)
    elems = []

    elems.append(max([data[r][cc] for cc in range(c-1, -1, -1)]))
    elems.append(max([data[rr][c] for rr in range(r-1, -1, -1)]))
    elems.append(max([data[r][cc] for cc in range(c+1, n_cols)]))
    elems.append(max([data[rr][c] for rr in range(r+1, n_rows)]))

    return elems


def calculate_tree_score(data, r, c):
    n_cols = len(data[0])
    n_rows = len(data)
    current_tree = data[r][c]
    trees = []

    num_trees = 0
    for cc in range(c-1, -1, -1):
        num_trees += 1
        val = data[r][cc]
        if val >= current_tree:
            break
    trees.append(num_trees)

    num_trees = 0
    for rr in range(r-1, -1, -1):
        num_trees += 1
        val = data[rr][c]
        if val >= current_tree:
            break
    trees.append(num_trees)

    num_trees = 0
    for cc in range(c+1, n_cols):
        num_trees += 1
        val = data[r][cc]
        if val >= current_tree:
            break
    trees.append(num_trees)

    num_trees = 0
    for rr in range(r+1, n_rows):
        num_trees += 1
        val = data[rr][c]
        if val >= current_tree:
            break
    trees.append(num_trees)

    return reduce((lambda x, y: x * y), trees)


def day8_1(data: List[int]) -> int:
    n_cols = len(data[0])
    n_rows = len(data)

    visible_trees = 0
    for r in range(n_rows):
        for c in range(n_cols):
            if r == 0 or c == 0 or r == n_rows-1 or c == n_cols-1:
                visible_trees += 1
            else:
                surrounding_trees = get_max_surrounding_trees(data, r, c)
                current_tree = data[r][c]
                if any(map(lambda x: x < current_tree, surrounding_trees)):
                    visible_trees += 1
    return visible_trees


def day8_2(data: List[int]) -> int:
    n_cols = len(data[0])
    n_rows = len(data)

    visible_trees_scores = []
    for r in range(n_rows):
        for c in range(n_cols):
            visible_trees_scores.append(calculate_tree_score(data, r, c))
    return max(visible_trees_scores)


if __name__ == "__main__":
    data = read_data(8, parser=parse_row, test=True)
    do(8, data, answers=[21, 8], test=True)
    data = read_data(8, parser=parse_row)
    do(8, data, answers=[1776, 234416])
