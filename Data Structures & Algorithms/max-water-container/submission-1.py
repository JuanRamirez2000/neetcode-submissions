class Solution:
    def maxArea(self, heights: List[int]) -> int:
        curr_max = 0
        l, r = 0, len(heights) - 1
        while l != r:
            vol = (r - l) * min(heights[r], heights[l])
            if vol > curr_max:
                curr_max = vol
            if heights[r] < heights[l]:
                r -= 1
            else:
                l += 1
        return curr_max