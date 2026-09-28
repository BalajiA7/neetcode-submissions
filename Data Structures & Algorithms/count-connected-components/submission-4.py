class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjacentList = {i:[] for i in range(n)}
        for u,v in edges:
            adjacentList[u].append(v)
            adjacentList[v].append(u)
        
        visited = set()
        def dfs(i):
            visited.add(i)

            for j in adjacentList[i]:
                if j not in visited:
                    dfs(j)
        
        x = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                x+=1

        return x
        