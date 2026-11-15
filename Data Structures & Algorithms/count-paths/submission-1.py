class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[-1] * n for _ in range(m)]

        def allUniquePats(row, col):
            if memo[row][col] != -1:
                return memo[row][col]

            if row == 0 or col == 0:
                return 1
            
            if row < 0 or col < 0:
                return 0
            
            memo[row][col] = allUniquePats(row-1, col) + allUniquePats(row, col-1)
            return memo[row][col]
        

        return allUniquePats(m-1, n-1)