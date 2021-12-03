
from common import *


def parse_digits(input):
    return [c for c in input]


def calculate_num_pos(measures, pos):
    num_z = 0
    num_o = 0
    for m in measures:
        if m[pos] == '0':
            num_z += 1
        else:
            num_o += 1
    return (num_z, num_o)


def day3_1(measures: list) -> int:
    length_digits = len(measures[0])
    nums = [calculate_num_pos(measures, pos) for pos in range(length_digits)]

    gamma = ''.join([("0" if n_z > n_o else "1") for (n_z, n_o) in nums])
    epsilon = ''.join([("1" if n_z > n_o else "0") for (n_z, n_o) in nums])

    return int(gamma, 2) * int(epsilon, 2)


def calculate_oxygen(measures):
    sub_measures = measures
    for pos in range(len(measures[0])):
        if len(sub_measures) == 1:
            break

        (num_z, num_o) = calculate_num_pos(sub_measures, pos)
        if num_z == num_o:
            sub_measures = list(filter(lambda x: x[pos] == "1", sub_measures))
        else:
            sub_measures = list(filter(lambda x:
                                       (x[pos] == "0" and num_z > num_o) or
                                       (x[pos] == "1" and num_z < num_o), sub_measures))
    return int(''.join(sub_measures[0]), 2)


def calculate_co2(measures):
    sub_measures = measures
    for pos in range(len(measures[0])):
        if len(sub_measures) == 1:
            break

        (num_z, num_o) = calculate_num_pos(sub_measures, pos)
        if num_z == num_o:
            sub_measures = list(filter(lambda x: x[pos] == "0", sub_measures))
        else:
            sub_measures = list(filter(lambda x:
                                       (x[pos] == "0" and num_z < num_o) or
                                       (x[pos] == "1" and num_z > num_o), sub_measures))
    return int(''.join(sub_measures[0]), 2)


def day3_2(measures: list) -> int:
    return calculate_oxygen(measures) * calculate_co2(measures)


if __name__ == "__main__":
    data = read_data(3, parser=parse_digits, test=True)
    do(3, data, answers=[198, 230], test=True)

    data = read_data(3, parser=parse_digits)
    do(3, data, answers=[3885894, 4375225])
