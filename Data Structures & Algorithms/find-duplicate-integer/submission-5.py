class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n_dict = {}
        for num in nums:
            if num not in n_dict:
                n_dict[num] = 1
            else:
                return num