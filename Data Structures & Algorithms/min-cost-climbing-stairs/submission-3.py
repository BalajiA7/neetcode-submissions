class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        # dp = [0] * (n+1)
        prev, curr = 0, 0

        for i in range(2, n+1):
            prev, curr = curr, min(
                curr + cost[i-1], 
                prev + cost [i-2]
            ) 
            # dp[i] = min(
            #     dp[i-1] + cost[i-1], 
            #     dp[i-2] + cost [i-2]
            # )
        
        return curr