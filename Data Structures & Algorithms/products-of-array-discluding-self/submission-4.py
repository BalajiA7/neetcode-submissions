class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        preProd = [1] * len(nums)
        postProd =[1] * len(nums)
        
        for i in range(1, len(nums)):
            sumValue = preProd[i-1] * nums[i-1]
            preProd[i] = sumValue
        
        for i in range(len(nums)-2, -1, -1):
            sumValue = postProd[i+1] * nums[i+1]
            postProd[i] = sumValue
        
        res = []
        for i in range(len(nums)):
            res.append(preProd[i] * postProd[i])
        
        return res
            


        