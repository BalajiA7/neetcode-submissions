class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if(len(nums) == 0):
            return 0
        
        curr_count = 1
        max_count = 1
        nums = sorted(nums) 
        for i in range(1, len(nums)):
            print(curr_count, max_count)
            if nums[i] == nums[i-1]:
                continue
            elif nums[i] == nums[i-1] + 1:
                curr_count +=1
            else:
                max_count = max(max_count, curr_count)
                curr_count = 1
                
        max_count = max(max_count, curr_count)
        return max_count

            

        