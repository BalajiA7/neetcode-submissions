class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        
        curr_prod = 1
        for i in range(1, len(nums)):
            curr_prod = curr_prod * nums[i-1]
            res[i] = curr_prod

        curr_prod = 1
        for i in range(len(nums)-2, -1, -1):
            curr_prod = curr_prod * nums[i+1]
            res[i] = res[i] * curr_prod

        return res
        