class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-x for x in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            a = heapq.heappop(maxHeap) * -1
            b = heapq.heappop(maxHeap) * -1
            diff = abs(a-b)
            heapq.heappush(maxHeap, diff * -1)
        
        return maxHeap[0] * -1

        