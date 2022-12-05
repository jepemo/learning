from typing import List
from common import *


def get_duplicated_items(comp1, comp2):
    return list(set([c1 for c1 in comp1 for c2 in comp2 if c1 == c2]))


def get_score(item):
    if ord(item) >= ord('a') and ord(item) <= ord('z'):
        return ord(item) - ord('a') + 1
    elif ord(item) >= ord('A') and ord(item) <= ord('Z'):
        return ord(item) - ord('A') + 27


def get_common_item(r1, r2, r3):
    return list(set([c1 for c1 in r1 for c2 in r2 for c3 in r3 if c1 == c2 == c3]))


def day3_1(rucksacks: List[str]) -> int:
    score = 0
    for rucksack in rucksacks:
        comp1, comp2 = rucksack[0:len(
            rucksack)//2], rucksack[len(rucksack)//2:]
        duplicated_items = get_duplicated_items(comp1, comp2)
        score += sum([get_score(x) for x in duplicated_items])

    return score


def day3_2(rucksacks: List[str]) -> int:
    score = 0
    for ind in range(0, len(rucksacks), 3):
        [r1, r2, r3] = rucksacks[ind:ind+3]
        score += sum([get_score(x) for x in get_common_item(r1, r2, r3)])

    return score


if __name__ == "__main__":
    data = read_data(3, parser=str, test=True)
    do(3, data, answers=[157, 70], test=True)
    data = read_data(3, parser=str)
    do(3, data, answers=[7980, 2881])
