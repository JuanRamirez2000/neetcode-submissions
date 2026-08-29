class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        final_arr = [0] * len(nums)
        pref = [0] * len(nums) 
        suff = [0] * len(nums)

        # Set beginning and end to 1 so that we can actually multiply
        pref[0] = suff[len(nums)-1] = 1

        #Skip the first number
        for i in range(1, len(nums)):
            #prev = previosNumber * prevProduct
            pref[i] = nums[i-1] * pref[i-1]
        
        #Skip last, go backwards
            #suff = nextNumber * nextProduct
        for i in range(len(nums) - 2, -1, -1):
            suff[i] = nums[i + 1] * suff[i + 1]

        for i in range(len(nums)):
            final_arr[i] = pref[i] * suff[i]
        return final_arr