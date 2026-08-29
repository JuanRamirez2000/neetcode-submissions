class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        ans = 0
        while left < right:
            base = (right - left)
            height = min(heights[right], heights[left])
            volume = base * height
            ans = max(ans, volume)
            if heights[right] > heights[left]:
                left += 1
            else:
                right -= 1
        return ans