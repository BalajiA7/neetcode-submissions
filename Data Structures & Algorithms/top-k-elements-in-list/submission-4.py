class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = {}
        freqArr = [[] for i in range(len(nums)+1)]

        for value in nums:
            freqMap[value] = freqMap.get(value, 0) + 1
        
        for num,freq in freqMap.items():
            freqArr[freq].append(num)
        
        print(freqMap, freqArr)
        
        res = []
        for i in range(len(freqArr)-1, 0, -1):
            groups = freqArr[i]

            for item in groups:
                res.append(item)
                if len(res) == k:
                    return res        