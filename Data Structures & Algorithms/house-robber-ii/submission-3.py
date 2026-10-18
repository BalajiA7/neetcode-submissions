class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        def robHouse(i, start, memo):
            if i < start:
                return 0
            
            if i in memo:
                return memo[i]
            
            pick = nums[i] + robHouse(i-2, start, memo)
            notPick = robHouse(i-1, start, memo)
            
            memo[i] = max(pick, notPick)
            return memo[i]
        
        return max(robHouse(n-1,1, {}), robHouse(n-2, 0, {}))
        