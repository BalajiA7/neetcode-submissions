class MedianFinder:

    def __init__(self):
        self.nums = []

    def addNum(self, num: int) -> None:
        self.nums.append(num)

    def findMedian(self) -> float:
        self.nums.sort()
 
        length = len(self.nums)
        # the length could be even or odd
        mid = length // 2
        if length % 2 == 0:
            # even case
            return (self.nums[mid-1] + self.nums[mid]) / 2

        else:
            # odd case
            return self.nums[mid]
        