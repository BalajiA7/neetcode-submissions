class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # top down approach
        n = len(nums)
        totalSum = sum(nums)
        target = totalSum // 2
        if totalSum % 2:
            return False
        memo = [[-1] * (target+1) for _ in range(n)]
        # print(memo)
        
        def subSequence(ind, target):
            if target == 0:
                return True
            
            if ind == 0:
                return nums[0] == target
            
            if memo[ind][target] != -1:
                return memo[ind][target]
            
            # not pick
            notPick = subSequence(ind-1, target)
            # pick 
            pick = False
            if target > nums[ind]:
                pick = subSequence(ind-1, target-nums[ind])
            
            memo[ind][target] = pick or notPick
            return memo[ind][target]
        
        return subSequence(n-1, target)
        