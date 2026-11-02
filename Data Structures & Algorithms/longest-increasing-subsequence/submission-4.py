class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [[-1] * (n+1) for i in range(n)]

        def lis(idx, prevIdx):
            if idx == n:
                return 0
            if memo[idx][prevIdx+1] != -1:
                return memo[idx][prevIdx+1]
            
            longestSubSequence = 0
            for i in range(idx, n):
                if prevIdx == -1 or nums[prevIdx] < nums[i]:
                    longestSubSequence = max(longestSubSequence, 1 + lis(i+1, i))
            
            memo[idx][prevIdx+1] = longestSubSequence
            return longestSubSequence
        
        return lis(0, -1)
                
                
        