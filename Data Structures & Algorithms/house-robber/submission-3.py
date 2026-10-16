class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {}

        def robHouse(i):
            if i == 0:
                return nums[0]
            
            if i < 0:
                return 0

            if i in memo:
                return memo[i]

            # pick the house
            pick = nums[i] + robHouse(i-2)
            # Not pick
            notPick = robHouse(i-1)
            
            memo[i] = max(pick,notPick)
            return memo[i]
        
        return robHouse(n-1)