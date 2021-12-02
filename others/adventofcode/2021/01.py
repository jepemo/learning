from typing import List
from common import *

def day1_1(nums: List[int]) -> int:
    return sum(idx > 0 and nums[idx - 1] < num 
               for idx, num in enumerate(nums))

def day1_2(nums: List[int]) -> int:
    return sum(idx > 0 and idx < len(nums) - 2 and sum(nums[idx-1:idx+2]) < sum(nums[idx:idx+3])
               for idx in range(len(nums)))

if __name__ == "__main__":
    data = read_data(1, test=True)
    do(1, data, answers=[7, 5], test=True)
    data = read_data(1)
    do(1, data, answers=[1477, 1523])
