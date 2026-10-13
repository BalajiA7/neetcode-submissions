class Solution:
    def climbStairs(self, n: int) -> int:
        
        memoization = {}
        
        def stairs(n):
            if n in memoization:
                return memoization[n]

            if n < 0:
                return 0
        
            if n == 0:
                return 1
            
            memoization[n] = stairs(n-1) + stairs(n-2)
            return memoization[n]
            
        stairs(n)
        return memoization[n]