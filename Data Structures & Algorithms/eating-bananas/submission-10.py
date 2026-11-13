class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            # mid -> bananas per hour
            mid = (l+r) // 2
            hour = 0
            for pile in piles:
                hour += math.ceil(pile / mid)

            if hour > h:
                # hour is too high, let increase the eating rate
                l = mid + 1
            else:
                # hour is <= h, let decrease further to get better eating rate
                res = mid
                r = mid - 1
        
        return res
        
        # for i in range(1, n+1):
        #     # i -> bananas per hour
        #     hour = 0
        #     for pile in piles:
        #         hour += math.ceil(pile / i)
        #     # print(i, hour)
        #     if hour <= h:
        #         return i
        
        # return n

        