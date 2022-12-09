import math
from dataclasses import dataclass
from typing import List
from common import *


@dataclass
class Movement:
    dir: str
    num: int


def parse_movements(movs):
    def parse_item(item):
        parts = item.split()
        return Movement(parts[0], int(parts[1]))
    return list(map(parse_item, movs))


class StateMultiple:
    def __init__(self):
        self.tail_path = []
        self.knots = [(0, 0) for _d in range(10)]

    def _get_new_pos(self, node, dir):
        (x, y) = node
        if dir == "U":
            return (x, y + 1)
        elif dir == "D":
            return (x, y - 1)
        elif dir == "L":
            return (x - 1, y)
        elif dir == "R":
            return (x + 1, y)

    def _calculate_knot(self, next_node, node):
        (xhead, yhead) = next_node
        (xtail, ytail) = node

        if next_node in [(xtail + i, ytail + j) for i in [-1, 0, 1] for j in [-1, 0, 1]]:
            return node

        xdiff = xhead - xtail
        ydiff = yhead - ytail
        # new_tail_pos = self.tail

        xdir = 0
        ydir = 0
        if abs(xdiff) > 1:
            xdir = 1 if xdiff > 0 else -1
            if yhead != ytail:
                ydir = 1 if ydiff > 0 else -1
        elif abs(ydiff) > 1:
            ydir = 1 if ydiff > 0 else -1
            if xhead != xtail:
                xdir = 1 if xdiff > 0 else -1

        return (xtail + xdir, ytail + ydir)

    def move(self, mov):
        # print("MOV:", mov)
        for _d in range(mov.num):
            new_knots = []
            last_node = None
            for idx, node in enumerate(self.knots):
                new_node = self._get_new_pos(
                    node, mov.dir) if idx == 0 else self._calculate_knot(last_node, node)

                new_knots.append(new_node)
                last_node = new_node
            self.tail_path.append(new_knots[-1])
            self.knots = new_knots

    def __str__(self):
        return f"{self.head}-{self.tail}"


class State:
    def __init__(self, ini_head, ini_tail):
        self.head = ini_head
        self.tail = ini_tail
        self.head_path = [ini_head]
        self.tail_path = [ini_tail]

    def _get_new_pos(self, dir):
        (x, y) = self.head
        if dir == "U":
            return (x, y + 1)
        elif dir == "D":
            return (x, y - 1)
        elif dir == "L":
            return (x - 1, y)
        elif dir == "R":
            return (x + 1, y)

    def _update_tail(self):
        (xhead, yhead) = self.head
        (xtail, ytail) = self.tail

        if self.head in [(xtail + i, ytail + j) for i in [-1, 0, 1] for j in [-1, 0, 1]]:
            return

        xdiff = xhead - xtail
        ydiff = yhead - ytail
        new_tail_pos = self.tail

        # print("->", xdiff, ydiff)

        xdir = 0
        ydir = 0
        if abs(xdiff) > 1:
            xdir = 1 if xdiff > 0 else -1
            if yhead != ytail:
                ydir = 1 if ydiff > 0 else -1
        elif abs(ydiff) > 1:
            ydir = 1 if ydiff > 0 else -1
            if xhead != xtail:
                xdir = 1 if xdiff > 0 else -1

        new_tail_pos = (xtail + xdir, ytail + ydir)

        self.tail = new_tail_pos
        self.tail_path.append(new_tail_pos)

    def move_head(self, mov):
        # print("MOV:", mov)
        for _d in range(mov.num):
            new_pos = self._get_new_pos(mov.dir)
            self.head = new_pos
            self.head_path.append(new_pos)
            self._update_tail()
            # print(self)

    def __str__(self):
        return f"{self.head}-{self.tail}"


def calculate_result1(state):
    positions = map(lambda x: f"{x[0]}-{x[1]}", state.tail_path)
    return len(set(positions))


def day9_1(data: List[str]) -> int:
    movements = parse_movements(data)
    state = State((0, 0), (0, 0))
    for mov in movements:
        state.move_head(mov)

    return calculate_result1(state)


def day9_2(data: List[str]) -> int:
    movs = parse_movements(data)
    state = StateMultiple()
    for mov in movs:
        state.move(mov)
        # print(state.knots)
        # break

    # print(state.tail_path)
    return calculate_result1(state)


if __name__ == "__main__":
    data = read_data(9, parser=str, test=True)
    do(9, data, answers=[13, 36], test=True)
    data = read_data(9, parser=str)
    do(9, data, answers=[6023, 2533])
