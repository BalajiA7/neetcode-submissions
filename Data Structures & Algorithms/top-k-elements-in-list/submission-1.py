class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        group_freq = {}
        for val in nums:
            group_freq[val] = group_freq.get(val, 0) + 1
        
        sorted_items = sorted(group_freq.items(), key=lambda x: x[1], reverse=True)

        result = []
        for i in range(k):
            result.append(sorted_items[i][0])
        
        return result
        
