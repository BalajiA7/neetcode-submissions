class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # top down approach
        n = len(nums)
        totalSum = sum(nums)
        target = totalSum // 2
        if totalSum % 2:
            return False
        dp = [[False] * (target+1) for _ in range(n)]
        # print(memo)

        # basecases
        for i in range(n):
            dp[i][0] = True

        dp[0][nums[0]] = True

        for ind in range(1, n):
            for t in range(1, target+1):
                notPick = dp[ind-1][t]
                # pick 
                pick = False
                if t >= nums[ind]:
                    pick = dp[ind-1][t-nums[ind]]
                
                dp[ind][t] = pick or notPick
        
        return dp[n-1][target]

        
        # def subSequence(ind, target):
        #     if target == 0:
        #         return True
            
        #     if ind == 0:
        #         return nums[0] == target
            
        #     if memo[ind][target] != -1:
        #         return memo[ind][target]
            
        #     # not pick
        #     notPick = subSequence(ind-1, target)
        #     # pick 
        #     pick = False
        #     if target > nums[ind]:
        #         pick = subSequence(ind-1, target-nums[ind])
            
        #     memo[ind][target] = pick or notPick
        #     return memo[ind][target]
        
        # return subSequence(n-1, target)
        