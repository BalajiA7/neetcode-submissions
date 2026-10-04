class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        time = 0
        minHeap = []
        visited = set()

        adjList = defaultdict(list)

        for s, d, t in times:
            adjList[s].append((t, d))

        heapq.heappush(minHeap, (0, k))

        while minHeap:
            d1, n1 = heapq.heappop(minHeap)
            if n1 in visited:
                continue
            visited.add(n1)
            time = max(time, d1)
            for d2, n2 in adjList[n1]:
                if n2 not in visited:
                    heapq.heappush(minHeap, (d1 + d2, n2))

        return time if len(visited) == n else -1
                