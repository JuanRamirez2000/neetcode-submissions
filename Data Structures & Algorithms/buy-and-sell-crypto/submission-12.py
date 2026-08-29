class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        left = 0
        right = 1

        while right < len(prices) :
            if prices[right] > prices[left]:
                cost = prices[right] - prices[left]
                profit = max(cost, profit)
                right += 1
            else:
                left += 1
                right = left + 1
        return profit