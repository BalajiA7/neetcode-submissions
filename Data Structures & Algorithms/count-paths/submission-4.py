class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # dp = [[0] * n for _ in range(m)]
        prev = [0] * n

        for row in range(m):
            curr = [0] * n
            for col in range(n):
                if row == 0 and col == 0:
                    curr[col] = 1
                else:
                    up = prev[col] if row > 0 else 0
                    left = curr[col-1] if col > 0 else 0

                    curr[col] = up + left
            prev = curr
        
        return prev[n-1]

        # def allUniquePats(row, col):
        #     if memo[row][col] != -1:
        #         return memo[row][col]

        #     if row == 0 and col == 0:
        #         return 1
            
        #     if row < 0 or col < 0:
        #         return 0
            
        #     memo[row][col] = allUniquePats(row-1, col) + allUniquePats(row, col-1)
        #     return memo[row][col]
        

        # return allUniquePats(m-1, n-1)