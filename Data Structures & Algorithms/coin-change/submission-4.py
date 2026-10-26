class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        n = len(coins)
        dp = [0] * (amount + 1)
        # memo = {}

        if amount == 0:
            return 0

        for i in range(1, amount+1):
            minValue = float("inf")
            for j in range(n):
                if (i - coins[j]) >= 0:
                    minValue = min(minValue, 1 + dp[i-coins[j]])
            dp[i] = minValue
        
        return dp[amount] if dp[amount] != float("inf") else -1
            
        
        # def minCoins(amount):
        #     if amount == 0:
        #         return 0

        #     if amount in memo:
        #         return memo[amount]

        #     minValue = float("inf")
        #     for i in range(n):
        #         if (amount - coins[i]) >= 0:
        #             minValue = min(minValue, 1 + minCoins(amount-coins[i]))
            
        #     # print(amount, minValue)
        #     memo[amount] = minValue
        #     return minValue
        
        # denominations = minCoins(amount)
        # return -1 if denominations == float("inf") else denominations

