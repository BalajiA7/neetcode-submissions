class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = [0] * (len(nums) - k + 1)

        for i in range(len(nums)-k+1):
            maxValue = float("-inf")
            for j in range(i,i+k):
                maxValue = max(maxValue, nums[j])
            res[i] = maxValue
        
        return res