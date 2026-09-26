class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjacencyList = defaultdict(list)

        for u,v in edges:
            adjacencyList[u].append(v)
            adjacencyList[v].append(u)
        
        visited =  set()

        def dfs(i,prev):
            if i in visited:
                return False
            
            visited.add(i)
            for j in adjacencyList[i]:
                if prev != j and dfs(j, i) == False:
                    return False

            return True
        
        if dfs(0, -1) == False:
            return False
        
        print(visited)
        return len(visited) == n
        