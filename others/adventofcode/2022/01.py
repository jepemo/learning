from typing import List
from common import *


def get_elf_calories(nums):
    elfs = {}
    ind = 0
    for num in nums:
        if num == '':
            ind += 1
        else:
            if ind not in elfs:
                elfs[ind] = 0
            elfs[ind] += int(num)

    return elfs


def day1_1(nums: List[str]) -> int:
    elfs = get_elf_calories(nums)
    return max(elfs.values())


def day1_2(nums: List[str]) -> int:
    elfs = get_elf_calories(nums)
    calories = elfs.values()
    ordered_calories = list(reversed(sorted(calories)))
    return sum(ordered_calories[0:3])


if __name__ == "__main__":
    data = read_data(1, parser=str, test=True)
    do(1, data, answers=[24000, 45000], test=True)
    data = read_data(1, parser=str)
    do(1, data, answers=[69528, 206152])
