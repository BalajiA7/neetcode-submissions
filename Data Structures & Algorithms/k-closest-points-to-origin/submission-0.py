class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # for each coordinate calc distance between origin
        distances = []
        for val in points:
            x, y = val
            distance  = math.sqrt(x*x + y*y)
            distances.append([distance,val])
        
        # now put that array into heap either i can sort the array elements
        distances.sort(reverse=True)
        print(distances)
        # finally return the k closes point in the list
        result = []
        for i in range(len(distances)-1, -1, -1):
            if k > 0:
                result.append(distances[i][1])
                k-=1
        
        return result

