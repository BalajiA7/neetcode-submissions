class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxValue = max(piles)
        l = 1
        r = maxValue
        res = 0

        while l <= r:
            mid = l + (r-l) // 2
            calcHours = 0
            for bananas in piles:
                calcHours += math.ceil(bananas / mid)
            print("Mid is ", mid, "CalHours is ", calcHours)
            if calcHours > h:
                l = mid+1               
            elif calcHours <=h:
                res = mid
                r = mid-1

        return res





        # print("Piles", piles, h)
        # for i in range(1, maxValue + 1):
        #     hours = 0
        #     for j in range(0, len(piles)):
        #         hours += math.ceil(piles[j] / i)
        #     print("with eating rate of ", i, " I can eat in hours",hours)
        #     if hours <= h:
        #         return i
        



        