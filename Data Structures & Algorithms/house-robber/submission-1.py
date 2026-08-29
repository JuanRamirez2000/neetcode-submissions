from functools import cache

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        @cache
        def dp(i):
            #rob first house if we arrive to first
            if i  == 0:
                return nums[0]
            #if we arrive to second then we need to consider the first one as well
            elif i == 1:
                return max(nums[0], nums[i])
            
            return max((nums[i] + dp(i - 2)), dp(i - 1))

        #start at the last house and go backwards
        return dp(len(nums) - 1)