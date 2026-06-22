class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if(len(nums) == 0):
            return 0

        nums_set = set()
        for val in nums:
            nums_set.add(val)
        
        max_count = 1
        for i in range(0, len(nums)):
            if nums[i] - 1 in nums_set:
                continue
            curr_count = 1
            curr_ele = nums[i] + 1
            while(curr_ele in nums_set):
                curr_count += 1
                max_count = max(max_count, curr_count)
                curr_ele += 1

        return max_count

            

        