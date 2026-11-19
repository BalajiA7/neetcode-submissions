class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        n = len(coins)
        dp = [[-1] * (amount+1) for _ in range(n)]

        def dfs(idx, amount):
            if idx < 0:
                return 0

            if amount == 0:
                return 1
            
            if dp[idx][amount] != -1:
                return dp[idx][amount]
            
            ways = 0
            # pick the idx coin
            if amount >= coins[idx]:
                ways += dfs(idx, amount - coins[idx])
            
            # not pick the idx coin
            ways += dfs(idx-1, amount)
            
            dp[idx][amount] = ways
            return ways
        
        return dfs(n-1, amount)