class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [[-1] * (amount+1) for _ in range(n)]

        def dfs(idx, amount):
            if idx < 0:
                return float("infinity")
            
            if amount == 0:
                return 0
            
            if dp[idx][amount] != -1:
                return dp[idx][amount]
            
            pick = float("infinity")
            # pick the idx coin
            if amount >= coins[idx]:
                pick = 1 + dfs(idx, amount - coins[idx])
            
            # not pick the idx coin
            notPick = dfs(idx-1, amount)
            
            dp[idx][amount] = min(pick, notPick)
            return dp[idx][amount]
        
        val = dfs(n-1, amount)
        
        return val if val != float("infinity") else -1
        