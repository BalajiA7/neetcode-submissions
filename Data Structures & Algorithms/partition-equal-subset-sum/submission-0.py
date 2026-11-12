class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        totalSum = sum(nums)
        targetSum = totalSum // 2

        # for odd sum, equal partition is not possible
        if totalSum % 2 != 0:
            return False
        
        def partition(idx, currSum):
            if currSum == targetSum:
                return True
            
            if currSum > targetSum or idx >= n:
                return False
            
            # pick case and not pick case
            return partition(idx+1, currSum+ nums[idx]) or partition(idx+1, currSum)
        
        return partition(0, 0)

        
        

        