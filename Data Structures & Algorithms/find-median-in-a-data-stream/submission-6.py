class MedianFinder:
    def __init__(self):
        self.left = [] #max Heap because I want the max value on the left side
        self.right = [] #min Heap because I want the min value on thhe rigt side

    def addNum(self, num: int) -> None:
        heapq.heappush(self.left, num * -1)

        # left top value would be smaller than the right top value
        if len(self.right) and (self.left[0] * -1) > self.right[0]:
            val = heapq.heappop(self.left)
            heapq.heappush(self.right, val * -1)
        
        # stablize if the len of left is more than 2
        if len(self.left) > len(self.right) + 1:
            val = heapq.heappop(self.left)
            heapq.heappush(self.right, val * -1)
        
        # stablize if the len of right is more than 2
        if len(self.right) > len(self.left) + 1:
            val = heapq.heappop(self.right)
            heapq.heappush(self.left, val * -1)


    def findMedian(self) -> float:
        if len(self.left) == len(self.right):
            return (self.left[0] * -1  + self.right[0]) / 2.0
        elif len(self.left) > len(self.right):
            return self.left[0] * -1
        else:
            return self.right[0]
