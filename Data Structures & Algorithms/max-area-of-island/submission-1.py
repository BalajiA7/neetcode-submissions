class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        visited = [[0] * m for i in range(n)]

        def bfs(i, j, area):
            queue = deque()
            queue.append((i, j))
            visited[i][j] = 1

            while queue:
                row, col = queue.popleft()
                neighbours = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                area += 1

                for nr, nc in neighbours:
                    r = row + nr
                    c = col + nc
                    if 0 <= r < n and 0 <= c < m and not visited[r][c] and grid[r][c] == 1:
                        queue.append((r,c))
                        visited[r][c] = 1
            return area

        res = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and not visited[i][j]:
                    res = max(res, bfs(i, j, 0))

        return res 