from typing import List
from common import *

tests1 = {
    "mjqjpqmgbljsphdztnvjfqwrcgsmlb": 7,
    "bvwbjplbgvbhsrlpgdmjqwftvncz": 5,
    "nppdvjthqldpwncqszvftbrmjlhg": 6,
    "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg": 10,
    "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw": 11
}

test2 = {
    "mjqjpqmgbljsphdztnvjfqwrcgsmlb": 19,
    "bvwbjplbgvbhsrlpgdmjqwftvncz": 23,
    "nppdvjthqldpwncqszvftbrmjlhg": 23,
    "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg": 29,
    "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw": 26
}


def get_value(line, size_pkg):
    size_msg = len(line)
    for x in range(size_msg):
        if x < size_msg - 4:
            elems = line[x:x+size_pkg]
            if len(set([x for x in elems])) == size_pkg:
                return x + size_pkg
    return 0


def day6_1(data: List[str]) -> int:
    # for k, v in tests1.items():
    #     print(get_value(k, 4), v)

    for msg in data:
        return get_value(msg, 4)

    return 0


def day6_2(data: List[str]) -> int:
    for k, v in test2.items():
        print(get_value(k, 14), v)

    for msg in data:
        return get_value(msg, 14)

    return 0


if __name__ == "__main__":
    data = read_data(6, parser=str, test=True)
    do(6, data, answers=[7, 0], test=True)
    data = read_data(6, parser=str)
    do(6, data, answers=[1275, 'RNRGDNFQG'])
