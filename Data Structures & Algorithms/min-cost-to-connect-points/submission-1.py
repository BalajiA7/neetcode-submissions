class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adjList = defaultdict(list)

        for i in range(n):
            x1,y1 = points[i] 
            for j in range(i+1, n):
                x2,y2 = points[j]
                distance = abs(x1-x2) + abs(y1-y2)
                adjList[i].append([distance, j])
                adjList[j].append([distance, i])
        
        minPath = 0
        visited = set()
        minH = [[0,0]]

        while len(visited) != n:
            distance, node = heapq.heappop(minH)
            if node in visited:
                continue
            minPath += distance
            visited.add(node)

            for neighbourD, neighbourN in adjList[node]:
                if neighbourN not in visited:
                    heapq.heappush(minH, [neighbourD, neighbourN])

        return minPath

            



        