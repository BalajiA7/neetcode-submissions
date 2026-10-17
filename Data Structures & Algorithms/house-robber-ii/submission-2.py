class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        def robHouse(i, n, memo):
            if i >= n:
                return 0
            
            if i in memo:
                return memo[i]
            
            pick = nums[i] + robHouse(i+2, n, memo)
            notPick = robHouse(i+1, n, memo)
            
            memo[i] = max(pick, notPick)
            return memo[i]
        
        return max(robHouse(0,n-1, {}), robHouse(1, n, {}))
        