class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjacencyList = defaultdict(list)
        visited = [0] * numCourses
       
        for a,b in prerequisites:
            adjacencyList[a].append(b)
        
        def dfs(i):
            if visited[i] == 1:
                return False
            
            if visited[i] == 2:
                return True

            visited[i] = 1
            for neighbours in adjacencyList[i]:
                if not dfs(neighbours):
                    return False

            visited[i] = 2
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True
        


        