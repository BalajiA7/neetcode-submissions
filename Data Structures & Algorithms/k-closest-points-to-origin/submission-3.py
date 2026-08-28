class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # for each coordinate calc distance between origin
        distances = []
        for val in points:
            x, y = val
            distance  = x**2 + y**2
            heapq.heappush(distances, [distance, val])                
        
        # now put that array into heap either i can sort the array elements
        # distances.sort()

        # finally return the k closes point in the list
        result = []
        for i in range(k):
            val = heapq.heappop(distances)
            result.append(val[1])

        return result
        
        # points.sort(key=lambda p: p[0]**2 + p[1]**2)
        # return points[:k]

