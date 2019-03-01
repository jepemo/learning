class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for ind1 in range(0, len(nums)):
            for ind2 in range(0, len(nums)):
                v1 = nums[ind1]
                v2 = nums[ind2]
                if v1 + v2 == target:
                    return [ind1, ind2]
                
        return []
