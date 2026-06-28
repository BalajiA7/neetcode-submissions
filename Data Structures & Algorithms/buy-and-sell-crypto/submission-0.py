class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        for i in range(0, len(prices)):
            for j in range(i+1, len(prices)):
                max_profit = max(max_profit, prices[j] - prices[i])


        return max_profit
        