class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n, m = len(nums1), len(nums2)
        length = n+m
        median1,median2 = 0, 0
        i,j = 0, 0

        for count in range((length // 2) + 1):
            median2 = median1
            if i < n and j < m:
                if nums1[i] >= nums2[j]:
                    median1 = nums2[j]
                    j+=1
                else:
                    median1 = nums1[i]
                    i+=1
            elif i < n:
                median1 = nums1[i]
                i+=1
            else:
                median1 = nums2[j]
                j+=1
        
        if length % 2 == 1:
            return float(median1)
        else:
            return float(median1 + median2) / 2
