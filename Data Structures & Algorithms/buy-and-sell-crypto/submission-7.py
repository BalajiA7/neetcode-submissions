class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minValue = prices[0]
        res = 0

        for i in range(1, len(prices)):
            # Buy on lower price
            if prices[i] < minValue:
                minValue = prices[i]
            else:
                # sell on higher prices
                res = max(res, prices[i]-minValue)
                
        return res
        