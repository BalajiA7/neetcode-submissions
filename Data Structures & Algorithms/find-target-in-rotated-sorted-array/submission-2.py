class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) -1

        while l<=r:
            print("Left is ", l, "right is ", r, "mid is ",  (l+r) // 2)
            m = (l+r) // 2
            if nums[m] == target:
                return m

            leftSorted = nums[l] <= nums[m]
            rightSorted = nums[m] <= nums[r]

            isLeftSide= leftSorted and nums[l] <= target <= nums[m]
            isRightSide = rightSorted and nums[m] <= target <= nums[r]

            if isLeftSide:
                r = m-1
            elif isRightSide:
                l = m+1
            else:
               if rightSorted:
                r=m-1
               else:
                l=m+1

        return -1

        