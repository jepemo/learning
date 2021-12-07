from common import *


def day7_1(positions):
    fuels = {}
    for i in range(len(positions)):
        fuels[i] = 0
        for p in positions:
            fuels[i] += abs(i - p)

    return min(fuels.values())


def day7_2(positions):
    fuels = {}
    for i in range(len(positions)):
        fuels[i] = 0
        for p in positions:
            v = abs(i - p)
            r = sum([x for x in range(1, v+1, 1)])
            fuels[i] += r

    return min(fuels.values())


if __name__ == "__main__":
    data = read_data(7, sep=',', test=True)
    do(7, data, answers=[37, 168], test=True)

    data = read_data(7, sep=',')
    do(7, data, answers=[336040, 94813675])
