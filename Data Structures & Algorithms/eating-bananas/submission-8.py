class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = float("-infinity")
        
        while l<=r:
            midHrs = (l+r) // 2

            hrs = 0
            for pile in piles:
                hrs+= math.ceil(pile/midHrs)
            if hrs > h:
                # increase the midhrs to reduce the res
                l = midHrs + 1
            else:
                print(midHrs)
                res = midHrs
                r = midHrs - 1
        
        return res


        # for i in range(1,max(piles)+1):
        #     hrs = 0
        #     for pile in piles:
        #         hrs+= math.ceil(pile/i)
        #     if hrs <= h:
        #         return i
        