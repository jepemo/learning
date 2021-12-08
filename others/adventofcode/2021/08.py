from common import *
from typing import Dict

import sys


def read_input(filename):
    res = []
    for line in list(map(lambda l: l.split(" | "), open(filename).read().split('\n'))):
        fp = line[0]
        sp = line[1]
        res.append([fp.split(), sp.split()])
    return res


def day8_1(data):
    num_digits = 0
    for line in data:
        signals = line[0]
        nums = line[1]
        for i in nums:
            if len(i) in [2, 3, 4, 7]:
                num_digits += 1

    return num_digits


def get_key(signals: Dict[str, int], value: int) -> str:
    for k, v in signals.items():
        if v == value:
            return k
    return ""


def is_5(code: str, digits: Dict[str, int]):
    patt4 = get_key(digits, 4)
    rr = ''.join(set(code).union(set(patt4)))
    return len(rr) == len(code) + 1


def digit_contains(container, contained):
    rr = ''.join(set(container).union(set(contained)))
    return len(rr) == len(container)


def get_digits(signals: Dict[str, int]):
    # 0 -> 6
    # 1 -> 2
    # 2 -> 5
    # 3 -> 5
    # 4 -> 4
    # 5 -> 5
    # 6 -> 6
    # 7 -> 3
    # 8 -> 7
    # 9 -> 6

    digits = {}
    for signal in signals:
        code = ''.join(sorted(signal))
        if len(signal) == 2:
            digits[code] = 1
        elif len(signal) == 3:
            digits[code] = 7
        elif len(signal) == 4:
            digits[code] = 4
        elif len(signal) == 7:
            digits[code] = 8

    for signal in signals:
        code = ''.join(sorted(signal))
        if len(signal) == 6:
            # 0, 6, 9
            patt1 = get_key(digits, 1)
            patt4 = get_key(digits, 4)
            if digit_contains(signal, patt4):
                digits[code] = 9
            elif not digit_contains(signal, patt1):
                digits[code] = 6
            else:
                digits[code] = 0
        elif len(signal) == 5:
            # 2, 3, 5
            patt = get_key(digits, 1)
            if digit_contains(code, patt):
                digits[code] = 3
            elif is_5(code, digits):
                digits[code] = 5
            else:
                digits[code] = 2

    return digits


def get_num(nums, digits):
    v = ''
    for num in nums:
        code = ''.join(sorted(num))
        v += f"{digits[code]}"

    return int(v)


def test():
    ss = {"cagedb": 0,
          "ab": 1,
          "gcdfa": 2,
          "fbcad": 3,
          "eafb": 4,
          "cdfbe": 5,
          "cdfgeb": 6,
          "dab": 7,
          "acedgfb": 8,
          "cefabd": 9}
    res = get_digits(list(ss.keys()))

    for k, v in ss.items():
        code = ''.join(sorted(k))
        vv = res[code]
        print(v, "===", vv)

    print(res)


def day8_2(data):
    final_nums = []
    for line in data:
        signals = line[0]
        nums = line[1]

        digits = get_digits(signals)
        # print(digits)
        # sys.exit(0)
        final_nums.append(get_num(nums, digits))

    return sum(final_nums)


if __name__ == "__main__":
    # test()
    data = read_input('data/test8.txt')
    do(8, data, answers=[26, 61229], test=True)

    data = read_input('data/input8.txt')
    do(8, data, answers=[303, 961734])
