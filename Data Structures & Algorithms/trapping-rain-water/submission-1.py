class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0:
            return 0

        pref = [0] * n 
        suff = [0] * n 

        pref[0] = height[0]
        for l in range(1, n):
            pref[l] = max(pref[l - 1], height[l])
        
        suff[n - 1] = height[n - 1]
        for r in range(len(height) - 2, -1, -1):
            suff[r] = max(suff[r + 1], height[r])
        
        res = 0
        for i in range(n):
            res += min(pref[i], suff[i]) - height[i]
        return res