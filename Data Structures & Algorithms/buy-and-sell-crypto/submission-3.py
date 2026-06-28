class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        # for i in range(0, len(prices)):
        #     for j in range(i+1, len(prices)):
        #         max_profit = max(max_profit, prices[j] - prices[i])
        # [10,100,1,6,7,1]
        i = 0
        j = 1

        while j < len(prices):
            if prices[i] < prices[j]:
                max_profit = max(max_profit, prices[j] - prices[i])
            else:
                i = j
            j+=1

        return max_profit
        