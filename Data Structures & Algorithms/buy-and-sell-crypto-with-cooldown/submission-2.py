class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0] * 2 for _ in range(n+2)]
        # print(dp)

        for i in range(n-1, -1, -1):
            # Buy stock and not buy
            dp[i][1] = max(-prices[i] + dp[i+1][0], dp[i+1][1])
            # sell stock and not sell
            dp[i][0] = max(prices[i] + dp[i+2][1], dp[i+1][0])

        
        # 0 -> already own a stock, can sell or hold
        # 1 -> free to buy
        # def dfs(i, buy):
        #     if i >= n:
        #         return 0
            
        #     if dp[i][buy] != -1:
        #         return dp[i][buy]
            
        #     profit = 0
        #     if buy == 1:
        #         # Buy stock and not buy
        #         profit = max(-prices[i] + dfs(i+1, 0), dfs(i+1, 1))
        #     else:
        #         # sell stock and not sell
        #         profit = max(prices[i] + dfs(i+2, 1),  dfs(i+1, 0))
            
        #     dp[i][buy] = profit
        #     return profit
        
        return dp[0][1]
               
            