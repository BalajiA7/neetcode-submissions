class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        queue = deque()
        
        fresh = 0
        for r in range(n):
            for c in range(m):
                if grid[r][c] == 2:
                    queue.append((r,c))
                elif grid[r][c] == 1:
                    fresh+=1
        
        direction = [[1,0], [-1,0], [0,1], [0,-1]]

        time = 0
        while queue and fresh:
            length = len(queue)
            time+=1

            while length:
                r,c = queue.popleft()

                for nr, nc in direction:
                    row = nr+r
                    col = nc+c
                    if 0 <= row < n and 0 <= col < m and grid[row][col] == 1:
                        grid[row][col] = 0
                        fresh -=1
                        queue.append((row, col))

                length -=1

        return time if fresh == 0 else -1
