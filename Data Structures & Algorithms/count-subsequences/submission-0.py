class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)
        dp = [[-1] * (m+1) for _ in range(n+1)]

        def dfs(i, j):
            if dp[i][j] != -1:
                return dp[i][j]

            if i == n:
                return 1 if j == m else 0
            
            if j == m:
                return 1
            
            total = 0
            # pick call
            if s[i] == t[j]:
                total += dfs(i+1, j+1)

            # not pick
            total += dfs(i+1, j)
            
            dp[i][j] = total
            return total
        
        return dfs(0, 0)
        