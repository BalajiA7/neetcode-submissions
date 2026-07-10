class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxSequence = 0
        hashSet = set(nums)

        for val in hashSet:
            if (val-1) not in hashSet:
                # Beginning of the sequence
                num = val
                count = 0
                while num in hashSet:
                    count +=1
                    maxSequence = max(maxSequence, count)
                    # hashSet.remove(num)
                    num+=1

        return maxSequence



        