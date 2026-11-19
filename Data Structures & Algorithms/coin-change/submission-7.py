class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        prev = [-1] * (amount+1)

        for idx in range(n):
            curr = [-1] * (amount+1)
            curr[0] = 0
            for a in range(1, amount+1):
                pick = float("infinity")
                # pick the idx coin
                if a >= coins[idx]:
                    pick = 1 + curr[a - coins[idx]]
                
                # not pick the idx coin
                notPick = prev[a] if idx - 1 >= 0 else float("infinity")
                
                curr[a] = min(pick, notPick)
            prev = curr
        
        val = prev[amount]
        return val if val != float("infinity") else -1       