class MedianFinder:

    def __init__(self):
        self.small, self.large = [], []
        # small is going to be maxheap (so we maintain minvalue)
        # large is going to be minheap (so we maintain maxvalue)

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small , -1 * num)

        # compare top element of small <= top element of large
        if (self.small and self.large and (-1 * self.small[0]) > self.large[0]):
            ele = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, ele)

        # if length of small & large >= 2
        if len(self.small) > len(self.large) + 1:
            ele = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, ele)
        if len(self.large) > len(self.small) + 1:
            ele = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * ele)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        else:
            return (-1 * self.small[0] + self.large[0]) / 2