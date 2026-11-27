class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)
        dp = [[0] * (m+1) for _ in range(n+1)]

        for i in range(n+1):
            dp[i][m] = 1
        
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                print(i, j)
                total = 0
                # pick call
                if s[i] == t[j]:
                    total += dp[i+1][j+1]

                # not pick
                total += dp[i+1][j]
                
                dp[i][j] = total
        
        return dp[0][0]
        