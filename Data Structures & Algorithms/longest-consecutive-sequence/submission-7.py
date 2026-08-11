class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashSet = set(nums)
        res = 0

        for val in hashSet:
            if (val-1) not in hashSet:
                temp = val
                while temp in hashSet:
                    temp+=1
                res = max(res, temp - val)
        
        return res
        