class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        while len(stones) > 1:
            stones.sort()
            a = stones.pop()
            b = stones.pop()
            diff = abs(a-b)
            stones.append(diff)
        
        return stones[0]
        