import sys
from common import *


def read_test_data():
    test_data = """11111
19991
19191
19991
11111"""
    return map(lambda x: map(lambda y:  int(y), list(x)), test_data.split("\n"))


class Grid:
    def __init__(self, data):
        self.octopuses = []
        for row in data:
            grid_row = []
            for col in row:
                grid_row.append(Octopus(col))
            self.octopuses.append(grid_row)

    def calculate_next_state(self):
        for row in self.octopuses:
            for col in row:
                col.inc()

        self._propagate_flashes(0)
        self._reset_flashes()

    def _reset_flashes(self):
        for r in self.octopuses:
            for c in r:
                c.processed = False
                c.has_flashed = False

    def all_sync(self):
        n_rows = len(self.octopuses)
        n_cols = len(self.octopuses[0])
        n_flashes = sum([o.is_flashing() for r in self.octopuses for o in r])
        # print("Sync?", n_flashes)
        return n_flashes == (n_rows * n_cols)

    def _propagate_flashes(self, it=0):
        # print(f"Propagate {it}")
        # print(self)
        has_flashed = False
        for n_row, row in enumerate(self.octopuses):
            for n_col, octopus in enumerate(row):
                if octopus.is_flashing() and not octopus.processed:
                    octopus.processed = True
                    points = self._get_adjacent_points(n_col, n_row)
                    # print(points)
                    for (p_x, p_y) in points:
                        o_point = self.octopuses[p_y][p_x]

                        if not o_point.is_flashing():
                            o_point.inc()

                            if (o_point.is_flashing()):
                                # print("New point:", p_x, p_y)
                                has_flashed = True
                            # has_flashed = has_flashed or o_point.is_flashing()

        if has_flashed:
            self._propagate_flashes(it+1)

    def num_of_flashes(self):
        return sum([o.num_of_flashes for r in self.octopuses for o in r])

    def _get_adjacent_points(self, pos_x, pos_y):
        num_rows = len(self.octopuses)
        num_cols = len(self.octopuses[0])

        points = []

        if pos_x > 0 and pos_y > 0:
            points.append((pos_x - 1, pos_y - 1))
        if pos_y > 0:
            points.append((pos_x, pos_y - 1))
        if pos_x < num_cols - 1 and pos_y > 0:
            points.append((pos_x + 1, pos_y - 1))
        if pos_x < num_cols - 1:
            points.append((pos_x + 1, pos_y))
        if pos_x < num_cols - 1 and pos_y < num_rows - 1:
            points.append((pos_x + 1, pos_y + 1))
        if pos_y < num_rows - 1:
            points.append((pos_x, pos_y + 1))
        if pos_x > 0 and pos_y < num_rows - 1:
            points.append((pos_x - 1, pos_y + 1))
        if pos_x > 0:
            points.append((pos_x - 1, pos_y))

        return points

    def __str__(self):
        res = ""
        for r in self.octopuses:
            for c in r:
                res += f"{c}"
            res += "\n"
        return res


class Octopus:
    def __init__(self, energy_level):
        self.energy_level = energy_level
        self.has_flashed = False
        self.num_of_flashes = 0
        self.processed = False

    def __str__(self):
        return f"\033[1m{self.energy_level}\033[0m" if self.is_flashing() \
            else f"{self.energy_level}"

    def is_flashing(self):
        return self.energy_level == 0

    def inc(self):
        self.energy_level += 1
        if self.energy_level > 9:
            self.energy_level = 0
            self.has_flashed = True
            self.num_of_flashes += 1


def day11_1(data) -> int:
    grid = Grid(data)
    for i in range(100):
        # print(f"Iteration: {i}")
        # print(grid)

        grid.calculate_next_state()

    # print("FINAL")
    # print(grid)

    return grid.num_of_flashes()


def day11_2(data) -> int:
    # print(data)
    # data = read_test_data()
    grid = Grid(data)
    sync = False
    it = 0
    while not sync:
        # for i in range(1000):
        # print(f"Iteration: {i}")
        # print(grid)

        if grid.all_sync():
            sync = True
            break

        grid.calculate_next_state()
        it += 1

    # print("FINAL")
    # print(grid)

    return it


if __name__ == "__main__":
    data = read_data(11, parser=lambda x: list(map(int, list(x))), test=True)
    do(11, data, answers=[1656, 195], test=True)

    data = read_data(11, parser=lambda x: list(map(int, list(x))))
    do(11, data, answers=[1656, 0])
