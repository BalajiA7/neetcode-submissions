class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        visited = [[0] * m for i in range(n)]

        def dfs(i, j):
            if i < 0 or j < 0 or i >= n or j >= m or grid[i][j] == '0' or visited[i][j]:
                return

            visited[i][j] = True

            dfs(i, j-1)
            dfs(i, j+1)
            dfs(i+1, j)
            dfs(i-1, j)
        
        res = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1" and not visited[i][j]:
                    res+=1
                    dfs(i, j)

        return res
        
        