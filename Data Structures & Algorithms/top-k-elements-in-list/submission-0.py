class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        group_freq = {}
        for i in range(len(nums)):
            curr_freq = 1
            if(nums[i] in group_freq): continue
            for j in range(i+1,len(nums)):
                if(nums[i] == nums[j]):
                    curr_freq += 1
            group_freq[nums[i]] = curr_freq
        
        print(group_freq, group_freq.items())
        sorted_items = sorted(group_freq.items(), key=lambda x: x[1], reverse=True)
        print(sorted_items)

        result = []
        for i in range(k):
            result.append(sorted_items[i][0])
        
        return result
        
