class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # top down approach
        n = len(nums)
        totalSum = sum(nums)
        target = totalSum // 2
        if totalSum % 2:
            return False

        prev = [False] * (target+1)
        
        # basecases
        prev[0] = True
        if nums[0] <= target:
            prev[nums[0]] = True

        for ind in range(1, n):
            curr = [False] * (target+1)
            curr[0] = True

            for t in range(1, target+1):
                notPick = prev[t]
                # pick 
                pick = False
                if t >= nums[ind]:
                    pick = prev[t-nums[ind]]
                
                curr[t] = pick or notPick
            prev = curr
        
        return prev[target]

        
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
        