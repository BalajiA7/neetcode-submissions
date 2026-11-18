class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        # memo = [[0] * m for _ in range(n)]
        prevRow = [0] * m

        for i in range(n):
            currRow = [0] * m
            for j in range(m):                    
                # both characters are same
                if text1[i] == text2[j]:
                    currRow[j] = 1 + (prevRow[j-1] if i > 0 and j > 0 else 0)
                else:
                    # both characters are not same
                    left = currRow[j-1] if j > 0 else 0
                    up = prevRow[j] if i > 0 else 0
                    currRow[j] = max(left,up)
            prevRow = currRow

        # def lcs(i, j):
        #     if i < 0  or j < 0:
        #         return 0
            
        #     if memo[i][j] != -1:
        #         return memo[i][j]
            
        #     val = 0
        #     # both characters are same
        #     if text1[i] == text2[j]:
        #         val = 1 + lcs(i-1, j-1)
        #     else:
        #         # both characters are not same
        #         val = max(lcs(i, j-1), lcs(i-1, j))
            
        #     memo[i][j] = val
        #     return memo[i][j]
        
        return prevRow[m-1]