class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1)
        m = len(nums2)
        arr = []
        res = 0

        for val in nums1:
            arr.append(val)
        
        for val in nums2:
            arr.append(val)
        
        l = 0
        r = len(arr) -1
        arr.sort()

        while l<=r:
            res = (arr[l] + arr[r]) / 2
            l+=1
            r-=1

        return res
        