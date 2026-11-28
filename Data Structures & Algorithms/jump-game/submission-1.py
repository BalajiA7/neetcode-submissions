class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        memo = [-1] * n

        def dfs(idx):
            if memo[idx] != -1:
                return memo[idx]

            if idx >= n-1:
                return True
            
            maxJump = nums[idx]
            for i in range(1, maxJump+1):
                if dfs(idx+i):
                    memo[idx] = True
                    return True
            
            memo[idx] = False
            return False
        
        return dfs(0)

