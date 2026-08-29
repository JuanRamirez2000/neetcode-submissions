from functools import cache 
class Solution:
    def climbStairs(self, n: int) -> int:
        
        @cache
        def dp(i):
            #Base case at bottom of stair
            if i <= 1:
                return 1

            #memoize the solution
            # if i in memo:
            #     return memo[i]
            
            #go down to the next cases (1 step down or 2 steps down)
            # memo[i] = dp(i - 1) + dp(i - 2)
            # return memo[i]
            
            return dp(i - 1) + dp(i - 2)
        
        return dp(n)