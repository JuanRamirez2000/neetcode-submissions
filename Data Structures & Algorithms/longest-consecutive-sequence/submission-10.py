class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()

        start_nums = {}
        
        # This ensures that we have a num before it
        # IF the number before it is not in the nums then we say it is the start
        # Else we say that something comes after 
        for num in nums:
            if num - 1 not in nums:
                start_nums[num] = 0
            else:
                start_nums[num] = 1
        
        curr = 0
        max_leng = 0
        
        #find distance until next 0
        #this works because the array is sorted, so next 0 should be where the start of a new 
        #seq is
        for num in start_nums:
            if start_nums[num] == 0:
                curr = 1
            else:
                curr += 1
            
            max_leng = max(curr, max_leng)
        return max_leng
