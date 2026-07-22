class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1)
        m = len(nums2)
        length = n+m
        
        prev = 0
        curr = 0

        mid = length // 2
        pointer,i,j = 0,0,0

        while pointer <= mid:
            prev = curr

            #nums1 exhausted
            if i>=n:
                curr = nums2[j]
                j+=1

            #nums2 exhausted
            elif j>=m:
                curr = nums1[i]
                i+=1

            # both are valid
            elif nums1[i] <= nums2[j]:
                curr = nums1[i]
                i+=1

            elif nums2[j] <= nums1[i]:
                curr = nums2[j]
                j+=1
            
            pointer+=1

        return (prev+curr) /2 if length % 2 == 0 else curr

        