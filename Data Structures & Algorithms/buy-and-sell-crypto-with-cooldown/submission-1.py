class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[-1] * 2 for _ in range(n)]
        print(dp)
        
        # 0 -> already own a stock, can sell or hold
        # 1 -> free to buy
        def dfs(i, buy):
            if i >= n:
                return 0
            
            if dp[i][buy] != -1:
                return dp[i][buy]
            
            profit = 0
            if buy == 1:
                # Buy stock and not buy
                profit = max(-prices[i] + dfs(i+1, 0), dfs(i+1, 1))
            else:
                # sell stock and not sell
                profit = max(prices[i] + dfs(i+2, 1),  dfs(i+1, 0))
            
            dp[i][buy] = profit
            return profit
        
        return dfs(0, 1)
               
            