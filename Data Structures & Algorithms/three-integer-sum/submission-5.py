class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []

        for i in range(n):
            if i > 0 and nums[i-1] == nums[i]:
                continue
                
            j = i+1
            k = n-1
            while j < k:
                if nums[i] + nums[j] + nums[k] < 0:
                    j+=1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k-=1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    # skip duplicates
                    j = j+1
                    while j < n and nums[j-1] == nums[j]:
                        j+=1
                    k = k-1
                    while k >=0  and nums[k+1] == nums[k]:
                        k-=1
        
        return res

        