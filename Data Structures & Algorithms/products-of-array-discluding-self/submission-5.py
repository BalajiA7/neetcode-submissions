class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        
        for i in range(1, n):
            sumValue = res[i-1] * nums[i-1]
            res[i] = sumValue
        
        sumValue = 1 
        for i in range(n-2, -1, -1):
            sumValue *= nums[i+1]
            res[i] *= sumValue
 
        return res
            


        