class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        n = len(nums)
        prefix = 1
        suffix = 1
        res = nums[0]

        for i in range(n):
            if prefix == 0:
                prefix = 1
            if suffix == 0:
                suffix = 1

            prefix *= nums[i]
            suffix *= nums[n-i-1]
            res = max(res, prefix, suffix)

        return res


        # for i in range(n):
        #     value = 1
        #     for j in range(i, n):
        #         value *= nums[j]
        #         maxValue = max(maxValue, value)
        
        return maxValue