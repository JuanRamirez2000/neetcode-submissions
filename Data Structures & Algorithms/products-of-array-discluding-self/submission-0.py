class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        final_product = []

        for i in range(len(nums)):
            left = 1
            right = 1
            for val in nums[:i]:
                left *= val
            
            for val in nums[(i+1):]:
                right *= val

            final = left * right
            final_product.append(final)
        
        return final_product
        
        