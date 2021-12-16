from common import *
import heapq
import sys


class SquareGrid:
    def __init__(self, data):
        self.height = len(data)
        self.width = len(data[0])
        self.data = data

    def in_bounds(self, pos):
        (x, y) = pos
        return 0 <= x < self.width and 0 <= y < self.height

    def neightbors(self, pos):
        (x, y) = pos
        neighbors = [
            (x+1, y),
            (x-1, y),
            (x, y-1),
            (x, y+1)
        ]

        return list(filter(self.in_bounds, neighbors))


class GridWithWeights(SquareGrid):
    def __init__(self, data):
        super().__init__(data)

    def cost(self, to_node):
        (x, y) = to_node
        return self.data[y][x]

    def disjkstra_search(self, start, goal):
        frontier = PriorityQueue()
        frontier.put(start, 0)

        came_from = {}
        cost_so_far = {}

        came_from[start] = None
        cost_so_far[start] = 0

        while not frontier.empty():
            current = frontier.get()

            if current == goal:
                break

            for next in self.neightbors(current):
                new_cost = cost_so_far[current] + self.cost(next)
                if next not in cost_so_far or new_cost < cost_so_far[next]:
                    cost_so_far[next] = new_cost
                    priority = new_cost
                    frontier.put(next, priority)
                    came_from[next] = current

        return came_from, cost_so_far


class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self):
        return not self.elements

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]


def day15_1(data):
    graph = GridWithWeights(data)
    start = (0, 0)
    goal = (graph.width-1, graph.height-1)
    came_from, cost_so_far = graph.disjkstra_search(
        start, goal)

    # print("came_from=", came_from)
    # print("cost_so_far", cost_so_far)

    return cost_so_far[goal]


def inc_v(vec):
    res = []
    for v in vec:
        if v == 9:
            res.append(1)
        else:
            res.append(v+1)
    return res


def create_new_map(data):
    first_part = []
    for row in data:
        new_row = row.copy()
        last_col = row
        for i in range(4):
            new_col = inc_v(last_col)
            new_row.extend(new_col)
            last_col = new_col

        first_part.append(new_row)

    result = first_part.copy()
    ind = 0
    size = len(first_part)
    for i in range(4):
        # print(ind, ind+size)
        for r in result[ind:ind+size]:
            # print(r)
            result.append(inc_v(r))

        # print(result)
        ind += size

    return result


def day15_2(data):
    new_map = create_new_map(data)

    graph = GridWithWeights(new_map)
    start = (0, 0)
    goal = (graph.width-1, graph.height-1)
    _came_from, cost_so_far = graph.disjkstra_search(
        start, goal)

    return cost_so_far[goal]


if __name__ == "__main__":
    data = read_data(15, parser=lambda x: list(map(int, list(x))), test=True)
    do(15, data, answers=[40, 315], test=True)

    data = read_data(15, parser=lambda x: list(map(int, list(x))))
    do(15, data, answers=[685, 2995])
