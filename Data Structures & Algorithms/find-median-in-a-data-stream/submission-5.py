class MedianFinder:

    def __init__(self):
        self.left = [] #maxHeap
        self.right = [] #minHeap
        

    def addNum(self, num: int) -> None:
        # push to left by default
        heapq.heappush(self.left, num * -1)
        
        # if left is having greater values than right
        if self.left and self.right and self.left[0]*-1 > self.right[0]:
            val = heapq.heappop(self.left) * -1
            heapq.heappush(self.right, val)
        
        # fix left to right balancing
        if len(self.left) > len(self.right) + 1:
            val = heapq.heappop(self.left) * -1
            heapq.heappush(self.right, val)  
        
        # fix right to left balancing
        if len(self.right) > len(self.left) + 1:
            val = heapq.heappop(self.right)
            heapq.heappush(self.left, val * -1)
        

    def findMedian(self) -> float:
        if (len(self.left) + len(self.right)) % 2 == 1:
            return self.left[0] * -1 if len(self.left) > len(self.right) else self.right[0]
        else:
            return (self.left[0] * -1+ self.right[0])/ 2.0
        
        