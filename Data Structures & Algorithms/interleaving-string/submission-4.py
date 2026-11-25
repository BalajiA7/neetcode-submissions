class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n, m = len(s1), len(s2)

        if (n + m) != len(s3):
            return False

        dp = [[-1] * (m+1) for _ in range(n+1)]

        def interLeave(i, j):
            if dp[i][j] != -1:
                return dp[i][j]

            if i == n and j == m:
                return True
            
            if i < n and s1[i] == s3[i+j] and interLeave(i+1, j):
                dp[i][j] = 1
                return True
            
            if j < m and s2[j] == s3[i+j] and interLeave(i, j+1):
                dp[i][j] = 1
                return True

            dp[i][j] = 0
            return False
        
        return interLeave(0, 0)
        