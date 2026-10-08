class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        adjList = defaultdict(list)
        directions = [[-1,0], [1,0], [0,-1],[0, 1]]
        # Building min adjacency List for each (i,j)
        for i in range(n):
            for j in range(m):
                for r, c in directions:
                    nr = i + r
                    nc = j + c
                    if 0 <= nr < n and 0 <= nc < m:
                        adjList[grid[i][j]].append(grid[nr][nc])
        
        time = 0
        visited = set()
        minH = [grid[0][0]]

        print(adjList)

        while True:
            val = heapq.heappop(minH)
            if val in visited:
                continue

            time = max(time, val)
            visited.add(val)

            if val == grid[n-1][m-1]:
                return time

            for neighbourVal in adjList[val]:
                if neighbourVal not in visited:
                    heapq.heappush(minH, neighbourVal)

        return time
    
            