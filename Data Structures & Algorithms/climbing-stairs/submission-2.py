class Solution:
    def climbStairs(self, n: int) -> int:
        
        memo = {1: 1, 2: 2}
        
        def stairs(n):
            if n in memo:
                return memo[n]
            
            memo[n] = stairs(n-1) + stairs(n-2)
            return memo[n]
            
        
        return stairs(n)