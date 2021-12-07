from common import *
import sys
import gc
import math


def day6_1(data):
    for day in range(80):
        # print(f"day: {day}", data)
        new_elems = []
        for idx, state in enumerate(data):
            if state == 0:
                new_elems.append(8)
                data[idx] = 6
            else:
                data[idx] -= 1
        data.extend(new_elems)

    return len(data)


def day6_2(data):
    current_state = {i: 0 for i in range(9)}

    for i in data:
        current_state[i] += 1

    for _day in range(256):
        current_new_state = {i: 0 for i in range(9)}
        for i in range(9):
            if i > 0:
                current_new_state[i-1] = current_state[i]
        current_new_state[8] += current_state[0]
        current_new_state[6] += current_state[0]

        current_state = current_new_state

    return sum(current_state.values())


if __name__ == "__main__":
    data = read_data(6, sep=',', test=True)
    do(6, data, answers=[5934, 26984457539], test=True)

    data = read_data(6, sep=',')
    do(6, data, answers=[376194, 1693022481538])
