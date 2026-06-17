class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        group_freq = {}
        freq = [[] for items in range(len(nums) + 1)]
        for val in nums:
            group_freq[val] = group_freq.get(val, 0) + 1
        
        for nums, count in group_freq.items():
            freq[count].append(nums)
        
        result = []

        for i in range(len(freq) -1, 0,-1):
            for val in freq[i]:
                result.append(val)
                if len(result) == k:
                    return result
        
        
