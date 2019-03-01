class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        acc = 0
        res = []
        ind = 0
        while acc < target:
            acc += nums[ind]
            res.append(ind)
            ind += 1
            
        return res
