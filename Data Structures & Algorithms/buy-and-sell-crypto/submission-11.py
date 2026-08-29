class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_val = prices[0]
        for n in prices:
            if n < min_val:
                min_val = n
            trade = n - min_val
            if trade > profit:
                profit = trade
        return profit 
