class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        n = len(grid)
        m = len(grid[0])
        queue = deque()

        for r in range(n):
            for c in range(m):
                if grid[r][c] == 0:
                    queue.append((r,c))
        
        direction = [[1,0], [-1,0], [0,1], [0,-1]]
        distance = 0
        
        while queue:
            r, c = queue.popleft()

            for i, j in direction:
                nr = r + i
                nc = c + j
                if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == 2147483647:
                    grid[nr][nc] = grid[r][c] + 1 
                    queue.append((nr,nc))

                            