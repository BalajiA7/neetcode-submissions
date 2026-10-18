class Solution:
    def maxProfit(self, nums):
        n = len(nums)
        dp = [0] * n

        for i in range(0, n):
            pick = nums[i]
            if i > 1:
                pick += dp[i-2]
            notPick = dp[i-1]
            dp[i] = max(pick, notPick)
        
        return dp[n-1]

    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n == 1:
            return nums[0]
        
        return max(self.maxProfit(nums[:n-1]), self.maxProfit(nums[1:]))
        
