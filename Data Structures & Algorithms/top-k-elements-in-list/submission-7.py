class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        heap = []
        for e, v in freq.items():
            heapq.heappush(heap, (-v, e))

        res = []
        while k > 0:
            val = heapq.heappop(heap)[1]
            res.append(val)
            k-=1

        return res

