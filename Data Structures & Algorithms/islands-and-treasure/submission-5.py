class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        n = len(grid)
        m = len(grid[0])
        
        queue = deque()
        for r in range(n):
            for c in range(m):
                if grid[r][c] == 0:
                    queue.append((r,c,1))
        
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        
        while queue:
            r,c,pos = queue.popleft()

            for dr, dc in directions:
                row = dr+r
                col = dc+c
                if (0<=row<n) and (0<=col<m) and (grid[row][col] == 2147483647):
                    grid[row][col] = pos
                    queue.append((row,col,pos+1))
        
        