class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        minValue = nums[0]

        while l<=r:
            mid = (l+r) // 2
            minValue = min(minValue, nums[mid])

            if nums[mid] < nums[r]:
                # go left to find minValue
                r = mid-1
            else:
                # go right to find minValue
                l = mid +1
        
        return minValue
