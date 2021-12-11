from common import *
import sys

points = {
    ")": 3,
    # "(": 3,
    "]": 57,
    # "[": 57,
    "}": 1197,
    # "{": 1197,
    ">": 25137,
    # "<": 25137
}

c_points = {
    "(": 1,
    "[": 2,
    "{": 3,
    "<": 4,
}


def is_open(c):
    return c == "(" or c == "[" or c == "{" or c == "<"


def is_close(c):
    return c == ")" or c == "]" or c == "}" or c == ">"


def match(c0, c1):
    return (c0 == "(" and c1 == ")") \
        or (c0 == "[" and c1 == "]") \
        or (c0 == "{" and c1 == "}") \
        or (c0 == "<" and c1 == ">")


def day10_1(data):
    result = 0
    for line in data:
        chars = []
        for c in line:
            if is_open(c):
                chars.append(c)
            else:
                if len(chars) > 0:
                    last_c = chars[-1]
                    if not match(last_c, c):
                        result += points[c]
                        break
                    else:
                        chars.pop()
                else:
                    print("Not possible")
    return result


def day10_2(data):
    result = []
    for line in data:
        line_results = 0
        chars = []
        corrupted = False
        for c in line:
            if is_open(c):
                chars.append(c)
            else:
                if len(chars) > 0:
                    last_c = chars[-1]
                    if not match(last_c, c):
                        corrupted = True
                        break
                    else:
                        chars.pop()
                else:
                    print("Not possible")

        if corrupted:
            continue

        # print(chars)
        for c in reversed(chars):
            line_results *= 5
            line_results += c_points[c]

        # print(line_results)
        # sys.exit(0)

        result.append(line_results)

    ll = list(sorted(result))
    return ll[len(ll) // 2]


if __name__ == "__main__":
    data = read_data(10, parser=lambda x: list(x), test=True)
    do(10, data, answers=[26397, 288957], test=True)

    data = read_data(10, parser=lambda x: list(x))
    do(10, data, answers=[374061, 2116639949])
