class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixSum = [1] * len(nums)
        suffixSum = [1] * len(nums)
        
        #calculate prefix sum
        for i in range(1, len(nums)):
            prefixSum[i] = prefixSum[i-1] * nums[i-1]
        print(prefixSum)

         #calculate prefix sum
        for i in range(len(nums)-2, -1, -1):
            suffixSum[i] = suffixSum[i+1] * nums[i+1]
        print(suffixSum)

        #calculate the result
        result = []
        for i in range(len(nums)):
            result.append(prefixSum[i] * suffixSum[i])

        return result