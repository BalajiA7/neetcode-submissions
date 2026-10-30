class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1)
        m = len(nums2)
        length = (n+m)
        prev, curr, mid = 0, 0 , 0
        i, j = 0, 0

        while mid <= (length/2):
            prev = curr
            
            if i >= n:
                curr = nums2[j]
                j+=1
            elif j >= m:
                curr = nums1[i]
                i+=1
            elif nums1[i] <= nums2[j]:
                curr = nums1[i]
                i+=1
            else:
                curr = nums2[j]
                j+=1
            
            mid+=1
        
        return (prev+curr) / 2 if length % 2 == 0 else curr
        