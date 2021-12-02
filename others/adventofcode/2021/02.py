from common import *

def parse_direction(elem):
    elems = elem.split()
    return [elems[0].strip(), int(elems[1].strip())]

def day2_1(instructions: list) -> int:
    pos_x = 0
    pos_y = 0
    for [direction, num] in instructions:
        if direction == "forward":
            pos_x += num
        elif direction == "up":
            pos_y -= num
        elif direction == "down":
            pos_y += num

    return pos_x * pos_y

def day2_2(instructions: list) -> int:
    pos_x = 0
    pos_y = 0
    aim = 0
    for [direction, num] in instructions:
        if direction == "forward":
            pos_x += num
            pos_y += (aim * num)
        elif direction == "up":
            aim -= num
        elif direction == "down":
            aim += num

    return pos_x * pos_y

if __name__ == "__main__":
    data = read_data(2, parser=parse_direction, test=True)
    do(2, data, answers=[150, 900], test=True)

    data = read_data(2, parser=parse_direction)
    do(2, data, answers=[1670340, 1954293920])