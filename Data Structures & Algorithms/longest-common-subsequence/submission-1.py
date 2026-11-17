class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        memo = [[-1] * m for _ in range(n)]

        def lcs(i, j):
            if i >= n or j >= m:
                return 0
            
            if memo[i][j] != -1:
                return memo[i][j]
            
            val = 0
            # both characters are same
            if text1[i] == text2[j]:
                val = 1 + lcs(i+1, j+1)
            else:
                # both characters are not same
                val = max(lcs(i, j+1), lcs(i+1, j))
            
            memo[i][j] = val
            return memo[i][j]
        
        return lcs(0,0)


            
        