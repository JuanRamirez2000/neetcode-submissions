class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        lowest = prices[0]

        for n in prices:

            #Buy lowest
            if n < lowest:
                lowest = n
            
            #Comparison if the current number - lowest is best than profit
            new_prof = n - lowest
            if new_prof > profit:
                profit = new_prof
        
        return profit