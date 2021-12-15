from typing import Collection
from common import *
import sys
from collections import Counter


def read_custom_data(test=True):
    filename = "test14.txt" if test else "input14.txt"

    out = {
        "template": [],
        "pair_insertion": {}
    }
    with open(f"data/{filename}") as fin:
        lines = fin.readlines()
        out["template"] = list(lines[0].strip())

        for line in lines[2:]:
            elems = line.strip().split(" -> ")
            out["pair_insertion"][elems[0]] = elems[1]

    return out


def calculate_result1(serie):
    counts = {}
    for s in serie:
        if s not in counts:
            counts[s] = 0
        counts[s] += 1

    max_num = max(counts.values())
    min_num = min(counts.values())
    return max_num - min_num


def day14_1(data, steps=10):
    serie = [x for x in data["template"]]
    insertions = data["pair_insertion"]
    for i in range(steps):
        pos = 0
        # print(''.join(serie))
        new_serie = []
        while pos < len(serie)-1:
            pair = ''.join(serie[pos:pos+2])
            rule = insertions[pair]
            # print(pair, rule)
            new_serie.append(serie[pos])
            new_serie.append(rule)
            # new_serie.append(serie[pos+1])
            # print(new_serie)
            # if pos == 1:
            #     sys.exit(0)
            pos += 1
        new_serie.append(serie[-1])
        serie = new_serie.copy()
        # print(''.join(new_serie))

    return calculate_result1(serie)


def combine_results(res1, res2):
    c1 = Counter(res1)
    c2 = Counter(res2)
    res = c1 + c2
    return dict(res)


def add_result(res, k, v):
    if k not in res:
        res[k] = 0
    res[k] += v

    return res


def generate_pairs(ll):
    pairs = [ll[i:i+2] for i in range(0, len(ll)-1)]
    for pp in pairs:
        yield pp


CACHE = {}


def calculate(pair, insertions, steps):
    # print(steps)
    key = f"{''.join(pair)}-{steps}"
    if key in CACHE:
        return CACHE[key]

    if steps == 0:
        # sys.exit(0)
        # return add_result(res, pair[0], 1)
        return {
            pair[0]: 1,
            # pair[1]: 1
        }

    insertion = insertions[''.join(pair)]
    next_value = [pair[0], insertion, pair[1]]
    res = {}
    for new_pair in generate_pairs(next_value):
        partial_res = calculate(new_pair, insertions, steps - 1)
        res = combine_results(res, partial_res)

    CACHE[key] = res

    return res


def day14_2(data, steps=10):
    serie = [x for x in data["template"]]
    insertions = data["pair_insertion"]

    # print(serie)
    res = {}
    for pair in generate_pairs(serie):
        partial_res = calculate(pair, insertions, steps)
        res = combine_results(res, partial_res)

    res[serie[-1]] += 1

    # print(res)

    max_num = max(res.values())
    min_num = min(res.values())
    return max_num - min_num


if __name__ == "__main__":
    # data = read_custom_data(test=True)
    # print("TEST=", day14_1(data, steps=10), "=== 1588")

    data = read_custom_data(test=False)
    print("RES=", day14_1(data, steps=10), "=== 2027")

    # data = read_custom_data(test=True)
    # print("TEST=", day14_2(data, steps=40), "=== 2188189693529")

    data = read_custom_data(test=False)
    # X <<< 13056394203021
    print("RES=", day14_2(data, steps=40), "=== ")
