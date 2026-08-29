from functools import cache
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        @cache
        def dp(i):
            if i <= 1:
                return cost[i]
            
            return min((cost[i] + dp(i - 1)), (cost[i] + dp(i - 2)))

        return min(dp(len(cost) - 1), dp(len(cost) - 2))