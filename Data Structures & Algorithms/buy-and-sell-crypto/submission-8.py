class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = prices[0], prices[0]
        profit = 0

        for i in range(1, len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            else:
                sell = prices[i]
                profit = max(profit, sell - buy)
        
        return profit
        