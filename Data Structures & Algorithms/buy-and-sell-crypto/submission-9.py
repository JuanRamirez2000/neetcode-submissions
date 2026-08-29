class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        lowest = prices[0]

        for n in prices:
            if n < lowest:
                lowest = n
            
            new_prof = n - lowest

            
            if new_prof > profit:
                profit = new_prof
        return profit