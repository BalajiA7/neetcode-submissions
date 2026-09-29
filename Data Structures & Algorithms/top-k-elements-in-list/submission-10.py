class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        bucket = [[] for _ in range(len(nums) + 1)]

        for num,count in freq.items():
            bucket[count].append(num)
        
        res = []
        for i in range(len(bucket)-1, -1, -1):
            group = bucket[i]
            for j in group:
                res.append(j)
                if len(res) == k:
                    return res


            

