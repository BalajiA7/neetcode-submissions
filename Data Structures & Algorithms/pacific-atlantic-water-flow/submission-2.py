class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n = len(heights)
        m = len(heights[0])
        res = []

        def dfs(r, c, height, visited):
            if r < 0 or c < 0:
                return (True,False)
            
            if r >= n or c >= m:
                return (False, True)
            
            if visited[r][c] or heights[r][c] > height:
                return (False, False)

            currHeight = heights[r][c]
            visited[r][c] = True

            # pacific
            leftPacific, leftAtlantic = dfs(r, c-1, currHeight, visited)
            topPacific, topAtlantic  = dfs(r-1, c, currHeight, visited)
            # atlantic
            bottomPacific, bottomAtlantic = dfs(r+1, c, currHeight, visited)
            rightPacific, rightAtlantic = dfs(r, c+1, currHeight, visited)
            
            pacific = leftPacific or topPacific or bottomPacific or rightPacific
            atlantic = bottomAtlantic or rightAtlantic or leftAtlantic or topAtlantic

            # visited[r][c] = False

            return (pacific, atlantic)
        

        for r in range(n):
            for c in range(m):
                visited = [[0 for i in range(m)] for i in range(n)]
                pacific, atlantic = dfs(r,c, heights[r][c], visited)
                if pacific and atlantic:
                    res.append([r,c])
        
        return res
