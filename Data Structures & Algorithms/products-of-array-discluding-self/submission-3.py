class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixSum = [1] * len(nums)
        # suffixSum = [1] * len(nums)
        
        #calculate prefix sum
        for i in range(1, len(nums)):
            prefixSum[i] = prefixSum[i-1] * nums[i-1]

        #calculate prefix sum
        suffixSum = 1
        for i in range(len(nums)-2, -1, -1):
            # suffixSum[i] = suffixSum[i+1] * nums[i+1]
            suffixSum = suffixSum * nums[i+1]
            prefixSum[i] = prefixSum[i] * suffixSum

        print(prefixSum)

        #calculate the result
        # for i in range(len(nums)):
        #     result.append(prefixSum[i] * suffixSum[i])

        return prefixSum