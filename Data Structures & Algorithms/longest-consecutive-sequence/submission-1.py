class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        ## Sort the nums
        nums.sort()

        ## Create a dict of num: boolean_value
        ## If the num is the start of a sequence then 0
        ## else then 1
        start_nums = {}

        for num in nums:
            if num - 1 not in nums:
                start_nums[num] = 0
            else:
                start_nums[num] = 1

        max_length = 0
        curr = 0    

        ## Check to see if the num is the start of a sequence.
        ## If the value is 0 then it is a start and the current value is reset
        ## If it is a 1 then it is a number after a previous consecutive number
        ## So we add 1 to curr and check if curr is more than the current max
        for num in start_nums:
            if start_nums[num] == 0:
                curr = 1
            else:
                curr += 1

            if curr > max_length:
                max_length = curr
        return max_length 
        
