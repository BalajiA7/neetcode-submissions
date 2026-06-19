class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_arr = [1] * len(nums)
        suffix_arr = [1] * len(nums)
        
        curr_prod = 1
        for i in range(1, len(nums)):
            curr_prod = curr_prod * nums[i-1]
            prefix_arr[i] = curr_prod

        curr_prod = 1
        for i in range(len(nums)-2, -1, -1):
            curr_prod = curr_prod * nums[i+1]
            suffix_arr[i] = curr_prod

        print(prefix_arr, suffix_arr)

        res = []
        for i in range(0, len(nums)):
            res.append(prefix_arr[i] * suffix_arr[i])
        return res
        