class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[-1] * (n+1) for _ in range(n)]

        def lis(idx, prevIdx):
            if idx == n:
                return 0
            
            if dp[idx][prevIdx+1] != -1:
                return dp[idx][prevIdx+1]
            
            res = 0
            # pick case
            if prevIdx == -1 or nums[prevIdx] < nums[idx]:
                res = 1 + lis(idx+1, idx)
            
            # not pick
            res = max(res, lis(idx+1, prevIdx))
            
            dp[idx][prevIdx+1] = res
            return  dp[idx][prevIdx+1]
        
        return lis(0, -1)
                
                
        