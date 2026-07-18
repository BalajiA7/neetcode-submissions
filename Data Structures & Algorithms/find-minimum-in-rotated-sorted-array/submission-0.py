class Solution:
    def findMin(self, nums: List[int]) -> int:
        minValue = nums[0]

        for ele in nums:
            minValue = min(minValue, ele)
        
        return minValue
        