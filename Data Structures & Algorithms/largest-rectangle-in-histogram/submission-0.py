class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0

        for i in range(0, len(heights)):
            minHeight = heights[i]
            currMax = heights[i]
            res = max(currMax, res)
            for j in range(i+1, len(heights)):
                minHeight = min(minHeight, heights[j])
                currMax = minHeight * (j-i+1)
                res = max(currMax, res)
                
        return res

        