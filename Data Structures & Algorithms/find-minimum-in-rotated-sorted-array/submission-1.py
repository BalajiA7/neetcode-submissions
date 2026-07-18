class Solution:
    def findMin(self, nums: List[int]) -> int:
        l =0
        r = len(nums)-1
        minValue = float('infinity')

        while l<=r:
            mid = l + (r-l) // 2
            minValue = min(minValue, nums[mid])

            if nums[r] < nums[mid]:
                l = mid + 1
            else:
                r = mid -1
        
        return minValue
        