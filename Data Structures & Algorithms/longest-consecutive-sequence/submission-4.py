class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if(len(nums) == 0):
            return 0

        nums_set = set(nums)
        max_count = 1

        for num in nums:
            if (num - 1) not in nums_set:
                curr_count = 1
                curr_ele = num

                while (curr_ele + 1) in nums_set:
                    curr_count += 1
                    curr_ele += 1

                max_count = max(max_count, curr_count)

        return max_count

            

        