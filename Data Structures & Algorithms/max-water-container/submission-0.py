class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0 
        right = len(heights) - 1 
        max_area = 0 

        while left != right:
            curr_area = (right - left) * min(heights[left], heights[right])
            if curr_area > max_area:
                max_area = curr_area
            
            if heights[right] < heights[left]:
                right -= 1
            else:
                 left += 1
        
        return max_area
