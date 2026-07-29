class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = r

        while l <= r:
            midK = (l+r) // 2

            currHour = 0
            for values in piles:
                currHour += math.ceil(values / midK)
            
            print(currHour, midK)
           
            if currHour > h:
                # k too small
                l = midK+1
            else:
                res = min(res, midK)
                r = midK-1
                

        return res
        