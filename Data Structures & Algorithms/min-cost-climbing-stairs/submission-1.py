class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        memo = {}
        
        def minCostStairs(x):
            if x >= n:
                return 0
            
            if x in memo:
                return memo[x]

            memo[x] = cost[x] + min(minCostStairs(x+1) , minCostStairs(x+2))
            return memo[x]
        
        minCostStairs(0)
        return min(memo[0], memo[1])
