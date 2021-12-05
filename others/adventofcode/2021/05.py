from common import *


def line_parser(line):
    parts = line.split("->")
    return [p.strip().split(",") for p in parts]


def get_max_dim(data):
    return max([int(p) for line in data for pair in line for p in pair])+1


def create_empty_matrix(max_dim):
    m = []
    for _i in range(max_dim):
        m.append([0 for _j in range(max_dim)])

    return m


def get_num_cross(m):
    c = 0
    for row in m:
        for elem in row:
            if elem >= 2:
                c += 1

    return c


def day5_1(data):
    max_dim = get_max_dim(data)
    m = create_empty_matrix(max_dim)

    for line in data:
        [x1, y1] = list(map(int, line[0]))
        [x2, y2] = list(map(int, line[1]))
        if x1 != x2 and y1 != y2:
            continue

        inc_x = 1 if x1 <= x2 else -1
        inc_y = 1 if y1 <= y2 else -1

        for i in range(x1, x2+inc_x, inc_x):
            for j in range(y1, y2+inc_y, inc_y):
                m[i][j] += 1

    return get_num_cross(m)


def are_in_diagonal(x1, y1, x2, y2, max_dim):
    inc_x = 1 if x1 <= x2 else -1
    inc_y = 1 if y1 <= y2 else -1

    x = x1
    y = y1
    while True:
        if x == x2 and y == y2:
            return True

        if x > max_dim or x < 0 or y > max_dim or y < 0:
            return False

        x += inc_x
        y += inc_y


def day5_2(data):
    max_dim = get_max_dim(data)
    m = create_empty_matrix(max_dim)

    for line in data:
        [x1, y1] = list(map(int, line[0]))
        [x2, y2] = list(map(int, line[1]))

        if not are_in_diagonal(x1, y1, x2, y2, max_dim) and (x1 != x2 and y1 != y2):
            continue

        inc_x = 1 if x1 <= x2 else -1
        inc_y = 1 if y1 <= y2 else -1

        if x1 == x2 or y1 == y2:
            if x1 == x2:
                for y in range(y1, y2+inc_y, inc_y):
                    m[y][x1] += 1
            else:
                for x in range(x1, x2+inc_x, inc_x):
                    m[y1][x] += 1

            # for i in range(x1, x2+inc_x, inc_x):
            #     for j in range(y1, y2+inc_y, inc_y):
            #         m[j][i] += 1
        else:
            # print("DIA:", x1, y1, x2, y2, max_dim)
            x, y = x1, y1
            while True:
                if x == x2 and y == y2:
                    m[y][x] += 1
                    break

                m[y][x] += 1

                x += inc_x
                y += inc_y

    # for l in m:
    #     print(l)

    return get_num_cross(m)


if __name__ == "__main__":
    data = read_data(5, parser=line_parser, test=True)
    do(5, data, answers=[5, 12], test=True)

    data = read_data(5, parser=line_parser)
    # 19633 < X < 19674
    do(5, data, answers=[6548, 0])
