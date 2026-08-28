class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for x, y in points:
            distance  = x**2 + y**2
            heapq.heappush(distances, [-distance, [x,y]])                
            if len(distances) > k:
                heapq.heappop(distances)
        
        print(distances)
        # points.sort(key=lambda p: p[0]**2 + p[1]**2)
        return [point for distance, point in distances]