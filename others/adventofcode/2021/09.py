from common import *
import sys


def day9_1(data):
    n_rows = len(data)
    n_cols = len(data[0])

    selected = []

    for n_row in range(n_rows):
        for n_col in range(n_cols):
            val = data[n_row][n_col]
            adjacents = []
            if n_row > 0:
                adjacents.append(data[n_row - 1][n_col])
            if n_col > 0:
                adjacents.append(data[n_row][n_col - 1])
            if n_col < n_cols-1:
                adjacents.append(data[n_row][n_col + 1])
            if n_row < n_rows-1:
                adjacents.append(data[n_row + 1][n_col])

            if min(adjacents) > val:
                selected.append(val)

    return sum(map(lambda x: 1 + x, selected))


def get_adjent_postions(data, n_row, n_col):
    n_rows = len(data)
    n_cols = len(data[0])
    positions = []

    if n_row > 0:
        positions.append((n_row - 1, n_col))
    if n_col > 0:
        positions.append((n_row, n_col - 1))
    if n_col < n_cols-1:
        positions.append((n_row, n_col + 1))
    if n_row < n_rows-1:
        positions.append((n_row + 1, n_col))

    return positions


def get_min_positions(data):
    n_rows = len(data)
    n_cols = len(data[0])

    min_positions = []

    for n_row in range(n_rows):
        for n_col in range(n_cols):
            val = data[n_row][n_col]

            adjacents = get_adjent_postions(data, n_row, n_col)

            adjacent_values = list(
                map(lambda pos: data[pos[0]][pos[1]], adjacents))

            if min(adjacent_values) > val:
                min_positions.append((n_row, n_col))

    return min_positions


def get_basin_elems(data, min_position):
    elems = {}
    working_elems = [min_position]
    root_key = f"{min_position[0]}-{min_position[1]}"
    elems[root_key] = min_position
    while working_elems != []:
        new_working_elems = []
        for we in working_elems:
            val = data[we[0]][we[1]]
            adjacents = get_adjent_postions(data, we[0], we[1])
            for adjacent_pos in adjacents:
                val_adj = data[adjacent_pos[0]][adjacent_pos[1]]
                if val_adj == 9:
                    continue
                key = f"{adjacent_pos[0]}-{adjacent_pos[1]}"
                if val_adj > val and key not in elems:
                    elems[key] = adjacent_pos
                    new_working_elems.append(adjacent_pos)

        working_elems = new_working_elems

    return list(elems.values())


def day9_2(data):
    num_basin_elems = []
    min_positions = get_min_positions(data)
    for min_position in min_positions:
        basin_elems = get_basin_elems(data, min_position)
        # print(min_position, "->", basin_elems)
        # sys.exit(0)
        num_basin_elems.append(len(basin_elems))

    ff = list(reversed(sorted(num_basin_elems)))[0:3]

    return ff[0] * ff[1] * ff[2]


if __name__ == "__main__":
    data = read_data(9, parser=lambda x: list(map(int, list(x))), test=True)
    do(9, data, answers=[15, 1134], test=True)

    data = read_data(9, parser=lambda x: list(map(int, list(x))))
    do(9, data, answers=[500, 970200])
