from common import *


def read_custom_data(test=False):
    filename = "test13.txt" if test else "input13.txt"

    res = {
        "grid": [],
        "folds": []
    }

    with open(f"data/{filename}") as fin:
        lines = fin.readlines()
        dots = True
        for line in lines:
            if line.strip() == '':
                dots = False
                continue

            if dots:
                point = line.strip().split(",")
                res["grid"].append([int(point[0]), int(point[1])])
            else:
                fs = line.strip().split()
                ff = fs[2].split("=")
                res["folds"].append([ff[0], int(ff[1])])

    return res


class Grid:
    def __init__(self, data):
        self.data = data

    def print(self):
        for point in self.data:
            print(point)

    def print_grid(self):
        points = [f"{x}-{y}" for [x, y] in self.data]
        max_x = max([p[0] for p in self.data])
        max_y = max([p[1] for p in self.data])

        # print(max_x, max_y)

        for y in range(max_y+1):
            for x in range(max_x+1):
                point = f"{x}-{y}"
                if point in points:
                    print("#", end='')
                else:
                    print(".", end='')
            print("")

    def fold(self, dir_dist):
        dir = dir_dist[0]
        dist = dir_dist[1]

        print("=>> Folding:", dir, "=", dist)

        if dir == "y":
            self.fold_y(dist)
        else:
            self.fold_x(dist)

    def fold_y(self, dist):
        # remove points with y=dist
        self.data = list(filter(lambda x: x[1] != dist, self.data))

        new_points = []
        for point in self.data:
            x = point[0]
            y = point[1]
            if y > dist:
                new_points.append([x, dist-(y-dist)])
            else:
                new_points.append([x, y])

        # print(new_points)
        self.data = new_points

    def fold_x(self, dist):
        # remove points with x=dist
        self.data = list(filter(lambda x: x[0] != dist, self.data))

        new_points = []
        for point in self.data:
            x = point[0]
            y = point[1]
            if x > dist:
                new_points.append([dist-(x-dist), y])
            else:
                new_points.append([x, y])

        # print(new_points)
        self.data = new_points

    def count_dots(self):
        points = [f"{x}-{y}" for [x, y] in self.data]
        points = list(dict.fromkeys(points))
        return len(points)


def day13_1(data):
    grid = Grid(data["grid"])

    # for ff in data["folds"]:
    #     grid.print_grid()
    #     grid.fold(ff)
    first_intruction = data["folds"][0]
    grid.fold(first_intruction)
    # grid.print_grid()
    return grid.count_dots()


def day13_2(data):
    grid = Grid(data["grid"])

    for ff in data["folds"]:
        # grid.print_grid()
        grid.fold(ff)

    grid.print_grid()
    return 0


if __name__ == "__main__":
    data = read_custom_data(test=True)
    print("TEST=", day13_1(data), "=== 17")

    data = read_custom_data(test=False)
    print("RES=", day13_1(data), "=== 704")

    data = read_custom_data(test=False)
    day13_2(data)
