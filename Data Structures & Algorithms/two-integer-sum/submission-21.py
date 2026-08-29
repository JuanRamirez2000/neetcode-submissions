class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        usedMap = {}

        for i, n in enumerate(nums):
            difference = target - n
            if difference in usedMap:
                return [usedMap[difference], i]
            usedMap[n] = i
        #Why does this solution work:
        #the difference is used a + b = target
        # or simply target - b = a
        #This is useful because if target - b in usedMap 
        #then we would know that this equation has already been solved

        #O(n^2) solution
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if i == j:
        #             continue
        #         if nums[i] + nums[j] == target:
        #             return [i, j]