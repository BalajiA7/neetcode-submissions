class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) -1

        while l<=r:
            print("Left is ", l, "right is ", r, "mid is ",  (l+r) // 2)
            m = (l+r) // 2
            if nums[m] == target:
                return m

            # Left half is sorted
            if nums[l] <= nums[m]:
                # Target lies in the left half
                if nums[l] <= target < nums[m]:
                    r=m-1
                else:
                    l=m+1
            # Right half is sorted
            else:
               #Target lies in the right half
               if nums[m] < target <= nums[r]:
                   l=m+1
               else:
                   r=m-1

        return -1

        