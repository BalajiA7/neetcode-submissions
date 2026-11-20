class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        n = len(nums)
        dp = {}

        def ways(idx, currTarget):
            if idx < 0:
                return 1 if currTarget == 0 else 0
            
            if (idx,currTarget) in dp:
                return dp[(idx, currTarget)]
            
            add = ways(idx-1, currTarget - nums[idx])
            subtract = ways(idx-1, currTarget + nums[idx])
            
            dp[(idx, currTarget)] = add + subtract
            return dp[(idx, currTarget)]
        
        return ways(n-1, target)