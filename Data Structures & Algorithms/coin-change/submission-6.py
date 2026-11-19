class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [[-1] * (amount+1) for _ in range(n)]

        for i in range(n):
            dp[i][0] = 0

        for idx in range(n):
            for a in range(1, amount+1):
                pick = float("infinity")
                # pick the idx coin
                if a >= coins[idx]:
                    pick = 1 + dp[idx][a - coins[idx]]
                
                # not pick the idx coin
                notPick = dp[idx-1][a] if idx - 1 >= 0 else float("infinity")
                
                dp[idx][a] = min(pick, notPick)
        
        val = dp[n-1][amount]
        return val if val != float("infinity") else -1
        