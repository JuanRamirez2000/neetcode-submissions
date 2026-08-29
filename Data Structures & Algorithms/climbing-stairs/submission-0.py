from functools import cache
class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        def dp(idx):
            if idx < 2:
                return 1
            return (dp(idx - 1) + dp(idx - 2))

        return dp(n)