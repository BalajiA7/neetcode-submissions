class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        n, m = len(matrix), len(matrix[0])
        visited = [[False] * m for _ in range(n)]
        direction = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        dp = [[-1] * m for _ in range(n)]
        longestPath = 0

        def dfs(i, j):
            if dp[i][j] != -1:
                return dp[i][j]

            if visited[i][j]:
                return 0
            
            visited[i][j] = True
            longestPath = 0

            for dr,dc in direction:
                row = i + dr
                col = j + dc
                if row >= 0 and row < n and col >=0 and col < m and matrix[row][col] > matrix[i][j]:
                    longestPath = max(longestPath, 1 + dfs(row, col))
            
            visited[i][j] = False
            dp[i][j] = longestPath
            return longestPath

        for i in range(n):
            for j in range(m):
                longestPath = max(longestPath,  1 + dfs(i, j))
        
        return longestPath