class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) -1

        while left<=right:
            mid = (left+right) // 2
            if nums[mid] == target:
                return mid

            # Left half is sorted
            if nums[left] <= nums[mid]:
                # Target lies in the left half
                if nums[left] <= target < nums[mid]:
                    right=mid-1 # move left
                else:
                    left=mid+1 # move right
            # Right half is sorted
            else:
               #Target lies in the right half
               if nums[mid] < target <= nums[right]:
                   left=mid+1 # move right
               else:
                   right=mid-1 # move left

        return -1

        