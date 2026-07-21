class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        stack = []

        for price in prices:
            if stack and price > stack[-1]:
                res = max(res, price - stack[-1])
            else: 
                stack.append(price)

        return res