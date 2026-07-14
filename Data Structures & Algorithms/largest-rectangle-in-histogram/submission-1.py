class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        n = len(heights)

        for i in range(0,n):
            minHeight = float("inf")

            for j in range(i, n):
                minHeight = min(minHeight, heights[j])
                area = minHeight * (j-i+1)
                res = max(area, res)

        return res

        