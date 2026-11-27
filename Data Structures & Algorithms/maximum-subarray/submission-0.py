class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        res = nums[0]
        currSum = 0

        for i in range(n):
            currSum += nums[i]
            res = max(res, currSum)
            if currSum < 0:
                currSum = 0
        
        return res


        