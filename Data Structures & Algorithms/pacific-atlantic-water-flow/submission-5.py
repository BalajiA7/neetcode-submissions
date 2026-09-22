class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n = len(heights)
        m = len(heights[0])
        pacificSet = set()
        atlanticSet = set()


        def dfs(r, c, visited):
            if (r,c) in visited:
                return

            visited.add((r,c))
            for dr,dc in [[1, 0], [-1, 0],[0, 1], [0, -1]]:
                nr = r+dr
                nc = c+dc
                if (0<= nr <n) and (0<= nc < m) and (nr,nc) not in visited and heights[nr][nc] >= heights[r][c]:
                    dfs(nr,nc, visited) 

        
        # pacific -> top and left
        for c in range(m):
            dfs(0,c,pacificSet)
        
        for r in range(n):
            dfs(r,0,pacificSet)

        # atlantic -> bottom and right
        for c in range(m):
            dfs(n-1,c,atlanticSet)
        
        for r in range(n):
            dfs(r,m-1,atlanticSet)
            
        res = []
        for r in range(n):
            for c in range(m):
                if (r,c) in pacificSet and (r,c) in atlanticSet:
                    res.append([r,c])
        
        return res
