class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sol = {}
        for idx, n in enumerate(nums):
            diff = target - n
            if diff in sol.keys():
                return [min(sol[diff], idx), max(sol[diff],idx)]
            else:
                sol[n] = idx
         