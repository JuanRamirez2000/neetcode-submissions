class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        ans = 0
        while left < right:
            #Base is the distance between two bars
            #height is the minimum of the two bars
            #volume is simply area of the square
            base = (right - left)
            height = min(heights[right], heights[left])
            volume = base * height

            #we only care about the max volume here
            ans = max(ans, volume)

            #if one bar is shorter than the other then move the shorter one over
            if heights[right] > heights[left]:
                left += 1
            else:
                right -= 1
        return ans