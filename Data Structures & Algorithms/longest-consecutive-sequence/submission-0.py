class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()

        start_nums = {}

        for num in nums:
            if num - 1 not in nums:
                start_nums[num] = 0
            else:
                start_nums[num] = 1

        max_length = 0
        curr = 0    
        for num in start_nums:
            if start_nums[num] == 0:
                curr = 1
            else:
                curr += 1

            if curr > max_length:
                max_length = curr
        return max_length 
        
