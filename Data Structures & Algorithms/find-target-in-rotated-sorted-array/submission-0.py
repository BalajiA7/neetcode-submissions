class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i,val in enumerate(nums):
            if val == target:
                return i

        return -1

        