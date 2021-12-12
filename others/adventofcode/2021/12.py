import sys
from collections import defaultdict
from common import *


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add(self, from_name: str, to_name: str):
        self.graph[from_name].append(to_name)
        self.graph[to_name].append(from_name)

    def print(self):
        for k, v in self.graph.items():
            print(k, "->", v)

    def find_all_paths(self, ini, end, path=[], get_next_nodes=None):
        # print("->", ini, end, path)
        path = path + [ini]
        if ini == end:
            # print("--> (1)", path)
            return [path]

        if get_next_nodes is None:
            get_next_nodes = self._default_get_next_nodes

        paths = []
        for node in get_next_nodes(self.graph, ini, path):
            new_paths = self.find_all_paths(
                node, end, path.copy(), get_next_nodes=get_next_nodes)
            # print("xx", new_paths)
            for np in new_paths:
                # print("Add to result:", np)
                paths.append(np)

        # print("--> (2)", paths)

        return paths

    def _default_get_next_nodes(self, graph, node, path):
        # print("AAA")
        next_nodes = graph[node]
        return list(filter(lambda x: x not in path, next_nodes))

    def next_vertex(self, name):
        return self.graph(name)


def get_next_nodes1(graph, node, path):
    # print("BBB")
    next_nodes = graph[node]
    res = []
    for n in next_nodes:
        if str.islower(n) and n in path:
            continue
        res.append(n)

    return res


def get_num_nodes(path):
    res = {}
    for p in path:
        if p not in res:
            res[p] = 0
        res[p] += 1
    return res


def get_max_lowers(num_nodes):
    for k, v in num_nodes.items():
        if str.islower(k) and v > 1:
            return True
    return False


def get_next_nodes2(graph, node, path):
    # print("CCC")
    next_nodes = graph[node]
    num_nodes = get_num_nodes(path)
    max_lowers = get_max_lowers(num_nodes)
    res = []
    for n in next_nodes:
        # print(path, n, next_nodes)
        if str.islower(n) and n in path and max_lowers:
            continue

        if n in ['start', 'end'] and n in path:
            continue

        res.append(n)

    return res


def read_test1():
    raw = """start-A
start-b
A-c
A-b
b-d
A-end
b-end"""
    return map(lambda x: x.split("-"), raw.split("\n"))


def read_test2():
    raw = """dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc"""
    return map(lambda x: x.split("-"), raw.split("\n"))


def create_graph(data):
    graph = Graph()
    for l in data:
        graph.add(l[0], l[1])
    return graph


def day12_1(data):
    # print(data)
    graph = create_graph(data)
    paths = graph.find_all_paths(
        'start', 'end', get_next_nodes=get_next_nodes1)
    return len(paths)


def day12_2(data):
    # print(data)
    graph = create_graph(data)
    paths = graph.find_all_paths(
        'start', 'end', get_next_nodes=get_next_nodes2)
    return len(paths)


if __name__ == "__main__":
    data = read_data(12, parser=lambda x: x.split("-"), test=True)
    # data = read_test1()  # 10
    # data = read_test2() # 19
    do(12, data, answers=[226, 3509], test=True)

    data = read_data(12, parser=lambda x: x.split("-"))
    do(12, data, answers=[3510, 122880])
