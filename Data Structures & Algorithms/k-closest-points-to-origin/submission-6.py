class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        maxHeap = []
        for point in points:
            a, b = point
            distance = (a*a + b*b) * -1
            heapq.heappush(maxHeap, [distance, [a,b]])
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
        
        res = []
        while len(maxHeap):
            distance, point = heapq.heappop(maxHeap)
            res.append(point)

        return res

        