from typing import List
from common import *


def day4_1(ranges: List[str]) -> int:
    num_contained = 0
    for r in ranges:
        [r1, r2] = r.split(',')
        [min0, max0] = map(int, r1.split('-'))
        [min1, max1] = map(int, r2.split('-'))

        if (min0 >= min1 and max0 <= max1) or (min1 >= min0 and max1 <= max0):
            num_contained += 1

    return num_contained


def day4_2(ranges: List[str]) -> int:
    num_contained = 0
    for r in ranges:
        [r1, r2] = r.split(',')
        [min0, max0] = map(int, r1.split('-'))
        [min1, max1] = map(int, r2.split('-'))

        if (max0 >= min1 and max0 <= max1) or (max1 >= min0 and max1 <= max0):
            num_contained += 1

    return num_contained


if __name__ == "__main__":
    data = read_data(4, parser=str, test=True)
    do(4, data, answers=[2, 4], test=True)
    data = read_data(4, parser=str)
    do(4, data, answers=[441, 0])
