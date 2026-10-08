class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        # adjList = defaultdict(list)
        directions = [[-1,0], [1,0], [0,-1],[0, 1]]

        # Building min adjacency List for each (i,j)
        # for i in range(n):
        #     for j in range(m):
        #         for r, c in directions:
        #             nr = i + r
        #             nc = j + c
        #             if 0 <= nr < n and 0 <= nc < m:
        #                 adjList[grid[i][j]].append(grid[nr][nc])
        
        time = 0
        visited = set()
        minH = [(grid[0][0], 0, 0)]

        while True:
            height,r,c = heapq.heappop(minH)
            if (r,c) in visited:
                continue

            time = max(time, height)
            visited.add((r,c))

            if r == n-1 and c == m-1:
                return time

            for dr, dc in directions:
                nr,nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < m:
                    heapq.heappush(minH, (grid[nr][nc], nr, nc))

        return time
    
            