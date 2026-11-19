class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        n = len(coins)
        prev = [0] * (amount+1)

        # base case
        # for i in range(n):
        #     dp[i][0] = 1

        for idx in range(n):
            curr = [0] * (amount+1)
            curr[0] = 1
            for a in range(1, amount+1):
                # pick the idx coin
                if a >= coins[idx]:
                    curr[a] += curr[a - coins[idx]]
                
                # not pick the idx coin
                curr[a] += prev[a] if idx - 1 >=0 else 0
            
            prev = curr

        # def dfs(idx, amount):
        #     if idx < 0:
        #         return 0

        #     if amount == 0:
        #         return 1
            
        #     if dp[idx][amount] != -1:
        #         return dp[idx][amount]
            
        #     ways = 0
        #     # pick the idx coin
        #     if amount >= coins[idx]:
        #         ways += dfs(idx, amount - coins[idx])
            
        #     # not pick the idx coin
        #     ways += dfs(idx-1, amount)
            
        #     dp[idx][amount] = ways
        #     return ways
        
        return prev[amount]