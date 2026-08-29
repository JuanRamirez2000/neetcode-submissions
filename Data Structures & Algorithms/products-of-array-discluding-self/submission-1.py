class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        final_arr = []
        for i in range(len(nums)):
            left = 1
            right = 1 

            #Prefix product
            for val in nums[:i]:
                left *= val

            #Suffix product
            for val in nums[(i+1):]:
                right *= val

            final_arr.append(left * right)
        return final_arr