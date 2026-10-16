class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        
        prev2 = 0
        prev1 = nums[0]

        for i in range(1, n):
            pick = nums[i] + prev2
            notPick = prev1

            curr = max(pick, notPick)
            prev2 = prev1
            prev1 = curr
        
        return prev1