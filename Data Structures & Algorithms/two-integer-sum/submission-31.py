class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, num in enumerate(nums):
            res = target - num
            if res in seen.keys():
                return [min(seen[res], i), max(seen[res], i)]
            else:
                seen[num] = i
        